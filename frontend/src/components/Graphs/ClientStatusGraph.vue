<template>
  <div class="bg-white rounded-xl border border-gray-200 p-4 shadow-sm">
    <h3 class="text-sm font-semibold text-gray-700 mb-3">Client status distribution</h3>

    <div class="h-72">
      <Doughnut v-if="items.length" :data="chartData" :options="chartOptions" />
      <div v-else class="h-full flex items-center justify-center">
        <p class="text-sm text-gray-400">No clients to show</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { Doughnut } from 'vue-chartjs'
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'

// ATENTIE: doughnut/pie folosesc ArcElement, NU BarElement.
// Si NU au scale (nu e cartezian) -> fara CategoryScale/LinearScale.
ChartJS.register(ArcElement, Tooltip, Legend)

const props = defineProps({
  statuses: { type: Array, default: () => [] }, // [{ status: 'active', count: 12 }, ...]
})

// defensiva null/undefined - lectia de la bug-ul cu sursele
const items = computed(() => props.statuses ?? [])

// paleta indexata pe pozitie (nu stiu ce statusuri ai pe Client - vezi nota de jos)
const PALETTE = [
  '#3b82f6',
  '#10b981',
  '#f59e0b',
  '#ef4444',
  '#6366f1',
  '#8b5cf6',
  '#14b8a6',
  '#9ca3af',
]

// capitalizare simpla: 'active' -> 'Active'
const label = (s) => (s ? s.charAt(0).toUpperCase() + s.slice(1) : '—')

const chartData = computed(() => ({
  labels: items.value.map((s) => label(s.status)),
  datasets: [
    {
      data: items.value.map((s) => s.count),
      backgroundColor: items.value.map((_, i) => PALETTE[i % PALETTE.length]),
      borderWidth: 2,
      borderColor: '#fff',
    },
  ],
}))

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  cutout: '60%', // grosimea inelului
  plugins: {
    legend: { position: 'right' }, // doughnut-ul ARE nevoie de legenda (altfel nu stii ce e fiecare felie)
    tooltip: {
      callbacks: {
        label: (ctx) => {
          const total = ctx.dataset.data.reduce((a, b) => a + b, 0)
          const pct = total ? Math.round((ctx.parsed / total) * 100) : 0
          return ` ${ctx.label}: ${ctx.parsed} (${pct}%)`
        },
      },
    },
  },
}
</script>
