import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '@/utils/api.js'
import { ca, fi } from 'vuetify/locale'

export const useLeadStore = defineStore('leads', () =>{
  const leads = ref([])
  const allLeads = ref([]) // used for dashboard
  const loading = ref(false)
  const error = ref('')
  const lead = ref({})
  const succes_message = ref('')
  const lost_reasons = ref([])
  /* LeadNotes
  * */

  const leadNotes = ref([])
  const leadNote= ref({})

  /* Pagination */
  const showNextButton = ref(false)
  const showPreviousButton = ref(false)
  const currentPage = ref(1)
  /* Filters */
  const companyName = ref('')
  const status = ref('')
  const priority = ref('')
  const totalCount = ref(null)



  async function fetchLeads(currentPage, companyName, status, priority, assigned_to) {
    loading.value = true
    error.value = null

    try {
      let url = `/api/v1/leads/`
      const params = new URLSearchParams()

      if (currentPage) {
        params.append('page', currentPage)
      }
      if (companyName) {
        params.append('company__icontains', companyName)
      }
      if (status) {
        params.append('status', status)
      }
      if (priority) {
        params.append('priority', priority)
      }
      if (assigned_to){
        params.append('assigned_to',assigned_to)
      }
      const queryString = params.toString()
      if (queryString) {
        url += `?${queryString}`
      }

      const response = await api.get(url)
      totalCount.value = response.data.count

      //if we have .results (pagination)
      // if not we just take
      leads.value = response.data.results || response.data

      showNextButton.value = !!response.data.next
      showPreviousButton.value = !!response.data.previous
    } catch (err) {
      error.value = 'Error. Cannot load the leads from the server'
      console.log(err)
    } finally {
      loading.value = false
    }
  }

  async function fetchAllLeads(){
    loading.value = true
    error.value = null

    try{
      const response = await api.get('/api/v1/leads/fetchAllLeads')
      allLeads.value = response.data
    }catch (err){
      error.value = 'Error while fetching all the leads!'
      console.error(err)
    }finally {
      loading.value = false
    }
  }

  async function addLead(leadData){
     try{
       const response = await api.post('/api/v1/leads/',leadData)
       leads.value.push(response.data)
       return response.data
     }catch (err){
       console.error('Error at adding the leads',err)
       error.value = err.response?.data
     }
  }

  async function getLead(id) {
    loading.value = true
    error.value = null

    try {
      const response = await api.get(`/api/v1/leads/${id}/`)
      lead.value = response.data
    } catch (err) {
      error.value = 'Error while trying to get the lead'
      console.error(err)
    } finally {
      loading.value = false
    }
  }

  async function editLead(id, leadData) {
    loading.value = true
    error.value = null

    try {
      const response = await api.patch(`/api/v1/leads/${id}/`, leadData)

      lead.value = response.data

      //Synch the global list without refreshing
      leads.value = leads.value.map((item) => {
        if (item.id === parseInt(id)) {
          return response.data
        }
        return item
      })

      return response.data
    } catch (err) {
      error.value = 'Error while editing the lead'
      throw err
    } finally {
      loading.value = false
    }
  }

  async function changeStatus(id,newStatus){
    loading.value = true
    error.value = null

    try{
      const response = await api.patch(`/api/v1/leads/${id}/`,newStatus)
      lead.value = response.data

    }catch (err){
      error.value = 'Error while changing the status'
      throw err
    }finally {
      loading.value = false
    }
  }

  async function deleteLead(id) {
    loading.value = true
    error.value = null

    try {
      await api.delete(`/api/v1/leads/${id}/`)
      lead.value = {}

      leads.value = leads.value.filter((item) => item.id !== parseInt(id))
    } catch (err) {
      error.value = 'Error while deleting the lead'
      throw err
    } finally {
      loading.value = false
    }
  }

  function showMessage(msg){
    succes_message.value = msg
    setTimeout(() => {
      succes_message.value = ''
    },3000)
  }



async function convertToClient(lead_id){
    loading.value = true
    error.value = null

  try{
    const response =  await api.post(`/api/v1/convert_lead_to_client/`, {lead_id: lead_id})
    console.log('Converted to client')
    return response.data
  }catch (err){
      error.value = 'Cannot convert the lead to client!'
    console.error(err)
  }finally {
      loading.value = false
  }
}

/* Lead Notes
* */

async function getLeadNote(noteID,lead_id){
  loading.value = true
  error.value = null

  try{
    const response = await api.get(`/api/v1/lead-notes/${noteID}/?lead_id=${lead_id}`)
    leadNote.value = response.data.results || response.data
  }catch (err){
    error.value = 'Error while getting the notes!'
    console.error(err)
  }finally {
    loading.value = false
  }
}

async function getLeadNotes(lead_id){
  loading.value = true
  error.value = null

  try{
    const response = await api.get(`/api/v1/lead-notes/?lead_id=${lead_id}`)
    leadNotes.value = response.data
  }catch (err){
    error.value = 'Error while getting the lead notes!'
    console.error(err,error.value)
  }finally {
    loading.value = false
  }
}

async function postLeadNote(noteData){
  try{
    const response = await api.post('/api/v1/lead-notes/', noteData)
    leadNotes.value.unshift(response.data) // Set the element at the beggning
  }catch (err){
    error.value = 'Error while adding the note '
    console.error(err, error.value)
  }
}

async function editLeadNote(lead_id,noteID,noteData){
  loading.value = true
  error.value = null

  try{
    const response = await api.patch(`/api/v1/lead-notes/${noteID}/?lead_id=${lead_id}`,noteData)
    leadNote.value = response.data

    leadNotes.value = leadNotes.value.map((item) => {
      if(item.id === parseInt(noteID)){
        return response.data
      }
      return item
    })
  }catch (err){
    error.value = 'Error while editing the note'
    throw err
  }finally {
    loading.value = false
  }
}

async function deleteLeadNote(noteID,lead_id){
  loading.value = true
  error.value = null

  if(!lead_id){
    console.error('No lead_id , the deletion cannot contiune without it!')
  }

  try{
    await api.delete(`/api/v1/lead-notes/${noteID}/?lead_id=${lead_id}`)
    leadNotes.value = leadNotes.value.filter((item) => item.id !== parseInt(noteID))
  }catch (err){
    error.value = 'Error while deleting the leadNote'
    console.error(err)
  }finally {
    loading.value = false
  }
}

async function get_lost_reasons(){
  loading.value = true
  error.value = null

  try{
    const resp = await api.get('api/v1/lost-reason')
    lost_reasons.value = resp.data
  }catch (err){
    console.error("Could not get the lost-reasons.",err)
  }finally {
    loading.value = false
  }
}




  return {
    leads,
    lead,
    loading,
    error,
    fetchLeads,
    addLead,
    getLead,
    editLead,
    deleteLead,
    showMessage,
    succes_message,
    convertToClient,
    showNextButton,
    showPreviousButton,
    currentPage,
    companyName,
    getLeadNote,
    getLeadNotes,
    postLeadNote,
    leadNotes,
    leadNote,
    deleteLeadNote,
    editLeadNote,
    status,
    changeStatus,
    totalCount,
    fetchAllLeads,
    allLeads,
    get_lost_reasons,
    lost_reasons
  }

})
