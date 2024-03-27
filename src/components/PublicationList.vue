<script setup>
import Publication from './Publication.vue';
import jpubs from '../data/journal.json';
import bpubs from '../data/book.json';
import ipubs from '../data/international.json';
import npubs from '../data/national.json';
</script>

<template>
<h2>Publications</h2> 

<h3>Journal Publications </h3>
  <ol>
    <div v-for="(pub, index) in jpubs" :key="index">
      <Publication v-bind="pub"/>
    </div> 
  </ol>

<h3>Book Chapters </h3>
  <ol>
    <div v-for="(pub, index) in bpubs" :key="index">
      <Publication v-bind="pub"/>
    </div> 
  </ol>

<h3>International Conferences </h3>
  <ol>
    <div v-for="(pub, index) in ipubs" :key="index">
      <Publication v-bind="pub"/>
    </div> 
  </ol>

<h3>National Conferences </h3>
  <ol>
    <div v-for="(pub, index) in npubs" :key="index">
      <Publication v-bind="pub"/>
    </div> 
  </ol>
</template>
