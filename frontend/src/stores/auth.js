import {defineStore} from 'pinia'
import {ref,computed} from 'vue'

import api from '@/utils/api.js'


export const useAuthStore = defineStore('auth', ()=> {
  // -- STATE --
  const token = ref(localStorage.getItem('token') || '')
  const refreshToken = ref(localStorage.getItem('refresh_token') || '')

  const user = ref({
    id : localStorage.getItem('userid') || 0,
    username : localStorage.getItem('username') || ''
  })

  const team = ref({
    id: localStorage.getItem('teamid') || 0,
    name : localStorage.getItem('name') || ''
  })

  // -- GETTERS --
  const isAuthenticated = computed(() => !!token.value)

  // -- ACTIONS --
  // 1. Succes login

  // -- SETTING THE TOKEN IN THE LOCAL STORAGE --
  function setToken(access,refresh) {
    token.value = access
    localStorage.setItem('token', access)
    api.defaults.headers.common['Authorization'] = `Bearer ${access}`

    if(refresh){
      refreshToken.value = refresh
      localStorage.setItem('refresh_token',refresh)
    }
  }


// -- REMOVE THE TOKEN FROM THE LOCAL STORAGE AND THE USER--
  function removeToken(){
    token.value = ''
    refreshToken.value = ''
    user.value = {id:0 , username: ''}
    team.value = {id:0 , name: ''}

 // reset data
    localStorage.removeItem('token')
    localStorage.removeItem('refresh_token')
    localStorage.removeItem('userid')
    localStorage.removeItem('username')
    localStorage.removeItem('teamid')
    localStorage.removeItem('name')


    delete api.defaults.headers.common['Authorization']
  }

  function setUser(userData){
    user.value = userData
    localStorage.setItem('userid',userData.id)
    localStorage.setItem('username',userData.username)
  }
//Set team into localStorage
  function setTeam(teamData){
    team.value = teamData
    localStorage.setItem('teamid',teamData.id)
    localStorage.setItem('name',teamData.name)
  }

  //Initialize store
  //Aceasta functie se apeleaza doar cand dam refresh la pagina (App.vue)
  function initializeStore() {
    if (localStorage.getItem('token')) {
      const storedToken = localStorage.getItem('token')
      token.value = storedToken

      api.defaults.headers.common['Authorization'] = `Bearer ${storedToken}`
    } else {
      token.value = ''
      delete api.defaults.headers.common['Authorization']
    }
  }




  return {
    token,
    refreshToken,
    user,
    team,
    isAuthenticated,
    setToken,
    removeToken,
    setUser,
    setTeam,
    initializeStore
  }
})


