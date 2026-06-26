<template>
  <v-app>
    <v-container>
      <v-confirm-edit ok-text="Save" v-model="model">
        <template v-slot:default="{ model: proxyModel, actions }">
          <v-card class="mx-auto" max-width="320" title="Add event">
            <template v-slot:text>
              <v-text-field v-model="proxyModel.value" messages="Modify my value"></v-text-field>
            </template>

            <template v-slot:actions>
              <v-spacer></v-spacer>

              <component :is="actions"></component>
            </template>
          </v-card>
        </template>
      </v-confirm-edit>
    </v-container>
  </v-app>
</template>
<script setup>
import { shallowRef } from 'vue'

const model = shallowRef('')
</script>
