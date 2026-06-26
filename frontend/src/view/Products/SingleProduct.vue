<template>
  <div class="flex gap-6">
    <div class="bg-white border border-gray-200 shadow-md rounded-2xl p-6 md:p-8 w-2/3">
      <h2 class="text-xl font-bold text-gray-800 mb-6 border-b border-gray-100 pb-4">
        <span class="text-blue-900">{{ product.sku }}</span>
        <span class="text-gray-500"> | </span>
        <span title="Product Name" class="text-blue-900">{{ product.name }}</span>
        <button
          v-if="userStore.user.is_staff"
          type="button"
          title="Edit button"
          aria-label="Edit product"
          class="ml-2 p-1.5 rounded-md text-gray-400 hover:text-blue-600 hover:bg-blue-50 transition cursor-pointer"
          @click="router.push({ name: 'EditProduct', params: { id: route.params.id } })"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="w-5 h-5"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L6.832 19.82a4.5 4.5 0 0 1-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 0 1 1.13-1.897L16.863 4.487Zm0 0L19.5 7.125"
            />
          </svg>
        </button>
        <span class="block text-gray-400 text-sm"
          >Status:
          <span v-if="product.is_active">
            <svg
              class="w-5 h-5 text-green-600 inline-flex"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="2"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
              /></svg
            >Active
          </span>
          <span v-else>
            <svg
              class="w-5 h-5 text-red-600 inline-flex"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="2"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
          </span>
        </span>
      </h2>
      <div class="">
        <div class="mt-2">
          <span class="block text-sm font-medium text-gray-500 mb-1">Category</span>
          <span class="block text-base font-semibold text-gray-900">{{
            product.category?.name || '-'
          }}</span>
        </div>

        <div class="mt-2">
          <span class="block text-sm font-medium text-gray-500 mb-1">Description</span>
          <span class="block text-base font-semibold text-gray-900">{{
            product.description || '-'
          }}</span>
        </div>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-y-6 gap-x-8">
        <div>
          <span class="block text-sm font-medium text-gray-500 mb-1">Product type</span>
          <span class="block text-base font-semibold text-gray-900">{{ product.type || '-' }}</span>
        </div>
      </div>

      <div class="mt-2">
        <span class="block text-sm font-medium text-gray-500 mb-1">Unit of measure</span>
        <span class="block text-base font-semibold text-gray-900">{{
          product.unit_of_measure || '-'
        }}</span>
      </div>

      <div class="mt-2">
        <span class="block text-sm font-medium text-gray-500 mb-1">Base price</span>
        <span class="block text-base font-semibold text-gray-900">{{
          product.base_price || '-'
        }}</span>
      </div>
      <div class="mt-2">
        <span class="block text-sm font-medium text-gray-500 mb-1">Currency</span>
        <span class="block text-base font-semibold text-gray-900">{{
          product.currency || '-'
        }}</span>
      </div>

      <div class="mt-2">
        <span class="block text-sm font-medium text-gray-500 mb-1">Vat rate</span>
        <span class="block text-base font-semibold text-gray-900">{{
          product.vat_rate + ' %' || '-'
        }}</span>
      </div>
      <div class="mt-4">
        <router-link
          class="bg-blue-900 hover:bg-blue-700 text-white p-1 font-semibold rounded-lg"
          :to="{ name: 'Products' }"
          title="Back to all Products"
          >Back</router-link
        >
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useProductStore } from '@/stores/productStore.js'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/userStore.js'
import DefaultModal from '@/components/Modals/DefaultModal.vue'
const productStore = useProductStore()
const router = useRouter()
const route = useRoute()

const product = computed(() => productStore.product)
const userStore = useUserStore()
onMounted(async () => {
  await productStore.getProductById(route.params.id)
  console.log(userStore.user)
  console.log(productStore.product)
})

const handleEdit = () => {}
</script>

<style scoped></style>
