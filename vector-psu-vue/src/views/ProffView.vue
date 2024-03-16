<template>
    <h1> выбор професии</h1> 
    <div class="row">
        <div class="col-2">
            <div v-for="i in interestList"
                 @click="selecInterest(i)"  
                 :class="i.id==filter.interest?.id? 'selected':''"
                >
                {{i.name}}
                </div>
    </div>

        <div class="col-8">
     Предменты
     {{courseList}}
    </div>

        <div class="col-2">
            Профессии
    </div>

    </div>
</template>

<script setup>
import {ref,onMounted,watch } from "vue"
import {Interest,Course} from "@/api.js"
const interestList = ref([])
async function getInterest(){
    interestList.value = await  Interest.objects.filter()
}

function selecInterest(i){
    filter.value.interest = i
}
const filter = ref({interest:undefined})

const courseList =ref([])
async function getCourse(){
    courseList.value  = await Course.objects.filter(filter.value)
}
onMounted(()=>getInterest())
watch(()=>filter.value,()=>getCourse(),{deep:true})



</script>

<style>
</style>
