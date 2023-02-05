<template>
    <main role="main" class="col-12 p-4 main-section">
        <div class="container">
            <div class="row">
                <div class="col-6 text-center block">
                    <h4>Account Settings</h4>
                    <input v-model="appID" type="text" placeholder="App ID" class="form-control">
                    <input v-model="appHash" type="text" placeholder="App Hash" class="form-control mt-4">
                    <button @click="saveBotData" class="btn btn-primary mt-4">Save</button>
                </div>
                <div class="col-3">
                    <div v-if="message" class="alert alert-success" role="alert">
                        {{ message }}
                    </div>
                    <div v-if="error" class="alert alert-danger" role="alert">
                        {{ error }}
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import axios from 'axios';

export default {
    name: 'CabinetSettingsContent',
    data() {
        return {
            appID: null,
            appHash: null,
            message: '',
            error: ''
        }
    },
    methods: {
        async getBotData() {
            const response = await axios.get('/get-bot-data');
            this.appID = response.data.app_id;
            this.appHash = response.data.app_hash;
        },
        async saveBotData() {
            const url = `/change-bot-data?app_id=${this.appID}&app_hash=${this.appHash}`;
            if (this.appHash && this.appID)
                try {
                    await axios.put(url)
                    this.message = 'Saved';
                    this.error = '';
                } catch(e) {
                    this.error = 'Something went wront';
                    this.message = '';
                }
            else {
                this.error = 'Something went wront';
                this.message = '';
            }
        }
    },
    mounted() {
        this.getBotData();
    }
}
</script>

<style  scoped>
.main-section {
    width: 80%;
}

.block {
    box-shadow: 0 1px 5px #0003, 0 2px 2px #00000024, 0 3px 1px -2px #0000001f;
    border-radius: 4px;
    padding: 30px;
}
</style>