<template>

  <div class="w-full bg-white overflow-hidden rounded-2xl">

    <div class="py-32 md:py-48 px-4 flex justify-center items-center">
      <div class="bg-white p-12 md:p-16 rounded-3xl shadow-xl max-w-4xl text-center">
        <h1
          class="text-4xl md:text-5xl font-extrabold tracking-tighter mb-6 text-gray-950 leading-tight"
        >
          CRM for small and medium businesses
        </h1>
        <p class="text-lg md:text-xl text-gray-700 leading-relaxed max-w-2xl mx-auto">
          Organize and keep track of your leads and teams with modern features including A.I.
          implementations.
        </p>
      </div>
    </div>


    <section class="py-24 bg-white">
      <div class="max-w-7xl mx-auto px-4 flex flex-col items-center">
        <div class="text-center mb-16 md:mb-20">
          <h2
            class="text-3xl md:text-4xl font-extrabold tracking-tighter text-gray-950 mb-4 leading-tight"
          >
            Everything you need to grow
          </h2>
          <p class="text-lg text-gray-700 max-w-2xl mx-auto leading-relaxed mb-16 md:mb-20">
            A unified platform that eliminates chaos from your sales process.
          </p>
        </div>


        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">

          <div
            class="bg-white p-12 rounded-3xl border border-gray-100 text-center flex flex-col items-center shadow-none hover:border-gray-200 transition-all"
          >
            <div
              class="w-14 h-14 bg-blue-100 rounded-xl flex items-center justify-center mb-8 text-blue-600 shadow-none"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-8 w-8"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="1.5"
                  d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
                />
              </svg>
            </div>
            <h3 class="text-2xl font-bold mb-4 text-gray-950">Lead Management</h3>
            <p class="text-lg text-gray-700 leading-relaxed">
              Track every interaction and never lose a potential client again through personalized
              sales pipelines.
            </p>
          </div>


          <div
            class="bg-white p-12 rounded-3xl border border-gray-100 text-center flex flex-col items-center shadow-none hover:border-gray-200 transition-all"
          >
            <div
              class="w-14 h-14 bg-blue-100 rounded-xl flex items-center justify-center mb-8 text-blue-600 shadow-none"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-8 w-8"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="1.5"
                  d="M13 10V3L4 14h7v7l9-11h-7z"
                />
              </svg>
            </div>
            <h3 class="text-2xl font-bold mb-4 text-gray-950">AI Assistant</h3>
            <p class="text-lg text-gray-700 leading-relaxed">
              Extract leads, clients, team members and relevant data using the AI Assistant.
            </p>
          </div>


          <div
            class="bg-white p-12 rounded-3xl border border-gray-100 text-center flex flex-col items-center shadow-none hover:border-gray-200 transition-all"
          >
            <div
              class="w-14 h-14 bg-blue-100 rounded-xl flex items-center justify-center mb-8 text-blue-600 shadow-none"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-8 w-8"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="1.5"
                  d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"
                />
              </svg>
            </div>
            <h3 class="text-2xl font-bold mb-4 text-gray-950">Team Collaboration</h3>
            <p class="text-lg text-gray-700 leading-relaxed">
              Assign leads, leave internal comments, and monitor each member's performance in
              real-time.
            </p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.custom-shadow {
  text-shadow: 4px 4px 0px rgba(30, 58, 138, 0.5);
}
</style>
<script setup>
import { onMounted } from 'vue'
import { initCarousels } from 'flowbite'

onMounted(() => {
  initCarousels()
})
</script>

<style scoped>
.custom-shadow {
  text-shadow: 0 4px 15px rgba(147, 197, 253, 0.5);
}
</style>
