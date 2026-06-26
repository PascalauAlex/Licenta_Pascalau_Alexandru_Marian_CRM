<template>
  <nav class="bg-gray-900 text-white shadow-md">
    <div class="container mx-auto flex items-center justify-between px-6 h-16">
      <div class="flex items-center space-x-2">
        <RouterLink to="/">
          <span class="text-2xl font-bold tracking-tight">
            CRM<span class="text-blue-500">.</span>
          </span>
        </RouterLink>
      </div>

      <div class="flex items-center space-x-4 h-full font-medium p-2">
        <RouterLink
          to="/"
          class="hover:text-blue-400 transition font-semibold inline-flex hover:underline"
        >
          Home
        </RouterLink>

        <template v-if="authStore.isAuthenticated">
          <RouterLink
            to="/dashboard"
            class="hover:text-blue-400 transition font-semibold inline-flex hover:underline"
          >
            Analitics</RouterLink
          >
          <RouterLink
            class="hover:text-blue-400 transition font-semibold hover:underline"
            :to="{ name: 'Calendar' }"
          >
            Calendar
          </RouterLink>
          <RouterLink
            class="hover:text-blue-400 transition font-semibold hover:underline"
            :to="{ name: 'Tasks' }"
          >
            Tasks
          </RouterLink>
          <RouterLink
            to="/dashboard/leads"
            class="hover:text-blue-400 transition font-semibold hover:underline"
          >
            Leads</RouterLink
          >
          <RouterLink
            :to="{ name: 'Clients' }"
            class="hover:text-blue-400 transition font-semibold inline-flex hover:underline"
          >
            Clients</RouterLink
          >
          <RouterLink
            class="hover:text-blue-400 transition font-semibold inline-flex hover:underline"
            :to="{ name: 'Products' }"
            >Products</RouterLink
          >
          <RouterLink
            :to="{ name: 'TeamView' }"
            class="hover:text-blue-400 transition font-semibold inline-flex hover:underline"
          >
            Team</RouterLink
          >
        </template>

        <div class="border-l border-gray-700 h-8 mx-2"></div>

        <div v-if="!authStore.isAuthenticated" class="flex space-x-2">
          <RouterLink
            to="/log-in"
            class="px-4 py-2 hover:text-blue-400 transition-all font-semibold hover:underline"
          >
            Login
          </RouterLink>

          <RouterLink
            to="/sign-up"
            class="px-4 py-2 bg-blue-600 rounded-lg hover:bg-blue-700 transition-all font-semibold"
          >
            Sign Up
          </RouterLink>
        </div>

        <div v-else class="flex items-center space-x-3">
          <RouterLink
            to="/dashboard/my-account"
            class="px-4 py-2 border border-blue-600 rounded-lg hover:bg-blue-600/10 transition-all font-semibold text-blue-400"
          >
            <strong>{{ userStore.user.last_name || 'Admin' }}</strong>
          </RouterLink>

          <button
            @click="logout"
            class="px-4 py-2 bg-red-600 rounded-lg hover:bg-red-700 transition-all font-semibold inline-flex"
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
                d="M8.25 9V5.25A2.25 2.25 0 0 1 10.5 3h6a2.25 2.25 0 0 1 2.25 2.25v13.5A2.25 2.25 0 0 1 16.5 21h-6a2.25 2.25 0 0 1-2.25-2.25V15m-3 0-3-3m0 0 3-3m-3 3H15"
              />
            </svg>
            Logout
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth.js'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/userStore.js'

const authStore = useAuthStore()
const router = useRouter()
const userStore = useUserStore()

const logout = () => {
  authStore.removeToken()
  console.log('Logged-out')
  router.push('/log-in')
}
</script>
