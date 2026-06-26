<template>
  <div class="w-full max-w-md p-6 bg-white border border-gray-100 shadow-sm rounded-2xl">
    <div class="mb-4">
      <h3 class="text-lg font-semibold text-gray-800">Status distribution</h3>
    </div>
    <div class="relative w-full h-64">
      <Doughnut id="leads-status-chart" :options="chartOptions" :data="chartData" />
    </div>
  </div>
</template>

<script setup>
import { Doughnut } from 'vue-chartjs'
import { Chart as ChartJS, Tooltip, Legend, ArcElement } from 'chart.js'
import { computed } from 'vue'

ChartJS.register(Tooltip, Legend, ArcElement)

const props = defineProps({
  leads: {
    type: Array,
    default: () => [],
  },
})

// numărătoarea trăiește în computed → reactivă la props.leads
const chartData = computed(() => {
  const c = { new: 0, contacted: 0, inprogress: 0, won: 0, lost: 0 }
  for (const lead of props.leads ?? []) {
    if (lead.status === 'new') c.new += 1
    else if (lead.status === 'contacted') c.contacted += 1
    else if (lead.status === 'inprogress') c.inprogress += 1
    else if (lead.status === 'won') c.won += 1
    else c.lost += 1 // orice altceva (inclusiv 'lost') intră aici
  }

  return {
    labels: ['New', 'Contacted', 'In progress', 'Won', 'Lost'],
    datasets: [
      {
        data: [c.new, c.contacted, c.inprogress, c.won, c.lost],
        backgroundColor: [
          '#3b82f6', // blue-500
          '#eab308', // yellow-500
          '#a855f7', // purple-500
          '#22c55e', // green-500
          '#ef4444', // red-500
        ],
        borderWidth: 0,
        hoverOffset: 6,
      },
    ],
  }
})

const chartOptions = computed(() => ({
  responsive: true,
  maintainAspectRatio: false,
  cutout: '80%',
  plugins: {
    legend: {
      position: 'bottom',
      labels: {
        usePointStyle: true,
        padding: 20,
        font: { size: 13 },
      },
    },
  },
}))
</script>
