<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
    <div class="container">
        <router-link to="/"> ОП </router-link>
        <router-link to="/proff"> Подбор профессии </router-link>
      <RouterView/>
      </div>

</template>

