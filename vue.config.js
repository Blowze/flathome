const { defineConfig } = require("@vue/cli-service");
const path = require("path");

module.exports = defineConfig({
    transpileDependencies: true,
    lintOnSave: true,
    configureWebpack: {
        resolve: {
            extensions: [".js", ".scss", ".vue"],
            alias: {
                src: path.resolve("./src"),
                assets: path.resolve("./src/assets"),
                scss: path.resolve("./src/assets/scss"),
                components: path.resolve("./src/components"),
            },
        },
    },
});
