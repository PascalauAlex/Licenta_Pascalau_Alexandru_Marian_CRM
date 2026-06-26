<template>
  <LeadChecklistModal :showCheckList="showChecklist" @close-modal="cancelDrag">
    <LeadCheckList
      v-if="selectedLead"
      :lead="selectedLead"
      @checklist-saved="onChecklistSaved"
    ></LeadCheckList>
  </LeadChecklistModal>

  <div class="flex gap-3 overflow-x-auto pb-4 min-h-[70vh] w-full">
    <div
      v-for="col in boardColumns"
      :key="col.id"
      class="flex-1 min-w-[200px] bg-gray-50 flex flex-col rounded-lg border border-gray-200 shadow-sm"
    >
      <div class="p-3 border-b border-gray-200" :class="col.headerClass">
        <h3 class="font-bold flex justify-between items-center text-sm lg:text-base">
          {{ col.title }}
          <span
            class="bg-white text-gray-600 text-xs px-2 py-1 rounded-full border border-gray-200"
          >
            {{ columns[col.id].length }}
          </span>
        </h3>
      </div>

      <div class="flex-1 p-2 lg:p-3">
        <draggable
          v-model="columns[col.id]"
          group="leads"
          item-key="id"
          class="h-full min-h-[200px]"
          @change="onChange($event, col.id)"
          ghost-class="opacity-50"
          drag-class="cursor-grabbing"
        >
          <template #item="{ element }">
            <div
              class="bg-white p-4 rounded-lg shadow-sm mb-3 border border-gray-200 cursor-grab hover:shadow-md transition-shadow"
            >
              <div class="flex justify-between items-start mb-2">
                <h4 class="font-bold text-blue-900 truncate pr-2" :title="element.company">
                  <router-link :to="{ name: 'SingleLead', params: { id: element.id } }">{{
                    element.company
                  }}</router-link>
                </h4>
                <span
                  :class="[
                    getPriorityColor(element.priority),
                    'text-xs font-bold px-2 py-1 rounded bg-gray-50 border',
                  ]"
                >
                  {{ element.priority }}
                </span>
              </div>

              <div class="text-sm text-gray-600 space-y-1 mb-3">
                <p class="truncate">
                  <span class="font-semibold text-gray-800">Contact person:</span>
                  {{ element.contact_person }}
                </p>
                <p>
                  <span class="font-semibold text-gray-800">Estimated Value:</span>
                  {{ element.estimated_value }} $
                </p>
                <p>
                  <span class="font-semibold text-gray-800">Confidence:</span>
                  {{ element.confidence }} %
                </p>
              </div>

              <div
                class="pt-2 border-t border-gray-100 flex justify-between items-center text-xs text-gray-500"
              >
                <span class="flex items-center gap-1">
                  <svg
                    class="w-4 h-4 text-gray-400"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                    ></path>
                  </svg>
                  {{ getAssignedName(element) }}
                </span>
              </div>
            </div>
          </template>
        </draggable>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import draggable from 'vuedraggable'
import { useLeadStore } from '@/stores/leadStore.js'
import LeadChecklistModal from '@/components/Leads/LeadChecklistModal.vue'
import LeadCheckList from '@/components/Leads/LeadCheckList.vue'

const leadStore = useLeadStore()

const boardColumns = [
  {
    id: 'new',
    title: 'New',
    headerClass: 'bg-blue-500 text-white rounded-t-lg hover:text-blue-600 hover:bg-white',
  },
  {
    id: 'contacted',
    title: 'Contacted',
    headerClass: 'bg-yellow-500 text-white rounded-t-lg hover:text-yellow-500 hover:bg-white',
  },
  {
    id: 'inprogress',
    title: 'In Progress',
    headerClass: 'bg-purple-500 rounded-t-lg hover:text-purple-500 hover:bg-white',
  },
  {
    id: 'won',
    title: 'Won',
    headerClass: 'bg-green-500 rounded-t-lg hover:text-green-500 hover:bg-white',
  },
  {
    id: 'lost',
    title: 'Lost',
    headerClass: 'bg-red-500 rounded-t-lg hover:text-red-500 hover:bg-white',
  },
  {
    id: 'inactive',
    title: 'Inactive',
    headerClass: 'bg-gray-500 rounded-t-lg hover:text-gray-500 hover:bg-white',
  },
]

const showChecklist = ref(false)
const selectedLead = ref(null) // Reține lead-ul pe care facem acțiunea
const intendedStatus = ref('') // Reține statusul unde utilizatorul a tras cardul

const columns = ref({
  new: [],
  contacted: [],
  inprogress: [],
  won: [],
  lost: [],
  inactive: [],
})

// Am scos logica de ordonare într-o funcție separată pentru a o putea refolosi (la undo)
const rebuildColumns = (leads) => {
  columns.value.new = []
  columns.value.contacted = []
  columns.value.inprogress = []
  columns.value.won = []
  columns.value.lost = []
  columns.value.inactive = []

  if (leads && leads.length > 0) {
    leads.forEach((lead) => {
      const status = (lead.status || 'new').toLowerCase().replace(/\s/g, '')
      if (columns.value[status]) {
        columns.value[status].push(lead)
      } else {
        columns.value.new.push(lead)
      }
    })
  }
}

// Watch the changes in the store
watch(
  () => leadStore.leads,
  (newLeads) => {
    rebuildColumns(newLeads)
  },
  { immediate: true, deep: true },
)

const toggleChecklist = () => {
  showChecklist.value = !showChecklist.value
}

// Se declanșează la drop în coloană nouă
const onChange = (event, newStatus) => {
  if (event.added) {
    const lead = event.added.element
    const currentStatus = (lead.status || '').toLowerCase().replace(/\s/g, '')

    if (currentStatus === 'inactive') {
      rebuildColumns(leadStore.leads)
      return
    }

    // Setăm datele temporare și deschidem modalul
    selectedLead.value = lead
    intendedStatus.value = newStatus
    if (lead.status !== 'inactive') {
      toggleChecklist()
    }
  } else {
  }
}

// Funcția de "Undo" dacă se apasă pe X în modal
const cancelDrag = () => {
  toggleChecklist()
  selectedLead.value = null
  intendedStatus.value = ''

  // Reconstruim coloanele direct din store.
  // Deoarece în store nu am salvat încă modificarea, cardul se va întoarce vizual la locul lui.
  rebuildColumns(leadStore.leads)
}

// Se apelează când componenta LeadCheckList emite succesul salvării
const onChecklistSaved = () => {
  // Aici poți apela leadStore pentru a trimite cererea PATCH către backend
  // ex: leadStore.updateStatusWithChecklist(selectedLead.value.id, intendedStatus.value, checklistData)

  toggleChecklist()
  selectedLead.value = null
  intendedStatus.value = ''
}

const getPriorityColor = (priority) => {
  const colors = { low: 'text-green-600', medium: 'text-blue-600', high: 'text-red-600' }
  return colors[priority?.toLowerCase()] || 'text-gray-600'
}

const getAssignedName = (lead) => {
  if (!lead.assigned_to) return 'N/A'
  return lead.assigned_to.last_name && lead.assigned_to.first_name
    ? `${lead.assigned_to.last_name} ${lead.assigned_to.first_name}`
    : lead.assigned_to.username || 'N/A'
}
</script>

<style scoped>
::-webkit-scrollbar {
  height: 8px;
}
::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}
::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}
</style>
