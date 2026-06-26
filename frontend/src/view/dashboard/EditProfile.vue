<template>
  <div class="max-w-md mx-auto my-10">
    <h1 class="text-2xl font-bold mb-8 text-gray-800">Edit Profile</h1>
    <form @submit.prevent="onSubmit" class="mx-auto">
      <div class="relative z-0 w-full mb-5 group:">
        <input
          type="text"
          v-model="last_name"
          id="last_name"
          class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
          placeholder=" "
        />
        <label
          for="last_name"
          class="peer-focus:font-medium absolute text-sm text-gray-500 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 peer-focus:text-blue-600 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
          >Last Name</label
        >
      </div>

      <div class="relative z-0 w-full mb-5 group:">
        <input
          type="text"
          v-model="first_name"
          id="first_name"
          class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
          placeholder=" "
        />
        <label
          for="last_name"
          class="peer-focus:font-medium absolute text-sm text-gray-500 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 peer-focus:text-blue-600 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
          >First Name</label
        >
      </div>

      <div class="relative z-0 w-full mb-5 group:">
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
          >Phone number</label
        >
      </div>

      <div class="relative z-0 w-full mb-5 group:">
        <label class="block mb-2 text-sm font-medium text-gray-500" for="profile_picture">
          Imagine de profil
        </label>
        <input
          type="file"
          id="profile_picture"
          accept="image/png, image/jpeg, image/jpg"
          @change="handleFileUpload"
          class="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none file:mr-4 file:py-2 file:px-4 file:rounded-l-lg file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
        />
        <p class="mt-1 text-xs text-gray-500">Accepted files JPG , JPEG and PNG.</p>
      </div>

      <div class="flex items-center gap-4 mt-8">
        <button
          type="submit"
          class="text-white bg-blue-600 hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-8 py-2.5 text-center transition-all shadow-md"
        >
          Save Changes
        </button>
        <router-link
          :to="{ name: 'MyAccount' }"
          class="text-gray-700 bg-white border border-gray-300 hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-200 font-medium rounded-lg text-sm px-8 py-2.5 text-center transition-colors shadow-sm"
        >
          Back
        </router-link>
      </div>
    </form>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/userStore.js'
import { useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import { useToast } from 'vue-toast-notification'

const userStore = useUserStore()
const router = useRouter()

const last_name = ref('')
const first_name = ref('')
const toast = useToast()

const phone = ref('')
const profile_picture = ref(null)
onMounted(async () => {
  if (!userStore.user || !userStore.user.id) {
    await userStore.getUser()
  }

  if (userStore.user && userStore.user.id) {
    last_name.value = userStore.user.last_name
    first_name.value = userStore.user.first_name
  }

  if(userStore.userProfile){
    last_name.value = userStore.user.last_name || ''
    first_name.value = userStore.user.first_name || ''
  }
  if(userStore.userProfile){
    phone.value = userStore.userProfile.phone || ''
  }
})

const onSubmit = async () => {
  const formData = new FormData()

  formData.append('first_name', first_name.value)
  formData.append('last_name', last_name.value)
  formData.append('userprofile.phone', phone.value)

  if (profile_picture.value instanceof File) {
    formData.append('userprofile.profile_picture', profile_picture.value)
  }

  try {
    await userStore.editUser(formData)
    router.push({ name: 'MyAccount' })
    toast.success('User profile was modified succesfully!')

  } catch (err) {
    alert('Error while editing the profile')
    console.log('Error from backend: ', err.response?.data)
    console.error(err)
    toast.error('Error while modifing user profile!')
  }
}

const handleFileUpload = (event) => {
  profile_picture.value = event.target.files[0]
}
</script>
