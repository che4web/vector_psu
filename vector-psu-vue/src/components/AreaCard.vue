<script setup>
import {ref} from "vue"
const props = defineProps(['course_list','typ'])
function filterCourse(course_list){
    if (course_list){
        return course_list.filter((item)=>item.known_area==props.typ)
    }
}
const typeName=ref({
    "IT":'Информатика',  
    "FZ":'Физика',  
    "MT":'Математика',  
})
</script>
<template lang="pug">
div(class="col-4" :class="'area-'+props.typ")
    .card-title  {{typeName[props.typ]}}
    .card-body
        div(v-for="course in filterCourse(props.course_list)")  {{course.name}} 
</template>
