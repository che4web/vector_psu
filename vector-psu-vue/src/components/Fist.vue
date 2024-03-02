<script setup>
import { ref,onMounted,watch } from 'vue'
import axios from 'axios'
import {Program,Speciality,Course} from "@/api.js"
const programName = ref('')
const programList = ref([])
const filter = ref({search:''})
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

async function selectProgram(program){
    program.is_active = !program.is_active
    program.course_list = await Course.objects.filter({program:program.id})
}
function filterCourse(course_list,typ){
    if (course_list){
    return course_list.filter((item)=>item.known_area==typ)
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
            <div class="program-card" v-for="program in programList" @click="selectProgram(program)">
                <div class="row">
                    <div class="col-6">
                        <h3>{{index}} {{program.name}} </h3>
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
                        <div class="col-4 area-MT">
                            <div class="card-title"> Математика</div>
                            
                            <div class="card-body">
                            <div v-for="course in filterCourse(program.course_list,'MT')">  {{course.name}}</div> 
                        </div>
                        </div>

                        <div class="col-4 area-FZ">
                            <div class="card-title"> Физика</div>
                            <div class="card-body">
                            <div v-for="course in filterCourse(program.course_list,'FZ')">  {{course.name}}</div>
                        </div>
                        </div>

                        <div class="col-4 area-IT">
                            <div class="card-title"> Информатика</div>
                            <div class="card-body">
                            <div v-for="course in filterCourse(program.course_list,'IT')">  {{course.name}}</div>
                            </div>
                        </div>
                    </div>
                </div >
            </div>
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
