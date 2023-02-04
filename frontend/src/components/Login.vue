<template>
    <div class="center">
        <h4>Authorization</h4>
        <div v-if="error" class="alert alert-danger" role="alert">
            {{ error }}
        </div>
        <div v-if="!accessCode">
            <p>Put your access code to continue</p>
            <div class="d-flex">
                <input v-model="code" type="text" class="form-control" placeholder="Access code">
                <button @click="sendCode" class="btn btn-primary ms-2">Check</button>
            </div>
        </div>
        <div v-else class="mt-4">
            <telegram-login-temp mode="callback" telegram-login="DistributionTelegramAuthBot" @callback="saveData" />
        </div>
    </div>
</template>

<script>
import { telegramLoginTemp } from 'vue3-telegram-login'
import axios from 'axios'

export default {
    name: 'Login',
    components: {
        telegramLoginTemp,
    },
    data() {
        return {
            accessCode: false,
            code: '',
            error: ''
        }
    },
    methods: {
        async sendCode() {
            try {
                await axios.get(`check-admin-code?api_key=${this.code}`);
                this.error = '';
                this.accessCode = true;
            } catch (e) {
                this.error = 'Invalid code';
                this.accessCode = false;
            }
        },
        saveData(user) {
            localStorage.setItem('tgData', JSON.stringify(user));
            localStorage.setItem('adminCode', this.code);
            axios.defaults.headers.common['Authorization-Admin'] = this.code;
            this.$store.commit('initializeStore');
            this.$router.push('/cabinet');
        }
    }
}
</script>

<style scoped>
.center {
    margin: auto;
    margin-top: 300px;
    text-align: center;
    width: 20%;
    box-shadow: 0 1px 5px #0003, 0 2px 2px #00000024, 0 3px 1px -2px #0000001f;
    border-radius: 4px;
    padding: 24px;
}
</style>