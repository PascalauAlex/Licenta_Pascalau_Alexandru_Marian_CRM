<template>
  <div class="max-w-md mx-auto my-10">
    <h1 class="text-2xl font-bold mb-8 text-gray-800">Edit Lead</h1>

    <form @submit.prevent="onSubmit" class="mx-auto">
      <div class="relative z-0 w-full mb-5 group">
        <input
          type="text"
          v-model="company"
          id="company"
          class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
          placeholder=" "
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
      </div>
      <div class="grid md:grid-cols-2 md:gap-6">
        <label for="countries" class="block mb-2.5 text-sm font-medium text-heading"
          >Select an user for the lead</label
        >
        <select
          id="countries"
          class="block w-full px-3 py-2.5 bg-neutral-secondary-medium border border-default-medium text-heading text-sm rounded-base focus:ring-brand focus:border-brand shadow-xs placeholder:text-body"
          v-model="assigned_to"
        >
          <option selected>Choose member</option>
          <option v-for="member in teamStore.team.members" :key="member.id" :value="member.id">
            {{ member.username }}
          </option>
        </select>
      </div>
      <div class="grid md:grid-cols-2 md:gap-6">
        <label for="status" class="block mb-2.5 text-sm font-medium text-heading">
          Change status
        </label>
        <select
          id="status"
          class="block w-full px-3 py-2.5 bg-neutral-secondary-medium border border-default-medium text-heading text-sm rounded-base focus:ring-brand focus:border-brand shadow-xs placeholder:text-body"
          v-model="status"
        >
          <option selected>Choose status</option>
          <option v-for="option in statusOptions" :key="option.value" :value="option.value">
            {{ option.value }}
          </option>
        </select>
      </div>

      <div class="flex items-center gap-4 mt-8">
        <button
          type="submit"
          class="text-white bg-blue-600 hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-8 py-2.5 text-center transition-all shadow-md"
        >
          Save Changes
        </button>
        <router-link
          :to="{name:'SingleLead',params:{id:route.params.id}}"
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
import { useRoute, useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import { useTeamStore } from '@/stores/teamStore.js'

const leadStore = useLeadStore()
const route = useRoute()
const router = useRouter()

// Refs pentru formular
const company = ref('')
const contact_person = ref('')
const email = ref('')
const phone = ref('')
const website = ref('')
const confidence = ref('')
const estimated_value = ref('')
const status = ref('new')
const priority = ref('medium')
const assigned_to = ref('')
const teamStore = useTeamStore()

const statusOptions = [
  { value: 'new', label: 'New' },
  { value: 'contacted', label: 'Contacted' },
  { value: 'inprogress', label: 'In progress' },
  { value: 'lost', label: 'Lost' },
  { value: 'won', label: 'Won' },
]



// POPULARE DATE LA INCARCARE
onMounted(async () => {
  const id = route.params.id
  await leadStore.getLead(id) // Luam datele de la server
  await teamStore.fetchTeam()

  //Assign the old values to the form inputs
  if (leadStore.lead) {
    company.value = leadStore.lead.company
    contact_person.value = leadStore.lead.contact_person
    email.value = leadStore.lead.email
    phone.value = leadStore.lead.phone
    website.value = leadStore.lead.website
    confidence.value = leadStore.lead.confidence
    estimated_value.value = leadStore.lead.estimated_value
    status.value = leadStore.lead.status
    priority.value = leadStore.lead.priority
    assigned_to.value = leadStore.leads.assgined_to || ''
  }
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
    assigned_to: assigned_to.value,
  }
  try {
    await leadStore.editLead(route.params.id, formData)
    router.push({ name: 'SingleLead', params: { id: route.params.id } })
  } catch (err) {
    alert('Error while editing the lead')
    console.log(err)
  }
}
</script>
