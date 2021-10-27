<script setup lang="ts">
import { getHighlighter, setCDN } from 'shiki'
import { onMounted, ref } from 'vue'

const usage = ref('')

onMounted(async () => {
  setCDN('https://unpkg.com/shiki/')
  const highlighter = await getHighlighter({
    theme: 'one-dark-pro',
    langs: ['css'],
  })

  const baseUrl = window.location.href

  const code = `/* declare font face */
@font-face {
  font-family: 'Sarasa Mono TC Nerd Font';
  font-style: normal;
  font-weight: 200;
  src: url('${baseUrl}fonts/sarasa-mono-tc-extralight-nerd-font.woff');
}

@font-face {
  font-family: 'Sarasa Mono TC Nerd Font';
  font-style: italic;
  font-weight: 200;
  src: url('${baseUrl}fonts/sarasa-mono-tc-extralightitalic-nerd-font.woff');
}

@font-face {
  font-family: 'Sarasa Mono TC Nerd Font';
  font-style: normal;
  font-weight: 300;
  src: url('${baseUrl}fonts/sarasa-mono-tc-light-nerd-font.woff');
}

@font-face {
  font-family: 'Sarasa Mono TC Nerd Font';
  font-style: italic;
  font-weight: 300;
  src: url('${baseUrl}fonts/sarasa-mono-tc-lightitalic-nerd-font.woff');
}

@font-face {
  font-family: 'Sarasa Mono TC Nerd Font';
  font-style: normal;
  font-weight: 400;
  src: url('${baseUrl}fonts/sarasa-mono-tc-regular-nerd-font.woff');
}

@font-face {
  font-family: 'Sarasa Mono TC Nerd Font';
  font-style: italic;
  font-weight: 400;
  src: url('${baseUrl}fonts/sarasa-mono-tc-italic-nerd-font.woff');
}

@font-face {
  font-family: 'Sarasa Mono TC Nerd Font';
  font-style: normal;
  font-weight: 600;
  src: url('${baseUrl}fonts/sarasa-mono-tc-semibold-nerd-font.woff');
}

@font-face {
  font-family: 'Sarasa Mono TC Nerd Font';
  font-style: italic;
  font-weight: 600;
  src: url('${baseUrl}fonts/sarasa-mono-tc-semibolditalic-nerd-font.woff');
}

@font-face {
  font-family: 'Sarasa Mono TC Nerd Font';
  font-style: normal;
  font-weight: 700;
  src: url('${baseUrl}fonts/sarasa-mono-tc-bold-nerd-font.woff');
}

@font-face {
  font-family: 'Sarasa Mono TC Nerd Font';
  font-style: italic;
  font-weight: 700;
  src: url('${baseUrl}fonts/sarasa-mono-tc-bolditalic-nerd-font.woff');
}

/* then use 'Sarasa Mono TC Nerd Font' as font-family */
body {
  font-family: 'Sarasa Mono TC Nerd Font';
}
`

  usage.value = highlighter.codeToHtml(code, 'css')
})
</script>

<template>
  <div :class="usage ? 'hidden' : ''">spinner</div>
  <div :class="usage ? '' : 'hidden'" v-html="usage"></div>
</template>
