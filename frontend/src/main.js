import { createApp } from 'vue'
import { createPinia } from 'pinia'
import './assets/main.css'
import api from '@/utils/api.js'

import App from './App.vue'
import router from './router'
import {createVuetify} from 'vuetify'
import 'vue-toast-notification/dist/theme-bootstrap.css'

import Vuedraggable from 'vuedraggable/src/vuedraggable.js'
import ToastPlugin from 'vue-toast-notification'



const app = createApp(App)
const vuetify = createVuetify({theme:{defaultTheme:'light'}})



app.use(createPinia())
app.use(router)
app.use(vuetify)

app.use(Vuedraggable)
app.use(ToastPlugin,{
  position:"bottom-left",
  timeout:3000,
  closeOnClick:true
})


// Check if we have the token on start
const token = localStorage.getItem('token')
if (token) {
  api.defaults.headers.common['Authorization'] = `Bearer ${token}`
}

app.mount('#app')



