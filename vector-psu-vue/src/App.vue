<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template lang="pug">
div
    nav(class="navbar navbar-expand-lg navbar-light bg-light")
        .container
            a(class="navbar-brand" href="#") Navbar
            button(class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation")
                span(class="navbar-toggler-icon")
            div(class="collapse navbar-collapse" id="navbarSupportedContent")
                ul(class="navbar-nav mr-auto")
                    li(class="nav-item active")
                            router-link(to="/" class="nav-link ") ОП 
                    li(class="nav-item")
                             router-link(to="/proff" class="nav-link ") Подбор профессии 
    div(class="container")
        RouterView
</template>

