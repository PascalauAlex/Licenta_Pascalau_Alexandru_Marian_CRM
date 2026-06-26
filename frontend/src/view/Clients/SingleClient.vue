<template>
  <div v-if="clientStore.client && !clientStore.loading" class="max-w-6xl mx-auto pb-20">
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-8">
      <div class="flex items-center gap-4">
        <img
          v-if="clientStore.client.profile_picture"
          :src="clientStore.client.profile_picture"
          alt="Profile Picture"
          class="w-16 h-16 rounded-full object-cover border-2 border-gray-200 shadow-md"
        />
        <div
          v-else
          class="w-16 h-16 rounded-full bg-blue-600 flex items-center justify-center text-white font-bold text-2xl shadow-md border-2 border-white"
        >
          {{ clientStore.client.name?.charAt(0).toUpperCase() || 'C' }}
        </div>

        <h1 class="font-bold text-heading text-3xl md:text-4xl">
          {{ clientStore.client.name }}
        </h1>
      </div>

      <div class="flex items-center gap-3 bg-white p-2 rounded-xl border border-gray-200 shadow-sm">
        <router-link
          :to="{ name: 'EditClient', params: { id: route.params.id } }"
          class="px-4 py-2 text-sm font-bold text-blue-600 hover:bg-blue-50 rounded-lg transition-all"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="size-6"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L6.832 19.82a4.5 4.5 0 0 1-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 0 1 1.13-1.897L16.863 4.487Zm0 0L19.5 7.125"
            />
          </svg>
        </router-link>
        <div class="w-px h-6 bg-gray-200"></div>
        <button
          @click="toggleModal"
          class="px-4 py-2 text-sm font-bold text-red-300 hover:bg-red-600 hover:text-white rounded-lg transition-all"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="size-6"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M2.25 13.5h3.86a2.25 2.25 0 0 1 2.012 1.244l.256.512a2.25 2.25 0 0 0 2.013 1.244h3.218a2.25 2.25 0 0 0 2.013-1.244l.256-.512a2.25 2.25 0 0 1 2.013-1.244h3.859m-19.5.338V18a2.25 2.25 0 0 0 2.25 2.25h15A2.25 2.25 0 0 0 21.75 18v-4.162c0-.224-.034-.447-.1-.661L19.24 5.338a2.25 2.25 0 0 0-2.15-1.588H6.911a2.25 2.25 0 0 0-2.15 1.588L2.35 13.177a2.25 2.25 0 0 0-.1.661Z"
            />
          </svg>
        </button>
        <div class="w-px h-6 bg-gray-200"></div>
        <button
          @click="handleDelete"
          class="px-4 py-2 text-sm font-bold text-red-600 hover:bg-red-50 rounded-lg transition-all"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="size-6"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0"
            />
          </svg>
        </button>
      </div>
    </div>

    <div class="bg-white border border-gray-200 shadow-md rounded-2xl p-6 md:p-8">
      <h2 class="text-xl font-bold text-gray-800 mb-6 border-b border-gray-100 pb-4">
        Client Details
      </h2>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-y-6 gap-x-8">
        <div>
          <span class="block text-sm font-medium text-gray-500 mb-1">Contact Person</span>
          <span class="block text-base font-semibold text-gray-900">{{
            clientStore.client.contact_person || '-'
          }}</span>
        </div>

        <div>
          <span class="block text-sm font-medium text-gray-500 mb-1">Email</span>
          <a
            :href="`mailto:${clientStore.client.email}`"
            class="block text-base font-semibold text-blue-600 hover:underline"
          >
            {{ clientStore.client.email || '-' }}
          </a>
        </div>

        <div>
          <span class="block text-sm font-medium text-gray-500 mb-1">Phone</span>
          <span class="block text-base font-semibold text-gray-900">{{
            clientStore.client.phone || '-'
          }}</span>
        </div>

        <div>
          <span class="block text-sm font-medium text-gray-500 mb-1">Website</span>
          <a
            v-if="clientStore.client.website"
            :href="clientStore.client.website"
            target="_blank"
            class="block text-base font-semibold text-blue-600 hover:underline"
          >
            {{ clientStore.client.website }}
          </a>
          <span v-else class="block text-base font-semibold text-gray-900">N/A</span>
        </div>

        <div>
          <span class="block text-sm font-medium text-gray-500 mb-1">Assigned to</span>
          <span class="block text-base font-semibold text-gray-900">
            {{
              clientStore.client.assigned_to?.last_name +
                ' ' +
                clientStore.client.assigned_to?.first_name || 'Not assigned'
            }}
          </span>
        </div>

        <div>
          <span class="block text-sm font-medium text-gray-500 mb-1">Status</span>
          <span
            :class="getStatusColor(clientStore.client.status)"
            class="inline-flex items-center gap-1.5 px-3 py-1 border rounded-lg text-sm font-bold capitalize transition-colors"
          >
            <span class="w-1.5 h-1.5 rounded-full bg-current"></span>
            {{ clientStore.client.status }}
          </span>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-8 pt-6 border-t border-gray-100">
        <div>
          <span class="block text-xs font-medium text-gray-400 mb-1">Client Since</span>
          <span class="block text-sm text-gray-600">{{
            formatDate(clientStore.client.created_at)
          }}</span>
        </div>
        <div>
          <span class="block text-xs font-medium text-gray-400 mb-1">Last Update</span>
          <span class="block text-sm text-gray-600">{{
            formatDate(clientStore.client.modified_at || clientStore.client.created_at)
          }}</span>
        </div>
        <div class="mt-4">
          <button @click="toggleMoreDetails" class="flex items-center gap-1 cursor-pointer">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <polyline points="6 9 12 15 18 9" />
            </svg>
            <span class="text-medium text-gray-600">
              More
            </span>
          </button>
        </div>
      </div>
      <div
        class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-8 pt-6 border-t border-gray-100"
        v-if="moreDetails"
      >
        <div>
          <span class="block text-xs font-medium text-gray-400 mb-1">Source</span>
          <span class="block text-sm text-gray-600">
            {{ clientStore.client.source || '-' }}
          </span>
        </div>
        <div>
          <span class="block text-xs font-medium text-gray-400 mb-1">Last Contacted</span>
          <span class="block text-sm text-gray-600">
            {{ clientStore.client.last_contacted_date || '-' }}
          </span>
        </div>
        <div>
          <span class="block text-xs font-medium text-gray-400 mb-1">Address</span>
          <span class="block text-sm text-gray-600">{{clientStore.client.address || '-'}}</span>

        </div>
      </div>
    </div>

    <div class="mt-10 bg-white shadow-md rounded-xl border border-gray-200 overflow-hidden">
      <div class="bg-gray-800 px-6 py-4 border-b border-gray-700">
        <h3 class="text-lg font-bold text-white">Activities and Client Notes</h3>
      </div>

      <div class="p-6">
        <form
          @submit.prevent="submitQuickNote"
          class="mb-10 bg-gray-50 p-4 rounded-lg border border-gray-200"
        >
          <div class="grid grid-cols-1 gap-4">
            <div>
              <label class="block text-xs font-semibold text-gray-600 uppercase mb-1"
                >Note title</label
              >
              <input
                v-model="noteName"
                type="text"
                placeholder="Ex: Customer call, Office visit..."
                class="w-full p-2 text-sm border border-gray-300 rounded focus:ring-2 focus:ring-blue-400 outline-none"
              />
            </div>

            <div>
              <label class="block text-xs font-semibold text-gray-600 uppercase mb-1"
                >Description</label
              >
              <textarea
                v-model="noteBody"
                rows="3"
                placeholder="What have you discussed so far?"
                class="w-full p-3 text-sm border border-gray-300 rounded focus:ring-2 focus:ring-blue-400 outline-none"
                required
              ></textarea>
            </div>

            <div class="flex justify-end">
              <button
                type="submit"
                :disabled="isSubmitting || !noteBody.trim()"
                class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded font-medium text-sm transition-all disabled:opacity-50"
              >
                {{ isSubmitting ? 'Saving...' : 'Save note' }}
              </button>
            </div>
          </div>
        </form>

        <div v-if="clientStore.notes && clientStore.notes.length > 0" class="space-y-6">
          <div v-for="note in clientStore.notes" :key="note.id" class="flex gap-4 group">
            <div class="flex flex-col items-center">
              <div
                class="w-3 h-3 bg-blue-500 rounded-full mt-1.5 shadow-[0_0_0_4px_rgba(59,130,246,0.1)]"
              ></div>
              <div class="w-0.5 h-full bg-gray-100"></div>
            </div>

            <div class="flex-1 pb-6">
              <div class="flex justify-between items-start">
                <div>
                  <h4 class="text-sm font-bold text-gray-900">{{ note.name }}</h4>
                  <p class="text-xs text-gray-500 mb-2">
                    Added by
                    <span class="font-semibold text-gray-700">{{
                      note.created_by.userprofile.full_name || 'Membru Team'
                    }}</span>
                    at
                    {{ new Date(note.created_at).toLocaleString('ro-RO') }}
                  </p>
                </div>

                <button
                  @click="handleDeleteNote(note.id)"
                  class="text-gray-300 hover:text-red-500 transition-colors opacity-0 group-hover:opacity-100 p-1"
                  title="Șterge nota"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-4 w-4"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
                    />
                  </svg>
                </button>
              </div>
              <div class="bg-gray-50 p-4 rounded-xl border border-gray-100 shadow-sm mt-1">
                <p class="text-sm text-gray-700 whitespace-pre-line leading-relaxed">
                  {{ note.body }}
                </p>
              </div>
            </div>
          </div>
        </div>

        <div v-else class="text-center py-12">
          <p class="text-gray-400 text-sm">Nu există note pentru acest client.</p>
        </div>
      </div>
    </div>
  </div>

  <div v-else class="flex items-center justify-center min-h-[400px]">
    <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
  </div>

  <DefaultModal :modalActive="modalActive" @close-modal="toggleModal">
    <h2 class="text-2xl font-semibold mb-6 text-gray-800 border-b pb-2">Send Mail</h2>

    <form @submit.prevent="sendMail" class="space-y-6">
      <div class="flex flex-col gap-1">
        <label for="to" class="text-sm font-medium text-gray-500 uppercase tracking-wider"
          >To:</label
        >
        <input
          type="email"
          id="to"
          v-model="emailForm.to"
          placeholder="recipient@example.com"
          class="w-full border-0 border-b-2 border-gray-200 bg-transparent py-2 px-0 focus:ring-0 focus:border-blue-600 transition-colors outline-none text-gray-700"
          required
        />
      </div>

      <div class="flex flex-col gap-1">
        <label for="subject" class="text-sm font-medium text-gray-500 uppercase tracking-wider"
          >Subject:</label
        >
        <input
          type="text"
          id="subject"
          v-model="emailForm.subject"
          placeholder="Enter subject"
          class="w-full border-0 border-b-2 border-gray-200 bg-transparent py-2 px-0 focus:ring-0 focus:border-blue-600 transition-colors outline-none text-gray-700"
          required
        />
      </div>

      <div class="flex flex-col gap-1">
        <label for="message" class="text-sm font-medium text-gray-500 uppercase tracking-wider"
          >Message:</label
        >
        <textarea
          id="message"
          v-model="emailForm.message"
          rows="3"
          placeholder="Write your message here..."
          class="w-full border-0 border-b-2 border-gray-200 bg-transparent py-2 px-0 focus:ring-0 focus:border-blue-600 transition-colors outline-none text-gray-700 resize-none"
          required
        ></textarea>
      </div>

      <div class="flex flex-col gap-2">
        <label class="text-sm font-medium text-gray-500 uppercase tracking-wider"
          >Attachments:</label
        >
        <div class="relative flex items-center">
          <input
            type="file"
            id="file"
            multiple
            @change="onFileChange"
            class="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100 transition-all cursor-pointer"
          />
        </div>
      </div>

      <div class="pt-4 flex justify-end">
        <button
          type="submit"
          :disabled="isLoading"
          class="bg-blue-950 text-white px-6 py-2 rounded-lg flex items-center gap-2 transition-all hover:bg-blue-900 disabled:opacity-50 disabled:cursor-not-allowed shadow-md"
        >
          <svg
            v-if="isLoading"
            class="animate-spin h-5 w-5 text-white"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
          >
            <circle
              class="opacity-25"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              stroke-width="4"
            ></circle>
            <path
              class="opacity-75"
              fill="currentColor"
              d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
            ></path>
          </svg>

          <span>{{ isLoading ? 'Sending...' : 'Send' }}</span>
        </button>
      </div>

      <div class="mt-4">
        <p
          v-if="error"
          class="text-red-500 text-sm text-right bg-red-50 p-2 rounded border border-red-100 italic"
        >
          {{ error }}
        </p>
        <p
          v-if="isSucces"
          class="text-green-600 text-sm font-bold text-right flex items-center justify-end gap-1"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="2"
            stroke="currentColor"
            class="size-4"
          >
            <path stroke-linecap="round" stroke-linejoin="round" d="m4.5 12.75 6 6 9-13.5" />
          </svg>
          Email sent successfully!
        </p>
      </div>
    </form>
    <InboxEmail :client-id="route.params.id" class="mt-8 border-t pt-6"></InboxEmail>
  </DefaultModal>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { computed, onMounted, ref } from 'vue'
