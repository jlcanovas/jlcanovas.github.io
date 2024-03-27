<script setup>
const props = defineProps({
  title: String,
  authors: String,
  reference: String,
  year: String,
  url: String
})
</script>

<template>
<li>
    <strong>{{ title }}</strong>.
    {{ authors }}.
    {{ reference }},
    {{ year }}.

    <a :href="url">Publisher site</a>.
</li>
</template>