<template>
  <div v-if="!leads">
    <Line :data="chartData" :options="chartOptions"></Line>
  </div>
</template>

<script setup>
import { Line } from 'vue-chartjs'
import { onBeforeMount, onMounted, ref } from 'vue'
import {
  CategoryScale,
  Chart as ChartJS,
  Filler,
  LinearScale,
  LineElement,
  PointElement,
  Tooltip,
} from 'chart.js'
ChartJS.register(LineElement, PointElement, CategoryScale, LinearScale, Filler, Tooltip)

const props = defineProps({
  leads: {
    type:Array,
    default: () => [],
    required: true,
  },
})

const chartData = ref({})
const chartOptions = ref({})

onBeforeMount(() => {
  chartData.value = props.leads
})
onMounted(() => {
  console.log(chartData.value)
})
</script>

<style scoped></style>
