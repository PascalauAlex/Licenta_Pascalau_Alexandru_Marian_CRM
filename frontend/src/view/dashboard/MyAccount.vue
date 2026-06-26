<template>
  <div class="max-w-4xl mx-auto p-6 mt-10 bg-white rounded-xl shadow-md border border-gray-100">
    <div class="mb-8 border-b pb-6">
      <div class="flex items-center gap-4">
        <img
          v-if="userProfile.profile_picture || userProfile.picture_url"
          :src="userProfile.profile_picture || userProfile.picture_url"
          alt="Profile Picture"
          class="w-16 h-16 rounded-full object-cover border-2 border-gray-200 shadow-md"
        />
        <div
          v-else
          class="w-16 h-16 rounded-full bg-blue-900 flex items-center justify-center text-white font-bold text-2xl shadow-md border-2 border-white"
        >
          {{ user.last_name?.charAt(0).toUpperCase() || 'C' }}
        </div>

        <h1 class="font-bold text-heading text-3xl md:text-4xl">
          {{ userProfile.full_name || user.last_name + ' ' + user.first_name }}
        </h1>
      </div>
      <div></div>
      <div class="text-right">
        <router-link
          :to="{ name: 'EditProfile' }"
          class="inline-flex items-center gap-2 bg-white border border-gray-300 hover:bg-gray-50 text-gray-700 font-medium py-2 px-4 rounded-lg shadow-sm transition-colors text-sm"
          >Edit</router-link
        >
      </div>
      <div class="flex">
        <h3 class="font-bold">
          Team:
          <router-link
            class="hover:text-blue-900 hover:underline"
            :to="{ name: 'TeamView' }">{{ team.name }}</router-link>
        </h3>
      </div>
    </div>
    <div class="grid-container">
      <div class="bg-white p-6 rounded-lg border border-blue-100 profile_card group">
        <h2 class="text-2xl font-bold mb-5 text-blue-900">Account Info</h2>
        <div class="space-y-4 text-blue group-hover:font-medium transition-colors duration-300">
          <p>
            <strong class="font-bold text-blue-800">Last Name: </strong
            >{{ user?.last_name || 'N/A' }}
          </p>
          <p>
            <strong class="font-bold text-blue-800">First Name: </strong
            >{{ user?.first_name || 'N/A' }}
          </p>
          <p><strong class="font-bold text-blue-800">Email: </strong>{{ user?.email || 'N/A' }}</p>
          <p>
            <strong class="font-bold text-blue-800">Date joined: </strong
            >{{ user?.date_joined ? formatDate(user.date_joined) : 'N/A' }}
          </p>
        </div>
      </div>

      <div class="bg-white p-6 rounded-lg border border-blue-100 profile_card group">
        <h2 class="text-2xl font-semibold mb-5 text-blue-900">Profile Details</h2>
        <div class="space-y-4 text-black group-hover:font-medium transition-colors duration-300">
          <p>
            <strong class="font-bold text-blue-800">Full Name: </strong
            >{{ userProfile?.full_name || 'N/A' }}
          </p>
          <p>
            <strong class="font-bold text-blue-800">Phone: </strong
            >{{ userProfile?.phone || 'N/A' }}
          </p>
        </div>
      </div>
    </div>
  </div>


</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useUserStore } from '@/stores/userStore.js'
import { storeToRefs } from 'pinia'
import formatDate from '../../../services/formatDate.js'
import { watch } from 'vue'
import { useTeamStore } from '@/stores/teamStore.js'

const userStore = useUserStore()
const teamStore = useTeamStore()

const team = computed(() => teamStore.team)
const { user } = storeToRefs(userStore)
const userProfile = computed(() => userStore.userProfile)

onMounted(async () => {
  if (!userStore.user) {
    await userStore.getUser()
  }
  console.log(userProfile.value)
  if (userStore.user.id) {
    await userStore.getUserProfile(userStore.user.id)
  }
  console.log(useUserStore())
  await teamStore.fetchTeam()

})

watch(
  user,
  (newVal) => {
    if (newVal && newVal.last_name) {
      document.title = `My account | ${newVal.last_name}`
    }
  },
  { immediate: true },
)
</script>

<style>
.profile_card {
  transition: all 0.3s ease;
  color: black;
}

.profile_card:hover {
  transform: scale(1.01) rotate(0deg) translate(0px, -5px) skewX(0deg);
  box-shadow: 0 15px 20px rgba(0, 0, 0, 0.3);
  opacity: 1;
  filter: brightness(1);
  background-color: #ffffff;
  color: black;
}
</style>
