import { createStore } from "vuex";
import axios from "axios";

export default createStore({
  state: {
    tgData: "",
    auth: false,
    adminCode: "",
  },
  getters: {
    tgData(state) {
      return state.tgData;
    },
    auth(state) {
      return state.auth;
    },
  },
  mutations: {
    initializeStore(state) {
      const tgData = JSON.parse(localStorage.getItem("tgData"));
      const adminCode = localStorage.getItem("adminCode");
      if (tgData) {
        state.tgData = tgData;
        state.adminCode = adminCode;
        axios.defaults.headers.common["Authorization-Admin"] = adminCode;
        state.auth = true;
      } else {
        axios.defaults.headers.common["Authorization-Admin"] = null;
        state.auth = false;
        state.adminCode = null;
        localStorage.removeItem("adminCode");
      }
    },
  },
  actions: {},
  modules: {},
});
