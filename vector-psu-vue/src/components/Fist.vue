<script setup>
import { ref,onMounted } from 'vue'
import axios from 'axios'
const programName = ref('')
const programList = ref([])

async function getProgramList(){
    programList.value = (await axios.get('/api/program/?program_name='+programName.value)).data
}
onMounted(()=>getProgramList())

</script>

<template>
    <input v-model="programName"> 
    <h1> my first component</h1>
    <button @click="adCounter"> +</button>
    <button @click="getProgramList"> получить программы</button>
    <ul> <li v-for="program in programList">{{program.name}}</li></ul>
</template>
