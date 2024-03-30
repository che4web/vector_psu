<script setup>
import {ref} from "vue"

import {Program,Speciality,Course} from "@/api.js"

import AreaCard from "@/components/AreaCard.vue"
const props = defineProps(['program'])

const program = ref(props.program)
async function selectProgram(program){
    program.is_active = !program.is_active
    program.course_list = await Course.objects.filter({program:program.id})
}

</script>
<template>

            <div class="program-card" @click="selectProgram(program)"  >
                <div class="row">
                    <div class="col-6">
                        <h3> 
                            <router-link 
                                :to="{name:'program-detail',params:{id:program.id}}"
                                >
                                {{program.name}} 
                            </router-link> 
                        </h3>
                    </div>
                    <div class="col-6">
                        <div class="text-end"><b>  Бакалавриат 4 года. </b></div>
                    </div>
                </div>
                <div > {{program.description.slice(0,100)}} ... </div>
                <div > ЕГЭ </div>
                <div> <span v-for="ege in program.ege_list">  {{ege.ege_name}}: <b>{{ege.value}},  </b></span> </div>
                курсы
                <div v-if="program.is_active"> 
                    <div class="row">
                        <AreaCard :course_list="program.course_list" typ="MT"/>
                        <AreaCard :course_list="program.course_list" typ="FZ"/>
                        <AreaCard :course_list="program.course_list" typ="IT"/>
                    </div>
                </div >
            </div>
</template>
