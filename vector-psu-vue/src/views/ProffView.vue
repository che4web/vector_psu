<template>
    <h1> выбор професии</h1> 
    <div class="row">
        <div class="col-3">
            <h2> Что тебе нравиться?</h2>
            <div v-for="i in interestList"
                 @click="selecInterest(i)"  
                 :class="filter.interest?.indexOf(i.id)>=0? 'selected':''"
                >
                <SquareCheck v-if="filter.interest?.indexOf(i.id)>=0"/>
                <Square v-else />
                {{i.name}}
                </div>
    </div>

        <div class="col-3">
            <h2> Кем работать</h2>
            <div class="card mb-2" v-for="s in specialityList" @click="selectSpeciality(s)">
                <div class="card-body ">
                    <h5 class="card-title">{{s.name}} </h5>
                    <div class="speciality-card" :class="activeSpeciality==s.id?'show':'hide'"> {{s.description}} </div>
                    
                </div>

            </div>
     </div>
        <div class="col-6">
        <h2> Что будешь изучать</h2>
     <div v-for="c in courseList" 
         :class="['area-'+c.known_area,c.speciality_list.indexOf(activeSpeciality)>=0? 'selected':'']"> 
         {{c.name}} 
    </div>
    </div>

    </div>
</template>

<script setup>
import {ref,onMounted,watch } from "vue"
import {Interest,Course,Speciality} from "@/api.js"
import { SquareCheck,Square } from 'lucide-vue-next';
const interestList = ref([])
async function getInterest(){
    interestList.value = await  Interest.objects.filter()
}

function selecInterest(i){
    let index = filter.value.interest.indexOf(i.id)
    console.log(index)
    if (index>=0){
        //filter.value.interest = 
            filter.value.interest.splice(index,1)
    }else{
        filter.value.interest.push(i.id)
    }
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

.hide{
    height:0px
}
.show{
    height:300px

}
.speciality-card{
    transition: all 0.3s;
    overflow:hidden
}
</style>
