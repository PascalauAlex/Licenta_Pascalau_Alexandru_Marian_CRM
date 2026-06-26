<template>
  <div class="flex items-center gap-6 mb-8">
    <h1 class="font-bold tracking-tight text-heading md:text-5xl lg:text-4xl">Products</h1>
    <div
      class="flex items-center bg-white border border-gray-200 shadow-sm rounded-xl px-4 py-2 text-sm"
    >
      <div class="flex items-center gap-2 pr-4 border-r border-gray-200">
        <span class="text-gray-500 font-medium">Total:</span>
        <span class="font-bold text-blue-600 bg-blue-50 px-2 py-0.5 rounded-md">
          {{ productStore.products.length }}
        </span>
      </div>

      <div class="flex items-center gap-4 pl-4 overflow-x-auto">
        <div class="flex items-center gap-3 ml-2">
          <span class="text-gray-300">|</span>

          <button
            @click="toggleAddProduct"
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
            Add product
          </button>
        </div>
      </div>
    </div>
  </div>
  <div class="">
    <div class="block"><ProductsTable /></div>
  </div>
  <div v-if="addProductModal">
    <DefaultModal :modalActive="addProductModal" @close-modal="toggleAddProduct" class="w-full h-full">
      <div>
        <button
          class="btn bg-blue-900 text-white p-2 mr-2 rounded-lg font-bold hover:bg-blue-800 cursor-pointer"
          @click="toggleCategoryModal"
          :disabled="categoryModal"
        >
          Add category
        </button>
        <button
          class="btn bg-blue-900 text-white p-2 mr-2 rounded-lg font-bold hover:bg-blue-800 cursor-pointer"
          @click="toggleProductModal"
          :disabled="productModal"
        >
          Add product
        </button>
      </div>
      <AddProductForm v-if="productModal"></AddProductForm>
      <AddCategoryForm v-if="categoryModal"></AddCategoryForm>
    </DefaultModal>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import ProductsTable from '@/components/ProductsComponents/ProductsTable.vue'
import { useProductStore } from '@/stores/productStore.js'
import DefaultModal from '@/components/Modals/DefaultModal.vue'
import AddProductForm from '@/components/ProductsComponents/AddProductForm.vue'
import AddCategoryForm from '@/components/ProductsComponents/AddCategoryForm.vue'
const productStore = useProductStore()
const filterStatus = ref(false)
const addProductModal = ref(false)
const categoryModal = ref(false)
const productModal = ref(true)

const toggleCategoryModal = () => {
  categoryModal.value = !categoryModal.value
  productModal.value = false
}

const toggleProductModal = () => {
  productModal.value = !productModal.value
  categoryModal.value = false
}

const toggleAddProduct = () => {
  addProductModal.value = !addProductModal.value
}

const toggleFilter = () => {
  filterStatus.value = !filterStatus.value
}
</script>

<style scoped></style>
