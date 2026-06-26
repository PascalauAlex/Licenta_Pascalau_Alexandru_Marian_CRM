<template>
  <div>
    <div class="flex items-center gap-6 mb-8">
      <h1 class="font-bold tracking-tight text-heading md:text-5xl lg:text-4xl">Clients</h1>

      <div
        class="flex items-center bg-white border border-gray-200 shadow-sm rounded-xl px-4 py-2 text-sm"
      >
        <div class="flex items-center gap-2 pr-4 border-r border-gray-200">
          <span class="text-gray-500 font-medium">Total:</span>
          <span class="font-bold text-blue-600 bg-blue-50 px-2 py-0.5 rounded-md">
            {{ clientStore.clients.length }}
          </span>
        </div>

        <div class="flex items-center gap-4 pl-4 overflow-x-auto">
          <div
            v-for="(count, status) in clientStatusCounts"
            :key="status"
            class="flex items-center gap-1.5 whitespace-nowrap"
          >
            <span class="text-gray-500 capitalize">{{ status }}:</span>
            <span class="font-bold text-gray-700">{{ count }}</span>
          </div>

          <div class="flex items-center gap-3 ml-2">
            <span class="text-gray-300">|</span>

            <ExportModal :leads="clientStore.clients" @export="exportClients" />

            <router-link
              :to="{ name: 'AddClient' }"
              class="inline-flex items-center gap-1.5 bg-white border border-gray-300 hover:bg-gray-50 text-gray-700 font-medium py-1.5 px-3 rounded-md shadow-sm transition-colors text-sm"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="2"
                stroke="currentColor"
                class="w-4 h-4"
              >
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
              </svg>
              Add Client
            </router-link>
            <button
              class="inline-flex items-center gap-1.5 bg-white border border-gray-300 hover:bg-gray-50 text-gray-700 font-medium py-1.5 px-3 rounded-md shadow-sm transition-colors text-sm"
              @click="toggleFilter"
            >
              <svg
                class="w-4 h-4"
                aria-hidden="true"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
              >
                <path
                  stroke="currentColor"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M18.796 4H5.204a1 1 0 0 0-.753 1.659l5.302 6.058a1 1 0 0 1 .247.659v4.874a.5.5 0 0 0 .2.4l3 2.25a.5.5 0 0 0 .8-.4v-7.124a1 1 0 0 1 .247-.659l5.302-6.059c.566-.646.106-1.658-.753-1.658Z"
                />
              </svg>
              Filter
            </button>
          </div>
        </div>
      </div>
    </div>

    <transition
      enter-active-class="transition duration-300 ease-out"
      enter-from-class="transform -translate-y-4 opacity-0"
      enter-to-class="transform translate-y-0 opacity-100"
      leave-active-class="transition duration-200 ease-in"
      leave-from-class="transform translate-y-0 opacity-100"
      leave-to-class="transform -translate-y-4 opacity-0"
    >
      <div v-if="showFilter" class="mb-4 flex items-center gap-3 shadow-sm p-3 rounded-lg bg-white">
        <label class="font-bold text-lg text-blue-900">Name: </label>
        <input
          v-model="searchQuery"
          @keyup.enter="performSearch"
          type="text"
          placeholder="Search by name..."
          class="border border-gray-300 rounded-lg px-4 py-2 w-full max-w-sm focus:ring-2 focus:ring-blue-700 focus:outline-none"
        />
        <label class="font-bold text-lg">Status</label>
        <select v-model="statusQuery"  class="rounded-lg border-gray-200 shadow-sm" @change="performSearch">
             <option v-for="s in statuses" :key="s.value" :value="s.value">
               {{s.label}}
             </option>
        </select>
        <button
          @click="performSearch"
          class="bg-blue-900 text-white px-5 py-2 rounded-lg hover:bg-blue-700 transition "
        >
          Search
        </button>

        <button
          @click="clearSearch"
          class="text-gray-700 outline-1 rounded-lg hover:text-red-600 px-3 py-2 transition align-end"
        >
          Reset
        </button>
      </div>
    </transition>

    <div v-if="clientStore.loading">
      <h3>Loading...</h3>
    </div>

    <div v-else>
      <div class="relative overflow-x-auto bg-white shadow-xs rounded-base border border-default">
        <table class="w-full text-sm text-left rtl:text-right text-body">
          <thead
            class="text-sm text-body bg-neutral-secondary-medium border-b border-default-medium"
          >
            <tr>
              <th scope="col" class="px-6 py-3 font-bold">Name</th>
              <th scope="col" class="px-6 py-3 font-bold">Status</th>
              <th scope="col" class="px-6 py-3 font-bold">Contact person</th>
              <th scope="col" class="px-6 py-3 font-bold">Email</th>
              <th scope="col" class="px-6 py-3 font-bold">Phone</th>
            </tr>
          </thead>
          <tbody>
            <tr
              class="bg-neutral-primary-soft border-b border-default hover:bg-neutral-secondary-medium hover:bg-gray-100 hover:cursor-pointer"
              v-for="client in clientStore.clients"
              :key="client.id"
              id="table-hover"
              @click="router.push({ name: 'SingleClient', params: { id: client.id } })"
            >
              <th scope="row" class="px-6 py-4 font-medium text-heading whitespace-nowrap">
                <div class="flex items-center gap-3">
                  <img
                    v-if="client.profile_picture"
                    :src="client.profile_picture"
                    alt="Profile Picture"
                    class="w-8 h-8 rounded-full object-cover border border-gray-200 shadow-sm"
                  />
                  <div
                    v-else
                    class="w-8 h-8 rounded-full bg-gray-200 flex items-center justify-center text-gray-600 font-bold text-sm shadow-sm"
                  >
                    {{ client.name.charAt(0).toUpperCase() }}
                  </div>

                  <router-link
                    :to="{ name: 'SingleClient', params: { id: client.id } }"
                    class="text-blue-600 hover:underline font-bold"
                  >
                    {{ client.name }}
                  </router-link>
                </div>
              </th>
              <td class="px-6 py-4">{{ client.status }}</td>
              <td class="px-6 py-4">{{ client.contact_person }}</td>
              <td class="px-6 py-4">{{ client.email }}</td>
              <td class="px-6 py-4">{{ client.phone }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { useclientStore } from '@/stores/clientsStore.js'
import ExportModal from '@/components/Metadata/ExportModal.vue'
import api from '@/utils/api.js'
import { useToast } from 'vue-toast-notification'
import { useRouter } from 'vue-router'

const clientStore = useclientStore()
const searchQuery = ref('')
const statusQuery = ref('')
const router = useRouter()


const statuses = computed(() => [
    {value:'',label:'Choose status'},
    {value:'new',label: 'New'},
    {value:'active',label: 'Active'},
    {value: 'on_hold',label: 'On hold'},
    {value: 'former', label: 'Former'},
    {value: 'vip', label: 'VIP'}
])



const showFilter = ref(false)

const toast = useToast()

const toggleFilter = () => {
  showFilter.value = !showFilter.value
}

onMounted(() => {
  clientStore.fetchClients()
  console.log(clientStore.clients)
})

const performSearch = () => {
  console.log(statusQuery.value)
  clientStore.fetchClients(searchQuery.value,statusQuery.value)
}

const clearSearch = () => {
  searchQuery.value = ''
  clientStore.fetchClients()
}

const clientStatusCounts = computed(() => {
  const counts = {}

  if (!clientStore.clients) return counts

  clientStore.clients.forEach((client) => {
    // Presupunem că proprietatea se numește 'status' pe obiectul client
    const status = client.status || 'unknown'

    if (counts[status]) {
      counts[status]++
    } else {
      counts[status] = 1
    }
  })

  return counts
})

async function exportClients(format) {
  try {
    const res = await api.get('/api/v1/clients/exportCSV/', {
      responseType: 'blob',
    })
    const url = URL.createObjectURL(new Blob([res.data]))
    const a = document.createElement('a')
    a.href = url
    a.download = `clients_export.${format}`
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(url)
    toast.info('Clients exported successfully!')
  } catch (err) {
    console.error('Export failed:', err)
    toast.error('Export failed. Please try again.')
  }
}
</script>
