import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '@/utils/api.js'
import { useAuthStore } from '@/stores/auth.js'


export const useTeamStore = defineStore('team',() => {
  const team = ref([])
  const loading = ref(false)
  const error = ref('')

  const authStore = useAuthStore()


  async function addTeam(teamData){
    loading.value = true
    error.value = ''

    try{
      const response = await api.post('/api/v1/teams/',teamData)
      team.value.push(response.data)

      //actualizam AuthStore cu noua echipa
      authStore.setTeam(response.data)
      console.log('Echipa creata cu succes!',response.data)

    }catch (err){
      console.error('Error at adding a team', err)
      if(err.response && err.response.data){
        error.value = JSON.stringify(err.response.data)
      }
      else {
        error.value = "Something went wrong. Please try again."
      }
      throw err
    }finally {
      loading.value =false
    }
  }

  async function fetchTeam(){
    loading.value = true
    error.value = null

    try{
      const response = await api.get('/api/v1/teams/get_my_team/')
      team.value = response.data
    }catch (err){
      error.value = 'Error. Cannot load the teams from the server'
      console.error(err)
    }finally {
      loading.value = false
    }
  }

  async function joinWithTeamCode(teamCode){
    loading.value = true
    error.value = null

    try{
      const response = await api.post('/api/v1/teams/join_team_by_code/',teamCode)
      return response
    }catch (err){
      error.value = err
      console.error(err,error.value)

    }
  }




  return {
    team,
    loading,
    error,
    addTeam,
    fetchTeam,
    joinWithTeamCode
  }
})
