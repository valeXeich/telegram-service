<template>
    <main role="main" class="col-12 p-4 main-section">
        <div class="container">
            <div class="row">
                <div class="col-6">
                    <table class="table table-bordered">
                        <thead>
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">APIKEY</th>
                            </tr>
                        </thead>
                        <tbody v-for="(key, index) in apiKeys" :key="index">
                            <tr>
                                <th scope="row">{{ index+ 1 }}</th>
                                <td>{{ key.api_key }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="col-6">
                    <button class="btn btn-success" @click="createApiKey">
                        <i class="bi bi-plus"></i>
                        Create new APIKey
                    </button>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import axios from 'axios';

export default {
    name: 'CabinetContent',
    props: ['apiKeys'],
    methods: {
        async createApiKey() {
            const response = await axios.post('create-api-key');
            this.apiKeys.push(response.data)
        },
    }
}
</script>

<style  scoped>
.main-section {
    width: 80%;
}
</style>