import formatDate from '/services/formatDate.js'
import { useclientStore } from '@/stores/clientsStore.js'
import { watch } from 'vue'
import DefaultModal from '@/components/Modals/DefaultModal.vue'
import InboxEmail from '@/components/Email/InboxEmail.vue'
import { useEmailStore } from '@/utils/emailStore.js'
import { storeToRefs } from 'pinia'

const clientStore = useclientStore()
const route = useRoute()
const router = useRouter()
const client = computed(() => clientStore.client)
const emailStore = useEmailStore()
const { isLoading, error, isSucces } = storeToRefs(emailStore)

const noteName = ref('')
const noteBody = ref('')
const isSubmitting = ref(false)
const moreDetails = ref(false)
const modalActive = ref(false)

const toggleMoreDetails = () => {
  moreDetails.value = !moreDetails.value
}

onMounted(async () => {
  const id = route.params.id
  await clientStore.getClient(id)
  await clientStore.getClientNotes(id)
  console.log(clientStore.client)

  if (clientStore.client?.email) {
    emailForm.value.to = clientStore.client.email
  }
})

const toggleModal = () => {
  modalActive.value = !modalActive.value
}

const getStatusColor = (status) => {
  const colors = {
    new: 'bg-blue-50 text-blue-700 border-blue-200',
    active: 'bg-green-50 text-green-700 border-green-200',
    inactive: 'bg-yellow-50 text-yellow-700 border-yellow-200',
    on_hold: 'bg-orange-50 text-orange-700 border-orange-200',
    former: 'bg-gray-50 text-gray-700 border-gray-200',
    vip: 'bg-purple-100 text-purple-700 border-purple-300 shadow-sm',
  }

  return colors[status] || 'bg-gray-50 text-gray-700 border-gray-200'
}

