import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '@/utils/api.js'


export const useAssistantStore = defineStore('assistantAI', () =>{
const loading = ref(false)
const llm_response = ref('')
  const messages = ref([])





async function sendMessage(message){
    try{
      loading.value = true
      messages.value.push({'role':'user','content':message})
      const response = await api.post(`/api/v1/assistant/`,{message})
      console.log(response.data)
      messages.value.push({ role: 'assistant', content:  response.data.llm_response})
      console.log(messages.value)

    }catch (error){
      error.value = 'Error while sending the message to LLM!'
      console.error("sendMessage Error",error.value)
    }finally {
      loading.value = false
    }
  }



  return {
  sendMessage,
  loading,
  llm_response,
    messages
}
})
