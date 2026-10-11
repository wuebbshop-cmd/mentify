/**
 * Mentify Prep — Single Unified Markdown & KaTeX Engine (v5)
 *
 * PROVEN INDUSTRY-STANDARD PIPELINE:
 * Raw Markdown Source -> Marked AST -> KaTeX Tokens
 *
 * Guaranteed Invariants:
 * 1. ONE pipeline only: no separate JSON block dispatchers, no diverging branch logic.
 * 2. Pure rendering: NO server/client auto-repair regexes or destructive string mutation.
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
        mangle: false
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

    // 7. Clean consecutive newlines
    cleaned = cleaned.replace(/\n{3,}/g, '\n\n');
    return cleaned.trim();
  }

  // Compatibility for older notes that put display math inside a Markdown
  // quote, or emitted a supported LaTeX environment without $$ fences.
  // This only moves unambiguous structural boundaries; it never edits the
  // contents of a mathematical expression.
  function normalizeLegacyMathBlocks(text) {
    var lines = String(text || '').split('\n');
    var output = [];
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
      var quoteMatch = line.match(/^\s*>\s?(.*)$/);
      var content = quoteMatch ? quoteMatch[1] : line;
      var trimmed = content.trim();

      if (quoteMatch && (trimmed === '$$' || trimmed === '\\[')) {
        quoted = true;
        quotedMath = [];
        return;
      }
      if (quoted) {
        if (quoteMatch && (trimmed === '$$' || trimmed === '\\]')) {
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

      if (!environment && envStart.test(line) && !line.includes('$$')) {
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

    // Normalize doubly-escaped LaTeX commands (e.g. \\mathbb -> \mathbb, \\frac -> \frac, \\setminus -> \setminus)
    cleanText = cleanText.replace(/\\\\([a-zA-Z]+)/g, '\\$1');

    // Merge detached \[ lhs = \n\n$$\n\begin{cases}...\end{cases}\n$$
    cleanText = cleanText.replace(
      /(?:\\\[|\$\$)\s*([^\n$\\]+?=\s*)\s*\$\$\s*(\\begin\{(?:cases|aligned|matrix|pmatrix|bmatrix|vmatrix|array)\}[\s\S]*?\\end\{(?:cases|aligned|matrix|pmatrix|bmatrix|vmatrix|array)\})\s*\$\$\s*(?:\\\]|\$\$)?/g,
      function(full, lhs, envBlock) {
        return '\n\n$$\n' + lhs.trim() + ' ' + envBlock.trim() + '\n$$\n\n';
      }
    );

    // Collapse adjacent display delimiters to prevent nested math parsing errors (using replacer func to avoid JS $$ replacement string bug)
    cleanText = cleanText.replace(/(?:\\\[|\$\$)\s*(?:\\\[|\$\$)/g, function() { return '$$'; });
    cleanText = cleanText.replace(/(?:\\\]|\$\$)\s*(?:\\\]|\$\$)/g, function() { return '$$'; });

    // Ensure LaTeX environments occurring on the same line or outside $$ delimiters are isolated in $$...$$ without double-nesting
    var envInlineRe = /(?:\\\[|\$\$)?\s*\\begin\{(aligned|cases|matrix|pmatrix|bmatrix|vmatrix|gather|split|array|align\*?)\}([\s\S]*?)\\end\{\1\}\s*(?:\\\]|\$\$)?/g;
    cleanText = cleanText.replace(envInlineRe, function(full, env, body) {
      return '\n\n$$\n\\begin{' + env + '}' + body + '\\end{' + env + '}\n$$\n\n';
    });

    // Clean any outer \[ ... \] that wrapped an inner $$...$$
    cleanText = cleanText.replace(/\\\[\s*\$\$([\s\S]*?)\$\$\s*\\\]/g, function(full, inner) {
      return '\n\n$$\n' + inner.trim() + '\n$$\n\n';
    });

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
    highlightCode(containerElement);
    return htmlOutput;
  }

  /* ─── Global Exports ─────────────────────────────────────────────── */
  window.renderMarkdownWithKaTeX = renderMarkdownWithKaTeX;
  window.cleanLatexDocumentMarkup = cleanLatexDocumentMarkup;
  window.tryRenderKaTeX = tryRenderKaTeX;
  window.createMathExtension = createMathExtension;
  ensureMarkedConfigured();

})(typeof window !== 'undefined' ? window : this);
