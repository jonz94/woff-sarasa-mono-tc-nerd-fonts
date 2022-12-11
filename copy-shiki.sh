#!/bin/bash

if [ -d public/shiki ]; then
  exit 0
fi

mkdir -p public/shiki

cp -r -L node_modules/shiki/dist public/shiki/dist
cp -r -L node_modules/shiki/languages public/shiki/languages
cp -r -L node_modules/shiki/themes public/shiki/themes

# resolve "LinkError: WebAssembly.instantiate()" issue
# credit: https://github.com/shikijs/shiki/issues/382#issuecomment-1340178768
cp -L node_modules/vscode-oniguruma/release/onig.wasm public/shiki/dist
