import markdownlint from "markdownlint";
import { globby } from "globby";
import relativeLinksRule from "markdownlint-rule-relative-links";

const files = await globby(["**/*.md", "!**/node_modules/**", "!venv/**"]);

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

    // Horizontal rule style
    MD035: false,

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
