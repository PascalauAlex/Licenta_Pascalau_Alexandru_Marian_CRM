<template>
  <div class="bg-white rounded-xl border border-gray-200 p-4 shadow-sm">
    <h3 class="text-sm font-semibold text-gray-700 mb-3">Pipeline stage value</h3>

    <div class="h-72">
      <Bar v-if="items.length" :data="chartData" :options="chartOptions" />
      <div v-else class="h-full flex items-center justify-center">
        <p class="text-sm text-gray-400">No value data!</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const props = defineProps({
  stages: { type: Array, default: () => [] }, // [{ status: 'new', total: 15000 }, ...]
})


const items = computed(() => props.stages ?? [])


const STATUS_LABELS = {
  new: 'New',
  contacted: 'Contacted',
  inprogress: 'In progress',
  won: 'Won',
  lost: 'Lost',
  inactive: 'Inactive',
}

const STATUS_COLORS = {
  new: '#3b82f6',
  contacted: '#6366f1',
  inprogress: '#f59e0b',
  won: '#10b981',
  lost: '#ef4444',
  inactive: '#9ca3af',
}

const fmt = (v) => Number(v ?? 0).toLocaleString('ro-RO') // separator de mii

const chartData = computed(() => ({
  labels: items.value.map((s) => STATUS_LABELS[s.status] ?? s.status),
  datasets: [
    {
      label: 'Value',
      data: items.value.map((s) => Number(s.total ?? 0)), // null -> 0
      backgroundColor: items.value.map((s) => STATUS_COLORS[s.status] ?? '#3b82f6'),
      borderRadius: 4,
      maxBarThickness: 56,
    },
  ],
}))

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: { display: false },
    tooltip: {
      callbacks: {
        label: (ctx) => ` ${fmt(ctx.parsed.y)} RON`,
      },
    },
  },
  scales: {
    x: { grid: { display: false } },
    y: {
      beginAtZero: true,
      grid: { color: '#f3f4f6' },
      ticks: { callback: (v) => fmt(v) }, // 15.000 in loc de 15000
    },
  },
}
</script>
