<template>
  <v-app>
    <div class="flex flex-col min-h-screen">
      <header class="navbar-base">
        <NavBar v-if="!route.meta.hideNavbar" />
      </header>

      <main class="flex-1 bg-gray-100">
        <section class="container mx-auto py-8 px-4">
          <router-view />
        </section>
      </main>

      <footer class="bg-gray-900 text-white p-6 text-center">
        <p>&copy; CRM-Pascalau Alexandru Marian 2026</p>
      </footer>
    </div>
  </v-app>
</template>

<script setup>
import NavBar from '@/components/layout/NavBar.vue'
import { onMounted } from 'vue'
import { RouterView } from 'vue-router'
import { useAuthStore } from '@/stores/auth.js'
import { useUserStore } from '@/stores/userStore.js'
import { useRoute } from 'vue-router'

const authStore = useAuthStore()
const userStore = useUserStore()
const route = useRoute()

//INITAILIZAM DUPA REFRESH
onMounted(async () => {
  authStore.initializeStore()

  if (authStore.token && !userStore.user.id) {
    await userStore.getUser()
  }

  if (userStore.user.id) {
    await userStore.getUserProfile(userStore.user.id)
  }
})
</script>

<style></style>
