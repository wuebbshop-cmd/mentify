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

  var KATEX_COMMON_MACROS = {
    "\\cdotp": "\\cdot",
    "\\cdotv": "\\cdot",
    "\\muT": "\\mu\\text{T}",
    "\\muA": "\\mu\\text{A}",
    "\\muV": "\\mu\\text{V}",
    "\\muF": "\\mu\\text{F}",
    "\\mum": "\\mu\\text{m}",
    "\\mus": "\\mu\\text{s}",
    "\\mug": "\\mu\\text{g}",
    "\\muC": "\\mu\\text{C}",
    "\\muW": "\\mu\\text{W}",
    "\\muH": "\\mu\\text{H}",
    "\\muJ": "\\mu\\text{J}",
    "\\muN": "\\mu\\text{N}",
    "\\muL": "\\mu\\text{L}",
    "\\muK": "\\mu\\text{K}",
    "\\muPa": "\\mu\\text{Pa}",
    "\\muHz": "\\mu\\text{Hz}",
    "\\muWb": "\\mu\\text{Wb}"
  };

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
    // Normalize \cdotp and \cdotv (punctuation dots) to standard \cdot
    cleanLatex = cleanLatex.replace(/\\cdot[pv]\b/g, '\\cdot');
    // Normalize concatenated Greek prefixes with units (e.g. \muT -> \mu\text{T}, \muA -> \mu\text{A})
    cleanLatex = cleanLatex.replace(/\\mu([A-Z][a-zA-Z]*|m|s|g|l|mol)\b/g, '\\mu\\text{$1}');
    // Normalize unescaped percent signs inside math so KaTeX does not treat them as TeX comments
    cleanLatex = cleanLatex.replace(/(?<!\\)%/g, '\\%');

    if (window.katex && typeof window.katex.renderToString === 'function') {
      try {
        return window.katex.renderToString(cleanLatex, {
          displayMode: !!displayMode,
          output: 'html',
          throwOnError: false,
          strict: false,
          trust: true,
          macros: KATEX_COMMON_MACROS
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

  // ─────────────────────────────────────────────────────────────────────────────
  // Academic Visuals Renderer v2 — Mermaid · Chart.js · SVG · SmilesDrawer
  //
  // Fix 1: CDN libraries may load async on slow/mobile connections.
  //         renderAcademicVisuals is called after DOM insertion; we retry if libs 
  //         are not yet available (up to 12 retries with 200ms intervals = 2.4s).
  // Fix 2: Mermaid generates small SVGs because mermaid.initialize() uses default
  //         width caps. We override SVG to fill container via CSS transform-origin.
  // Fix 3: Mermaid syntax errors (unquoted math labels) are auto-sanitized.
  //         Bomb icon suppressed; graceful fallback card rendered instead.
  // Fix 4: Chart.js supports {x,y} coordinate pairs for parametric curves/circles
  //         by switching x-axis to 'linear' type automatically.
  // Fix 5: Chemical structure detection includes language-json blocks with "smiles".
  // ─────────────────────────────────────────────────────────────────────────────

  function sanitizeMermaidCode(rawText) {
    if (!rawText) return '';
    var text = rawText.trim();

    // Strip HTML <br> tags (breaks Mermaid mindmaps and node lexers)
    text = text.replace(/<br\s*\/?>/gi, ' ');

    // Normalize mindmap root syntax: root((Label))
    text = text.replace(/root\(\((.*?)\)\)/gi, function(m, p1) {
      return 'root((' + p1.replace(/[()]/g, '').trim() + '))';
    });

    // Auto-quote rectangle node labels containing math chars, punctuation, or parens
    text = text.replace(/(\b[a-zA-Z0-9_]+)\[(?!")([^\]\n]+?)\]/g, function(m, id, label) {
      if (/[+\-*\/^=<>(){},:;?]/.test(label)) {
        return id + '["' + label.replace(/"/g, "'").trim() + '"]';
      }
      return m;
    });

    // Auto-quote diamond labels: A{Is x > 0?} -> A{"Is x > 0?"}
    text = text.replace(/(\b[a-zA-Z0-9_]+)\{(?!")([^}\n]+?)\}/g, function(m, id, label) {
      if (/[+\-*\/^=<>()[\]:;?]/.test(label)) {
        return id + '{"' + label.replace(/"/g, "'").trim() + '"}';
      }
      return m;
    });

    // Auto-quote rounded nodes: A(x^2 + y^2 = r^2) -> A("x^2 + y^2 = r^2")
    // Skip if it is double parens ((...)) e.g. circle/mindmap node
    text = text.replace(/(\b[a-zA-Z0-9_]+)\((?!\()((?!\")[^)\n]+?)\)/g, function(m, id, label) {
      if (/[+\-*\/^=<>\[\]{}:;?]/.test(label)) {
        return id + '("' + label.replace(/"/g, "'").trim() + '")';
      }
      return m;
    });

    return text;
  }

  function renderFallbackFlowDiagram(targetDiv, rawCode) {
    var raw = (rawCode || '').trim();
    if (!raw) return;

    // Handle mind maps fallback: render structured hierarchical outline tree
    if (/^mindmap\b/i.test(raw)) {
      var mlines = raw.split('\n');
      var mHtml = '<div style="padding:14px 12px;text-align:left;background:var(--hover);border:1px solid var(--border);border-radius:10px;">';
      mHtml += '<div style="font-size:0.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--primary);margin-bottom:12px;display:flex;align-items:center;gap:6px;"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M12 3v6m0 6v6M3 12h6m6 0h6"/></svg> Mind Map Summary</div>';
      mHtml += '<div style="display:flex;flex-direction:column;gap:6px;">';
      for (var mi = 0; mi < mlines.length; mi++) {
        var mline = mlines[mi];
        if (!mline.trim() || /^mindmap\b/i.test(mline.trim())) continue;
        var indentMatch = mline.match(/^(\s*)/);
        var indent = indentMatch ? indentMatch[1].length : 0;
        var cleanLabel = mline.trim().replace(/^root\(\((.*?)\)\)/i, '$1').replace(/^\(\((.*?)\)\)/, '$1').replace(/^["'\[\(\{]+|["'\]\)\}]+$/g, '').trim();
        if (!cleanLabel) continue;
        var isRoot = mi === 1 || /root\(/i.test(mline) || indent === 0;
        var marginL = Math.max(0, (indent - 2) * 12);
        if (isRoot) {
          mHtml += '<div style="font-weight:700;font-size:0.95rem;color:var(--primary);padding:6px 12px;background:var(--surface);border:1px solid var(--primary);border-radius:8px;display:inline-block;margin-bottom:4px;">' + escapeHtml(cleanLabel) + '</div>';
        } else {
          mHtml += '<div style="margin-left:' + marginL + 'px;display:flex;align-items:center;gap:6px;font-size:0.86rem;color:var(--text);">';
          mHtml += '<span style="color:var(--primary);font-size:0.65rem;">&#9679;</span>';
          mHtml += '<span style="background:var(--surface);padding:3px 9px;border-radius:6px;border:1px solid var(--border);">' + escapeHtml(cleanLabel) + '</span>';
          mHtml += '</div>';
        }
      }
      mHtml += '</div></div>';
      targetDiv.innerHTML = mHtml;
      return;
    }

    // Parse mermaid flowchart text into a readable step-by-step flow card
    var lines = raw.split('\n');
    var html = '<div style="padding:12px 4px;text-align:left;">';
    html += '<div style="font-size:0.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--primary);margin-bottom:12px;">&#9654; Diagram</div>';
    var nodeMap = {};
    var seen = {};

    for (var li = 0; li < lines.length; li++) {
      var line = lines[li].trim();
      if (!line || /^(graph|flowchart|mindmap|sequenceDiagram|stateDiagram)\b/i.test(line)) continue;

      // Extract node labels from mermaid syntax
      var nodeRe = /[A-Za-z0-9_]+(?:\[["']?([^"\]']+)["']?\]|\(["']?([^")']+)["']?\)|\{["']?([^"}']+)["']?\}|\(+([^)]+)\)+)/g;
      var nm;
      while ((nm = nodeRe.exec(line)) !== null) {
        var nodeId = nm[0].split(/[\[\(\{]/)[0];
        var nodeLabel = (nm[1] || nm[2] || nm[3] || nm[4] || '').trim();
        if (nodeLabel) nodeMap[nodeId] = nodeLabel;
      }

      // Render arrows as steps
      var arrowMatch = line.match(/^(.+?)\s*(?:-->|---\s*>|->|==>|--\s*>)\s*(?:\|([^|]+)\|)?\s*(.+)$/);
      if (arrowMatch) {
        var from = arrowMatch[1].trim();
        var cond = (arrowMatch[2] || '').trim();
        var to = arrowMatch[3].trim();

        var fromLabel = from.replace(/^[A-Za-z0-9_]+(?=[\[\(\{])/, '').replace(/^[A-Za-z0-9_]+$/, function(id) { return nodeMap[id] || id; });
        fromLabel = fromLabel.replace(/^["'\[\(\{]+|["'\]\)\}]+$/g, '').trim();
        var toLabel = to.replace(/^[A-Za-z0-9_]+(?=[\[\(\{])/, '').replace(/^[A-Za-z0-9_]+$/, function(id) { return nodeMap[id] || id; });
        toLabel = toLabel.replace(/^["'\[\(\{]+|["'\]\)\}]+$/g, '').trim();

        if (fromLabel && toLabel && !seen[from + '->' + to]) {
          seen[from + '->' + to] = true;
          html += '<div style="display:flex;align-items:center;gap:8px;margin:7px 0;flex-wrap:wrap;">';
          html += '<span style="background:var(--hover);border:1px solid var(--border);border-radius:8px;padding:5px 11px;font-size:.84rem;color:var(--text);">' + escapeHtml(fromLabel) + '</span>';
          if (cond) {
            html += '<span style="color:var(--primary);font-size:.82rem;font-weight:600;">&rarr; <em style=\'font-size:.78rem;color:var(--text-muted);\'>(' + escapeHtml(cond) + ')</em></span>';
          } else {
            html += '<span style="color:var(--primary);font-weight:700;font-size:1rem;">&rarr;</span>';
          }
          html += '<span style="background:var(--hover);border:1px solid var(--border);border-radius:8px;padding:5px 11px;font-size:.84rem;color:var(--text);">' + escapeHtml(toLabel) + '</span>';
          html += '</div>';
        }
      }
    }
    html += '</div>';
    targetDiv.innerHTML = html;
  }

  /**
   * renderAcademicVisuals: Main visual rendering dispatcher.
   * Called after markdown is set as innerHTML on the container.
   */
  function renderAcademicVisuals(containerElement) {
    if (!containerElement) return;

    // Defer until element is in DOM
    if (!document.body || !document.body.contains(containerElement)) {
      setTimeout(function() { renderAcademicVisuals(containerElement); }, 50);
      return;
    }

    // Check which libraries are actually needed by blocks in this container
    var containerText = containerElement.textContent || '';
    var needsMermaid = !!containerElement.querySelector('pre code.language-mermaid, pre code.mermaid, pre code.language-graph, pre code.language-flowchart') ||
                       /^\s*(mindmap|graph\s+(TD|TB|BT|RL|LR)|flowchart\s+(TD|TB|BT|RL|LR)|sequenceDiagram|stateDiagram)\b/im.test(containerText);
    var needsChart = !!containerElement.querySelector('pre code.language-chart') ||
                     (containerText.includes('"datasets"') && (containerText.includes('"line"') || containerText.includes('"scatter"')));
    var needsSmiles = !!containerElement.querySelector('pre code.language-chemical, pre code.language-smiles, pre code.language-molecule') ||
                      (containerText.includes('"smiles"') && containerText.includes('{'));

    var missingLibs = (needsMermaid && !window.mermaid) ||
                      (needsChart && !window.Chart) ||
                      (needsSmiles && !(window.SmilesDrawer || window.smilesDrawer));

    if (missingLibs) {
      var retryCount = (containerElement.__visualRetry | 0) + 1;
      containerElement.__visualRetry = retryCount;
      if (retryCount <= 12) {
        setTimeout(function() { renderAcademicVisuals(containerElement); }, 150 * Math.min(retryCount, 4));
        return;
      }
      // After retry limit, proceed with whatever is available
    }
    containerElement.__visualRetry = 0;

    var isDark = document.documentElement.classList.contains('dark-theme');

    // ─── Auto-detect untagged code blocks ───
    var allPreCode = containerElement.querySelectorAll('pre code:not([data-detected])');
    for (var ai = 0; ai < allPreCode.length; ai++) {
      var el = allPreCode[ai];
      el.setAttribute('data-detected', '1');
      var txt = el.textContent.trim();

      if (/^\s*(mindmap|graph\s+(TD|TB|BT|RL|LR)|flowchart\s+(TD|TB|BT|RL|LR)|sequenceDiagram|classDiagram|stateDiagram|erDiagram)\b/i.test(txt)) {
        el.classList.add('language-mermaid');
      } else if (!el.classList.contains('language-json') && txt.startsWith('{') && txt.includes('"smiles"')) {
        el.classList.add('language-chemical');
      } else if (/^\s*<svg[\s\S]*<\/svg>\s*$/i.test(txt)) {
        el.classList.add('language-svg');
      } else if (txt.startsWith('{') && (txt.includes('"datasets"') || txt.includes('"type"')) &&
                 (txt.includes('"line"') || txt.includes('"scatter"') || txt.includes('"bar"') || txt.includes('"pie"') || txt.includes('"datasets"'))) {
        el.classList.add('language-chart');
      } else if (el.classList.contains('language-json') && txt.includes('"smiles"')) {
        el.classList.remove('language-json');
        el.classList.add('language-chemical');
      }
    }

    // ─── 1. Mermaid (Mind Maps, Flowcharts, Decision Trees) ───────────────────
    if (window.mermaid) {
      try {
        if (!window.__prep_mermaid_initialized) {
          window.mermaid.initialize({
            startOnLoad: false,
            suppressErrorRendering: true,
            theme: isDark ? 'dark' : 'default',
            securityLevel: 'loose',
            fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
            fontSize: 15,
            themeVariables: {
              fontSize: '15px',
              fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
              primaryColor: isDark ? '#1e293b' : '#f0fdf4',
              primaryTextColor: isDark ? '#f8fafc' : '#0f172a',
              primaryBorderColor: '#10b981',
              lineColor: isDark ? '#94a3b8' : '#475569',
              secondaryColor: isDark ? '#334155' : '#e2e8f0',
              tertiaryColor: isDark ? '#1e293b' : '#f8fafc'
            },
            flowchart: {
              useMaxWidth: false,
              htmlLabels: true,
              curve: 'basis',
              nodeSpacing: 46,
              rankSpacing: 46,
              diagramPadding: 20
            },
            mindmap: {
              useMaxWidth: false,
              padding: 22
            },
            sequence: { useMaxWidth: false },
            er: { useMaxWidth: false }
          });
          window.__prep_mermaid_initialized = true;
        }

        var mermaidBlocks = containerElement.querySelectorAll(
          'pre code.language-mermaid, pre code.mermaid, pre code.language-graph, pre code.language-flowchart'
        );
        for (var mi = 0; mi < mermaidBlocks.length; mi++) {
          var codeEl = mermaidBlocks[mi];
          var preEl = codeEl.closest('pre');
          if (!preEl || preEl.dataset.renderedVisual) continue;
          preEl.dataset.renderedVisual = 'true';

          var rawMermaid = codeEl.textContent.trim();
          if (!rawMermaid) continue;

          var cleanMermaid = sanitizeMermaidCode(rawMermaid);
          var uId = 'mm_' + Math.random().toString(36).slice(2, 9) + '_' + (Date.now() % 100000);
          var renderId = 'mmsvg_' + uId;

          var wrap = document.createElement('div');
          wrap.className = 'prep-visual-wrap prep-mermaid-wrap';
          wrap.setAttribute('role', 'img');
          wrap.setAttribute('aria-label', 'Diagram');

          var inner = document.createElement('div');
          inner.className = 'prep-mermaid-inner';
          wrap.appendChild(inner);
          preEl.parentNode.replaceChild(wrap, preEl);

          (function(uid, text, container, raw) {
            try {
              window.mermaid.render(uid, text).then(function(result) {
                if (!result || !result.svg) {
                  renderFallbackFlowDiagram(container, raw);
                  return;
                }
                // Check if Mermaid generated an explicit error node (e.g. bomb icon element or error container)
                if (result.svg.indexOf('class="error-icon"') !== -1 || result.svg.indexOf('aria-roledescription="error"') !== -1) {
                  var errEl = document.getElementById('d' + uid);
                  if (errEl && errEl.parentNode) errEl.parentNode.removeChild(errEl);
                  renderFallbackFlowDiagram(container, raw);
                  return;
                }
                container.innerHTML = result.svg;
                var svg = container.querySelector('svg');
                if (svg) {
                  var vb = svg.getAttribute('viewBox');
                  var vbW = 600;
                  var vbH = 400;
                  if (vb) {
                    var parts = vb.trim().split(/[\s,]+/);
                    if (parts.length >= 4) {
                      vbW = parseFloat(parts[2]) || 600;
                      vbH = parseFloat(parts[3]) || 400;
                    }
                  } else {
                    vbW = parseFloat(svg.getAttribute('width')) || 600;
                    vbH = parseFloat(svg.getAttribute('height')) || 400;
                    svg.setAttribute('viewBox', '0 0 ' + vbW + ' ' + vbH);
                  }
                  svg.removeAttribute('width');
                  svg.removeAttribute('height');

                  // Make diagram clearly legible on both desktop and mobile
                  // Never squash wide mind maps or decision trees into microscopic unreadable text!
                  svg.style.display = 'block';
                  svg.style.margin = '0 auto';
                  svg.style.height = 'auto';

                  if (vbW > 0) {
                    var isNarrow = (window.innerWidth < 640);
                    var minLegibleW = isNarrow ? Math.min(vbW, 460) : Math.min(vbW, 680);
                    svg.style.minWidth = minLegibleW + 'px';
                    svg.style.maxWidth = Math.max(vbW, 620) + 'px';
                    svg.style.width = '100%';
                  } else {
                    svg.style.width = '100%';
                    svg.style.minHeight = '240px';
                  }

                  // Add swipe hint on mobile when diagram overflows container
                  if (wrap && !wrap.querySelector('.prep-mermaid-scroll-hint') && vbW > 450) {
                    var hint = document.createElement('div');
                    hint.className = 'prep-mermaid-scroll-hint';
                    hint.innerHTML = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 9l4-4 4 4m0 6l-4 4-4-4"/></svg> Scroll horizontally to view full diagram';
                    wrap.appendChild(hint);
                  }
                }
              }).catch(function(err) {
                window.console && console.warn('[Prep Renderer] mermaid.render rejected:', err);
                // Remove any error element mermaid may have injected
                var errEl = document.getElementById('d' + uid);
                if (errEl && errEl.parentNode) errEl.parentNode.removeChild(errEl);
                renderFallbackFlowDiagram(container, raw);
              });
            } catch(e) {
              window.console && console.warn('[Prep Renderer] mermaid.render threw synchronously:', e);
              renderFallbackFlowDiagram(container, raw);
            }
          })(renderId, cleanMermaid, inner, rawMermaid);
        }
      } catch(mErr) {
        window.console && console.warn('[Prep Renderer] Mermaid error:', mErr);
      }
    }

    // ─── 2. Chart.js (Scientific Graphs, Mathematical Curves) ─────────────────
    if (window.Chart) {
      try {
        var chartBlocks = containerElement.querySelectorAll(
          'pre code.language-chart'
        );
        for (var ci = 0; ci < chartBlocks.length; ci++) {
          var cCodeEl = chartBlocks[ci];
          var cPreEl = cCodeEl.closest('pre');
          if (!cPreEl || cPreEl.dataset.renderedVisual) continue;
          cPreEl.dataset.renderedVisual = 'true';

          var rawJson = cCodeEl.textContent.trim();
          if (!rawJson) continue;

          var cfg = null;
          try { cfg = JSON.parse(rawJson); } catch(e) {
            var m = rawJson.match(/\{[\s\S]*\}/);
            if (m) try { cfg = JSON.parse(m[0]); } catch(e2) {}
          }
          if (!cfg) continue;

          var textColor = isDark ? '#f1f5f9' : '#1e293b';
          var gridColor = isDark ? 'rgba(255,255,255,0.1)' : 'rgba(0,0,0,0.08)';

          var cWrap = document.createElement('div');
          cWrap.className = 'prep-visual-wrap prep-chart-wrap';
          if (cfg.title) {
            var tEl = document.createElement('div');
            tEl.className = 'prep-visual-title';
            tEl.textContent = cfg.title;
            cWrap.appendChild(tEl);
          }
          var cBox = document.createElement('div');
          cBox.className = 'prep-chart-canvas-box';
          var canvas = document.createElement('canvas');
          cBox.appendChild(canvas);
          cWrap.appendChild(cBox);
          cPreEl.parentNode.replaceChild(cWrap, cPreEl);

          // Detect coordinate-pair datasets for parametric curves
          var datasets = (cfg.data && cfg.data.datasets) || [];
          var hasXY = false;
          for (var di = 0; di < datasets.length; di++) {
            var pts = datasets[di].data || [];
            if (pts.length && typeof pts[0] === 'object' && 'x' in pts[0] && 'y' in pts[0]) {
              hasXY = true;
              datasets[di].showLine = datasets[di].showLine !== false;
              datasets[di].tension = datasets[di].tension != null ? datasets[di].tension : 0.3;
              datasets[di].fill = datasets[di].fill || false;
              datasets[di].pointRadius = datasets[di].pointRadius != null ? datasets[di].pointRadius : 2;
            }
          }

          var chartType = cfg.type || 'line';
          var isCircle = /circle|locus|ellipse/i.test(cfg.title || '');
          var userOpts = cfg.options || {};

          var opts = {
            responsive: true,
            maintainAspectRatio: isCircle,
            aspectRatio: isCircle ? 1 : undefined,
            animation: { duration: 400 },
            plugins: {
              legend: { labels: { color: textColor, font: { family: 'inherit', size: 12 } } },
              tooltip: { enabled: true, mode: 'nearest', intersect: false }
            }
          };

          if (chartType !== 'pie' && chartType !== 'doughnut') {
            opts.scales = {
              x: {
                type: hasXY ? 'linear' : undefined,
                ticks: { color: textColor, maxTicksLimit: 10 },
                grid: { color: gridColor },
                title: { display: !!(cfg.xLabel || (userOpts.scales && userOpts.scales.x && userOpts.scales.x.title && userOpts.scales.x.title.text)), text: (cfg.xLabel || ''), color: textColor }
              },
              y: {
                type: 'linear',
                ticks: { color: textColor, maxTicksLimit: 10 },
                grid: { color: gridColor },
                title: { display: !!(cfg.yLabel || (userOpts.scales && userOpts.scales.y && userOpts.scales.y.title && userOpts.scales.y.title.text)), text: (cfg.yLabel || ''), color: textColor }
              }
            };
          }

          // Deep-merge user options over defaults
          function mergeDeep(target, src) {
            for (var k in src) {
              if (src[k] && typeof src[k] === 'object' && !Array.isArray(src[k])) {
                target[k] = target[k] || {};
                mergeDeep(target[k], src[k]);
              } else {
                target[k] = src[k];
              }
            }
            return target;
          }
          opts = mergeDeep(opts, userOpts);
          if (hasXY && opts.scales && opts.scales.x) opts.scales.x.type = 'linear';

          try {
            new window.Chart(canvas, { type: chartType, data: cfg.data || {}, options: opts });
          } catch(cErr) {
            window.console && console.warn('[Prep Renderer] Chart error:', cErr);
          }
        }
      } catch(cE) {
        window.console && console.warn('[Prep Renderer] Chart processing error:', cE);
      }
    }

    // ─── 3. SVG / Geometry Diagrams ───────────────────────────────────────────
    try {
      var svgBlocks = containerElement.querySelectorAll(
        'pre code.language-svg, pre code.language-geometry'
      );
      for (var si = 0; si < svgBlocks.length; si++) {
        var sEl = svgBlocks[si];
        var sPreEl = sEl.closest('pre');
        if (!sPreEl || sPreEl.dataset.renderedVisual) continue;
        var svgText = sEl.textContent.trim();
        var svgMatch = svgText.match(/<svg[\s\S]*?<\/svg>/i);
        if (!svgMatch) continue;
        sPreEl.dataset.renderedVisual = 'true';
        var sWrap = document.createElement('div');
        sWrap.className = 'prep-visual-wrap prep-svg-wrap';
        sWrap.innerHTML = svgMatch[0];
        var embSvg = sWrap.querySelector('svg');
        if (embSvg) {
          if (!embSvg.getAttribute('viewBox')) {
            var sw = embSvg.getAttribute('width') || '400';
            var sh = embSvg.getAttribute('height') || '300';
            embSvg.setAttribute('viewBox', '0 0 ' + sw + ' ' + sh);
          }
          embSvg.removeAttribute('width');
          embSvg.removeAttribute('height');
          embSvg.style.cssText = 'width:100%;height:auto;max-width:100%;display:block;margin:0 auto;';
        }
        sPreEl.parentNode.replaceChild(sWrap, sPreEl);
      }
    } catch(svgE) {
      window.console && console.warn('[Prep Renderer] SVG error:', svgE);
    }

    // ─── 4. Chemical Molecular Structures (SmilesDrawer or Structured Card) ───
    try {
      var chemSelectors = [
        'pre code.language-chemical',
        'pre code.language-molecule',
        'pre code.language-smiles',
        'pre code.language-json'
      ].join(', ');
      var chemBlocks = containerElement.querySelectorAll(chemSelectors);
      for (var chi = 0; chi < chemBlocks.length; chi++) {
        var chEl = chemBlocks[chi];
        var chPre = chEl.closest('pre');
        if (!chPre || chPre.dataset.renderedVisual) continue;

        var rawChem = chEl.textContent.trim();
        if (!rawChem.includes('"smiles"') && !rawChem.includes('"structure"') &&
            !chEl.classList.contains('language-chemical') && !chEl.classList.contains('language-molecule') &&
            !chEl.classList.contains('language-smiles')) {
          continue; // Skip JSON blocks without SMILES
        }

        var chemName = '';
        var smilesStr = '';
        if (rawChem.startsWith('{')) {
          try {
            var chemObj = JSON.parse(rawChem);
            chemName = chemObj.name || chemObj.title || '';
            smilesStr = chemObj.smiles || chemObj.structure || '';
          } catch(e) {
            var sm = rawChem.match(/"smiles"\s*:\s*"([^"]+)"/i);
            if (sm) smilesStr = sm[1];
            var nm2 = rawChem.match(/"name"\s*:\s*"([^"]+)"/i);
            if (nm2) chemName = nm2[1];
          }
        } else if (/^smiles:\s*/i.test(rawChem)) {
          smilesStr = rawChem.replace(/^smiles:\s*/i, '').trim();
        } else {
          smilesStr = rawChem;
        }
        if (!smilesStr) continue;

        chPre.dataset.renderedVisual = 'true';
        var chWrap = document.createElement('div');
        chWrap.className = 'prep-visual-wrap prep-chem-wrap';

        if (chemName) {
          var chTitle = document.createElement('div');
          chTitle.className = 'prep-visual-title';
          chTitle.textContent = chemName;
          chWrap.appendChild(chTitle);
        }

        var SD = window.SmilesDrawer || window.smilesDrawer;
        if (SD) {
          var chSvg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
          chSvg.setAttribute('width', '340');
          chSvg.setAttribute('height', '220');
          chSvg.setAttribute('class', 'prep-chem-svg');
          chWrap.appendChild(chSvg);

          (function(ss, svg) {
            try {
              var DrawerClass = SD.SvgDrawer || SD.Drawer;
              var dr = new DrawerClass({ width: 340, height: 220, bondThickness: 1.6, padding: 14 });
              SD.parse(ss,
                function(tree) { dr.draw(tree, svg, isDark ? 'dark' : 'light'); },
                function(err) { svg.style.display = 'none'; }
              );
            } catch(de) { svg.style.display = 'none'; }
          })(smilesStr, chSvg);
        }

        var chLabel = document.createElement('div');
        chLabel.className = 'prep-chem-formula';
        chLabel.innerHTML = 'Molecular Structure (SMILES): <code>' + escapeHtml(smilesStr) + '</code>';
        chWrap.appendChild(chLabel);

        chPre.parentNode.replaceChild(chWrap, chPre);
      }
    } catch(chE) {
      window.console && console.warn('[Prep Renderer] Chemical structure error:', chE);
    }
  }


  var reportedMathWarnings = {};
  function warnMathReviewIssue(code, message) {
    if (reportedMathWarnings[code] || !window.console || typeof window.console.warn !== 'function') return;
    reportedMathWarnings[code] = true;
    window.console.warn('[Prep renderer][' + code + '] ' + message);
  }

  function normalizeInlineMathBoundaries(markdown) {
    var protectedBlocks = /(```[\s\S]*?```|`[^`\n]*`|\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\])/g;
    var inlineMath = /(?<!\\)\$(?!\$)([^$\n]+?)(?<!\\)\$(?!\$)|\\\(([\s\S]*?)\\\)/g;
    var segments = markdown.split(protectedBlocks);

    for (var segmentIndex = 0; segmentIndex < segments.length; segmentIndex += 2) {
      segments[segmentIndex] = segments[segmentIndex].replace(inlineMath, function (token, dollarBody, parenBody, offset, source) {
        var body = dollarBody === undefined ? parenBody : dollarBody;
        if (/^[A-Za-z0-9_]+$/.test(body.trim())) return token;

        var prefix = source.slice(0, offset);
        var suffix = source.slice(offset + token.length);
        var addSpaceBefore = /[A-Za-z0-9_]$/.test(prefix);
        var addSpaceAfter = /^[A-Za-z0-9_]/.test(suffix);
        if (addSpaceBefore || addSpaceAfter) {
          warnMathReviewIssue(
            'math.inline_boundary.missing_space',
            'Inserted prose spacing around a compound inline-math expression.'
          );
        }
        return (addSpaceBefore ? ' ' : '') + token + (addSpaceAfter ? ' ' : '');
      });
    }

    return segments.join('');
  }

  function warnOnMathReviewTokens(markdown) {
    var source = markdown.replace(/```[\s\S]*?```|`[^`\n]*`/g, '');
    if (/(?<!\\)\\Re\b/.test(source)) {
      warnMathReviewIssue(
        'math.notation.real_operator_ambiguous',
        'Review \\Re: use \\mathbb{R} for the real-number set, but retain \\Re for real-part notation.'
      );
    }
    if (/\btheseries\b/i.test(source)) {
      warnMathReviewIssue('text.ocr.merged_words', 'Possible OCR merge "theseries"; review or correct the source.');
    }
    if (/\bi\s+e\s+j\b/i.test(source) &&
        /\b(?:cov(?:ariance)?|var(?:iance)?|correlation|matrix|independent)\b/i.test(source)) {
      warnMathReviewIssue('math.ocr.not_equal', 'Possible OCR artifact "i e j" in statistical notation; review for "i != j".');
    }
  }

  var VALID_LATEX_N_COMMANDS = {
    nabla: 1, natural: 1, naturalnums: 1, ncong: 1, ne: 1, nearrow: 1, neg: 1,
    neq: 1, nexists: 1, ngeq: 1, ngeqq: 1, ngeqslant: 1, ngtr: 1, ni: 1,
    nleftarrow: 1, nLeftarrow: 1, nleftrightarrow: 1, nLeftrightarrow: 1,
    nleq: 1, nleqq: 1, nleqslant: 1, nless: 1, nmid: 1, noindent: 1,
    nolimits: 1, nonumber: 1, normalfont: 1, normalsize: 1, not: 1, notin: 1,
    nparallel: 1, nprec: 1, npreceq: 1, nrightarrow: 1, nRightarrow: 1,
    nshortmid: 1, nshortparallel: 1, nsim: 1, nsubseteq: 1, nsubseteqq: 1,
    nsucc: 1, nsucceq: 1, nsupseteq: 1, nsupseteqq: 1, ntriangleleft: 1,
    ntrianglelefteq: 1, ntriangleright: 1, ntrianglerighteq: 1, nu: 1,
    nvdash: 1, nvDash: 1, nVdash: 1, nVDash: 1, nwarrow: 1, newline: 1,
    newpage: 1
  };

  function replaceLiteralEscapedNewlines(text) {
    if (!text || text.indexOf('\\n') === -1) return text;
    var out = text.replace(/\\n(?![a-zA-Z])/g, '\n');
    out = out.replace(/\\(n[a-zA-Z]*)/g, function(full, cmd) {
      if (VALID_LATEX_N_COMMANDS[cmd]) return full;
      return '\n' + cmd.substring(1);
    });
    return out;
  }

  function convertLatexTabularToMarkdown(body) {
    var cleanedBody = body.replace(/\\(?:hline|toprule|midrule|bottomrule|cline\{[^}]*\})/g, '');
    var rawRows = cleanedBody.split(/\\\\/);
    var parsedRows = [];
    for (var r = 0; r < rawRows.length; r++) {
      var row = rawRows[r].trim();
      if (!row || row.indexOf('&') === -1) continue;
      var cells = row.split('&').map(function(c) {
        return c.trim().replace(/\s+/g, ' ');
      });
      parsedRows.push(cells);
    }
    if (!parsedRows.length) return body;
    var numCols = 0;
    for (var i = 0; i < parsedRows.length; i++) {
      if (parsedRows[i].length > numCols) numCols = parsedRows[i].length;
    }
    var mdLines = [];
    for (var idx = 0; idx < parsedRows.length; idx++) {
      var rowCells = parsedRows[idx].slice();
      while (rowCells.length < numCols) rowCells.push('');
      mdLines.push('| ' + rowCells.join(' | ') + ' |');
      if (idx === 0) {
        var sep = [];
        for (var c = 0; c < numCols; c++) sep.push('---');
        mdLines.push('| ' + sep.join(' | ') + ' |');
      }
    }
    return '\n\n' + mdLines.join('\n') + '\n\n';
  }

  /**
   * Convert raw LaTeX document commands and list environments into standard clean Markdown
   * while strictly preserving LaTeX mathematical notation inside math mode ($...$, $$...$$, \(..\), \[..\]).
   */
  function cleanLatexDocumentMarkup(text) {
    if (!text || typeof text !== 'string') return '';
    var cleaned = replaceLiteralEscapedNewlines(text).trim();

    // Fix corrupted encoding artifacts
    cleaned = cleaned.replace(/Cram\ufffdr\ufffdRao/g, 'Cram\u00e9r\u2013Rao');
    cleaned = cleaned.replace(/\ufffd/g, '\u2013');

    // 0. Convert verbatim and lstlisting environments into fenced R code blocks
    cleaned = cleaned.replace(/\\begin\{(?:verbatim|lstlisting)\}(?:\[[^\]]*\])?([\s\S]*?)\\end\{(?:verbatim|lstlisting)\}/g, function(_, body) {
      var codeBody = replaceLiteralEscapedNewlines(body).replace(/^\n+|\n+$/g, '');
      return '\n\n```r\n' + codeBody + '\n```\n\n';
    });

    // 0b. Strip outer table wrappers and convert tabular environments to Markdown tables
    cleaned = cleaned.replace(/\\begin\{table\}(?:\[[^\]]*\])?([\s\S]*?)\\end\{table\}/g, '$1');
    cleaned = cleaned.replace(/\\centering\b\s*/g, '');
    cleaned = cleaned.replace(/\\caption\{([^}]*)\}/g, '\n**$1**\n');
    cleaned = cleaned.replace(/\\label\{[^}]*\}/g, '');
    cleaned = cleaned.replace(/\\begin\{tabular\}\{[^}]*\}([\s\S]*?)\\end\{tabular\}/g, function(_, body) {
      return convertLatexTabularToMarkdown(body);
    });

    // 0c. Clean squashed or run-together Markdown headers
    // e.g. "text -## 7. Header", "text --## 7. Header", "text —## 7. Header", or "text\n-## 7. Header"
    cleaned = cleaned.replace(/([^\n])\s*(?:[-–—]{1,2})\s*(#{1,6}\s+[^\n]+)/g, '$1\n\n$2');
    cleaned = cleaned.replace(/^[ \t]*(?:[-*•]\s*)?(#{1,6}\s+[^\n]+)/gm, '$1');
    cleaned = cleaned.replace(/([^\n])\s+(#{1,6}\s+[A-Z0-9][^\n]+)/g, '$1\n\n$2');

    // 1. Clean document-level whitespace and layout commands
    cleaned = cleaned.replace(/\\noindent\s*/g, '');
    cleaned = cleaned.replace(/\\(?:vspace|hspace)\*?\{[^}]*\}/g, '');
    cleaned = cleaned.replace(/\\(?:bigskip|medskip|smallskip|newpage|clearpage|pagebreak|hrule)\b\s*/g, '');
    cleaned = cleaned.replace(/\\section\*?\{([^}]*)\}/g, '\n\n## $1\n\n');
    cleaned = cleaned.replace(/\\subsection\*?\{([^}]*)\}/g, '\n\n### $1\n\n');
    cleaned = cleaned.replace(/\\subsubsection\*?\{([^}]*)\}/g, '\n\n#### $1\n\n');

    // 2. Convert mark tags e.g. \hfill (3 marks) -> **(3 marks)**
    cleaned = cleaned.replace(/\\hfill\s*(\([0-9]+\s*(?:marks?|mks)\)|\[[0-9]+\s*(?:marks?|mks)\])/gi, function(_, m) {
      return '**' + m + '**';
    });
    cleaned = cleaned.replace(/\\hfill\s*/g, ' ');

    // 3. Protect fenced code blocks and display math while converting text styling commands
    var protectedPattern = /(```[\s\S]*?```|\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\])/g;
    var segments = [];
    var lastIndex = 0;
    var match;

    function cleanTextStylingInSegment(seg) {
      var s = seg.replace(/\*\*([^*\n]*?\\texttt\{[^}\n]*?)\*\*([^}\n]*)\}/g, function(_, p1, p2) {
        var inner = p1 + p2;
        inner = inner.replace(/\\texttt\{([^{}]*)\}/g, '`$1`');
        return '**' + inner + '**';
      });
      for (var pass = 0; pass < 3; pass++) {
        s = s.replace(/\\texttt\{([^{}]*)\}/g, function(_, inner) {
          return '`' + inner.replace(/\\%/g, '%').replace(/\\_/g, '_') + '`';
        });
      }
      var imathStore = [];
      s = s.replace(/(\$[^\$\n]+?\$|\\\([\s\S]*?\\\))/g, function(m) {
        imathStore.push(m);
        return '\x00IMATH' + (imathStore.length - 1) + '\x00';
      });
      for (var p2 = 0; p2 < 3; p2++) {
        s = s.replace(/\\textbf\{([^{}]*)\}/g, '**$1**');
        s = s.replace(/\\(?:textit|emph)\{([^{}]*)\}/g, '*$1*');
        s = s.replace(/\\underline\{([^{}]*)\}/g, '<u>$1</u>');
      }
      s = s.replace(/\x00IMATH(\d+)\x00/g, function(_, idx) {
        return imathStore[parseInt(idx, 10)];
      });
      return s;
    }

    while ((match = protectedPattern.exec(cleaned)) !== null) {
      segments.push(cleanTextStylingInSegment(cleaned.substring(lastIndex, match.index)));
      segments.push(match[0]);
      lastIndex = protectedPattern.lastIndex;
    }
    segments.push(cleanTextStylingInSegment(cleaned.substring(lastIndex)));
    cleaned = segments.join('');

    // 4. Handle nested enumerate environments (innermost first)
    function replaceInnerEnum(m, opt, body) {
      opt = opt || '';
      var isRoman = /\bi\b|\(i\)|i\)/i.test(opt);
      var isAlpha = /\ba\b|\(a\)|a\)/i.test(opt);

      var alphaSeq = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)', '(g)', '(h)', '(i)', '(j)'];
      var romanSeq = ['(i)', '(ii)', '(iii)', '(iv)', '(v)', '(vi)', '(vii)', '(viii)', '(ix)', '(x)'];
      var numSeq = [];
      for (var n = 1; n <= 30; n++) numSeq.push(n + '.');

      var defaultSeq = isRoman ? romanSeq : (isAlpha ? alphaSeq : numSeq);

      var itemRegex = /\\item(?:\[([^\]]*)\])?\s*/g;
      var parts = [];
      var lastIdx = 0;
      var labels = [];
      var itemMatch;
      while ((itemMatch = itemRegex.exec(body)) !== null) {
        if (parts.length === 0) {
          var prefix = body.substring(lastIdx, itemMatch.index).trim();
          if (prefix) parts.push(prefix);
        } else {
          parts.push(body.substring(lastIdx, itemMatch.index).trim());
        }
        labels.push(itemMatch[1] || null);
        lastIdx = itemRegex.lastIndex;
      }
      if (lastIdx > 0) {
        parts.push(body.substring(lastIdx).trim());
      }

      if (labels.length === 0) return body;

      var outLines = [];
      var itemOffset = (parts.length > labels.length) ? 1 : 0;
      if (itemOffset === 1 && parts[0]) {
        outLines.push(parts[0]);
      }

      for (var i = 0; i < labels.length; i++) {
        var lbl = labels[i];
        var content = parts[i + itemOffset] || '';
        if (!lbl) {
          lbl = (i < defaultSeq.length) ? defaultSeq[i] : '(' + (i + 1) + ')';
        }
        var contentLines = content.split('\n');
        if (contentLines.length > 0) {
          outLines.push(lbl + ' ' + contentLines[0]);
          for (var c = 1; c < contentLines.length; c++) {
            outLines.push(contentLines[c]);
          }
        } else {
          outLines.push(lbl);
        }
      }
      return '\n\n' + outLines.join('\n') + '\n\n';
    }

    var innerEnumRe = /\\begin\{enumerate\}(?:\[([^\]]*)\])?((?:(?!\\begin\{enumerate\})[\s\S])*?)\\end\{enumerate\}/;
    for (var round = 0; round < 6; round++) {
      if (!innerEnumRe.test(cleaned)) break;
      cleaned = cleaned.replace(innerEnumRe, replaceInnerEnum);
    }

    // 5. Handle itemize environments
    cleaned = cleaned.replace(/\\begin\{itemize\}(?:\[[^\]]*\])?([\s\S]*?)\\end\{itemize\}/g, function(_, body) {
      var items = body.split(/\\item\s*/);
      var out = [];
      for (var j = 1; j < items.length; j++) {
        var it = items[j].trim();
        if (it) out.push('- ' + it);
      }
      return '\n\n' + out.join('\n') + '\n\n';
    });

    // 6. Strip text alignment environments
    cleaned = cleaned.replace(/\\begin\{(?:center|flushleft|flushright)\}([\s\S]*?)\\end\{(?:center|flushleft|flushright)\}/g, '$1');

    // 7. Clean prose-mode LaTeX line breaks (\\) outside math/code blocks
    cleaned = cleanProseLatexBreaks(cleaned);

    // 8. Clean consecutive newlines
    cleaned = cleaned.replace(/\n{3,}/g, '\n\n');
    return cleaned.trim();
  }

  function cleanProseLatexBreaks(text) {
    if (!text || typeof text !== 'string') return text;
    var blockPattern = /(```[\s\S]*?```|\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\]|\$[^\$\n]+?\$|\\\(.*?\\\))/g;
    var segments = text.split(blockPattern);
    for (var i = 0; i < segments.length; i += 2) {
      if (segments[i]) {
        segments[i] = segments[i].replace(/(?:\\\\)[ \t]*(?:\\\\)?/g, '\n\n');
        segments[i] = segments[i].replace(/\\(?=[ \t]*\n|[ \t]*$)/g, '');
      }
    }
    return segments.join('').replace(/\n{3,}/g, '\n\n');
  }

  // Compatibility for older notes that put display math inside a Markdown
  // quote, or emitted a supported LaTeX environment without $$ fences.
  // This only moves unambiguous structural boundaries; it never edits the
  // contents of a mathematical expression.
  function normalizeLegacyMathBlocks(text) {
    var lines = String(text || '').split('\n');
    var output = [];
    var inDisplayMath = false;
    var inCodeFence = false;
    var quoted = false;
    var quotedMath = [];
    var envNames = 'aligned|cases|matrix|pmatrix|bmatrix|vmatrix|gather|split|array|align\\*?';
    var envStart = new RegExp('^\\s*\\\\begin\\{(?:' + envNames + ')\\}');
    var environment = false;
    var environmentStack = [];
    var environmentLines = [];

    function updateEnvironmentStack(line) {
      var tokenRe = new RegExp('\\\\(begin|end)\\{(' + envNames + ')\\}', 'g');
      var match;
      while ((match = tokenRe.exec(line)) !== null) {
        if (match[1] === 'begin') {
          environmentStack.push(match[2]);
        } else if (environmentStack[environmentStack.length - 1] === match[2]) {
          environmentStack.pop();
        }
      }
      return environmentStack.length === 0;
    }

    lines.forEach(function (line) {
      var trimmed = line.trim();

      // Protect code fences
      if (/^```/.test(trimmed)) {
        inCodeFence = !inCodeFence;
        output.push(line);
        return;
      }
      if (inCodeFence) {
        output.push(line);
        return;
      }

      var quoteMatch = line.match(/^\s*>\s?(.*)$/);
      var content = quoteMatch ? quoteMatch[1] : line;
      var contentTrimmed = content.trim();

      if (quoted) {
        if (quoteMatch && (contentTrimmed === '$$' || contentTrimmed === '\\]')) {
          output.push('$$', quotedMath.join('\n'), '$$');
          quoted = false;
        } else if (quoteMatch) {
          quotedMath.push(content);
        } else if (!line.trim()) {
          quotedMath.push('');
        } else {
          output.push('$$', quotedMath.join('\n'), '$$');
          quoted = false;
          output.push(line);
        }
        return;
      }

      if (quoteMatch && (contentTrimmed === '$$' || contentTrimmed === '\\[')) {
        quoted = true;
        quotedMath = [];
        return;
      }

      // Track unquoted display math ($$ ... $$)
      if (!quoted) {
        var dCount = (line.match(/\$\$/g) || []).length;
        if (dCount % 2 === 1) {
          inDisplayMath = !inDisplayMath;
        } else if (trimmed === '\\[' || trimmed === '\\]') {
          inDisplayMath = (trimmed === '\\[');
        }
      }

      // Only wrap environments if we are NOT already inside display math!
      if (!inDisplayMath && !environment && envStart.test(line) && !line.includes('$$')) {
        environment = true;
        environmentStack = [];
        environmentLines = [line.trim()];
        if (updateEnvironmentStack(line)) {
          output.push('$$', environmentLines.join('\n'), '$$');
          environment = false;
          environmentStack = [];
          environmentLines = [];
        }
        return;
      }
      if (environment) {
        environmentLines.push(line.trim());
        if (updateEnvironmentStack(line)) {
          output.push('$$', environmentLines.join('\n'), '$$');
          environment = false;
          environmentStack = [];
          environmentLines = [];
        }
        return;
      }

      output.push(line);
    });

    if (quoted && quotedMath.length) output.push('$$', quotedMath.join('\n'), '$$');
    if (environment && environmentLines.length) output.push(environmentLines.join('\n'));
    return output.join('\n');
  }

  /**
   * Universal Single-Pipeline Renderer:
   * Raw Markdown Source -> Marked AST -> KaTeX Tokens
   */

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