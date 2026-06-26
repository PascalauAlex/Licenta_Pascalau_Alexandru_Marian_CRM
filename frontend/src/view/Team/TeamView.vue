<template>
  <div>
    <div v-if="teamStore.loading" class="flex items-center justify-center py-10">
      <h3 class="text-gray-500 font-medium animate-pulse">Loading team data...</h3>
    </div>

    <div v-else-if="teamStore.team && teamStore.team.members">
      <div class="flex items-center justify-between flex-wrap gap-6 mb-8">
        <div class="border-sm rounded-lg shadow-sm p-2 bg-white w-1/3">
          <h1 class="font-bold tracking-tight text-heading md:text-5xl lg:text-4xl">
            {{ teamStore.team.name }}
          </h1>
          <p class="text-sm text-gray-500 mt-2 font-medium">
            Created at: {{ formatDate(teamStore.team.created_at) }}
          </p>
        </div>

        <div
          class="flex items-center bg-white border border-gray-200 shadow-sm rounded-xl px-4 py-2 text-sm"
        >
          <div class="flex items-center gap-2 pr-4 border-r border-gray-200">
            <span class="text-gray-500 font-medium">Members:</span>
            <span class="font-bold text-blue-600 bg-blue-50 px-2 py-0.5 rounded-md">
              {{ teamStore.team.members.length }}
            </span>
          </div>

          <div
            v-if="teamStore.team.created_by.id === userStore.user.id"
            class="flex items-center gap-3 pl-4 overflow-x-auto"
          >
            <router-link
              :to="{ name: 'AddTeam' }"
              class="inline-flex items-center gap-1.5 bg-white border border-gray-300 hover:bg-gray-50 text-gray-700 font-medium py-1.5 px-3 rounded-md shadow-sm transition-colors text-sm"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="2"
                stroke="currentColor"
                class="w-4 h-4"
              >
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
              </svg>
              Add Team
            </router-link>

            <router-link
              :to="{ name: 'AddMember' }"
              class="inline-flex items-center gap-1.5 bg-white border border-gray-300 hover:bg-gray-50 text-gray-700 font-medium py-1.5 px-3 rounded-md shadow-sm transition-colors text-sm"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="2"
                stroke="currentColor"
                class="w-4 h-4"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M18 18.72a9.094 9.094 0 003.741-.479 3 3 0 00-4.682-2.72m.94 3.198l.001.031c0 .225-.012.447-.037.666A11.944 11.944 0 0112 21c-2.17 0-4.207-.576-5.963-1.584A6.062 6.062 0 016 18.719m12 0a5.971 5.971 0 00-.941-3.197m0 0A5.995 5.995 0 0012 12.75a5.995 5.995 0 00-5.058 2.772m0 0a3 3 0 00-4.681 2.72 8.986 8.986 0 003.74.477m.94-3.197a5.971 5.971 0 00-.94 3.197M15 6.75a3 3 0 11-6 0 3 3 0 016 0zm6 3a2.25 2.25 0 11-4.5 0 2.25 2.25 0 014.5 0zm-13.5 0a2.25 2.25 0 11-4.5 0 2.25 2.25 0 014.5 0z"
                />
              </svg>
              Add Member
            </router-link>
            <button
              @click="generateCode"
              class="inline-flex items-center gap-1.5 cursor-pointer bg-white border border-gray-300 hover:bg-gray-50 text-gray-700 font-medium py-1.5 px-3 rounded-md shadow-sm transition-colors text-sm"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="2"
                stroke="currentColor"
                class="w-4 h-4"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M18 18.72a9.094 9.094 0 003.741-.479 3 3 0 00-4.682-2.72m.94 3.198l.001.031c0 .225-.012.447-.037.666A11.944 11.944 0 0112 21c-2.17 0-4.207-.576-5.963-1.584A6.062 6.062 0 016 18.719m12 0a5.971 5.971 0 00-.941-3.197m0 0A5.995 5.995 0 0012 12.75a5.995 5.995 0 00-5.058 2.772m0 0a3 3 0 00-4.681 2.72 8.986 8.986 0 003.74.477m.94-3.197a5.971 5.971 0 00-.94 3.197M15 6.75a3 3 0 11-6 0 3 3 0 016 0zm6 3a2.25 2.25 0 11-4.5 0 2.25 2.25 0 014.5 0zm-13.5 0a2.25 2.25 0 11-4.5 0 2.25 2.25 0 014.5 0z"
                />
              </svg>
              Generate invite code
            </button>
            <button
              class="inline-flex items-center gap-1.5 cursor-pointer bg-white border border-gray-300 hover:bg-gray-50 text-gray-700 font-medium py-1.5 px-3 rounded-md shadow-sm transition-colors text-sm"
            >
              <a target="_blank" href="http://localhost:8000/admin">Admin center</a>
            </button>
          </div>
        </div>
      </div>
      <div
        v-if="availableInviteCode"
        class="bg-white shadow-sm rounded-lg w-1/4 mt-2 mb-2 p-1 flex flex-col items-center"
      >
        <p class="text-lg font-bold text-gray-800">Invite code</p>
        <span class="text-lg font-mono tracking-wider text-blue-600 mt-1">
          {{ invite_code }}
        </span>
        <p class="text-gray-400 text-center">
          For safety reasons the invite code will expire in one minute!
        </p>
      </div>
      <div class="relative overflow-x-auto bg-white shadow-xs rounded-base border border-default">
        <table class="w-full text-sm text-left text-body">
          <thead
            class="text-sm text-body bg-neutral-secondary-medium border-b border-default-medium"
          >
            <tr>
              <th scope="col" class="px-6 py-4 font-bold">Member</th>
              <th scope="col" class="px-6 py-4 font-bold">Full Name</th>
              <th scope="col" class="px-6 py-4 font-bold">Rol</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="member in teamStore.team.members"
              :key="member.id"
              class="bg-neutral-primary-soft border-b border-default hover:bg-gray-50 transition-colors"
            >
              <th scope="row" class="px-6 py-4 font-medium text-heading whitespace-nowrap">
                <div class="flex items-center gap-3">
                  <div
                    class="w-8 h-8 rounded-full bg-blue-100 flex items-center justify-center text-blue-700 font-bold text-sm shadow-sm"
                  >
                    {{ member.username.charAt(0).toUpperCase() }}
                  </div>
                  <span class="font-bold text-gray-800">{{ member.username }}</span>
                </div>
              </th>
              <td class="px-6 py-4 text-gray-600">
                <template v-if="member.first_name || member.last_name">
                  {{ member.first_name }} {{ member.last_name }}
                </template>
                <span v-else class="text-gray-400 italic">Fără nume setat</span>
              </td>
              <td class="px-6 py-4">
                <span
                  v-if="member.id === teamStore.team.created_by.id"
                  class="px-2.5 py-1 bg-green-50 border border-green-200 text-green-700 text-xs font-medium rounded-md shadow-sm"
                >
                  Admin / Creator
                </span>
                <span
                  v-else
                  class="px-2.5 py-1 bg-gray-50 border border-gray-200 text-gray-600 text-xs font-medium rounded-md shadow-sm"
                >
                  Membru
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div
      v-else
      class="flex flex-col items-center justify-center py-20 bg-white border border-gray-200 rounded-xl shadow-sm mt-8 text-center px-4"
    >
      <svg
        class="w-16 h-16 text-gray-300 mb-4"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
        stroke-width="1.5"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M15 19.128a9.38 9.38 0 002.625.372 9.337 9.337 0 004.121-.952 4.125 4.125 0 00-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 018.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0111.964-3.07M12 6.375a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zm8.25 2.25a2.625 2.625 0 11-5.25 0 2.625 2.625 0 015.25 0z"
        />
      </svg>
      <h3 class="text-lg font-bold text-gray-900 mb-1">
        You don't belong to any team, please contact the administrator
      </h3>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { useTeamStore } from '@/stores/teamStore.js'
import formatDate from '../../../services/formatDate.js'
import { useUserStore } from '@/stores/userStore.js'
import api from '@/utils/api.js'

const teamStore = useTeamStore()
const userStore = useUserStore()

const userProfile = computed(() => userStore.userProfile)
const invite_code = ref('')

onMounted(() => {
  teamStore.fetchTeam()
  userStore.getUser()
})
const availableInviteCode = ref(false)

async function generateCode() {
  try {
    const response = await api.get('/api/v1/teams/generate_invite_code/')
    if (response.statusText === 'OK') {
      invite_code.value = response.data['invite_code']
      availableInviteCode.value = !availableInviteCode.value
    }
  } catch (error) {
    console.log(error)
  }
}
</script>
