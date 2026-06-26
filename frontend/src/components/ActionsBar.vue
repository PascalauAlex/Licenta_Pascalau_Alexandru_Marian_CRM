<template>
  <div
    class="inline-flex items-center bg-white border border-gray-200 shadow-sm rounded-lg px-4 py-2 text-sm w-fit"
  >
    <div class="flex items-center gap-2 pr-4 border-r border-gray-200">
      <slot name="statistics"></slot>
    </div>

    <div class="flex items-center gap-4 pl-4 overflow-x-auto">
      <div class="flex items-center gap-3 ml-2">
        <span class="text-gray-300">|</span>
        <slot name="addNew"></slot>
        <slot name="filter"></slot>
      </div>
    </div>
  </div>
</template>
<script setup>
defineProps({
  addNew: 'String',
})
</script>

<style scoped></style>
