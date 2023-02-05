<template>
    <CabinetHeader :data="tgData" />
    <div class="d-flex">
        <Sidebar />
        <CabinetSettinsContent/>
    </div>
</template>

<script>
import { mapGetters } from "vuex";
import CabinetHeader from "@/components/CabinetHeader.vue";
import Sidebar from "@/components/Sidebar.vue";
import CabinetSettinsContent from "./CabinetSettinsContent.vue";

export default {
    name: 'CabinetSettings',
    computed: mapGetters(["tgData"]),
    components: {
        CabinetHeader,
        Sidebar,
        CabinetSettinsContent
    }
}
</script>

<style scoped>
.d-flex {
    display: flex;

}
</style>