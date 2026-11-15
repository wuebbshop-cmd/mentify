/**
 * Mentify Prep — Single Unified Markdown & KaTeX Engine (v5)
 *
 * PROVEN INDUSTRY-STANDARD PIPELINE:
 * Raw Markdown Source -> Marked AST -> KaTeX Tokens
 *
 * Guaranteed Invariants:
 * 1. ONE pipeline only: no separate JSON block dispatchers, no diverging branch logic.
 * 2. Rendering preserves source content; a narrow whitespace pass separates
 *    compound inline math from adjacent prose without touching code or math.
 * 3. Math everywhere: Display math ($$...$$) and inline math ($...$) work inside
 *    paragraphs, blockquotes (Definition/Theorem boxes), lists, and tables.
 * 4. Code isolation: Code blocks with '$' (e.g. R df$column) are protected by
 *    Marked AST and never processed by KaTeX.
 * 5. Single pass: No secondary DOM-wide math scanner.
 */

(function (window) {
  'use strict';

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  /**
   * Robust KaTeX rendering with delimiter stripping and command normalization.
   */
  function tryRenderKaTeX(latex, displayMode) {
    if (!latex || !String(latex).trim()) return '';
    var cleanLatex = String(latex).trim();
    // Strip accidental redundant outer delimiters if passed inside latex token
    cleanLatex = cleanLatex.replace(/^(\$\$|\\\[|\$|\\\()/, '').replace(/(\$\$|\\\]|\$|\\\))$/, '').trim();
    // Normalize doubly-escaped LaTeX commands (e.g. \\mathbb -> \mathbb, \\frac -> \frac, \\setminus -> \setminus)
    cleanLatex = cleanLatex.replace(/\\\\([a-zA-Z]+)/g, '\\$1');
    if (window.katex && typeof window.katex.renderToString === 'function') {
      try {
        return window.katex.renderToString(cleanLatex, {
          displayMode: !!displayMode,
          output: 'html',
          throwOnError: false,
          strict: false,
          trust: true
        });
      } catch (e) {
        return '<span class="katex-fallback">' + escapeHtml(cleanLatex) + '</span>';
      }
    }
    return '<span class="katex-fallback">' + escapeHtml(cleanLatex) + '</span>';
  }

  /**
   * Marked Math Extension:
   * Registers both Block Math and Inline Math AST tokenizers.
   * Handles:
   *   - Block: standalone $$...$$, \[...\], and \begin{env}...\end{env}
   *   - Inline: $$...$$ (display mode inside callouts/paragraphs), \[...\], \(...\), and $...$
   */
  function createMathExtension() {
    var envs = '(?:aligned|cases|matrix|pmatrix|bmatrix|vmatrix|gather|split|array|align\\*?)';
    var envRe = new RegExp('^(?:[ \\t]*)?(\\\\begin\\{' + envs + '\\}[\\s\\S]+?\\\\end\\{' + envs + '\\})[ \\t]*(?:\\n|$)');

    return {
      extensions: [
        // ─── 1. Block-Level Math ─────────────────────────────────────
        {
          name: 'blockMath',
          level: 'block',
          start: function (src) {
            var i1 = src.indexOf('$$');
            var i2 = src.indexOf('\\[');
            var i3 = src.indexOf('\\begin{');
            var valid = [i1, i2, i3].filter(function (x) { return x !== -1; });
            return valid.length ? Math.min.apply(null, valid) : undefined;
          },
          tokenizer: function (src, tokens) {
            // Standalone $$ ... $$
            var matchDd = src.match(/^(?:[ \\t]*)?\$\$([\s\S]+?)\$\$[ \\t]*(?:\n|$)/);
            if (matchDd) {
              if (!/\n\s*#{1,6}\s+/.test(matchDd[1]) && !/\n\s*\n\s*\n/.test(matchDd[1])) {
                return {
                  type: 'blockMath',
                  raw: matchDd[0],
                  text: matchDd[1].trim()
                };
              }
            }
            // Standalone \[ ... \]
            var matchBracket = src.match(/^(?:[ \\t]*)?\\\[([\s\S]+?)\\\][ \\t]*(?:\n|$)/);
            if (matchBracket) {
              if (!/\n\s*#{1,6}\s+/.test(matchBracket[1])) {
                return {
                  type: 'blockMath',
                  raw: matchBracket[0],
                  text: matchBracket[1].trim()
                };
              }
            }
            // Standalone \begin{env} ... \end{env}
            var matchEnv = src.match(envRe);
            if (matchEnv) {
              return {
                type: 'blockMath',
                raw: matchEnv[0],
                text: matchEnv[1].trim()
              };
            }
          },
          renderer: function (token) {
            return '<div class="katex-display">' + tryRenderKaTeX(token.text, true) + '</div>\n';
          }
        },

        // ─── 2. Inline & Embedded Math ───────────────────────────────
        {
          name: 'inlineMath',
          level: 'inline',
          start: function (src) {
            var i1 = src.indexOf('$$');
            var i2 = src.indexOf('$');
            var i3 = src.indexOf('\\[');
            var i4 = src.indexOf('\\(');
            var valid = [i1, i2, i3, i4].filter(function (x) { return x !== -1; });
            return valid.length ? Math.min.apply(null, valid) : undefined;
          },
          tokenizer: function (src, tokens) {
            // Embedded display math $$ ... $$ (e.g. inside blockquotes, callouts, lists)
            var matchDd = src.match(/^\$\$([\s\S]+?)\$\$/);
            if (matchDd) {
              return {
                type: 'inlineMath',
                raw: matchDd[0],
                text: matchDd[1].trim(),
                display: true
              };
            }
            // Embedded display math \[ ... \]
            var matchBracket = src.match(/^\\\[([\s\S]+?)\\\]/);
            if (matchBracket) {
              return {
                type: 'inlineMath',
                raw: matchBracket[0],
                text: matchBracket[1].trim(),
                display: true
              };
            }
            // Inline \( ... \)
            var matchParen = src.match(/^\\\(([\s\S]+?)\\\)/);
            if (matchParen) {
              return {
                type: 'inlineMath',
                raw: matchParen[0],
                text: matchParen[1].trim(),
                display: false
              };
            }
            // Inline $ ... $ (handles trailing/leading spaces gracefully, ignores empty $$)
            var matchDollar = src.match(/^\$(?!\$)([^\$\n\r]+?)\$(?!\$)/);
            if (matchDollar) {
              return {
                type: 'inlineMath',
                raw: matchDollar[0],
                text: matchDollar[1].trim(),
                display: false
              };
            }
          },
          renderer: function (token) {
            if (token.display) {
              return '<div class="katex-display">' + tryRenderKaTeX(token.text, true) + '</div>';
            }
            return tryRenderKaTeX(token.text, false);
          }
        }
      ]
    };
  }

  var mathExtensionConfigured = false;
  function ensureMarkedConfigured() {
    if (mathExtensionConfigured) return;
    if (window.marked && typeof window.marked.use === 'function') {
      window.marked.use({
        gfm: true,
        breaks: true,
        headerIds: false,
        mangle: false,
        renderer: {
          image: function(tokenOrHref, title, text) {
            var href = (typeof tokenOrHref === 'object' && tokenOrHref) ? tokenOrHref.href : tokenOrHref;
            var alt = (typeof tokenOrHref === 'object' && tokenOrHref) ? tokenOrHref.text : text;
            var imgTitle = (typeof tokenOrHref === 'object' && tokenOrHref) ? tokenOrHref.title : title;
            var cleanAlt = escapeHtml(alt || '');
            var cleanHref = String(href || '').replace(/"/g, '&quot;');
            var cleanTitle = imgTitle ? ' title="' + escapeHtml(imgTitle) + '"' : '';
            var captionHtml = cleanAlt ? '<figcaption class="prep-visual-caption">' + cleanAlt + '</figcaption>' : '';
            return '<figure class="prep-visual-figure">' +
              '<img src="' + cleanHref + '" alt="' + cleanAlt + '"' + cleanTitle + ' loading="lazy">' +
              captionHtml +
              '</figure>';
          },
          table: function() {
            var html = '';
            if (arguments.length >= 2) {
              html = '<table>\n<thead>\n' + arguments[0] + '</thead>\n<tbody>\n' + arguments[1] + '</tbody>\n</table>\n';
            } else if (arguments.length === 1 && typeof arguments[0] === 'object' && arguments[0]) {
              var token = arguments[0];
              if (this && typeof this.constructor.prototype.table === 'function' && this.constructor.prototype.table !== this.table) {
                html = this.constructor.prototype.table.call(this, token);
              }
            }
            if (html) {
              return '<div class="markdown-table-wrapper" tabindex="0" role="region" aria-label="Scrollable table">\n' + html + '</div>\n';
            }
            return false;
          }
        }
      });
      window.marked.use(createMathExtension());
      mathExtensionConfigured = true;
    }
  }

  function highlightCode(containerElement) {
    if (window.Prism && typeof window.Prism.highlightAllUnder === 'function') {
      window.Prism.highlightAllUnder(containerElement);
    } else if (window.Prism && typeof window.Prism.highlightAll === 'function') {
      window.Prism.highlightAll();
    }
  }

  /**
   * Academic Visuals Renderer:
   * 1. Mermaid.js: Mind Maps, Flowcharts, State & Cycle Diagrams
   * 2. Chart.js: Scientific Curves, Functions, Data & Statistical Graphs
   * 3. SmilesDrawer: 2D Chemical Molecular Structures
   */
  function renderAcademicVisuals(containerElement) {
    if (!containerElement) return;

    // If containerElement is not yet attached to document DOM, defer until attached
    if (!document.body || !document.body.contains(containerElement)) {
      setTimeout(function () {
        renderAcademicVisuals(containerElement);
      }, 30);
      return;
    }

    var isDark = document.documentElement.classList.contains('dark-theme');

    // Auto-detect untagged diagrams (e.g. if the LLM outputted ``` instead of ```mermaid)
    var allPreCode = containerElement.querySelectorAll('pre code');
    for (var ai = 0; ai < allPreCode.length; ai++) {
      var itemEl = allPreCode[ai];
      var rawTxt = itemEl.textContent.trim();
      if (/^(mindmap|graph\s+(TD|TB|BT|RL|LR)|flowchart\s+(TD|TB|BT|RL|LR)|sequenceDiagram|classDiagram|stateDiagram|erDiagram)\b/.test(rawTxt)) {
        itemEl.classList.add('language-mermaid');
      } else if (rawTxt.startsWith('{"type"') && (rawTxt.includes('"datasets"') || rawTxt.includes('"line"') || rawTxt.includes('"bar"'))) {
        itemEl.classList.add('language-chart');
      }
    }

    // ─── 1. Mermaid.js (Mind Maps, Flowcharts, Cycles) ───
    if (window.mermaid) {
      try {
        if (!window.__prep_mermaid_initialized) {
          window.mermaid.initialize({
            startOnLoad: false,
            theme: isDark ? 'dark' : 'default',
            securityLevel: 'loose',
            fontFamily: 'inherit',
            flowchart: { useMaxWidth: true, htmlLabels: true, curve: 'basis' },
            mindmap: { useMaxWidth: true }
          });
          window.__prep_mermaid_initialized = true;
        }

        var mermaidBlocks = containerElement.querySelectorAll('pre code.language-mermaid, pre code.mermaid');
        for (var mi = 0; mi < mermaidBlocks.length; mi++) {
          var codeEl = mermaidBlocks[mi];
          var preEl = codeEl.closest('pre');
          if (!preEl || preEl.dataset.renderedVisual) continue;
          preEl.dataset.renderedVisual = 'true';

          var rawMermaid = codeEl.textContent.trim();
          if (!rawMermaid) continue;

          // Clean up common model idiosyncrasies (e.g. <br/> inside ((...)) breaks mindmap parser)
          var cleanMermaid = rawMermaid.replace(/\(\((.*?)(?:<br\s*\/?>)+(.*?)\)\)/gi, '(($1 $2))');

          var uniqueId = 'mermaid_' + Math.random().toString(36).substring(2, 9) + '_' + Date.now();
          var wrapper = document.createElement('div');
          wrapper.className = 'prep-visual-wrap prep-mermaid-wrap';
          wrapper.setAttribute('role', 'img');
          wrapper.setAttribute('aria-label', 'Diagram or Mind Map');

          var innerDiv = document.createElement('div');
          innerDiv.className = 'mermaid';
          innerDiv.id = uniqueId;

          wrapper.appendChild(innerDiv);
          preEl.parentNode.replaceChild(wrapper, preEl);

          // Render via mermaid.render()
          (function (uId, textToRender, targetDiv, fallbackRaw) {
            try {
              window.mermaid.render(uId, textToRender).then(function (result) {
                targetDiv.innerHTML = result.svg;
                var svg = targetDiv.querySelector('svg');
                if (svg) {
                  svg.style.maxWidth = '100%';
                  svg.style.height = 'auto';
                  svg.removeAttribute('height');
                }
              }).catch(function (err) {
                console.warn('[Prep Renderer] Mermaid render error:', err);
                targetDiv.innerHTML = '<pre style="text-align:left;font-size:0.8rem;color:var(--text-muted);background:transparent;border:0;padding:4px;overflow-x:auto;">' + escapeHtml(fallbackRaw) + '</pre>';
              });
            } catch (syncErr) {
              console.warn('[Prep Renderer] Mermaid sync error:', syncErr);
              targetDiv.innerHTML = '<pre style="text-align:left;font-size:0.8rem;color:var(--text-muted);background:transparent;border:0;padding:4px;overflow-x:auto;">' + escapeHtml(fallbackRaw) + '</pre>';
            }
          })(uniqueId, cleanMermaid, innerDiv, rawMermaid);
        }
      } catch (mErr) {
        console.warn('[Prep Renderer] Mermaid processing error:', mErr);
      }
    }

    // ─── 2. Chart.js (Data Graphs, Scientific & Economic Curves) ───
    if (window.Chart) {
      try {
        var chartBlocks = containerElement.querySelectorAll('pre code.language-chart, pre code.language-graph');
        for (var ci = 0; ci < chartBlocks.length; ci++) {
          var cCodeEl = chartBlocks[ci];
          var cPreEl = cCodeEl.closest('pre');
          if (!cPreEl || cPreEl.dataset.renderedVisual) continue;
          cPreEl.dataset.renderedVisual = 'true';

          var rawChartJson = cCodeEl.textContent.trim();
          if (!rawChartJson) continue;

          var chartConfig = null;
          try {
            chartConfig = JSON.parse(rawChartJson);
          } catch (jsonErr) {
            var jsonMatch = rawChartJson.match(/\{[\s\S]*\}/);
            if (jsonMatch) {
              try { chartConfig = JSON.parse(jsonMatch[0]); } catch (e) {}
            }
          }

          if (!chartConfig || typeof chartConfig !== 'object') continue;

          var textColor = isDark ? '#f1f5f9' : '#1e293b';
          var gridColor = isDark ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.08)';

          var chartWrapper = document.createElement('div');
          chartWrapper.className = 'prep-visual-wrap prep-chart-wrap';

          if (chartConfig.title) {
            var titleEl = document.createElement('div');
            titleEl.className = 'prep-visual-title';
            titleEl.textContent = chartConfig.title;
            chartWrapper.appendChild(titleEl);
          }

          var canvasBox = document.createElement('div');
          canvasBox.className = 'prep-chart-canvas-box';
          var canvas = document.createElement('canvas');
          canvasBox.appendChild(canvas);
          chartWrapper.appendChild(canvasBox);

          cPreEl.parentNode.replaceChild(chartWrapper, cPreEl);

          var chartType = chartConfig.type || 'line';
          var chartData = chartConfig.data || {};
          var userOptions = chartConfig.options || {};

          var defaultOptions = {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: {
                labels: { color: textColor, font: { family: 'inherit', size: 12 } }
              },
              tooltip: {
                enabled: true,
                mode: 'index',
                intersect: false
              }
            }
          };

          if (chartType !== 'pie' && chartType !== 'doughnut') {
            defaultOptions.scales = {
              x: {
                ticks: { color: textColor },
                grid: { color: gridColor },
                title: { color: textColor }
              },
              y: {
                ticks: { color: textColor },
                grid: { color: gridColor },
                title: { color: textColor }
              }
            };
          }

          var finalOptions = Object.assign(defaultOptions, userOptions);

          try {
            new window.Chart(canvas, {
              type: chartType,
              data: chartData,
              options: finalOptions
            });
          } catch (chartErr) {
            console.warn('[Prep Renderer] Chart creation error:', chartErr);
          }
        }
      } catch (cErr) {
        console.warn('[Prep Renderer] Chart processing error:', cErr);
      }
    }

    // ─── 3. SmilesDrawer (Chemical Molecular Structures) ───
    if (window.SmilesDrawer) {
      try {
        var chemBlocks = containerElement.querySelectorAll('pre code.language-chemical, pre code.language-molecule, pre code.language-smiles');
        for (var chI = 0; chI < chemBlocks.length; chI++) {
          var chemCodeEl = chemBlocks[chI];
          var chemPreEl = chemCodeEl.closest('pre');
          if (!chemPreEl || chemPreEl.dataset.renderedVisual) continue;
          chemPreEl.dataset.renderedVisual = 'true';

          var rawChem = chemCodeEl.textContent.trim();
          if (!rawChem) continue;

          var chemName = '';
          var smilesStr = '';
          if (rawChem.startsWith('{')) {
            try {
              var chemObj = JSON.parse(rawChem);
              chemName = chemObj.name || chemObj.title || '';
              smilesStr = chemObj.smiles || chemObj.structure || '';
            } catch (e) {
              smilesStr = rawChem;
            }
          } else {
            smilesStr = rawChem;
          }

          if (!smilesStr) continue;

          var chemWrapper = document.createElement('div');
          chemWrapper.className = 'prep-visual-wrap prep-chem-wrap';

          if (chemName) {
            var cTitleEl = document.createElement('div');
            cTitleEl.className = 'prep-visual-title';
            cTitleEl.textContent = chemName;
            chemWrapper.appendChild(cTitleEl);
          }

          var chemSvg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
          chemSvg.setAttribute('width', '320');
          chemSvg.setAttribute('height', '200');
          chemSvg.className = 'prep-chem-svg';
          chemWrapper.appendChild(chemSvg);

          var smilesLabel = document.createElement('div');
          smilesLabel.className = 'prep-chem-formula';
          smilesLabel.innerHTML = 'SMILES: <code>' + escapeHtml(smilesStr) + '</code>';
          chemWrapper.appendChild(smilesLabel);

          chemPreEl.parentNode.replaceChild(chemWrapper, chemPreEl);

          try {
            var drawer = new window.SmilesDrawer.SvgDrawer({
              width: 320,
              height: 200,
              bondThickness: 1.5,
              padding: 12
            });
            (function (sStr, sSvg) {
              window.SmilesDrawer.parse(sStr, function (tree) {
                drawer.draw(tree, sSvg, isDark ? 'dark' : 'light', false);
              }, function (parseErr) {
                console.warn('[Prep Renderer] SmilesDrawer parse notice:', parseErr);
                sSvg.style.display = 'none';
              });
            })(smilesStr, chemSvg);
          } catch (drawErr) {
            console.warn('[Prep Renderer] SmilesDrawer error:', drawErr);
          }
        }
      } catch (chErr) {
        console.warn('[Prep Renderer] SmilesDrawer processing error:', chErr);
      }
    }
  }

    function renderMarkdownWithKaTeX(rawInput, containerElement) {
    if (!containerElement) return '';
    if (!rawInput) {
      containerElement.innerHTML = '';
      return '';
    }

    ensureMarkedConfigured();

    // Normalize input to raw markdown string
    var markdownSource = '';
    if (typeof rawInput === 'string') {
      markdownSource = rawInput;
    } else if (rawInput && typeof rawInput === 'object') {
      // If passed a payload dict {content: "..."}
      if (typeof rawInput.content === 'string') {
        markdownSource = rawInput.content;
      } else {
        markdownSource = String(rawInput);
      }
    } else {
      markdownSource = String(rawInput);
    }

    // Clean literal escaped newlines and LaTeX document markup
    var cleanText = replaceLiteralEscapedNewlines(markdownSource).trim();
    cleanText = cleanLatexDocumentMarkup(cleanText);
    cleanText = normalizeLegacyMathBlocks(cleanText);
    warnOnMathReviewTokens(cleanText);
    cleanText = normalizeInlineMathBoundaries(cleanText);

    // Normalize doubly-escaped LaTeX commands (e.g. \\mathbb -> \mathbb, \\frac -> \frac, \\setminus -> \setminus)
    cleanText = cleanText.replace(/\\\\([a-zA-Z]+)/g, '\\$1');
    // Normalize stray \text{[...marks]} or [... \text{marks}] both inside and outside math
    cleanText = cleanText.replace(/\\text\{\s*\[?\s*(\d+)\s*(?:marks?|mks?)\s*\]?\s*\}/gi, '[$1 marks]');
    cleanText = cleanText.replace(/\[\s*(\d+)\s*\\text\{(?:marks?|mks?)\}\s*\]/gi, '[$1 marks]');
    cleanText = cleanText.replace(/\[\s*\\text\{(\d+)\s*(?:marks?|mks?)\}\s*\]/gi, '[$1 marks]');

    // Strip stray \text{...} occurring in Markdown prose outside math delimiters
    var proseOrMath = /(```[\s\S]*?```|\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\]|\$[^\$\n]+?\$|\\\([\s\S]*?\\\))/g;
    var pmParts = cleanText.split(proseOrMath);
    for (var pmi = 0; pmi < pmParts.length; pmi += 2) {
      if (pmParts[pmi]) {
        pmParts[pmi] = pmParts[pmi].replace(/(?<!\\)\\text\{([^{}\n]+)\}/g, '$1');
      }
    }
    cleanText = pmParts.join('');

    // Extract marks that got bundled inside $$...$$ at the end of display equations
    cleanText = cleanText.replace(/\$\$([\s\S]*?)\$\$/g, function(full, body) {
      var markMatch = body.match(/\s*(\[(?:\d+)\s*(?:marks?|mks?)\])\s*$/i);
      if (markMatch) {
        var cleanBody = body.substring(0, markMatch.index).trim();
        return '\n\n$$\n' + cleanBody + '\n$$\n\n' + markMatch[1] + '\n\n';
      }
      return full;
    });

    // Normalize align/align* to aligned so KaTeX renders natively inside ...
    cleanText = cleanText.replace(/\\begin\{align\*?\}/g, '\\begin{aligned}');
    cleanText = cleanText.replace(/\\end\{align\*?\}/g, '\\end{aligned}');

    // In math blocks, replace literal '*' with '\\ast' so Markdown's bold/italic parser
    // never confuses math superscripts (e.g. p^* or Q_1^*) with Markdown asterisks.
    // Guard against replacing '*' in environment names (e.g. \\begin{...*}).
    cleanText = cleanText.replace(/(\$\$[\s\S]*?\$\$|\$[^\$\n]+?\$)/g, function(m) {
      return m.replace(/(?<!\\begin\{[a-zA-Z]+|\\end\{[a-zA-Z]+)\*/g, '\\ast');
    });

    // Merge detached \[ lhs = \n\n$$\n\begin{cases}...\end{cases}\n$$
    cleanText = cleanText.replace(
      /(?:\\\[|\$\$)\s*([^\n$\\]+?=\s*)\s*\$\$\s*(\\begin\{(?:cases|aligned|matrix|pmatrix|bmatrix|vmatrix|array)\}[\s\S]*?\\end\{(?:cases|aligned|matrix|pmatrix|bmatrix|vmatrix|array)\})\s*\$\$\s*(?:\\\]|\$\$)?/g,
      function(full, lhs, envBlock) {
        return '\n\n$$\n' + lhs.trim() + ' ' + envBlock.trim() + '\n$$\n\n';
      }
    );

    // Collapse adjacent display delimiters on the same line only (never across newlines)
    cleanText = cleanText.replace(/(?:\\\[|\$\$)[ \t]*(?:\\\[|\$\$)/g, function() { return '$$'; });
    cleanText = cleanText.replace(/(?:\\\]|\$\$)[ \t]*(?:\\\]|\$\$)/g, function() { return '$$'; });

    // Ensure LaTeX environments occurring outside display math are isolated in $$...$$ without double-nesting
    var envBlocks = /(```[\s\S]*?```|\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\])/g;
    var envSegs = cleanText.split(envBlocks);
    var envRe = /\\begin\{(aligned|cases|matrix|pmatrix|bmatrix|vmatrix|gather|split|array|align\*?)\}([\s\S]*?)\\end\{\1\}/g;
    for (var esi = 0; esi < envSegs.length; esi += 2) {
      if (envSegs[esi]) {
        envSegs[esi] = envSegs[esi].replace(envRe, function(full, env, body) {
          return '\n\n$$\n\\begin{' + env + '}' + body + '\\end{' + env + '}\n$$\n\n';
        });
      }
    }
    cleanText = envSegs.join('');

    // Clean any outer \[ ... \] that wrapped an inner $$...$$
    cleanText = cleanText.replace(/\\\[\s*\$\$([\s\S]*?)\$\$\s*\\\]/g, function(full, inner) {
      return '\n\n$$\n' + inner.trim() + '\n$$\n\n';
    });

    // Guard against unclosed display math delimiters ($$) leaking across the document
    var checkLines = cleanText.split('\n');
    var inFence = false;
    var dBlockCount = 0;
    for (var cli = 0; cli < checkLines.length; cli++) {
      if (/^\s*```/.test(checkLines[cli])) {
        inFence = !inFence;
        continue;
      }
      if (!inFence) {
        var dm = checkLines[cli].match(/\$\$/g);
        if (dm) dBlockCount += dm.length;
      }
    }
    if (dBlockCount % 2 === 1) {
      cleanText += '\n\n$$\n';
    }

    // Prevent accidental 4-space indents outside code fences from turning into <pre><code> code blocks
    var lines = cleanText.split('\n');
    var inCodeFence = false;
    for (var li = 0; li < lines.length; li++) {
      if (/^\s*```/.test(lines[li])) {
        inCodeFence = !inCodeFence;
        continue;
      }
      if (!inCodeFence && /^[ ]{4,}\S/.test(lines[li])) {
        lines[li] = lines[li].replace(/^[ ]+/, '');
      }
    }
    cleanText = lines.join('\n');

    var htmlOutput = '';
    if (window.marked && typeof window.marked.parse === 'function') {
      htmlOutput = window.marked.parse(cleanText);
    } else {
      htmlOutput = escapeHtml(cleanText).replace(/\n/g, '<br>');
    }

    containerElement.innerHTML = htmlOutput;

    // Wrap any unwrapped table elements in .markdown-table-wrapper for responsive horizontal scrolling
    try {
      var tables = containerElement.querySelectorAll('table');
      for (var ti = 0; ti < tables.length; ti++) {
        var tbl = tables[ti];
        if (tbl.parentElement && !tbl.parentElement.classList.contains('markdown-table-wrapper')) {
          var wrapper = document.createElement('div');
          wrapper.className = 'markdown-table-wrapper';
          wrapper.setAttribute('tabindex', '0');
          wrapper.setAttribute('role', 'region');
          wrapper.setAttribute('aria-label', 'Scrollable table');
          tbl.parentNode.insertBefore(wrapper, tbl);
          wrapper.appendChild(tbl);
        }
      }
    } catch (tblErr) {
      // Non-blocking enhancement
    }

    highlightCode(containerElement);
    renderAcademicVisuals(containerElement);
    return htmlOutput;
  }

  /* ─── Global Exports ─────────────────────────────────────────────── */
  window.renderMarkdownWithKaTeX = renderMarkdownWithKaTeX;
  window.cleanLatexDocumentMarkup = cleanLatexDocumentMarkup;
  window.tryRenderKaTeX = tryRenderKaTeX;
  window.createMathExtension = createMathExtension;
  window.renderAcademicVisuals = renderAcademicVisuals;
  ensureMarkedConfigured();

})(typeof window !== 'undefined' ? window : this);
