<template>
  <header class="header">
    <nav class="d-flex justify-content-around align-items-center">
      <img class="m-2" src="@/assets/telegram.png" width="58" height="58" alt="Logo">
      <div class="d-flex">
        <a class="nav-link" href="#">Price</a>
        <a class="nav-link ms-5" href="#">Support</a>
        <a class="nav-link ms-5" href="https://fastapi-backend-production.up.railway.app/docs">Documentation</a>
      </div>
      <router-link v-if="!auth" to="/login">
        <button class="login-btn m-2">Personal Cabinet</button>
      </router-link>
      <router-link v-else to="/cabinet">
        <button class="login-btn m-2">Personal Cabinet</button>
      </router-link>
    </nav>
  </header>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: 'Header',
  computed: mapGetters(["auth"]),
}
</script>

<style scoped>
.login-btn {
  color: #ffffff;
  font-size: 14px;
  line-height: 1.55;
  font-weight: 400;
  border-width: 1px;
  border-radius: 30px;
  background-color: #44a5fa;
  background-position: center center;
  border-color: transparent;
  border-style: solid;
  transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out;
  padding: 10px;
}

.nav-link {
  color: #333333;
  font-size: 18px;
  font-weight: 400;
  font-family: 'Roboto', Arial, sans-serif;
}


.nav-link:hover {
  color: #44a5fa;
}

.header {
  box-shadow: 0px 3px 13px rgb(51 51 51 / 10%);
}
</style>