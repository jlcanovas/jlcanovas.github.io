<script setup>
import About from './components/About.vue'
import PublicationList from './components/PublicationList.vue';
import Projects from './components/Projects.vue';
</script>

<template>
  <h1>  
    Javier L. Cánovas Izquierdo
    <img id="photo-me" alt="my photo" src="./assets/photo.jpg" />
  </h1>

  <div id="box">
    <About />
    <PublicationList />
    <Projects />
  </div> 

</template> 

<style scoped>
</style>
