<template>
  <div>
    <button
      @click="isExportModalOpen = true"
      class="inline-flex items-center gap-2 bg-white border border-gray-300 hover:bg-gray-50 text-gray-700 font-medium py-2 px-4 rounded-lg shadow-sm transition-colors text-sm"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="size-4"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M3 16.5v2.25A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75V16.5M16.5 12 12 16.5m0 0L7.5 12m4.5 4.5V3"
        />
      </svg>
      Export
    </button>

    <DefaultModal :modalActive="isExportModalOpen" @close-modal="isExportModalOpen = false">
      <div class="mb-6">
        <h2 class="text-xl font-bold text-gray-900">Export Leads</h2>
        <p class="text-sm text-gray-500 mt-1">Select the format for exporting the data.</p>
      </div>

      <div class="grid grid-cols-3 gap-4 mb-8">
        <label
          class="relative flex flex-col items-center p-4 border rounded-xl cursor-pointer hover:bg-gray-50 transition-all"
          :class="
            selectedFormat === 'csv'
              ? 'border-blue-600 bg-blue-50/50 ring-1 ring-blue-600'
              : 'border-gray-200'
          "
        >
          <input type="radio" value="csv" v-model="selectedFormat" class="sr-only" />
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="size-8 text-green-600 mb-2"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            stroke-width="1.5"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m6.75 12-3-3m0 0-3 3m3-3v6m-1.5-15H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z"
            />
          </svg>
          <span class="font-bold text-gray-800 text-sm">.CSV</span>
          <span class="text-xs text-gray-500 mt-1 text-center">Excel / Sheets</span>
        </label>
        <div>
          <label
            class="relative flex flex-col items-center p-4 border rounded-xl cursor-pointer hover:bg-gray-50 transition-all"
            :class="
              selectedFormat === 'xlsx'
                ? 'border-blue-600 bg-blue-50/50 ring-1 ring-blue-600'
                : 'border-gray-200'
            "
          >
            <input type="radio" value="xlsx" v-model="selectedFormat" class="sr-only" />
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="size-8 text-emerald-500 mb-2"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="1.5"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 0 1 3 19.875v-6.75ZM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 0 1-1.125-1.125V8.625ZM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 0 1-1.125-1.125V4.125Z"
              />
            </svg>
            <span class="font-bold text-gray-800 text-sm">.XLSX</span>
            <span class="text-xs text-gray-500 mt-1 text-center">Native format</span>
          </label>
        </div>
        <div>

          <label
            class="relative flex flex-col items-center p-4 border rounded-xl cursor-pointer hover:bg-gray-50 transition-all"
            :class="
              selectedFormat === 'pdf'
                ? 'border-blue-600 bg-blue-50/50 ring-1 ring-blue-600'
                : 'border-gray-200'
            "
          >
            <input type="radio" value="pdf" v-model="selectedFormat" class="sr-only"  />
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="size-8 text-red-500 mb-2"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="1.5"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m0 12.75h7.5m-7.5-3H12m-3.75 15.75h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z"
              />
            </svg>
            <span class="font-bold text-gray-800 text-sm">.PDF</span>
            <span class="text-xs text-gray-500 mt-1 text-center">For report</span>
          </label>
        </div>
      </div>

      <div class="flex justify-end gap-3 pt-4 border-t border-gray-100">
        <button
          @click="isExportModalOpen = false"
          class="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 hover:bg-gray-50 rounded-lg transition-colors"
        >
          Cancel
        </button>

        <button
          @click="handleExport"
          class="px-5 py-2 text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 rounded-lg transition-colors shadow-sm flex items-center gap-2"
        >
          Download
          <span class="uppercase">({{ selectedFormat }})</span>
        </button>
      </div>
    </DefaultModal>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import DefaultModal from '@/components/Modals/DefaultModal.vue'
import api from '@/utils/api.js'
import { useToast } from 'vue-toast-notification'

//Controling the modal visibility
const isExportModalOpen = ref(false)
const toast = useToast()

//Default format is csv
const selectedFormat = ref('csv')

const props = defineProps({
  leads: {
    type: [Array],
    required: true,
  },
})

const emit = defineEmits(['export'])

function handleExport() {
  emit('export', selectedFormat.value)
  isExportModalOpen.value = false
}


</script>
