<template>
  <div class="max-w-3xl mx-auto p-6 h-200">
    <div class="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden h-full">
      <div
        class="px-8 py-6 border-b border-gray-200 bg-linear-to-r from-orange-50 via-white to-white h-full"
      >
        <div class="flex items-center gap-3">
          <div class="flex items-center justify-center w-10 h-10 bg-orange-100 rounded-lg">
            <svg
              class="w-5 h-5 text-orange-600"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="2"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M3 7a2 2 0 012-2h4l2 2h8a2 2 0 012 2v8a2 2 0 01-2 2H5a2 2 0 01-2-2V7z"
              />
            </svg>
          </div>
          <div>
            <h2 class="text-lg font-semibold text-gray-900">Add new category</h2>
            <p class="text-sm text-gray-500">Add a new category</p>
          </div>
        </div>
        <form @submit.prevent="addCategory" class="px-8 py-6 space-y-6">
          <div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1.5">
                Category Name <span class="text-red-500">*</span>
                <input
                  v-model="name"
                  type="text"
                  placeholder="Software"
                  required
                  class="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition outline-none"
                />
              </label>
              <button class="align-end justify-end bg-orange-900 rounded-lg p-2 text-white" type="submit">Add category</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
<script setup>
import { useProductStore } from '@/stores/productStore.js'
import { ref } from 'vue'

const productStore = useProductStore()
const name = ref('')


async function addCategory(){
  const categoryName = {
    name : name.value
  }

  try{
    await productStore.createCategory(categoryName)
  }catch (err){
    console.error(err)
  }
}

</script>

<style scoped></style>
