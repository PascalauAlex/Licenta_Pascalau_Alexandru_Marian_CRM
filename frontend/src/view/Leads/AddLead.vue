<template>
  <div class="max-w-md mx-auto my-10">
    <h1 class="text-2xl font-bold mb-8 text-gray-800">Add Lead</h1>

    <form @submit.prevent="onSubmit" class="mx-auto">
      <div class="relative z-0 w-full mb-5 group">
        <input
          type="text"
          v-model="company"
          id="company"
          class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
          placeholder=" "
          required
        />
        <label
          for="company"
          class="peer-focus:font-medium absolute text-sm text-gray-500 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 peer-focus:text-blue-600 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
          >Company Name</label
        >
      </div>

      <div class="relative z-0 w-full mb-5 group">
        <input
          type="text"
          v-model="contact_person"
          id="contact_person"
          class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
          placeholder=" "
          required
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
          required
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
      </div>

      <div class="grid md:grid-cols-2 md:gap-6">
        <div class="relative z-0 w-full mb-5 group">
          <input
            type="number"
            v-model="estimated_value"
            id="value"
            class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
            placeholder=" "
          />
          <label
            for="value"
            class="peer-focus:font-medium absolute text-sm text-gray-500 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 peer-focus:text-blue-600 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
            >Estimated Value</label
          >
        </div>

      </div>

      <div class="grid md:grid-cols-2 md:gap-6 mb-8">
        <div>
          <label for="countries" class="block mb-2.5 text-sm font-medium text-gray-500 text-heading"
            >Select an user for the lead</label
          >
          <select
            id="countries"
            class="block w-full px-3 py-2.5 bg-transparent  border-l-gray-50 border-r-gray-50 border-t-gray-50  text-heading text-sm rounded-base focus:ring-brand focus:border-brand shadow-xs placeholder:text-body"
            v-model="assigned_to"
            required
          >
            <option selected>Choose member</option>
            <option v-for="member in teamStore.team.members" :key="member.id" :value="member.id">
              {{ member.first_name }} {{ member.last_name }}
            </option>
          </select>
        </div>
      </div>

      <div class="flex items-center gap-4 mt-8">
        <button
          type="submit"
          class="text-white bg-blue-600 hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-8 py-2.5 text-center transition-all shadow-md"
        >
          Submit Lead
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
import { useLeadStore } from '@/stores/leadStore.js'
import { onMounted, ref } from 'vue'
import {useRouter} from 'vue-router'
import { useTeamStore } from '@/stores/teamStore.js'
import { useToast } from 'vue-toast-notification'

const router = useRouter()
const toast = useToast()

const company = ref('')
const contact_person = ref('')
const email = ref('')
const phone = ref('')
const website = ref('')
const confidence = ref('')
const estimated_value = ref('')
const status = ref('new')
const priority = ref('medium')

const leadStore = useLeadStore()
const teamStore = useTeamStore()
const assigned_to = ref('')

onMounted(async () => {
  await teamStore.fetchTeam()
  console.log(teamStore.team)
})

const onSubmit = async () => {
  const formData = {
    company: company.value,
    contact_person: contact_person.value,
    email: email.value,
    phone: phone.value,
    website: website.value,
    confidence: confidence.value,
    estimated_value: estimated_value.value,
    status: status.value,
    priority: priority.value,
    assigned_to : assigned_to.value,
  }
  try {
    await leadStore.addLead(formData)
    toast.success('New lead added succesfully!')
    router.push('/dashboard/leads')
  } catch (err) {
    console.error('Save failed', err)
    toast.error('Failed to add the lead.Please try again.')
  }
}
</script>
