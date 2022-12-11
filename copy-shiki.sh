#!/bin/bash

if [ -d public/shiki ]; then
  exit 0
fi

mkdir -p public/shiki

cp -r -L node_modules/shiki/dist public/shiki/dist
cp -r -L node_modules/shiki/languages public/shiki/languages
cp -r -L node_modules/shiki/themes public/shiki/themes
