<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    {{ this.method() }}
  </div>
</template>

<script>
import axios from 'axios'
// @ is an alias to /src
export default {
  name: 'HomeView',
  methods: {
    method(){
      axios.get('http://192.168.89.102:8000').then(
        response => console.log(response)
      )
    }
  }
}
</script>
