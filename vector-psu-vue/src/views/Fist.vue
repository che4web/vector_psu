<script setup>
import { ref,onMounted,watch } from 'vue'
import axios from 'axios'
import {Program,Speciality} from "@/api.js"
import ProgramCard from "@/components/ProgramCard.vue"

const filter = ref({search:''})
const programList = ref([])

async function getProgramList(){
    programList.value = await Program.objects.filter(filter.value)
}

const specialityList = ref([])
async function getSpecialityList(){
    specialityList.value = await Speciality.objects.filter()
}
onMounted(
    ()=>{
        getProgramList()
        getSpecialityList()
    })
watch(
    ()=>filter.value,
    ()=>getProgramList(),
    {deep:true}
)

function selectSpeciality(s){
    if (filter.value.speciality && filter.value.speciality.id==s.id){
        filter.value.speciality=undefined
    }else{
        filter.value.speciality=s
    }
}
</script>

<template>
    <div class="row">
        <div class="col-4">
            <h2> Фильтры </h2>
            <input v-model="filter.search" class="form-control"> 
            <div >
                <ul>
                    <li 
                                           v-for="s in specialityList" 
                                           :class="s.id==filter.speciality?.id? 'selected':''"
                                           @click="selectSpeciality(s)">{{s.name}} </li>
                </ul>
            </div >
            <button @click="getProgramList" class="btn btn-primary"> получить программы</button>
        </div>
        <div class="col-8">
            <h2> Образовательные программы </h2>
            <ProgramCard v-for="program in programList" :program="program"/>
    </div>
    </div>
</template>
<style>
.selected{
    font-weight:600;
}
.program-card{
    transition: all 1s;
    border: 1px solid #b1b1b1;
    border-radius: 15px;
    padding: 15px;
    margin-bottom:10px;
}
</style>
