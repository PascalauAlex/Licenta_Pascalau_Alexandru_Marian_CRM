import {defineStore} from 'pinia'
import {ref} from 'vue'
import api from '@/utils/api.js'

export const useclientStore = defineStore('clients', ()=>{
  const clients = ref([])
  const loading = ref(false)
  const client = ref({})
  const error = ref('')
  const notes = ref([])
  const note = ref({})
  const name = ref('')


  async function fetchClients(name,status){
    loading.value = true
    error.value = null

    try{
      let url = `/api/v1/clients/`
      if(name){
        url += `?name__icontains=${encodeURIComponent(name)}`
      }
      if(status){
        url += `?status=${encodeURIComponent(status)}`
      }

      const response = await api.get(url)
      clients.value = response.data

    }catch (err){
      error.value = 'Error. Cannot load the clients from the server'
      console.log(err)
    }finally {
      loading.value = false
    }
  }

  async function addClient(clientData) {
    try {
      const response = await api.post('/api/v1/clients/', clientData , {
        headers : {
          'Content-Type' : 'multipart/form-data'
        }
      })
      clients.value.push(response.data)
    } catch (err) {
      console.error('Error at adding the client', err)
      if(err.response){
        console.error('Detalii eroare Django',err.response.data)
      }
    }
  }

  async function getClient(id){
    loading.value = true
    error.value = null

    try{
      const response = await api.get(`/api/v1/clients/${id}/`)
      client.value = response.data
    }catch (err){
      error.value = 'Error while trying to get the client'
      console.error(err)
    }finally {
      loading.value = false
    }
  }


  async function getNote(noteID,client_id){
    loading.value = true
    error.value = null

    try{
      const response = await api.get(`/api/v1/notes/${noteID}/?client_id=${client_id}`)
      note.value = response.data

    }catch (err){
      error.value = 'Error while getting the note!'
      console.log(err)
    }finally {
      loading.value = false
    }
  }

  async function getClientNotes(client_id){
    loading.value = true
    error.value = null

    try{
      const response = await api.get(`/api/v1/notes/?client_id=${client_id}`)
      notes.value = response.data
    }catch (err){
      error.value = 'Error while getting the client notes'
      console.error(err )
    }finally {
      loading.value = false
    }
  }

  async function postNote(noteData){
    try{
      const response = await api.post('/api/v1/notes/',noteData)
      notes.value.push(response.data)
    }catch (err){
      console.error('Error while adding the note', err)
    }
  }



  async function editClient(id, clientData) {
    loading.value = true
    error.value = null

    try {
      const response = await api.patch(`/api/v1/clients/${id}/`, clientData)

      client.value = response.data

      if (Array.isArray(clients.value)) {
        clients.value = clients.value.map((item) => {
          if (item.id === parseInt(id)) {
            return response.data
          }
          return item
        })
      }

      return response.data
    } catch (err) {
      error.value = 'Eroare la editarea clientului'
      console.error(err)
      throw err
    } finally {
      loading.value = false
    }
  }

  async function editNote(client_id,noteID,noteData){
    loading.value = true
    error.value = null
    try{
      const response = await api.patch(`/api/v1/clients/${noteID}/?client_id=${client_id}`,noteData)
      note.value = response.data

      note.value = note.value.map((item) => {
        if(item.id === parseInt(noteID)){
          return response.data
        }
        return item
      })

    }catch (err){
      console.error(err)
    }finally {
      loading.value = false
    }

  }

  async function deleteClient(id) {
    loading.value = true
    error.value = null

    try {
      await api.delete(`/api/v1/clients/${id}/`)
      client.value = {}

      clients.value = clients.value.filter((item) => item.id !== parseInt(id))
    } catch (err) {
      error.value = 'Error while deleting the clients'
      throw err
    } finally {
      loading.value = false
    }
  }

  async function deleteNote(noteID,client_id){
    loading.value = true
    error.value = null
    if(!client_id){
      console.error('No client_id , the deletion cannot work without it!')
    }

    try{
      await api.delete(`/api/v1/notes/${noteID}/?client_id=${client_id}`)
      notes.value = notes.value.filter((item) => item.id !== parseInt(noteID))

    }catch (err){
      error.value = 'Error while deleting the note'
      throw err
    }finally {
      loading.value = false
    }
  }


  return {
    clients,
    client,
    loading,
    error,
    fetchClients,
    addClient,
    getClient,
    editClient,
    deleteClient,
    getClientNotes,
    notes,
    postNote,
    deleteNote,
    editNote,
    getNote,
    note,
    name
  }
})
