<template>
  <div class="bg-white rounded-xl border border-gray-200 p-4 shadow-sm">
    <h3 class="text-sm font-semibold text-gray-700 mb-3">Leads per team member</h3>
    <div class="h-72">
      <Bar v-if="items.length" :data="chartData" :options="chartOptions" />
      <div v-else class="h-full flex items-center justify-center">
        <p class="text-sm text-gray-400">No assigned member.</p>
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
  members: { type: Array, default: () => [] },
})
const items = computed(() => props.members ?? [])

const chartData = computed(() => ({
  labels: items.value.map((m) => m.name),
  datasets: [
    {
      label: 'leads',
      data: items.value.map((m) => m.count),
      backgroundColor: '#2563eb',
      borderRadius: 4,
      maxBarThickness: 48,
    },
  ],
}))

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
   indexAxis: 'y',
  plugins: {
    legend: { display: false },
    tooltip: { callbacks: { label: (ctx) => ` ${ctx.parsed.y ?? ctx.parsed.x} lead-uri` } },
  },
  scales: {
    x: { grid: { display: false } },
    y: { beginAtZero: true, ticks: { precision: 0 }, grid: { color: '#f3f4f6' } },
  },
}
</script>
