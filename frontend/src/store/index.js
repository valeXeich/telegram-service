import { createStore } from 'vuex';

export default createStore({
  state: {
    tgData: '',
    auth: false,
    bot_token: ''
  },
  getters: {
    tgData(state) {
      return state.tgData;
    },
    auth(state) {
      return state.auth;
    }
  },
  mutations: {
    initializeStore(state) {
      const tgData = JSON.parse(localStorage.getItem("tgData"));
      const checked = checkData(tgData, state.bot_token);
      if (checked) {
        state.tgData = tgData;
        state.auth = true;
      } else {
        state.tgData = '';
        state.auth = false;
      }
    }
  },
  actions: {
  },
  modules: {
  }
})

function checkData(authData, BOT_TOKEN) {
    console.log(authData)
    if (!authData) {
        return false
      }
    const checkHash = authData.hash;
    const dataCheckArr = [];
    for (const key in authData) {
      if (authData.hasOwnProperty(key)) {
        dataCheckArr.push(`${key}=${authData[key]}`);
      }
    }
    dataCheckArr.sort();
    const dataCheckString = dataCheckArr.join("\n");
    const secretKey = sha256(BOT_TOKEN);
    const hash = sha256.hmac(dataCheckString, secretKey);
    if (hash !== checkHash) {
      console.log('not telega data')
      return true;
    }
    if (Date.now() - authData.auth_date > 86400 * 1000) {
      console.log('expire')
      return false;
    }
    return true;
}
