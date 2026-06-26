<template>
  <div class="border-sm shadow-sm rounded-lg p-2">
    <h3>Assign new product to lead</h3>
  </div>
  <div class="border-sm shadow-sm rounded-lg p-2 mt-2">
    <div>
      <form @submit.prevent="save">
        <div>
          <label for="category" class="block text-sm font-medium text-gray-700 mb-2">
            Category <span class="text-red-500">*</span>
          </label>
          <select class="border-gray-300 rounded-lg w-full" v-model="category">
            <option disabled selected>Select category</option>
            <option value="product">Product</option>
            <option value="service">Service</option>
          </select>
        </div>
        <div>
          <label for="product" class="block text-sm font-medium text-gray-700 mb-2">
            Product <span class="text-red-500">*</span>
          </label>
          <select
            class="border-gray-300 rounded-lg w-full"
            v-model="selectedProduct"
            @change="addProductToLead"
          >
            <option :value="null" disabled>Select a product</option>
            <option v-for="item in productsByCategory(category)" :key="item.id" :value="item">
              [{{ item.sku }}] {{ item.name }} -- ({{ item.base_price }} {{ item.currency }})
            </option>
          </select>
        </div>
        <div
          v-for="interest in leadInterest"
          :key="interest.product.id"
          class="flex items-center gap-3 mt-2 p-2 border rounded-lg"
        >
          <span class="text-sm flex-1"
            >[{{ interest.product.sku }}] {{ interest.product.name }}</span
          >

          <input
            type="number"
            min="1"
            v-model="interest.quantity"
            class="border-gray-300 rounded-lg w-20"
          />

          <input
            type="number"
            min="0"
            max="100"
            placeholder="%"
            v-model="interest.discount"
            class="border-gray-300 rounded-lg w-20"
          />

          <button
            type="button"
            @click="removeFromCart(interest.product.id)"
            class="text-red-500 hover:text-red-700"
          >
            ✕
          </button>
        </div>

        <div class="pt-1">
          <label class="flex text-sm font-medium text-gray-700 mb-2">Total value</label>
          <span>{{ total }}</span>
        </div>
        <button
          class="bg-blue-900 text-white rounded-lg p-2 pl-3 pr-3 mt-2"
          type="submit"
        >
          Add
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/productStore.js'
import { computed, onMounted, ref } from 'vue'
import { useLeadStore } from '@/stores/leadStore.js'
import { useRoute } from 'vue-router'

const route = useRoute()
const category = ref('')
const productStore = useProductStore()
const selectedProduct = ref('')
const leadInterest = ref([])

onMounted(async () => {
  await productStore.getProducts()
})

const total = computed(() => {
  return leadInterest.value
    .reduce((sum, interest) => {
      const price = interest.product.base_price
      const quantity = interest.quantity || 1
      const discount = interest.discount || 0
      const lineTotal = price * quantity * (1 - discount / 100)
      return sum + lineTotal
    }, 0)
    .toFixed(2)
})

const productQuantity = ref(1)
const productDiscount = ref(0)

function productsByCategory(category) {
  if (!category) {
    return []
  }
  if (category === 'product') {
    return productStore.products.filter((p) => p.type === category)
  } else return productStore.products.filter((p) => p.type === category)
}

function addProductToLead() {
  if (!selectedProduct.value) {
    return
  }
  const product = selectedProduct.value
  const existing = leadInterest.value.find((i) => i.product.id === product.id)

  if (existing) {
    existing.quantity++
  } else {
    leadInterest.value.push({
      product,
      quantity: productQuantity.value,
      estimated_value: null,
      notes: '',
      discount: productDiscount.value,
    })
  }
  selectedProduct.value = null
}

function removeFromCart(productId) {
  leadInterest.value = leadInterest.value.filter((i) => i.product.id !== productId)
}

const save = async () => {
  const payload = {
    product_interests: leadInterest.value.map((i) => ({
      product: i.product.id,
      quantity: Number(i.quantity),
      discount: Number(i.discount) || 0,
    })),
  }
  try {
    await useLeadStore().editLead(route.params.id, payload)
  } catch (err) {
    console.error('Edit failed', err.response?.data)
  }
}
</script>
<style scoped></style>
