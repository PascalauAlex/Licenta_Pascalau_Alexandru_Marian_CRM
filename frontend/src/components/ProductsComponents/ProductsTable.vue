<template>
  <div class="relative overflow-x-auto bg-white shadow-xs rounded-base border border-default">
    <table class="w-full text-sm text-left rtl:text-right text-body">
      <thead class="text-sm text-body bg-neutral-secondary-medium border-b border-default-medium">
        <tr>
          <th scope="col" class="px-6 py-3 font-bold">No.</th>
          <th scope="col" class="px-6 py-3 font-bold">SKU</th>
          <th scope="col" class="px-6 py-3 font-bold">Name</th>
          <th scope="col" class="px-6 py-3 font-bold">category</th>
          <th scope="col" class="px-6 py-3 font-bold">Type</th>
          <th scope="col" class="px-6 py-3 font-bold">Unit of measure</th>
          <th scope="col" class="px-6 py-3 font-bold">Base Price</th>
          <th scope="col" class="px-6 py-3 font-bold">Currency</th>
          <th scope="col" class="px-6 py-3 font-bold">Vat rate</th>
          <th scope="col" class="px-6 py-3 font-bold">Is active</th>
        </tr>
      </thead>
      <tbody>
        <tr
          class="bg-neutral-primary-soft border-b border-default hover:bg-neutral-secondary-medium hover:bg-gray-100 hover:cursor-pointer"
          v-for="product in productStore.products"
          :key="product.id"
          id="table-hover"
          @click="router.push({ name: 'SingleProduct', params: { id: product.id } })"
        >
          <th class="px-6 py-4">
            {{ product.id }}
          </th>
          <td class="px-6 py-4">{{ product.sku }}</td>
          <td class="px-6 py-4">{{ product.name }}</td>
          <td class="px-6 py-4">{{ product.category.name }}</td>
          <td class="px-6 py-4">{{ capitalizeFirstLetter(product.type) }}</td>
          <td class="px-6 py-4">{{ capitalizeFirstLetter(product.unit_of_measure) }}</td>
          <td class="px-6 py-4">{{ product.base_price }}</td>
          <td class="px-6 py-4">{{ product.currency }}</td>
          <td class="px-6 py-4">{{ product.vat_rate }} %</td>
          <td class="px-6 py-4">
            <span v-if="product.is_active"
              ><svg
                class="w-5 h-5 text-green-600"
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
            ></span>
            <span v-else
              ><svg
                class="w-5 h-5 text-red-600"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"

              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
                /></svg
            ></span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useProductStore } from '@/stores/productStore.js'
import { useRouter } from 'vue-router'
const productStore = useProductStore()
const router = useRouter()

const capitalizeFirstLetter = (string) => {
  const firstLetter = string.charAt(0).toUpperCase()
  const remainingLetters = string.slice(1)
  return firstLetter + remainingLetters
}

onMounted(async () => {
  await productStore.getProducts()
  console.log(productStore.products)
})
</script>

<style scoped></style>
