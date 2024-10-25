/**
 * Run markdownlint via the API in order to add custom rules for our needs.
 */
import fs from "fs";
import path from "path";
import markdownlint from "markdownlint";
import { globby } from "globby";
import relativeLinksRule from "markdownlint-rule-relative-links";

const files = await globby(["**/*.md", "!**/node_modules/**"]);

const result = markdownlint.sync({
  config: {
    default: true,
    // Disable unordered list indentation rule, allowing flexible list indentation
    MD007: false,

    // Allow multiple consecutive blank lines
    MD012: false,

    // Disable line length limit, allowing lines to exceed default character limits
    MD013: false,

    // Allow multiple headings with the same content
    MD024: false,

    MD029: {
      style: "ordered",
    },

    // Disable blank lines required around lists
    MD032: false,

    // Allow inline HTML within Markdown content
    MD033: false,

    // Disable rule that flags bare URLs without angle brackets or proper linking
    MD034: false,

    // Allow documents to start without a top-level heading (e.g., '# Title')
    MD041: false,

    // Disable rule that flags using 'bold' style instead of headers
    MD045: false,

    // Allow link reference definitions without using them in the document
    MD046: false,

    // Disable rule that flags duplicate link definitions
    MD047: false,

    "relative-links": true
  },
  customRules: [
    relativeLinksRule,
    {
      names: ["video-file-exists"],
      description: "Check that video files referenced in <video> tags exist",
      tags: ["video", "files", "links"],
      function: function customRule(params, onError) {
        params.tokens.forEach((token) => {
          if (token.type === "html_block" && token.content.includes("<video")) {
            const srcMatch = token.content.match(/src="(.+?)"/);
            if (srcMatch) {
              const filePath = path.resolve(
                path.dirname(params.name),
                srcMatch[1]
              );
              if (!fs.existsSync(filePath)) {
                onError({
                  lineNumber: token.lineNumber,
                  detail: `Video file "${srcMatch[1]}" does not exist.`,
                });
              }
            }
          }
        });
      },
    },
  ],
  files,
  resultVersion: 1,
});

const resultString = result.toString();
const returnCode = resultString ? 1 : 0;

if (resultString) {
  console.error(resultString);
}

process.exit(returnCode);
