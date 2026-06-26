<template>
  <div class="h-[600px] bg-white rounded-xl shadow-md p-4 border border-gray-100 flex flex-col">
    <v-calendar v-model="focusDate" :view-mode="props.type" :events="props.events">
      <template #event="{ event }">
        <div
          :class="[
            'w-full h-full px-2 py-1 rounded-md text-xs font-semibold truncate cursor-pointer transition-all shadow-sm hover:shadow-md hover:scale-[1.02]',
            getEventColorClass(event.color || (event.raw && event.raw.color)),
          ]"
        >
          {{ event.title || (event.raw && event.raw.title) }}
        </div>
      </template>
    </v-calendar>
  </div>
</template>

<script setup>
import { defineProps, ref } from 'vue'

const focusDate = ref(new Date())

const props = defineProps({
  events: {
    type: Array,
    default: () => [],
  },
  type: {
    type: String,
    default: 'month',
  },
})

const getEventColorClass = (colorName) => {
  const colorMap = {
    orange: 'bg-orange-100 text-orange-700 border border-orange-300',
    purple: 'bg-purple-100 text-purple-700 border border-purple-300',
    blue: 'bg-blue-100 text-blue-700 border border-blue-300',
    green: 'bg-green-100 text-green-700 border border-green-300',
    red: 'bg-red-100 text-red-700 border border-red-300',
  }

  return colorMap[colorName] || 'bg-blue-100 text-blue-700 border border-blue-300'
}
</script>

<style scoped>

:deep(.v-calendar-month__day--today .v-btn) {
  background-color: #2563eb !important;
  color: white !important;
  font-weight: bold !important;
}


:deep(.v-calendar-weekly__day--today .v-btn),
:deep(.v-calendar-day--today .v-btn),
:deep(.v-calendar-header__day--today .v-btn) {
  background-color: #2563eb !important;
  color: white !important;
  font-weight: bold !important;
}


:deep(.v-calendar-month__day--today) {
  background-color: transparent !important;
}
</style>
