<script setup>
import {ref} from "vue"
const props = defineProps(['course_list','typ'])
function filterCourse(course_list,typ){
    if (course_list){
    return course_list.filter((item)=>item.known_area==typ)
    }
}
const typeName=ref({
    "IT":'Информатика',  
    "FZ":'Физика',  
    "MT":'Математика',  
})
</script>
<template>
        <div class="col-4" :class="'area-'+props.typ" >
            <div class="card-title"> {{typeName[props.typ]}}</div>
            <div class="card-body">
                <div v-for="course in filterCourse(props.course_list,'IT')">  {{course.name}} {{course.study_load}} часов </div>
            </div>
        </div>
</template>
