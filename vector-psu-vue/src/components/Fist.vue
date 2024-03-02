<script setup>
import { ref,onMounted,watch } from 'vue'
import axios from 'axios'
import {Program} from "@/api.js"
const programName = ref('')
const programList = ref([])

async function getProgramList(){
    programList.value = await Program.objects.filter({search:programName.value})
}
//onMounted(()=>getProgramList())
watch(
    ()=>programName.value,
    ()=>getProgramList()
)
</script>

<template>
    <input v-model="programName" class="form-control"> 
    <button @click="getProgramList" class="btn btn-primary"> получить программы</button>
    <ul> <li v-for="program in programList">{{program.name}}</li></ul>
</template>
