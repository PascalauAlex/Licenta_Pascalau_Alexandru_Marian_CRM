<template>
  <div class="max-w-md mx-auto my-10">
    <h1 class="text-2xl font-bold mb-8 text-gray-800">Edit Client</h1>

    <form @submit.prevent="onSubmit" class="mx-auto">
      <div class="relative z-0 w-full mb-5 group">
        <input
          type="text"
          v-model="name"
          id="company"
          class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
          placeholder=" "
        />
        <label
          for="name"
          class="peer-focus:font-medium absolute text-sm text-gray-500 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 peer-focus:text-blue-600 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
          >Name</label
        >
      </div>

      <div class="relative z-0 w-full mb-5 group">
        <input
          type="text"
          v-model="contact_person"
          id="contact_person"
          class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
          placeholder=" "
        />
        <label
          for="contact_person"
          class="peer-focus:font-medium absolute text-sm text-gray-500 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 peer-focus:text-blue-600 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
          >Contact Person</label
        >
      </div>

      <div class="relative z-0 w-full mb-5 group">
        <input
          type="email"
          v-model="email"
          id="email"
          class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
          placeholder=" "
        />
        <label
          for="email"
          class="peer-focus:font-medium absolute text-sm text-gray-500 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 peer-focus:text-blue-600 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
          >Email Address</label
        >
      </div>

      <div class="grid md:grid-cols-2 md:gap-6">
        <div class="relative z-0 w-full mb-5 group">
          <input
            type="text"
            v-model="phone"
            id="phone"
            class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
            placeholder=" "
          />
          <label
            for="phone"
            class="peer-focus:font-medium absolute text-sm text-gray-500 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 peer-focus:text-blue-600 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
            >Phone Number</label
          >
        </div>
        <div class="relative z-0 w-full mb-5 group">
          <input
            type="text"
            v-model="website"
            id="website"
            class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
            placeholder=" "
          />
          <label
            for="website"
            class="peer-focus:font-medium absolute text-sm text-gray-500 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 peer-focus:text-blue-600 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
            >Website (URL)</label
          >
        </div>

        <div class="relative z-0 w-full mb-5 group">
          <label for="status" class="block mb-2.5 text-sm font-medium text-heading">
            Select the status
          </label>

          <select
            id="status"
            class="block w-full px-3 py-2.5 bg-neutral-secondary-medium border border-default-medium text-heading text-sm rounded-base focus:ring-brand focus:border-brand shadow-xs placeholder:text-body"
            v-model="status"
          >
            <option selected>Choose status</option>
            <option
              v-for="option in statusOptions"
              :key="option.value"
              :value="option.value"
            >
              {{ option.label }}
            </option>
          </select>
        </div>
      </div>

      <div class="flex items-center gap-4 mt-8">
        <button
          type="submit"
          class="text-white bg-blue-600 hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-8 py-2.5 text-center transition-all shadow-md"
        >
          Save Changes
        </button>
        <router-link
          to="/dashboard/leads"
          class="text-gray-700 bg-white border border-gray-300 hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-200 font-medium rounded-lg text-sm px-8 py-2.5 text-center transition-colors shadow-sm"
        >
          Back
        </router-link>
      </div>
    </form>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import { useclientStore } from '@/stores/clientsStore.js'

const clientStore = useclientStore()
const route = useRoute()
const router = useRouter()

// Refs pentru formular
const name = ref('')
const contact_person = ref('')
const email = ref('')
const phone = ref('')
const website = ref('')
const status = ref('')

// POPULARE DATE LA INCARCARE
onMounted(async () => {
  const id = route.params.id
  await clientStore.getClient(id) // Luam datele de la server
  await clientStore.fetchClients()

  //Assign the old values to the form inputs
  if (clientStore.client) {
    name.value = clientStore.client.name
    contact_person.value = clientStore.client.contact_person || ''
    email.value = clientStore.client.email || ''
    phone.value = clientStore.client.phone || ''
    website.value = clientStore.client.website || ''
    status.value = clientStore.client.status
  }
})

// Adaugă asta în <script setup>
const statusOptions = [
  { value: 'new', label: 'New' },
  { value: 'active', label: 'Active' },
  { value: 'inactive', label: 'Inactive' },
  { value: 'on_hold', label: 'On Hold' },
  { value: 'former', label: 'Former' },
  { value: 'vip', label: 'VIP' },
]

const onSubmit = async () => {
  const formData = {
    name: name.value,
    contact_person: contact_person.value,
    email: email.value,
    phone: phone.value,
    website: website.value,
    status: status.value,
  }
  try {
    await clientStore.editClient(route.params.id, formData)
    router.push({ name: 'SingleClient', params: { id: route.params.id } })
  } catch (err) {
    alert('Error while editing the client')
    console.log(err)
  }
}
</script>
