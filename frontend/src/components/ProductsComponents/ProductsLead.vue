<template>
  <div
    class="relative overflow-x-auto bg-white shadow-xs rounded-base border border-default w-full"
  >
    <table class="w-full text-sm text-left rtl:text-right text-body">
      <thead class="text-sm text-body bg-neutral-secondary-medium border-b border-default-medium">
        <tr>
          <th scope="col" class="px-6 py-3 font-bold">Product</th>
          <th scope="col" class="px-6 py-3 font-bold">Quantity</th>
          <th scope="col" class="px-6 py-3 font-bold">U.M</th>
          <th scope="col" class="px-6 py-3 font-bold">Notes</th>
          <th scope="col" class="px-6 py-3 font-bold">Added at</th>
          <th scope="col" class="px-6 py-3 font-bold">Category</th>
          <th scope="col" class="px-6 py-3 font-bold">Value</th>
          <th scope="col" class="px-6 py-3 font-bold">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="interest in productStore.leadProduct"
          :key="interest.id"
          id="table-hover"
          class="bg-neutral-primary-soft border-b border-default hover:bg-neutral-secondary-medium hover:bg-gray-100 hover:cursor-pointer"
        >
          <th
            @click="router.push({ name: 'SingleProduct', params: { id: interest.product.id } })"
            class="px-6 py-4"
          >
            {{ interest.product.name }}
          </th>
          <th class="px-6 py-4">{{ interest.quantity }}</th>
          <th class="px-6 py-4">{{ capitalizeFirstLetter(interest.product.unit_of_measure) }}</th>
          <th class="px-6 py-4">{{ interest.notes }}</th>
          <th class="px-6 py-4">{{ formatDate(interest.added_at) }}</th>
          <th class="px-6 py-4">{{ interest.product.category.name }}</th>
          <th class="px-6 py-4">{{ interest.estimated_value }}</th>
          <th class="px-6 py-4">
            <button class="hover:text-red-500 pl-1" @click="deleteInterest(interest.id)">
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
                  d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0"
                />
              </svg>
            </button>
          </th>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useProductStore } from '@/stores/productStore.js'
import { useRoute } from 'vue-router'
import { useToast } from 'vue-toast-notification'
import router from '@/router/index.js'
import formatDate from '../../../services/formatDate.js'

const productStore = useProductStore()
const route = useRoute()
const toast = useToast()

onMounted(async () => {
  try {
    await productStore.getLeadProduct(route.params.id)
  } catch (err) {
    console.error('Error while getting the products for the lead!', err)
    toast.error('Error while getting the products for the lead!')
  }
})

function capitalizeFirstLetter(string) {
  const firstLetter = string.charAt(0).toUpperCase()
  return firstLetter + string.slice(1)

}

const deleteInterest = async (interestID) => {
  try {
    let ok = confirm('Are you sure to delete this interest?')
    if (ok) {
      await productStore.deleteLeadProductInterest(interestID)
    }
  } catch (err) {
    console.error(err)
  }
}
</script>

<style scoped></style>
