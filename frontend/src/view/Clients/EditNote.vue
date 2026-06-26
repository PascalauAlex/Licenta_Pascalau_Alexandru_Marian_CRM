<template>
  <div class="max-w-md mx-auto my-10">
    <h1 class="text-2xl font-bold mb-8 text-gray-800">Edit Note</h1>

    <form @submit.prevent="onSubmit" class="mx-auto">
      <div class="relative z-0 w-full mb-5 group">
        <input
          type="text"
          v-model="name"
          id="name"
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
          v-model="body"
          id="body"
          class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
          placeholder=" "
        />
        <label
          for="body"
          class="peer-focus:font-medium absolute text-sm text-gray-500 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 peer-focus:text-blue-600 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
          >Description</label
        >
      </div>


      <div class="flex items-center gap-4 mt-8">
        <button
          type="submit"
          class="text-white bg-blue-600 hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-8 py-2.5 text-center transition-all shadow-md"
        >
          Save Changes
        </button>
        <router-link
          :to="{name:'SingleClient', params:{id : route.params.client_id}}"
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
const client_id = route.params.client_id
const note_id = route.params.note_id

// Refs pentru formular
const name = ref('')
const body = ref('')

// POPULARE DATE LA INCARCARE
onMounted(async () => {
  const note_id = route.params.note_id
  const client_id = route.params.id
  await clientStore.getNote(note_id,client_id) // Luam datele de la server

  //Assign the old values to the form inputs
  if (clientStore.note) {
    name.value = clientStore.note.name || ''
    body.value = clientStore.note.body || ''

  }
})

const onSubmit = async () => {
  const formData = {
    name: name.value,
    body: body.value,

  }
  try {
    await clientStore.editNote(client_id, note_id, formData)
    router.push({ name: 'SingleClient', params: { id: route.params.id } })
  } catch (err) {
    alert('Error while editing the client')
    console.log(err)
  }
}
</script>
