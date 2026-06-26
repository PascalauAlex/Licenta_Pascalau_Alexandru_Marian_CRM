<template>
  <div v-if="totalPages > 1" class="flex items-center justify-between px-1 py-2">
    <span class="text-xs text-body">
      {{ rangeStart }}–{{ rangeEnd }} from {{ totalCount }} leads
    </span>

    <div class="flex items-center gap-1">
      <button
        type="button"
        :disabled="currentPage === 1"
        @click="changePage(currentPage - 1)"
        aria-label="Previous page"
        class="w-8 h-8 flex items-center justify-center rounded-base text-sm font-medium bg-neutral-secondary-medium border border-default-medium hover:bg-neutral-tertiary-medium hover:text-heading focus:outline-none focus:ring-2 focus:ring-neutral-tertiary transition-colors duration-150 select-none disabled:opacity-40 disabled:cursor-not-allowed"
      >
        <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
          <path
            d="M8.5 10.5L5 7l3.5-3.5"
            stroke="currentColor"
            stroke-width="1.5"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </svg>
      </button>

      <template v-for="page in pagesToShow" :key="page">
        <span
          v-if="page === '...'"
          class="w-8 h-8 flex items-center justify-center text-xs text-body select-none"
        >
          ···
        </span>

        <button
          v-else
          type="button"
          @click="changePage(page)"
          :aria-current="page === currentPage ? 'page' : undefined"
          class="w-8 h-8 flex items-center justify-center rounded-base text-sm font-medium border transition-colors duration-150 select-none focus:outline-none focus:ring-2 focus:ring-neutral-tertiary"
          :class="
            page === currentPage
              ? 'bg-blue-600 text-white border-blue-600'
              : 'bg-neutral-secondary-medium border-default-medium hover:bg-neutral-tertiary-medium hover:text-heading'
          "
        >
          {{ page }}
        </button>
      </template>

      <button
        type="button"
        :disabled="currentPage === totalPages"
        @click="changePage(currentPage + 1)"
        aria-label="Next page"
        class="w-8 h-8 flex items-center justify-center rounded-base text-sm font-medium bg-neutral-secondary-medium border border-default-medium hover:bg-neutral-tertiary-medium hover:text-heading focus:outline-none focus:ring-2 focus:ring-neutral-tertiary transition-colors duration-150 select-none disabled:opacity-40 disabled:cursor-not-allowed"
      >
        <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
          <path
            d="M5.5 3.5L9 7l-3.5 3.5"
            stroke="currentColor"
            stroke-width="1.5"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </svg>
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  currentPage: { type: Number, required: true },
  totalCount: { type: Number, required: true },
  pageSize: { type: Number, default: 10 },
})

const emit = defineEmits(['page-change'])

const totalPages = computed(() => Math.ceil(props.totalCount / props.pageSize))
const rangeStart = computed(() => (props.currentPage - 1) * props.pageSize + 1)
const rangeEnd = computed(() => Math.min(props.currentPage * props.pageSize, props.totalCount))

const pagesToShow = computed(() => {
  const total = totalPages.value
  const current = props.currentPage
  const pages = []

  if (total <= 7) {
    for (let i = 1; i <= total; i++) pages.push(i)
    return pages
  }

  pages.push(1)
  if (current > 3) pages.push('...')

  const from = Math.max(2, current - 1)
  const to = Math.min(total - 1, current + 1)
  for (let i = from; i <= to; i++) pages.push(i)

  if (current < total - 2) pages.push('...')
  pages.push(total)
  return pages
})

function changePage(page) {
  if (page < 1 || page > totalPages.value || page === props.currentPage) return
  emit('page-change', page)
}
</script>
