<template>
  <Header/>
  <router-view/>
  
</template>

<script>
import Header from "@/components/Header.vue"

export default {
  components: {
    Header,
  }
}
</script>

<style>

.blue-color {
  color: rgb(68, 165, 250);
}

</style>
