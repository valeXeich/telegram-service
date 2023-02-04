<template>
  <div class="col-12">
    <nav class="navbar bg-body-tertiary">
  <div class="container-fluid">
    <h4 class="navbar-brand text-white ms-3">TelegramUserBot</h4>
    <div class="dropdown me-5 dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
        <img class="img-fluid rounded-circle" width="38" height="38" src="https://t.me/i/userpic/320/MtEy23UMdIKA2ZTuxkxHSw9ZqyQXCS2kw4smEyU1HgI.jpg" alt="">
        <span class="text-white ms-2 username">Valex</span>
        <button class="custom-btn dropdown-toggle ms-1"></button>
        <ul class="dropdown-menu">
            <li><a class="dropdown-item text-red" href="#">Logout</a></li>
        </ul>
    </div>
  </div>
    </nav>

  </div>
</template>

<script>
    export default {
        props: {
            tgData: {
                type: Object,
                require: true,
            },
        },
    }
</script>

<style scoped>

.custom-btn {
    background-color: transparent;
    border: none;
    color: white;
}

.navbar-brand {
    font-weight: 400;
    font-size: 21px;
}

.navbar {
    background-color: #1976d2;
    
}

.username {
    font-size: 14px;
    font-weight: 500;
}

.text-red {
    color: #c10015
}

.dropdown:hover {
    cursor: pointer;
    background-color: #4189d0;
}
</style>