const submitQuickNote = async () => {
  if (!noteBody.value.trim() && !noteName.value.trim()) return
  isSubmitting.value = true

  const formData = {
    client_id: route.params.id,
    name: noteName.value.trim()
      ? `${noteName.value} - ${new Date().toLocaleDateString('ro-RO')}`
      : `Notă - ${new Date().toLocaleDateString('ro-RO')}`,
    body: noteBody.value,
  }

  try {
    await clientStore.postNote(formData)
    noteBody.value = ''
    noteName.value = ''
  } catch (err) {
    console.error('Eroare la salvarea notei:', err)
  } finally {
    isSubmitting.value = false
  }
}

const handleDelete = async () => {
  if (confirm('Are you sure that you want to delete the client? ')) {
    try {
      await clientStore.deleteClient(route.params.id)
      router.push('/clients/')
    } catch (err) {
      alert('Cannot delete the client')
      console.log(err)
    }
  }
}

const handleDeleteNote = async (noteID) => {
  if (confirm('Are you sure that you want to delete the note? ')) {
    try {
      const clientID = route.params.id
      await clientStore.deleteNote(noteID, clientID)
    } catch (err) {
      alert('Cannot delete this note!')
      console.error(err)
    }
  }
}

watch(
  client,
  (newVal) => {
    if (newVal && newVal.name) {
      document.title = `Details: ${newVal.name} | Client details`
    }
  },
  { immediate: true },
)

const emailForm = ref({
  to: '',
  subject: '',
  message: '',
  files: null,
  client: route.params.id,
})

const onFileChange = (e) => {
  emailForm.value.files = e.target.files
}

const sendMail = async () => {
  const ok = await emailStore.sendAndSaveMail(emailForm.value)

  if (ok) {
    emailForm.value = { to: '', subject: '', message: '', files: null, client: route.params.id }
  }
}
</script>
