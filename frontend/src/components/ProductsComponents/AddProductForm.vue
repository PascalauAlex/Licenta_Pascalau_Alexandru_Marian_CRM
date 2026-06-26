<template>
  <div class="max-w-3xl mx-auto p-6">
    <div class="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
      <!-- Header -->
      <div
        class="px-8 py-6 border-b border-gray-200 bg-linear-to-r from-indigo-50 via-white to-white"
      >
        <div class="flex items-center gap-3">
          <div class="flex items-center justify-center w-10 h-10 bg-indigo-100 rounded-lg">
            <svg
              class="w-5 h-5 text-indigo-600"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="2"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"
              />
            </svg>
          </div>
          <div>
            <h2 class="text-lg font-semibold text-gray-900">Add new product</h2>
            <p class="text-sm text-gray-500">Add an item to your catalog</p>
          </div>
        </div>
      </div>

      <!-- Form -->
      <form @submit.prevent="addProduct" class="px-8 py-6 space-y-6">
        <!-- SKU + Name -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div class="md:col-span-1">
            <label class="block text-sm font-medium text-gray-700 mb-1.5">
              SKU <span class="text-red-500">*</span>
            </label>
            <input
              v-model="sku"
              type="text"
              placeholder="LAPTOP-DELL-XPS15"
              required
              class="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition outline-none"
            />
          </div>

          <div class="md:col-span-2">
            <label class="block text-sm font-medium text-gray-700 mb-1.5">
              Name <span class="text-red-500">*</span>
            </label>
            <input
              v-model="name"
              type="text"
              placeholder="Dell XPS 15 Laptop"
              required
              class="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition outline-none"
            />
          </div>
        </div>

        <!-- Description -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1.5">Description</label>
          <textarea
            v-model="description"
            rows="3"
            placeholder="Optional product description..."
            class="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition outline-none resize-none"
          ></textarea>
        </div>

        <!-- Type + Category -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1.5">
              Type <span class="text-red-500">*</span>
            </label>
            <select
              v-model="type"
              class="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition outline-none bg-white"
            >
              <option value="product">Product</option>
              <option value="service">Service</option>
            </select>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1.5">
              Category <span class="text-red-500">*</span>
            </label>
            <select
              v-model="category_id"
              required
              class="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition outline-none bg-white"
            >
              <option disabled>Select a category...</option>
              <option
                v-for="category in productStore.categories"
                :value="category.id"
                :key="category.id"
              >{{category.name}}</option>
            </select>
          </div>
        </div>

        <!-- Unit of measure -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1.5">
            Unit of measure <span class="text-red-500">*</span>
          </label>
          <select
            v-model="unit_of_measure"
            class="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition outline-none bg-white"
          >
            <option value="piece">Piece</option>
            <option value="hour">Hour</option>
            <option value="month">Month</option>
            <option value="project">Project</option>
          </select>
        </div>

        <!-- Pricing section -->
        <div class="bg-gray-50 rounded-xl p-5 border border-gray-200">
          <div class="flex items-center gap-2 mb-4">
            <svg
              class="w-4 h-4 text-gray-500"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="2"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
            <h3 class="text-sm font-semibold text-gray-700">Pricing</h3>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div>
              <label class="block text-xs font-medium text-gray-600 mb-1.5">
                Base price <span class="text-red-500">*</span>
              </label>
              <input
                v-model.number="base_price"
                type="number"
                min="0"
                step="0.01"
                placeholder="0.00"
                required
                class="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition outline-none bg-white"
              />
            </div>

            <div>
              <label class="block text-xs font-medium text-gray-600 mb-1.5">Currency</label>
              <select
                v-model="currency"
                class="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition outline-none bg-white"
              >
                <option value="RON">RON</option>
                <option value="EUR">EUR</option>
                <option value="USD">USD</option>
                <option value="GBP">GBP</option>
              </select>
            </div>

            <div>
              <label class="block text-xs font-medium text-gray-600 mb-1.5">VAT rate (%)</label>
              <input
                v-model.number="vat_rate"
                type="number"
                min="0"
                max="100"
                step="0.01"
                class="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition outline-none bg-white"
              />
            </div>
          </div>
        </div>

        <!-- Active toggle -->
        <div
          class="flex items-center justify-between p-4 bg-gray-50 rounded-xl border border-gray-200"
        >
          <div>
            <p class="text-sm font-medium text-gray-700">Product status</p>
            <span class="inline-flex text-sm font-medium text-green-400" v-if="is_active"
              >Active</span
            >
            <span class="text-sm font-medium text-red-400" v-if="!is_active">Inactive</span>
            <button
              type="button"
              class="block text-sm bg-gray-600 rounded-lg p-1 text-white font-semibold hover:bg-gray-400 cursor-pointer"
              @click="is_active = !is_active"
            >
              Disable
            </button>
          </div>
        </div>

        <!-- Error message -->
        <div v-if="error" class="p-3 bg-red-50 border border-red-200 rounded-lg">
          <p class="text-sm text-red-700">{{ error }}</p>
        </div>

        <!-- Actions -->
        <div class="flex items-center justify-end gap-3 pt-4 border-t border-gray-200">
          <button
            type="button"
            @click="resetForm"
            class="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 transition focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
          >
            Cancel
          </button>
          <button
            type="submit"
            :disabled="loading"
            class="inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-white bg-blue-900 rounded-lg hover:bg-blue-800 transition focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <svg v-if="loading" class="w-4 h-4 animate-spin" fill="none" viewBox="0 0 24 24">
              <circle
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                stroke-width="3"
                class="opacity-25"
              />
              <path
                fill="currentColor"
                class="opacity-75"
                d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"
              />
            </svg>
            {{ loading ? 'Saving...' : 'Add product' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'

import { useProductStore } from '@/stores/productStore.js'

const productStore = useProductStore()

const loading = ref(false)
const error = ref(null)
const sku = ref('')
const name = ref('')
const description = ref('')
const type = ref('')
const category_id = ref('')
const unit_of_measure = ref()
const base_price = ref()
const is_active = ref(true)
const currency = ref()
const vat_rate = ref()

onMounted(async () => {
  try {
    await productStore.getCategories()
    console.log(productStore.categories)
  } catch (err) {
    console.error('Error while getting categories', err)
  }
})

const addProduct = async () => {
  const productData = {
    sku: sku.value,
    name: name.value,
    description: description.value,
    type: type.value,
    category_id: category_id.value,
    unit_of_measure: unit_of_measure.value,
    base_price: base_price.value,
    is_active: is_active.value,
    currency: currency.value,
    vat_rate: vat_rate.value,
  }

  try {
    await productStore.createProduct(productData)
  } catch (err) {
    console.error(err)
  }
}
</script>
