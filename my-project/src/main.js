// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

// 引入axios
// import Axios from 'axios'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

// 将luffyHeader 注册成全局组件
import LuffyHeader from "@/components/Common/LuffyHeader"

// 引入项目中全局 css
import '../static/global/index.css'
import * as api from './restful/api'

Vue.component(LuffyHeader.name, LuffyHeader)

Vue.config.productionTip = false

// 将axios挂载到 Vue原型
Vue.prototype.$http = api
Vue.use(ElementUI);

// Axios.defaults.baseURL = 'https://www.luffycity.com/api/v1/'

/* eslint-disable no-new */
new Vue({
	el: '#app',
	router,
	components: {App},
	template: '<App/>'
})
