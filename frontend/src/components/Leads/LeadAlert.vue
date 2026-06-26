<template>
  <div
    v-if="importantLeads.length > 0"
    class="bg-red-50 p-5 rounded-xl border border-red-200 mt-6 shadow-sm max-w-100"
  >
    <h3 class="font-bold text-red-700 mb-4 flex items-center gap-2 text-lg">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-6 w-6"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
        stroke-width="2"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
        />
      </svg>
      Leads not contacted for more than 3 days (Attention needed)
      <span
        class="font-bold bg-white p-1 rounded-2xl border-b-red-700 hover:text-black hover:cursor-pointer"
      >
        <button @click="$emit('close-alert')">X</button>
      </span>
    </h3>

    <div class="flex flex-col gap-3">
      <router-link
        v-for="alert in importantLeads"
        :key="alert.id"
        :to="{ name: 'SingleLead', params: { id: alert.id } }"
        class="bg-white p-4 rounded-lg border border-red-100 shadow-sm hover:shadow-md hover:border-red-300 transition-all flex justify-between items-center group cursor-pointer"
      >
        <div>
          <span class="text-sm font-bold text-gray-800 block">{{ alert.company }}</span>
          <span class="text-xs text-gray-500">{{ alert.mesaj }}</span>
        </div>

        <span
          class="text-sm text-red-500 font-bold group-hover:translate-x-1 transition-transform flex items-center gap-1"
        >
          See Details <span class="text-lg">&rarr;</span>
        </span>
      </router-link>
    </div>
  </div>
  <div
    v-else
    class="flex items-center gap-2 text-green-600 bg-green-50 p-3 rounded-lg border border-green-200"
  >
    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
      <path
        fill-rule="evenodd"
        d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
        clip-rule="evenodd"
      />
    </svg>
    <p class="text-sm font-medium">Great job! All the leads are up to date!.</p>
    <button @click="$emit('close-alert')">X</button>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  leads: {
    type: Array, // as a props we get a list of leads
    required: true,
  },
})

defineEmits(['close-alert'])

const importantLeads = computed(() => {
  const threeDays = 3 * 24 * 60 * 60 * 1000

  return props.leads
    .filter((lead) => {
      if (!lead.modified_at) return false

      const modified_date = new Date(lead.modified_at).getTime()
      const timePassed = Date.now() - modified_date

      return timePassed > threeDays && lead.status !== 'won' && lead.status !== 'lost'
    })
    .map((lead) => {
      return {
        id: lead.id,
        company: lead.company,
        mesaj: `${lead.company} needs a follow-up!`,
      }
    })
})
</script>
