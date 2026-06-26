<template>
  <div class="max-w-md mx-auto my-10">
    <h1 class="text-2xl font-bold mb-8 text-gray-800">Add Note</h1>

    <form @submit.prevent="onSubmit" class="mx-auto">
      <div class="relative z-0 w-full mb-5 group">
        <input
          type="text"
          v-model="name"
          id="name"
          class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
          placeholder=" "
          required
        />
        <label
          for="name"
          class="peer-focus:font-medium absolute text-sm text-gray-500 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 peer-focus:text-blue-600 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
          >Title</label
        >
      </div>

      <div class="relative z-0 w-full mb-5 group">
        <label
          for="body"
          class="text-gray-500 mb-10"
        >Description</label>
        <textarea
          type="text"
          v-model="body"
          id="body"
          class="bg-neutral-secondary-medium border border-default-medium text-heading text-sm rounded-base focus:ring-brand focus:border-brand block w-full p-3.5 shadow-xs placeholder:text-body"
          placeholder=" "
          required
        />


        <div class="flex items-center gap-4 mt-8">
          <button
            type="submit"
            class="text-white bg-blue-600 hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-8 py-2.5 text-center transition-all shadow-md"
          >
            Submit
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useclientStore } from '@/stores/clientsStore.js'
import router from '@/router/index.js'
import { useRoute } from 'vue-router'

const name = ref('')
const body = ref('')
const route = useRoute()

const clientStore = useclientStore()

const onSubmit = async () => {
  const formData = {
    name: name.value,
    body: body.value,
    client_id: route.params.id,
  }

  try {
    await clientStore.postNote(formData)
    router.push({ name: 'SingleClient', params: { id: route.params.id } })
  } catch (err) {
    console.error('Saving the note failed', err)
  }
}
</script>
