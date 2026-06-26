<script setup>
defineProps({
  columns: {
    type: Array,
    required: true, // Exemplu: [{ key: 'company', label: 'Company Name' }, ...]
  },
  items: {
    type: Array,
    required: true, // Datele primite de la API sau Store
  },
})
</script>

<template>
  <div
    class="relative overflow-x-auto bg-neutral-primary-soft shadow-xs rounded-base border border-default"
  >
    <table class="w-full text-sm text-left rtl:text-right text-body">
      <thead class="text-sm text-body bg-neutral-secondary-medium border-b border-default-medium">
        <tr>
          <th scope="col" class="p-4 w-4">
            <input
              type="checkbox"
              class="w-4 h-4 border border-default-medium rounded-xs bg-neutral-secondary-medium focus:ring-2 focus:ring-brand-soft"
            />
          </th>
          <th v-for="col in columns" :key="col.key" scope="col" class="px-6 py-3 font-medium">
            {{ col.label }}
          </th>
          <th scope="col" class="px-6 py-3 font-medium text-right">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(item, index) in items"
          :key="item.id || index"
          class="bg-neutral-primary-soft border-b border-default hover:bg-neutral-secondary-medium"
        >
          <td class="p-4">
            <input
              type="checkbox"
              class="w-4 h-4 border border-default-medium rounded-xs bg-neutral-secondary-medium focus:ring-2 focus:ring-brand-soft"
            />
          </td>

          <td v-for="col in columns" :key="col.key" class="px-6 py-4" >
            <slot :name="`cell-${col.key}`" :value="item[col.key]" :item="item">
              {{ item[col.key] || '--' }}
            </slot>
          </td>

          <td class="px-6 py-4 text-right">
            <div class="flex justify-end gap-3">
              <slot name="actions" :item="item"></slot>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
