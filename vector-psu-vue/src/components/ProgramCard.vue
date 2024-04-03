<script setup>
import {ref} from "vue"

import {Program,Speciality,Course} from "@/api.js"

import AreaCard from "@/components/AreaCard.vue"
const props = defineProps(['program'])

const program = ref(props.program)
async function selectProgram(program){
    program.is_active = !program.is_active
    program.course_list = await Course.objects.filter({program:program.id,prof_typ:"P"})
}

</script>
<template lang="pug">
.program-card( @click="selectProgram(program)")
    .row
        .col-6
            h3 
                router-link(
                    :to="{name:'program-detail',params:{id:program.id}}"
                    ) {{program.name}} 
        .col-6
            .text-end
                b  Бакалавриат 4 года. 
    div {{program.description.slice(0,100)}} ...
    div ЕГЭ
    div
        span(v-for="ege in program.ege_list")  {{ege.ege_name}}: 
            b {{ege.value}}
    div курсы
    div(v-if="program.is_active")
        .row
            AreaCard(:course_list="program.course_list" typ="MT")
            AreaCard(:course_list="program.course_list" typ="FZ")
            AreaCard(:course_list="program.course_list" typ="IT")
</template>
