<template>
  <div class="mt-10 bg-white shadow-md rounded-xl border border-gray-200 overflow-hidden">
    <form @submit.prevent="">
      <div class="px-6 py-4 border-b border-gray-200">
        <h1 class="text-xl font-bold mb-2">Add new task</h1>

        <label class="block text-medium font-semibold mb-1">Title</label>
        <input
          type="text"
          class="rounded-lg border-gray-200 w-full"
          placeholder="Task title..."
          v-model="taskTitle"
        />
        <label class="block text-medium font-semibold mb-1">Description</label>
        <textarea
          class="rounded-lg border-gray-200 w-full"
          v-model="taskDescription"
          placeholder="Description..."
        ></textarea>
        <label class="block text-medium font-semibold mb-1">Due date:</label>
        <input
          type="datetime-local"
          class="rounded-lg border-gray-200 w-full"
          v-model="taskDueDate"
        />
        <label class="block text-medium font-semibold mb-1">Assigned to:</label>
        <select
          id="members"
          class="block w-2/3 px-3 py-2.5 bg-transparent border-l-gray-50 border-r-gray-50 border-t-gray-50 text-heading text-sm rounded-base focus:ring-brand focus:border-brand shadow-xs placeholder:text-body"
          v-model="taskAssignedTo"
          required
        >
          <option selected>Choose member</option>
          <option v-for="member in teamStore.team.members" :key="member.id" :value="member.id">
            {{ member.first_name }} {{ member.last_name }}
          </option>
        </select>
        <label for="leads" class="block text-medium font-semibold mb-1">Lead: </label>
        <select
          id="leads"
          class="block w-2/3 px-3 py-2.5 bg-transparent border-l-gray-50 border-r-gray-50 border-t-gray-50 text-heading text-sm rounded-base focus:ring-brand focus:border-brand shadow-xs placeholder:text-body"
          v-model="leadAssignedTo"
          required
        >
          <option selected>Choose lead</option>
          <option v-for="lead in leadStore.allLeads" :key="lead.id" :value="lead.id">
            {{ lead.company }}
          </option>
        </select>
        <button class="bg-blue-900 p-2 rounded-lg text-white mt-2 w-full" @click="addTask">
          Add task
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { useTeamStore } from '@/stores/teamStore.js'
import { onMounted, ref } from 'vue'
import { useLeadStore } from '@/stores/leadStore.js'
import { useTaskStore } from '@/stores/taskStore.js'
import { useToast } from 'vue-toast-notification'

const teamStore = useTeamStore()
const leadStore = useLeadStore()
const taskStore = useTaskStore()
onMounted(async () => {
  await teamStore.fetchTeam()
  await leadStore.fetchAllLeads()
  console.log(leadStore.leads)
})
const taskTitle = ref('')
const taskDescription = ref('')
const taskDueDate = ref('')
const taskAssignedTo = ref('')
const leadAssignedTo = ref('')

const addTask = async () => {
  const formData = {
    title: taskTitle.value,
    description: taskDescription.value,
    assigned_to: taskAssignedTo.value,
    due_date: taskDueDate.value,
    lead_id: leadAssignedTo.value,
  }

  try {
    const result = await taskStore.createTask(formData)
    if (result) {
      useToast().success('Task created successfully!')
    }
  } catch (err) {
    console.error('Error while creating a new Task', err)
  }
}
</script>

<style scoped></style>
