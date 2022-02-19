<script setup lang="ts">
import Prompt from './TerminalPrompt.vue'
</script>

<template>
  <div class="w-screen overflow-hidden lg:w-auto">
    <div class="overflow-auto">
      <div
        class="flex h-64 min-w-max flex-col self-baseline rounded-none p-2 text-xl leading-tight lg:self-center lg:rounded"
        style="background: #121212"
      >
        <p class="inline-flex">
          <Prompt />
        </p>
        <p class="inline-flex">
          <span
            class="w-[1ch]"
            style="background: #dcdfe4; color: #dcdfe4"
          ></span>
          <span style="background: #121212; color: #dcdfe4"> </span>
          <span class="px-[1ch]" style="background: #121212; color: #a7cb8b">
            echo
          </span>
          <span style="background: #121212; color: white">
            Hello from terminal!
          </span>
        </p>
        <p class="inline-flex">
          <span style="background: #121212; color: white">
            Hello from terminal!
          </span>
        </p>
        <p class="inline-flex">
          <Prompt />
        </p>
        <p class="inline-flex">
          <span
            class="w-[1ch]"
            style="background: #dcdfe4; color: #dcdfe4"
          ></span>
          <span style="background: #121212; color: #dcdfe4"> </span>
        </p>
      </div>
    </div>
  </div>
</template>
