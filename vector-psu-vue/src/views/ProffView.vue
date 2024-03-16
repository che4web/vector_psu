<template>
    <h1> выбор професии</h1> 
    <div class="row">
        <div class="col-3">
            <div v-for="i in interestList"
                 @click="selecInterest(i)"  
                 :class="filter.interest?.indexOf(i.id)>=0? 'selected':''"
                >
                {{i.name}}
                </div>
    </div>

        <div class="col-3">
            Профессии
            <div v-for="s in specialityList" @click="selectSpeciality(s)"> {{s.name}} </div>
     </div>
        <div class="col-6">
     Предменты
     <div v-for="c in courseList" 
         :class="c.speciality_list.indexOf(activeSpeciality)>=0? 'selected':''"> 
           {{c.name}} 
    </div>
    </div>

    </div>
</template>

<script setup>
import {ref,onMounted,watch } from "vue"
import {Interest,Course,Speciality} from "@/api.js"
const interestList = ref([])
async function getInterest(){
    interestList.value = await  Interest.objects.filter()
}

function selecInterest(i){
    filter.value.interest.push(i.id)
}
const filter = ref({interest:[]})

const courseList =ref([])
async function getCourse(){
    courseList.value  = await Course.objects.filter(filter.value)
}
const activeSpeciality = ref(0)
function selectSpeciality(s){
    activeSpeciality.value=s.id
}
const specialityList =ref([])
async function getSpeciality(){
    specialityList.value  = await Speciality.objects.filter(filter.value)
}


onMounted(()=>getInterest())
watch(
    ()=>filter.value,
    ()=>{
        getCourse()
        getSpeciality()
    },{deep:true})



</script>

<style>
</style>
