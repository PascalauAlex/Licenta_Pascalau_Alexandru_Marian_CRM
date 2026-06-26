<template>
  <div class="w-full max-w-md p-6 bg-white border border-gray-100 shadow-sm rounded-2xl">
    <div class="mb-4">
      <h3 class="text-lg font-semibold text-gray-800">Confidence distribution</h3>
    </div>
    <div class="relative w-full h-64">
      <Bar id="leads-confidence-chart" :options="chartOptions" :data="chartData" />
    </div>
  </div>
</template>

<script setup>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import { computed } from 'vue'

ChartJS.register(Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const props = defineProps({
  leads: {
    type: Array,
    default: () => [],
  },
})


const chartData = computed(() => {
  let low = 0 // confidence < 25
  let medium = 0 // confidence 25–70
  let high = 0 // confidence > 70

  for (const lead of props.leads ?? []) {
    const confidence = lead.confidence ?? 0
    if (confidence < 25) low += 1
    else if (confidence <= 70) medium += 1
    else high += 1
  }

  return {
    labels: ['Low (0–24)', 'Medium (25–70)', 'High (71–100)'],
    datasets: [
      {
        data: [low, medium, high],
        backgroundColor: ['#ef4444', '#eab308', '#22c55e'],
        borderRadius: 6,
        borderWidth: 0,
      },
    ],
  }
})

const chartOptions = computed(() => ({
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: { display: false },
  },
  scales: {
    x: {
      grid: { display: false },
      ticks: { font: { size: 13 } },
    },
    y: {
      beginAtZero: true,
      grid: { color: 'rgba(0,0,0,0.05)' },
      ticks: { precision: 0, font: { size: 13 } },
    },
  },
}))
</script>
