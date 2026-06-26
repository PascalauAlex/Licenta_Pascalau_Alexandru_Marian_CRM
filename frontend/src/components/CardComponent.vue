<template>
  <div
    class="bg-neutral-primary-soft block max-w-sm p-6 border border-default rounded-base shadow-xs hover:bg-neutral-secondary-medium"
  >
    <router-link to="">
      <h5 class="text-2xl/7 font-bold text-blue-950 sm:truncate sm:text-3xl sm:tracking-tight">
        <slot name="title"></slot>
      </h5>
    </router-link>
    <p class="text-body"><slot name="description"></slot></p>
  </div>
</template>
