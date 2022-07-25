#!/bin/bash

mkdir -p dist/node_modules/shiki

cp -r -L node_modules/shiki/dist dist/node_modules/shiki/dist
cp -r -L node_modules/shiki/languages dist/node_modules/shiki/languages
cp -r -L node_modules/shiki/themes dist/node_modules/shiki/themes
