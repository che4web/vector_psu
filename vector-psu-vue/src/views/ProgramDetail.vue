<script setup>
import {ref,onMounted} from "vue"
import {useRoute} from "vue-router"

import {Program,Speciality,Course} from "@/api.js"

import AreaCard from "@/components/AreaCard.vue"

const props = defineProps(['id'])
const router = useRoute()

const program = ref({})
async function getProgram(){
    program.value = await Program.objects.get(router.params.id)
    program.value.course_list = await Course.objects.filter({program:program.id})
}
async function selectProgram(program){
    program.is_active = !program.is_active
    program.course_list = await Course.objects.filter({program:program.id})
}
onMounted(()=>getProgram())

</script>
<template>

            <div class="program-card" v-if="program" >
                <div class="row">
                    <div class="col-6">
                        <h3> {{program.name}} </h3>
                    </div>
                    <div class="col-6">
                        <div class="text-end"><b>  Бакалавриат 4 года. </b></div>
                    </div>
                </div>
                <div  v-if="program.description"> {{program.description.slice(0,100)}} ... </div>
                <div > ЕГЭ </div>
                <div> <span v-for="ege in program.ege_list">  {{ege.ege_name}}: <b>{{ege.value}},  </b></span> </div>
                курсы
                    <div class="row">
                        <div class="col-12" v-for="course in program.course_list">

                            <div class="card ">
                            <div class="card-body ">
                            <div class="row">
                                <div class="col-4">
                                <img :src="course.img_preview" class="course-img">
                                </div>
                                <div class="col-8">
                                    <h3>{{course.name}}</h3>
                        </div>
                        </div>
                        </div>
                        </div>
                        </div>
                    </div>
            </div>
</template>
<style>
.course-img{
    height:200px;
}
</style>
