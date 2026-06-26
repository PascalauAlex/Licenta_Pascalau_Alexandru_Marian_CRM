import {defineStore} from 'pinia'
import { ref } from 'vue'
import api from '@/utils/api.js'



export const useEmailStore = defineStore('email', () => {
  const isLoading = ref(false)
  const error = ref(null)
  const isSucces = ref(false)
  const leadEmails = ref([])
  const clientEmails = ref([])

  async function sendAndSaveMail(emailData) {
    isLoading.value = true
    error.value = null

    const formData = new FormData()

    if(emailData.lead) formData.append('lead',emailData.lead)
    if(emailData.client) formData.append('client',emailData.client)

    formData.append('to', emailData.to)
    formData.append('subject', emailData.subject)
    formData.append('message', emailData.message)

    if (emailData.files) {
      Array.from(emailData.files).forEach((file) => {
        formData.append('attachments', file)
      })
    }

    try {
       await api.post('api/v1/send-mail/', formData, {
         headers: {'Content-Type': undefined}
       })
      isSucces.value = true
      return true
    } catch (err) {
      error.value = err.response?.data || 'Eroare la trimitere'
      return false
    } finally {
      isLoading.value = false
    }
  }

  /* FETCHING THE EMAILS SENT TO A LEAD
   * RETRIVES DATA FROM THE BACKEND , GETTING IN RETURN EMAIL HISTORY
   * OF THE LEAD , IDENTIFIED BY LEAD ID */
  async function fetchLeadEmails(leadID) {
    isLoading.value = true
    error.value = null

    try {
      const response = await api.get(`api/v1/email-lead/${leadID}/`)
      leadEmails.value = response.data
    } catch (err) {
      error.value = 'FETCHING EMAIL HISTORY FAILED'
      console.error(err)
    } finally {
      isLoading.value = false
    }
  }

  /* FETCHING THE EMAILS SENT TO A CLIENT
   * RETRIVES DATA FROM THE BACKEND , GETTING IN RETURN EMAIL HISTORY
   * OF THE CLIENT , IDENTIFIED BY LEAD ID */

  async function fetchClientEmails(clientID){
    isLoading.value = true
    error.value = null

    try{
      const response = await api.get(`api/v1/email-client/${clientID}/`)
      clientEmails.value = response.data
    }catch (err){
      error.value = 'Error while getting emails of the client!'
      console.error(err)
    }finally {
      isLoading.value = false
    }
  }

  return {
    isSucces,
    isLoading,
    sendAndSaveMail,
    fetchLeadEmails,
    leadEmails,
    clientEmails,
    fetchClientEmails,
    error
  }
})
