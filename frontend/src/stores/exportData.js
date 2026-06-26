/*
import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '@/utils/api.js'

export const exportData = defineStore('exportData',() =>{
  const isExporting = ref(true)
  const error = ref(null)

  async function exportCSV(url,filename='export.csv',params={}){
    isExporting.value = true
    error.value = null

    try{
      const response = api.get(url,{
        params,
        responseType : 'blob'
      })

      // Take the file name from the header if it exist
      const disposition = response.headers['content-disposition']
      if(disposition){
        const match = disposition.match(/filename="(.+)"/)
        if (match) filename = match[1]
      }
      const blob = new Blob([response.data],{type:"text/csv"})

    }
  }



})
*/
