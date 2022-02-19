<script setup lang="ts">
import Title from './components/Title.vue'
import Terminal from './components/Terminal.vue'
import Usage from './components/Usage.vue'
</script>

<template>
  <main
    class="flex min-h-screen flex-col items-center justify-center space-y-8 px-0 py-8 lg:px-8"
  >
    <h1
      class="flex flex-col items-center space-x-0 bg-black p-4 text-3xl font-bold text-white sm:flex-row sm:space-x-[1ch]"
    >
      <span>Sarasa Mono TC</span>
      <span>⨯</span>
      <span>Nerd Fonts</span>
      <span>⨯</span>
      <span>WOFF Fonts</span>
    </h1>
    <Title>Avaliable styles</Title>
    <div class="text-lg">
      <p class="font-extralight">extralight</p>
      <p class="font-extralight italic">extralight italic</p>
      <p class="font-light">light</p>
      <p class="font-light italic">light italic</p>
      <p>normal</p>
      <p class="italic">italic</p>
      <p class="font-semibold">semibold</p>
      <p class="font-semibold italic">semibold italic</p>
      <p class="font-bold">bold</p>
      <p class="font-bold italic">bold italic</p>
    </div>
    <Title>Showcase</Title>
    <Terminal />
    <Title>Usage</Title>
    <Usage />
  </main>
  <footer>
    <div class="p-4 text-center text-white">
      <p>Built with ❤️ by jonz94</p>
    </div>
  </footer>
</template>
