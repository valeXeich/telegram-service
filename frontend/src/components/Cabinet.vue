<template>
    <CabinetHeader :data="tgData" />
    <div class="d-flex">
        <Sidebar />
        <CabinetContent :apiKeys="apiKeys" />
    </div>
</template>

<script>
import { mapGetters } from "vuex";
import CabinetHeader from "@/components/CabinetHeader.vue";
import Sidebar from "@/components/Sidebar.vue";
import CabinetContent from "@/components/CabinetContent.vue";
import axios from "axios";

export default {
    name: 'Cabinet',
    computed: mapGetters(["tgData"]),
    components: {
        CabinetHeader,
        Sidebar,
        CabinetContent
    },
    data() {
        return {
            apiKeys: []
        }
    },
    methods: {
        async getApiKeys() {
            const response = await axios.get('get-api-keys');
            console.log(response.data)
            this.apiKeys = response.data
        }
    },
    mounted() {
        this.getApiKeys()
    }
}
</script>

<style scoped>
.d-flex {
    display: flex;

}
</style>