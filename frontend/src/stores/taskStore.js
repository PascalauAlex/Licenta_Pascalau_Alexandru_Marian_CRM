import {defineStore} from 'pinia'
import {ref} from 'vue'
import api from '@/utils/api.js'





export const useTaskStore = defineStore('tasks', ()=> {
  const tasks = ref([])
  const loading = ref(false)
  const error = ref('')
  const task = ref({})
  const leadTasks = ref([])

  async function getTasks(status,assigned_to){
    loading.value = true
    error.value = null

    try{
      let URL = '/api/v1/tasks'
      const params = new URLSearchParams()
      if(status){
        params.append('status',status)
      }
      if(assigned_to){
        params.append('assigned_to',assigned_to)
      }

      const queryString = params.toString()
      if (queryString){
        URL += `?${queryString}`
      }


      const response = await api.get(URL)
      tasks.value = response.data

    }catch (err){
      error.value ='Error while getting the tasks!'
      console.error(err)
    }finally {
      loading.value = false
    }
  }

  async function getLeadTask(leadID){
    loading.value = true
    error.value = null

    try{
      const response = await api.get(`/api/v1/lead-tasks/${leadID}/`)
      leadTasks.value = response.data
    }catch (err){
      error.value = 'Error while getting the tasks for the lead'
      console.error(err, error.value)
    }
  }


  async function deleteTask(taskID){
    loading.value = true
    error.value = null

    try{
      await api.delete(`/api/v1/tasks/${taskID}/`)
      tasks.value = tasks.value.filter((item) => item.id !== parseInt(taskID))
      leadTasks.value = leadTasks.value.filter((item) => item.id !== parseInt(taskID))
    }catch (err){
      error.value = 'Error while deleting the task'
      console.error(err)
    }finally {
      loading.value = false
    }
  }


  async function changeStatus(taskID,newStatus){
    loading.value = true
    error.value = null

    try{
      const response = await api.patch(`/api/v1/tasks/${taskID}/`, newStatus)
      task.value = response.data
      // găsește și actualizează task-ul în array
      const index = tasks.value.findIndex((t) => t.id === taskID)
      if (index !== -1) {
        tasks.value[index] = response.data
      }
      const leadIndex = leadTasks.value.findIndex((t) => t.id === taskID)
      if (leadIndex !== -1) {
        leadTasks.value[leadIndex] = response.data
      }

      return true
    }catch (err){
      error.value = 'Error while starting the task!'
      console.error(err)
    }finally {
      loading.value = false
    }
  }

  async function finishTask(taskID,newStatus){
    loading.value = true
    error.value = null

    try{
      const response = await api.patch(`/api/v1/tasks/${taskID}/`, newStatus)
      task.value = response.data
      // găsește și actualizează task-ul în array
      const index = tasks.value.findIndex((t) => t.id === taskID)
      if (index !== -1) {
        tasks.value[index] = response.data
      }

      const leadIndex = leadTasks.value.findIndex((t) => t.id === taskID)
      if (leadIndex !== -1) {
        leadTasks.value[leadIndex] = response.data
      }

      return true
    }catch (err){
      error.value = 'Error while closing the task'
      console.error(err)
    }finally {
      loading.value = false
    }
  }

  async function createTask(taskData) {
    loading.value = true
    error.value = null

    try {
      const response = await api.post('/api/v1/tasks/', taskData)
      tasks.value.push(response.data)
      leadTasks.value.push(response.data)
      return true
    } catch (err) {
      error.value = 'Error while creating the task!'
      console.error(error.value, err)
      return false
    } finally {
      loading.value = false
    }
  }





  return{
    tasks,
    loading,
    error,
    getTasks,
    deleteTask,
    changeStatus,
    finishTask,
    getLeadTask,
    leadTasks,
    createTask
  }
})
