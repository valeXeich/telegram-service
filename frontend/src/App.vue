<template>
  <router-view/>
</template>

<script>

export default {
  beforeCreate() {
    this.$store.commit('initializeStore');
  }
}
</script>

<style>

.blue-color {
  color: rgb(68, 165, 250);
}

</style>
