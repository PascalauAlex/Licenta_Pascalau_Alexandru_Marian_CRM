<template>
  <div class="relative w-full h-screen overflow-hidden rounded-2xl">
    <img
      src="/images/new-york-window.jpg"
      alt="office-background-wallpaper"
      class="absolute inset-0 w-full h-full object-cover"
    />

    <div
      class="absolute inset-0 bg-blue-700/30 flex flex-col items-center justify-center text-center px-4"
    >
      <div class="bg-blue-900/70 rounded-3xl p-8 md:p-12 backdrop-blur-sm max-w-5xl">
        <h1 class="font-bold text-blue-100 text-7xl md:text-9xl mb-4 custom-shadow">CRM</h1>

        <p class="font-bold text-white text-xl md:text-3xl mb-8">
          Organize and keep track of your leads and teams with modern features including A.I.
          implementations.
        </p>

        <div class="flex flex-wrap gap-4 justify-center">
          <button
            class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-4 px-10 rounded-full transition-all shadow-lg transform hover:scale-105"
          >
            Start for Free
          </button>
          <button
            class="bg-white/10 hover:bg-white/20 text-white border border-white/30 font-bold py-4 px-10 rounded-full backdrop-blur-sm transition-all transform hover:scale-105"
          >
            Watch Demo
          </button>
        </div>
      </div>
    </div>
  </div>

  <section class="py-20 bg-gray-50">
    <div class="max-w-7xl mx-auto px-4">
      <div class="text-center mb-16">
        <h2 class="text-3xl md:text-5xl font-bold text-gray-900 mb-4">
          Everything you need to grow
        </h2>
        <p class="text-gray-600 max-w-2xl mx-auto text-lg">
          A unified platform that eliminates chaos from your sales process.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div
          class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow text-center"
        >
          <div
            class="w-14 h-14 bg-blue-100 rounded-xl flex items-center justify-center mb-6 text-blue-600 mx-auto"
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
                stroke-width="2"
                d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
              />
            </svg>
          </div>
          <h3 class="text-xl font-bold mb-3 text-gray-900">Lead Management</h3>
          <p class="text-gray-600">
            Track every interaction and never lose a potential client again through personalized
            sales pipelines.
          </p>
        </div>

        <div
          class="bg-blue-900 p-8 rounded-2xl shadow-xl text-white transform md:-translate-y-4 text-center border border-blue-800"
        >
          <div
            class="w-14 h-14 bg-blue-500 rounded-xl flex items-center justify-center mb-6 text-white mx-auto shadow-lg"
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
                stroke-width="2"
                d="M13 10V3L4 14h7v7l9-11h-7z"
              />
            </svg>
          </div>
          <h3 class="text-xl font-bold mb-3">AI Predictions</h3>
          <p class="text-blue-100">
            Our AI analyzes lead behavior and identifies which prospects have the highest conversion
            probability.
          </p>
        </div>

        <div
          class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow text-center"
        >
          <div
            class="w-14 h-14 bg-blue-100 rounded-xl flex items-center justify-center mb-6 text-blue-600 mx-auto"
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
                stroke-width="2"
                d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"
              />
            </svg>
          </div>
          <h3 class="text-xl font-bold mb-3 text-gray-900">Team Collaboration</h3>
          <p class="text-gray-600">
            Assign leads, leave internal comments, and monitor each member's performance in
            real-time.
          </p>
        </div>
      </div>
    </div>
  </section>

  <div class="bg-white py-16 border-y border-gray-100">
    <div
      class="max-w-7xl mx-auto px-4 flex flex-wrap justify-around items-center gap-12 text-center"
    >
      <div class="flex flex-col">
        <p class="text-5xl font-extrabold text-blue-600 mb-2">10k+</p>
        <p class="text-gray-500 uppercase tracking-widest text-sm font-bold">Active Users</p>
      </div>
      <div class="flex flex-col">
        <p class="text-5xl font-extrabold text-blue-600 mb-2">45%</p>
        <p class="text-gray-500 uppercase tracking-widest text-sm font-bold">Sales Growth</p>
      </div>
      <div class="flex flex-col">
        <p class="text-5xl font-extrabold text-blue-600 mb-2">24/7</p>
        <p class="text-gray-500 uppercase tracking-widest text-sm font-bold">AI Support</p>
      </div>
    </div>
  </div>

  <section class="py-24">
    <div
      class="max-w-5xl mx-auto px-6 bg-blue-600 rounded-3xl p-12 text-center text-white relative overflow-hidden shadow-2xl"
    >
      <div class="relative z-10">
        <h2 class="text-3xl md:text-5xl font-bold mb-6 italic">
          Ready to transform your business?
        </h2>
        <p class="text-blue-100 mb-10 text-xl max-w-2xl mx-auto">
          Join hundreds of companies using our CRM to automate their success and increase revenue.
        </p>
        <router-link
          :to="{name:'SignUp'}"
          class="bg-white text-blue-600 font-bold py-4 px-12 rounded-full hover:bg-gray-100 transition-all shadow-xl inline-block"
        >
          Create Free Account
        </router-link>
      </div>
      <div class="absolute -top-24 -right-24 w-80 h-80 bg-blue-500 rounded-full opacity-40"></div>
      <div class="absolute -bottom-24 -left-24 w-64 h-64 bg-blue-400 rounded-full opacity-30"></div>
    </div>
  </section>
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
