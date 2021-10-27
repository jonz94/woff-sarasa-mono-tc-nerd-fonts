<script setup lang="ts">
import Title from './components/Title.vue'
import Terminal from './components/Terminal.vue'
import Usage from './components/Usage.vue'
</script>

<template>
  <main
    class="flex flex-col justify-center items-center p-8 space-y-8 min-h-screen"
  >
    <Title>Sarasa Mono TC ⨯ Nerd Fonts ⨯ WOFF Fonts</Title>
    <Title>Avaliable styles</Title>
    <div class="text-lg">
      <p class="font-extralight">extralight</p>
      <p class="italic font-extralight">extralight italic</p>
      <p class="font-light">light</p>
      <p class="italic font-light">light italic</p>
      <p>normal</p>
      <p class="italic">italic</p>
      <p class="font-semibold">semibold</p>
      <p class="italic font-semibold">semibold italic</p>
      <p class="font-bold">bold</p>
      <p class="italic font-bold">bold italic</p>
    </div>
    <Title>Showcase</Title>
    <Terminal />
    <Title>Usage</Title>
    <Usage />
  </main>
</template>
