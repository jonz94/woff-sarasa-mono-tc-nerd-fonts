<script setup lang="ts">
import Title from './components/Title.vue'
import Terminal from './components/Terminal.vue'
import Usage from './components/Usage.vue'
</script>

<template>
  <main
    class="flex flex-col justify-center items-center px-0 py-8 lg:px-8 space-y-8 min-h-screen"
  >
    <h1
      class="bg-black text-white p-4 flex flex-col items-center sm:flex-row text-3xl font-bold space-x-0 sm:space-x-[1ch]"
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
