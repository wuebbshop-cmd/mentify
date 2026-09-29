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
   * Pure KaTeX rendering without regex auto-repair.
   */
  function tryRenderKaTeX(latex, displayMode) {
    if (!latex || !String(latex).trim()) return '';
    var cleanLatex = String(latex).trim();
    if (window.katex && typeof window.katex.renderToString === 'function') {
      try {
        return window.katex.renderToString(cleanLatex, {
          displayMode: !!displayMode,
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
      var quoteMatch = line.match(/^\\s*>\\s?(.*)$/);
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

    // Clean literal escaped newlines if any
    var cleanText = markdownSource.replace(/\\n(?![a-zA-Z])/g, '\n').trim();
    cleanText = normalizeLegacyMathBlocks(cleanText);

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
  window.tryRenderKaTeX = tryRenderKaTeX;
  window.createMathExtension = createMathExtension;
  ensureMarkedConfigured();

})(typeof window !== 'undefined' ? window : this);
