// This config utilizes a comprehensive Airbnb style guide and the vuejs plugin
// see: https://github.com/airbnb/javascript
// see: https://github.com/vuejs/eslint-plugin-vue
// see: https://github.com/meteorlxy/eslint-plugin-prettier-vue
// see: https://github.com/prettier/plugin-pug

module.exports = {
    root: true,
    parserOptions: {
        parser: "@babel/eslint-parser",
        sourceType: "module",
    },
    env: {
        browser: true,
        node: true,
        es6: true,
    },
    settings: {
        "prettier-vue": {
            // Settings for how to process Vue SFC Blocks
            SFCBlocks: {
                /**
                 * Use prettier to process `<template>` blocks or not
                 *
                 * If set to `false`, you may need to enable those vue rules that are disabled by `eslint-config-prettier`,
                 * because you need them to lint `<template>` blocks
                 *
                 * @default true
                 */
                template: true,

                /**
                 * Use prettier to process `<script>` blocks or not
                 *
                 * If set to `false`, you may need to enable those rules that are disabled by `eslint-config-prettier`,
                 * because you need them to lint `<script>` blocks
                 *
                 * @default true
                 */
                script: true,

                /**
                 * Use prettier to process `<style>` blocks or not
                 *
                 * @default true
                 */
                style: true,
            },

            // Use prettierrc for prettier options or not (default: `true`)
            usePrettierrc: true,
        },
    },
    extends: [
        "airbnb-base",
        "plugin:vue/recommended",
        "plugin:prettier-vue/recommended",
        "prettier",
    ],
    rules: {
        "class-methods-use-this": "off",
        "vue/max-attributes-per-line": [
            "error",
            { singleline: 5, multiline: 1 },
        ],
        "no-console": 0,
        "import/extensions": 0,
        "import/no-extraneous-dependencies": 0,
        "vue/no-lone-template": 0,
        "prefer-destructuring": 0,
        "no-plusplus": 0,
        "max-len": 0,
        "no-param-reassign": [
            "error",
            {
                props: true,
                ignorePropertyModificationsFor: ["acc", "e", "state"],
            },
        ],
        "no-continue": 0,
        "no-restricted-syntax": 0,
        "no-async-promise-executor": 0,
        "no-mixed-operators": 0,
        "no-unused-expressions": 0,
        "vue/no-v-html": 0,
        camelcase: 0,
    },
};
