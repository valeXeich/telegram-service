<template>
        <CabinetHeader @tgData="tgData"/>
        <div class="d-flex">
        <Sidebar/>
        <CabinetContent/>
</div>
</template>

<script>
import { mapGetters } from "vuex";
import CabinetHeader from "@/components/CabinetHeader.vue";
import Sidebar from "@/components/Sidebar.vue";
import CabinetContent from "@/components/CabinetContent.vue";

    export default {
        name: 'Cabinet',
        computed: mapGetters(["tgData"]),
        components: {
            CabinetHeader,
            Sidebar,
            CabinetContent
        }
    }
</script>

<style scoped>

.d-flex {
  display: flex;

}
</style>