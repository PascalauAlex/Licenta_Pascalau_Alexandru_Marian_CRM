<template>
  <Transition name="modal-outer">
    <div
      v-show="modalActive"
      class="fixed w-full h-screen top-0 left-0 flex justify-center items-center px-8 z-50 bg-white/10 backdrop-blur-md"
    >
      <Transition name="modal-inner">
        <div
          v-if="modalActive"
          class="p-8 bg-white/80 backdrop-blur-lg border border-white/20 max-w-md w-full rounded-2xl shadow-2xl"
        >
          <div class="flex justify-end mb-2">
            <button
              @click="$emit('close-modal')"
              class="text-gray-500 font-bold hover:text-red-500 transition-colors p-1"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="size-6"
              >
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />
              </svg>
            </button>
          </div>

          <div class="mb-6 text-gray-800">
            <slot />
          </div>
        </div>
      </Transition>
    </div>
  </Transition>
</template>

<script setup>


defineEmits(['close-modal'])

defineProps({
  modalActive: {
    type: Boolean,
    default: false,
  },
})
</script>

<style scoped>
.modal-outer-enter-active,
.modal-outer-leave-active {
  transition: opacity 0.3s cubic-bezier(0.52, 0.02, 0.19, 1.02);
}

.modal-outer-enter-from,
.modal-outer-leave-to {
  opacity: 0;
}

.modal-inner-enter-active {
  transition: all 0.3s cubic-bezier(0.52, 0.02, 0.19, 1.02);
}

.modal-inner-leave-active {
  transition: all 0.3s cubic-bezier(0.52, 0.02, 0.19, 1.02);
}

.modal-inner-enter-from {
  opacity: 0;
  transform: scale(0.8);
}

.modal-inner-leave-to {
  transform: scale(0.8);
}
</style>
