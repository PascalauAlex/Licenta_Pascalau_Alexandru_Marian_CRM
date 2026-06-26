<template>
  <div v-if="leadStore.loading">Loading...</div>
  <div>
    <div class="mb-5">
      <h1 class="font-bold text-2xl">Leads Statistics</h1>
    </div>
    <div class="flex mb-2">
      <div class="shadow-sm rounded-lg bg-white p-2 w-1/4 mr-2 h-full">
        <router-link :to="{ name: 'LeadsView' }">
          <div
            class="h-1/2 rounded-lg p-2 bg-blue-100 cursor-pointer border border-blue-100 hover:border-blue-300"
          >
            <h3 class="font-bold bg-blue-300 rounded-lg p-2">Leads</h3>
            <p class="font-semibold p-2">
              Total leads: <span class="bg-blue-300 rounded-lg p-2">{{ total_leads }}</span>
            </p>
          </div>
        </router-link>
        <div class="m-1"></div>
        <router-link :to="{ name: 'Clients' }">
          <div
            class="h-1/2 p-2 rounded-lg bg-amber-100 border border-amber-100 hover:border-amber-300"
          >
            <h3 class="font-bold bg-amber-300 rounded-lg p-2">Clients</h3>
            <p class="font-semibold p-2">
              Total clients: <span class="bg-amber-300 rounded-lg p-2">{{ total_clients }}</span>
            </p>
          </div>
        </router-link>
      </div>
      <div class="shadow-sm rounded-lg bg-white p-2 w-1/4">
        <router-link :to="{ name: 'TeamView' }">
          <div class="h-1/2 bg-red-100 border border-red-100 hover:border-red-300 rounded-lg p-2">
            <h3 class="font-bold bg-red-300 rounded-lg p-2">Team</h3>
            <p class="font-semibold p-2">
              Total members: <span class="bg-red-300 rounded-lg p-2">{{ total_members }}</span>
            </p>
          </div>
        </router-link>
        <div class="m-1"></div>
        <router-link :to="{ name: 'Tasks' }">
          <div
            class="h-1/2 p-2 rounded-lg bg-purple-100 border border-purple-100 hover:border-purple-300"
          >
            <h3 class="font-bold bg-purple-300 rounded-lg p-2">Tasks</h3>
            <p class="font-semibold p-2">
              Total tasks: <span class="bg-purple-300 rounded-lg p-2">{{ total_tasks }}</span>
            </p>
          </div>
        </router-link>
      </div>
    </div>
    <div class="flex flex-row gap-4">
      <DoughnutGraph :leads="leadStore.allLeads" />
      <ConfidenceChart :leads="leadStore.allLeads" />
      <WonLeads :leads="leadStore.allLeads"></WonLeads>
      <LeadSourceGraph :sources="leadSourcesCount"></LeadSourceGraph>
      <PipelineValueGraph :stages="pipelineByStage"></PipelineValueGraph>
    </div>
    <div class="w-full flex gap-4">
      <div class="w-1/3 shadow-sm text-lg mt-2 bg-white rounded-lg p-2">
        <h3 class="font-bold">Value of won leads</h3>
        <p class="font-semibold text-green-600">Won leads</p>
        <span class="font-bold text-xl pl-2">-> {{ wonStats.wonLeadsCount }}</span>
        <p class="font-semibold text-green-600">Total Value</p>
        <span class="font-bold text-xl inline-flex">-> {{ wonStats.totalValue }} </span>
      </div>

      <div class="w-1/3 shadow-sm text-lg mt-2 bg-white p-2 rounded-lg">
        <h3 class="font-bold">Inactive leads</h3>
        <p class="font-semibold text-gray-600">
          Number of inactive leads -> <span>{{ inactiveStats.inactiveLeadsCount }}</span>
        </p>
        <h3 class="font-bold">Conversion rate</h3>
        <span class="font-bold text-xl text-green-600">-> {{ conversion_rate?.toFixed(1) }}%</span>
      </div>
      <div
        class="w-1/3 shadow-sm text-lg mt-2 rounded-lg p-2 transition-colors"
        :class="
          staleLeads > 0 ? 'bg-amber-50 border border-amber-200' : 'bg-white border border-gray-100'
        "
      >
        <h3 class="font-bold">Stale leads</h3>
        <p class="font-semibold text-sm text-gray-500">Open, not contacted in 14+ days</p>
        <span
          class="font-bold text-2xl pl-2"
          :class="staleLeads > 0 ? 'text-amber-600' : 'text-green-600'"
        >
          -> {{ staleLeads }}
        </span>
        <p v-if="staleLeads > 0" class="text-sm text-amber-700 mt-1">Attention needed</p>
      </div>
    </div>
    <div class="w-full mt-2 flex">
      <div class="w-1/2"><ClientStatusGraph :statuses="clientStatusCount"></ClientStatusGraph></div>
      <div class="w-1/2 ml-2"><MemberLeadsGraph :members="memberLeads"></MemberLeadsGraph></div>
    </div>
  </div>
