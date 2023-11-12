import { createApp } from 'vue'
import App from './App.vue'
import components from '@/components/UI'


import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

//import { faEnvelope } from '@fortawesome/free-regular-svg-icons'
import { faTelegram } from '@fortawesome/free-brands-svg-icons'
import { faVk } from '@fortawesome/free-brands-svg-icons'
import { faMapLocationDot } from '@fortawesome/free-solid-svg-icons'
import router from './router/router'

//library.add(faEnvelope)
library.add(faTelegram)
library.add(faVk)
library.add(faMapLocationDot)


const app = createApp(App, )

components.forEach(component => {
    app.component(component.name, component)
})
app.component('font-awesome-icon', FontAwesomeIcon)
app.config.errorHandler = (err, instance, info) => {
    console.error(err)
  }
app
    .use(router)
    .mount('#app')
