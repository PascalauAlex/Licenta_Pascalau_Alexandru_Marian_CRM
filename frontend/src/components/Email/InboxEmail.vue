<script setup>
import { ref, onMounted, computed } from 'vue'
import { storeToRefs } from 'pinia'
import formatDate from '/services/formatDate.js'
import { useEmailStore } from '@/utils/emailStore.js'

const props = defineProps({
  leadId: { type: [String, Number], default: null },
  clientId: { type: [String, Number], default: null },
})

const emailStore = useEmailStore()
const { leadEmails, clientEmails, isLoading, error } = storeToRefs(emailStore)

const isLead = computed(() => !!props.leadId)
const emails = computed(() => (isLead.value ? leadEmails.value : clientEmails.value))

const expandedEmailId = ref(null)
const isComposeOpen = ref(false)

const toggleEmail = (id) => {
  expandedEmailId.value = expandedEmailId.value === id ? null : id
}

const loadEmailHistory = async () => {
  if (isLead.value) {
    await emailStore.fetchLeadEmails(props.leadId)
  } else {
    await emailStore.fetchClientEmails(props.clientId)
  }
}

onMounted(async () => {
  await loadEmailHistory()
})
</script>

<template>
  <div class="flex flex-col h-full">
    <div class="flex items-center justify-between mb-4 pb-2 border-b border-gray-100">
      <h3 class="text-lg font-semibold text-gray-800 flex items-center gap-2">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="w-5 h-5 text-blue-600"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M21.75 6.75v10.5a2.25 2.25 0 0 1-2.25 2.25h-15a2.25 2.25 0 0 1-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25m19.5 0v.243a2.25 2.25 0 0 1-1.07 1.916l-7.5 4.615a2.25 2.25 0 0 1-2.36 0L3.32 8.91a2.25 2.25 0 0 1-1.07-1.916V6.75"
          />
        </svg>
        Mail Inbox
      </h3>
      <div class="flex items-center gap-3">
        <button
          @click="loadEmailHistory"
          class="text-xs text-blue-600 hover:text-blue-800 flex items-center gap-1 transition-colors"
        >
          <svg
            :class="{ 'animate-spin': isLoading }"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="2"
            stroke="currentColor"
            class="w-4 h-4"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0 3.181 3.183a8.25 8.25 0 0 0 13.803-3.7M4.031 9.865a8.25 8.25 0 0 1 13.803-3.7l3.181 3.182m0-4.991v4.99"
            />
          </svg>
          Refresh
        </button>
        <button
          @click="isComposeOpen = !isComposeOpen"
          class="text-xs flex items-center gap-1 px-3 py-1.5 rounded-lg transition-colors"
          :class="
            isComposeOpen ? 'bg-gray-100 text-gray-600' : 'bg-blue-600 text-white hover:bg-blue-700'
          "
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="2"
            stroke="currentColor"
            class="w-3.5 h-3.5"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M16.862 4.487l1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L6.832 19.82a4.5 4.5 0 0 1-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 0 1 1.13-1.897L16.863 4.487Z"
            />
          </svg>
          {{ isComposeOpen ? 'Închide' : 'Compose' }}
        </button>
      </div>
    </div>

    <div v-if="isLoading" class="flex justify-center items-center py-8">
      <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
    </div>

    <div v-else-if="error" class="text-sm text-red-500 bg-red-50 p-3 rounded-lg text-center">
      {{ error }}
    </div>

    <div v-else-if="emails?.length === 0" class="text-center py-10 flex flex-col items-center">
      <div class="bg-gray-50 p-3 rounded-full mb-3">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="w-6 h-6 text-gray-400"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M2.25 13.5h3.86a2.25 2.25 0 0 1 2.012 1.244l.256.512a2.25 2.25 0 0 0 2.013 1.244h3.218a2.25 2.25 0 0 0 2.013-1.244l.256-.512a2.25 2.25 0 0 1 2.013-1.244h3.859m-19.5.338V18a2.25 2.25 0 0 0 2.25 2.25h15A2.25 2.25 0 0 0 21.75 18v-4.162c0-.224-.034-.447-.1-.661L19.24 5.338a2.25 2.25 0 0 0-2.15-1.588H6.911a2.25 2.25 0 0 0-2.15 1.588L2.35 13.177a2.25 2.25 0 0 0-.1.661Z"
          />
        </svg>
      </div>
      <p class="text-sm text-gray-500">No emails sent to this {{ isLead ? 'lead' : 'client' }}.</p>
    </div>

    <div v-else class="flex-1 overflow-y-auto pr-2 space-y-3 custom-scrollbar">
      <div
        v-for="email in emails"
        :key="email.id"
        class="border border-gray-100 rounded-lg overflow-hidden transition-all duration-200"
        :class="
          expandedEmailId === email.id ? 'bg-blue-50/30 shadow-sm' : 'bg-white hover:bg-gray-50'
        "
      >
        <div @click="toggleEmail(email.id)" class="p-3 cursor-pointer flex items-start gap-3">
          <div class="mt-1">
            <div
              class="w-8 h-8 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center font-bold text-xs"
            >
              {{ email.to_email.charAt(0).toUpperCase() }}
            </div>
          </div>
          <div class="flex-1 min-w-0">
            <div class="flex justify-between items-start mb-0.5">
              <h4 class="text-sm font-semibold text-gray-800 truncate pr-2">{{ email.subject }}</h4>
              <span class="text-[11px] text-gray-500 whitespace-nowrap">{{
                formatDate(email.created_at)
              }}</span>
            </div>
            <p class="text-xs text-gray-500 truncate">Către: {{ email.to_email }}</p>
          </div>
        </div>
        <div
          v-show="expandedEmailId === email.id"
          class="px-4 pb-4 pt-1 border-t border-gray-100/50"
        >
          <div class="bg-white p-3 rounded border border-gray-100 mt-2">
            <p class="text-sm text-gray-700 whitespace-pre-wrap leading-relaxed">
              {{ email.message_body }}
            </p>
          </div>
          <div class="mt-2 flex justify-end">
            <span
              class="inline-flex items-center px-2 py-0.5 rounded text-[10px] font-medium"
              :class="
                email.status === 'sent' || email.status === 'delivered'
                  ? 'bg-green-100 text-green-800'
                  : 'bg-yellow-100 text-yellow-800'
              "
            >
              Status: {{ email.status }}
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- COMPOSE -->
    <div v-if="isComposeOpen" class="border-t border-gray-100 pt-4 mt-4">
      <slot name="compose" />
    </div>
  </div>
</template>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
  width: 6px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background-color: #e5e7eb;
  border-radius: 20px;
}
.custom-scrollbar:hover::-webkit-scrollbar-thumb {
  background-color: #d1d5db;
}
</style>
