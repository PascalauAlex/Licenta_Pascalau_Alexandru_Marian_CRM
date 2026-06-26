<template>
  <div
    class="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-[url('public/images/layered-waves-haikei.svg')] bg-cover bg-center bg-no-repeat shadow-[inset_0_0_150px_rgba(0,0,0,0.15)]"
  >
    <div class="max-w-md w-full bg-white p-8 rounded-2xl shadow-xl border border-gray-100">
      <h1 class="text-3xl font-extrabold text-center text-gray-900 mb-8">Log in</h1>

      <div
        v-if="error"
        class="mb-4 p-3 bg-red-100 text-red-700 rounded-lg text-sm font-medium border border-red-200"
      >
        {{ error }}
      </div>

      <form class="space-y-5" @submit.prevent="handleLogin">
        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-1 leading-6"
            >Email or username</label
          >
          <div>
            <input
              type="text"
              name="email"
              v-model="email"
              placeholder="name@exemplu.com"
              class="block w-full rounded-lg border-0 py-2.5 px-4 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-600 sm:text-sm sm:leading-6 outline-none transition-all"
            />
          </div>
        </div>

        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-1 leading-6">Password</label>
          <div>
            <input
              type="password"
              name="password"
              v-model="password"
              placeholder="••••••••"
              class="block w-full rounded-lg border-0 py-2.5 px-4 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-600 sm:text-sm sm:leading-6 outline-none transition-all"
            />
          </div>
        </div>
        <div>
          <p>
            You don't have an account?
            <router-link :to="{ name: 'SignUp' }" class="text-blue-600 font-bold"
              >Sign In</router-link
            >
          </p>
        </div>
        <div class="pt-2">
          <button
            type="submit"
            class="flex w-full justify-center rounded-lg bg-blue-600 px-4 py-2.5 text-sm font-bold leading-6 text-white shadow-md hover:bg-blue-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600 transition-colors active:scale-95"
          >
            Submit
          </button>
        </div>
      </form>
      <p>Or</p>
      <button class="gsi-material-button" @click="loginWithGoogle">
        <div class="gsi-material-button-state"></div>
        <div class="gsi-material-button-content-wrapper">
          <div class="gsi-material-button-icon">
            <svg
              version="1.1"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 48 48"
              xmlns:xlink="http://www.w3.org/1999/xlink"
              style="display: block"
            >
              <path
                fill="#EA4335"
                d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"
              ></path>
              <path
                fill="#4285F4"
                d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"
              ></path>
              <path
                fill="#FBBC05"
                d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"
              ></path>
              <path
                fill="#34A853"
                d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"
              ></path>
              <path fill="none" d="M0 0h48v48H0z"></path>
            </svg>
          </div>
          <span class="gsi-material-button-contents">Sign in with Google</span>
          <span style="display: none">Sign in with Google</span>
        </div>
      </button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth.js'
import { ref } from 'vue'
import api from '@/utils/api.js'
import { useUserStore } from '@/stores/userStore.js'

const router = useRouter()
const authStore = useAuthStore()

const email = ref('')
const password = ref('')
const error = ref('')
const loading = ref(false)
const userStore = useUserStore()
const GOOGLE_CLIENT_ID = import.meta.env.VITE_GOOGLE_AUTH_CLIENT_ID
const BACKEND_URL = import.meta.env.VITE_BACKEND_URL

const loginWithGoogle = async () => {
  //Set the google auth to be redirected from login page
  const googleAuthUrl = 'https://accounts.google.com/o/oauth2/v2/auth'
  //redirect Uri from Google servers for getting the auth code
  const redirectUri = 'api/v1/auth/login/google/'

  //info that we want to get from the users
  const scope = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
  ].join(' ')


  const params = {
    response_type: 'code',
    client_id: GOOGLE_CLIENT_ID,
    redirect_uri: `${BACKEND_URL}/${redirectUri}`, //the same as in Google Cloud Platform
    prompt: 'select_account',
    access_type: 'offline',
    scope,
  }


  const urlParams = new URLSearchParams(params).toString()

  window.location = `${googleAuthUrl}?${urlParams}`
}

const handleLogin = async () => {
  console.log(`Logged in ${email.value}`)
  error.value = ''
  loading.value = true

  try {
    const response = await api.post('/api/v1/jwt/create/', {
      username: email.value, //Django use username
      password: password.value,
    })

    const access = response.data.access
    const refresh = response.data.refresh
    authStore.setToken(access, refresh)

    const userResponse = await api.get('/api/v1/users/me/')
    console.log('USER DATA : ', userResponse.data)

    authStore.setUser(userResponse.data)

    //Initializam si facem cerere pentru user pentru a avea datele incarcate
    await userStore.getUser()

    //redirect the user to dashboard
    router.push('/')
  } catch (err) {
    if (err.response && err.response.status == 400) {
      error.value = 'Email or password are incorect'
    } else {
      error.value = 'An error acoured trying to connect to the server'
    }
    console.error(err)
  } finally {
    loading.value = false
  }
}
</script>
