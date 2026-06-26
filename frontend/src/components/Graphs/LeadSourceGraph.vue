<template>
  <div class="bg-white rounded-xl border border-gray-200 p-4 shadow-sm">
    <h3 class="text-sm font-semibold text-gray-700 mb-3">Leads after source</h3>
    <div class="h-72">
      <Bar v-if="props.sources.length" :data="chartData" :options="chartOptions" />
      <div v-else class="h-full flex items-center justify-center">
        <p class="text-sm text-gray-400">No data for the sources.</p>
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
  sources: {
    type: Array,
    default: () => [],
  },
})


const chartData = computed(() => ({
  labels: props.sources.map((s) => s.source),
  datasets: [
    {
      label: 'Number of leads',
      data: props.sources.map((s) => s.count),
      backgroundColor: '#2563eb',
      hoverBackgroundColor: '#1d4ed8',
      borderRadius: 4,
      maxBarThickness: 48,
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
        label: (ctx) => ` ${ctx.parsed.y} leads`,
      },
    },
  },
  scales: {
    x: { grid: { display: false } },
    y: {
      beginAtZero: true,
      ticks: { precision: 0 },
      grid: { color: '#f3f4f6' },
    },
  },
}
</script>
