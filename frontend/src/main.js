import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'

axios.defaults.baseURL = 'http://127.0.0.1:8000/'

createApp(App).use(store).use(router).mount('#app')
