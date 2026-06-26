<template>
  <div>
    <div class="font-bold boder-default shadow-sm rounded-lg p-2">
      <h3>Move lead to another status</h3>
    </div>
    <div v-if="lead.status === 'new'" class="my-3">
      <form @submit.prevent="submitChecklist">
        <div
          class="flex items-center ps-4 bg-neutral-primary-soft border border-default rounded-base shadow-xs p-3 mb-3"
        >
          <ul>
            <li>
              <input
                type="checkbox"
                id="contacted"
                name="contacted"
                v-model="checklist_data.new.contacted"
                class="w-4 h-4 border border-default-medium rounded-xs bg-neutral-secondary-medium focus:ring-2 focus:ring-brand-soft"
              />
              <label for="contacted" class="text-heading"> Contacted </label>
            </li>
            <li>
              <label for="contact_method">Contact method: </label>
              <select v-model="checklist_data.new.contact_method" class="bg-blue-50 rounded">
                <option selected disabled value="">Chose a contact method</option>
                <option
                  v-for="option in contactMethods"
                  :key="option.value"
                  :value="option.value"
                  class="font-medium"
                >
                  {{ option.label }}
                </option>
              </select>
            </li>
          </ul>
        </div>
        <button
          type="submit"
          class="bg-blue-600 hover:bg-white hover:text-blue-600 hover:outline-1 text-white px-4 py-2 rounded font-medium text-sm transition-all disabled:opacity-50"
        >
          Save
        </button>
      </form>
    </div>

    <div v-if="lead.status === 'contacted'" class="my-3 bg-white p-4 rounded shadow">
      <form @submit.prevent="submitChecklist">
        <ul>
          <li>
            <input
              type="checkbox"
              id="has_budget"
              name="has_budget"
              v-model="checklist_data.contacted.has_budget"
              class="w-5 h-5 accent-blue-600 cursor-pointer"
            />
            <label for="has_budget"> Has Budget </label>
          </li>
          <li>
            <input
              type="checkbox"
              id="can_solve_problem"
              name="can_solve_problem"
              v-model="checklist_data.contacted.can_solve_problem"
              class="w-5 h-5 accent-blue-600 cursor-pointer"
            />
            <label for="can_solve_problem"> Can solve problem </label>
          </li>
          <li>
            <input
              type="checkbox"
              id="is_decision_maker"
              name="is_decision_maker"
              v-model="checklist_data.contacted.is_decision_maker"
              class="w-5 h-5 accent-blue-600 cursor-pointer"
            />
            <label for="is_decision_maker"> Is decision maker </label>
          </li>
        </ul>
        <button
          type="submit"
          class="bg-blue-600 hover:bg-white hover:text-blue-600 hover:outline-1 text-white px-4 py-2 mt-2 rounded font-medium text-sm transition-all disabled:opacity-50"
        >
          Save
        </button>
      </form>
    </div>

    <div v-if="lead.status === 'inprogress'" class="my-3 bg-white p-4 rounded shadow">
      <form @submit.prevent="submitChecklist">
        <div>
          <ul>
            <li>
              <input
                type="checkbox"
                id="offer_send"
                name="offer_send"
                v-model="checklist_data.inprogress.offer_send"
                class="w-5 h-5 accent-blue-600 cursor-pointer"
              />
              <label for="offer_send"> Offer send </label>
            </li>
            <li>
              <input
                type="checkbox"
                id="offer_dicussed"
                name="offer_discussed"
                v-model="checklist_data.inprogress.offer_discussed"
                class="w-5 h-5 accent-blue-600 cursor-pointer"
              />
              <label for="offer_dicussed"> Offer discussed </label>
            </li>
            <li>
              <input
                type="checkbox"
                id="negotiation_started"
                name="negotiation_started"
                value="false"
                v-model="checklist_data.inprogress.negotiation_started"
                class="w-5 h-5 accent-blue-600 cursor-pointer"
              />
              <label for="negotiation_started"> Negotiation started </label>
            </li>
          </ul>
        </div>

        <div v-if="checklist_data.inprogress.negotiation_started && !checklist_data.lost.lost">
          <input
            type="checkbox"
            id="won"
            name="won"
            value="false"
            v-model="checklist_data.won.won"
          />
          <label for="won"> Won</label>
        </div>
        <div v-if="checklist_data.inprogress && !checklist_data.won.won">
          <input
            type="checkbox"
            id="lost"
            name="lost"
            value="false"
            v-model="checklist_data.lost.lost"
          />
          <label for="lost"> Lost</label>
          <div v-if="checklist_data.lost.lost" class="shadow-sm rounded-lg p-2 mt-5">
            <h3>Enter the lost reason</h3>
            <label>Category</label>
            <select class="rounded-lg block" v-model="lost_reason_id">
              <option v-for="reason in leadStore.lost_reasons" :key="reason.id" :value="reason.id">
                {{ reason.name }}
              </option>
            </select>
            <div>
              <h3>Lost reason details</h3>
              <textarea class="rounded-lg" v-model="lost_reason_details"></textarea>
            </div>
          </div>
        </div>
        <button
          type="submit"
          class="bg-blue-600 hover:bg-white hover:text-blue-600 hover:outline-1 text-white px-4 py-2 mt-2 rounded font-medium text-sm transition-all disabled:opacity-50"
        >
          Save
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useLeadStore } from '@/stores/leadStore.js'
import { useToast } from 'vue-toast-notification'

const leadStore = useLeadStore()

const toast = useToast()

const props = defineProps({
  lead: {
    type: Object, // Am scos parantezele pătrate de aici, "Object" este clasa
    required: true,
  },
})

const lost_reason_id = ref(props.lead.lost_reason?.id ?? null)
const lost_reason_details = ref('')

const emit = defineEmits(['checklist-saved'])

const checklist_data = ref({
  new: { contacted: false, contact_method: '' },
  contacted: { has_budget: false, can_solve_problem: false, is_decision_maker: false },
  inprogress: { offer_send: false, offer_discussed: false, negotiation_started: false },
  won: { won: false },
  lost: { lost: false, reason: '' },
  ...props.lead.checklist,
})

watch(
  () => checklist_data.value.lost.lost,
  async (isLost) => {
    if (isLost) {
      try {
        await leadStore.get_lost_reasons()
      } catch (err) {
        console.error(err)
      }
    }
  },
  { immediate: true },
)

const contactMethods = [
  { value: 'email', label: 'Email' },
  { value: 'phone', label: 'Phone' },
  { value: 'linkedin', label: 'LinkedIn' },
  { value: 'other', label: 'Other' },
]

const submitChecklist = async () => {
  console.log(lost_reason_id.value)
  const payload = {
    checklist: checklist_data.value,
  }
  if (checklist_data.value.lost.lost) {
    payload.lost_reason_id = lost_reason_id.value
    payload.lost_reason_details = lost_reason_details.value
  }
  try {
    await leadStore.editLead(props.lead.id, payload)

    // După ce s-a salvat cu succes, emitem evenimentul către Kanban (ca să se închidă modalul)
    emit('checklist-saved')
    toast.success('The lead details were modified succesfully!', 1000, true)
  } catch (err) {
    console.error('Cannot save the checklist', err)
    toast.error('Something went wrong, please try again.')
  }
}
</script>

<style scoped></style>