</template>
<script setup>
import DoughnutGraph from '@/components/Graphs/DoughnutGraph.vue'
import { useLeadStore } from '@/stores/leadStore.js'
import { computed, onMounted, ref } from 'vue'
import ConfidenceChart from '@/components/ConfidenceChart.vue'
import { useToast } from 'vue-toast-notification'

import api from '@/utils/api.js'
import WonLeads from '@/components/Graphs/WonLeads.vue'
import LeadSourceGraph from '@/components/Graphs/LeadSourceGraph.vue'
import PipelineValueGraph from '@/components/Graphs/PipelineValueGraph.vue'
import ClientStatusGraph from '@/components/Graphs/ClientStatusGraph.vue'
import MemberLeadsGraph from '@/components/Graphs/MemberLeadsGraph.vue'

const leadStore = useLeadStore()

const toast = useToast()
const statistics = ref({})
const wonStats = computed(() => wonLeads(leadStore.allLeads))
const inactiveStats = computed(() => inactiveLeads(leadStore.allLeads))

const conversion_rate = ref(null)
const total_leads = ref(null)
const total_clients = ref(null)
const total_members = ref(null)
const total_tasks = ref(null)
const leadSourcesCount = ref([])
const pipelineByStage = ref([])
const clientStatusCount = ref([])
const memberLeads = ref([])
const topMember = computed(() => memberLeads.value[0] ?? null)
const staleLeads = ref(0)

onMounted(async () => {
  try {
    const resp = await api.get('api/v1/dashboard-statistics')
    await leadStore.fetchAllLeads()
    console.log(resp.data)
    statistics.value = resp.data
    extractStats(resp.data)

    toast.success('Resources loaded succesfully!')
  } catch (err) {
    toast.error('Error while fetching resources!')
    console.error(err)
  }
})
const inactiveLeads = (leads) => {
  let inactiveLeadsCount = 0
  for (let lead of leads) {
    if (lead.status == 'inactive') {
      inactiveLeadsCount++
    }
  }
  return { inactiveLeadsCount }
}

const wonLeads = (leads) => {
  let wonLeadsCount = 0
  let totalValue = 0
  for (let lead of leads) {
    if (lead.status == 'won') {
      wonLeadsCount++
      totalValue = lead.estimated_value + totalValue
    }
  }

  return { wonLeadsCount, totalValue }
}

const extractStats = (data) => {
  //Leads stats
  total_leads.value = data.lead_stats.total_leads
  conversion_rate.value = data.lead_stats.conversion_rate
  leadSourcesCount.value = data.lead_stats.lead_sources_count
  pipelineByStage.value = data.lead_stats.lead_value_by_stage
  memberLeads.value = data.lead_stats.lead_count_by_member
  staleLeads.value = data.lead_stats.stale_leads

  //Client stats
  total_clients.value = data.clients_stats.total_clients
  clientStatusCount.value = data.clients_stats.client_statuses_count

  //Team stats
  total_members.value = data.teams_stats.total_members

  //Task stats
  total_tasks.value = data.tasks_stats.total_tasks
}
</script>
