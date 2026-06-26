<template>
  <div
    class="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-[url('public/images/layered-waves-haikei.svg')] bg-cover bg-center bg-no-repeat shadow-[inset_0_0_150px_rgba(0,0,0,0.15)]"
  >
    <div class="max-w-md w-full bg-white p-8 rounded-2xl shadow-xl border border-gray-100">
      <h1 class="text-3xl font-extrabold text-center text-gray-900 mb-8">Sign Up</h1>

      <div
        v-if="error"
        class="mb-4 p-3 bg-red-100 text-red-700 rounded-lg text-sm font-medium border border-red-200"
      >
        {{ error }}
      </div>

      <form class="space-y-5" @submit.prevent="handleSubmit">
        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-1 leading-6">Email</label>
          <div>
            <input
              type="email"
              name="email"
              v-model="email"
              placeholder="name@exemple.com"
              required
              class="block w-full rounded-lg border-0 py-2.5 px-4 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-600 sm:text-sm sm:leading-6 outline-none transition-all"
            />
          </div>
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-1 leading-6">Password</label>
          <div>
            <input
              type="password"
              name="password1"
              v-model="password"
              placeholder="••••••••"
              required
              class="block w-full rounded-lg border-0 py-2.5 px-4 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-600 sm:text-sm sm:leading-6 outline-none transition-all"
            />
          </div>
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-1 leading-6"
            >Repeat password</label
          >
          <div>
            <input
              type="password"
              name="password2"
              v-model="rePassword"
              placeholder="••••••••"
              required
              class="block w-full rounded-lg border-0 py-2.5 px-4 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-600 sm:text-sm sm:leading-6 outline-none transition-all"
            />
          </div>
        </div>

        <div v-if="error"></div>

        <div class="pt-2">
          <button
            type="submit"
            class="flex w-full justify-center rounded-lg bg-blue-600 px-4 py-2.5 text-sm font-bold leading-6 text-white shadow-md hover:bg-blue-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600 transition-colors active:scale-95 disabled:opacity-50"
          >
            {{ loading ? 'Loading' : 'Submit' }}
          </button>
        </div>
      </form>

      <p class="mt-6 text-center text-sm text-gray-500">
        You have an accound already?
        <router-link
          :to="{ name: 'LogIn' }"
          class="font-semibold leading-6 text-blue-600 hover:text-blue-500"
          >Log in</router-link
        >
      </p>
    </div>
  </div>
</template>

<script setup>
import api from '@/utils/api.js'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const email = ref('')
const password = ref('')
const rePassword = ref('')
const error = ref('')
const loading = ref(false)

const handleSubmit = async () => {
  if (password.value !== rePassword.value) {
    error.value = 'Password do not match'
    return
  }

  error.value = ''
  loading.value = true

  try {
    await api.post('/api/v1/users/', {
      username: email.value,
      password: password.value,
    })

    router.push('/log-in')
  } catch (err) {
    if (err.response && err.response.data) {
      // take error from django
      const firstError = Object.values(err.response.data)[0]
      error.value = Array.isArray(firstError) ? firstError[0] : 'Something went wrong'
    } else {
      error.value = 'An error occured trying to connect to the server'
    }
    console.log(err)
  } finally {
    loading.value = false
  }
}
</script>
