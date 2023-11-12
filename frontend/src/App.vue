<template>
  <div class="app">
    <nav-bar/>
    <router-view v-slot="{ Component }">
      <transition name="fade" mode="out-in">
        <component :is="Component" />
      </transition>
  </router-view>
  </div>
</template>

<script>
export default {

}
</script>

<style>
body {
  background-color: rgb(30, 30, 30);
}
@font-face {
  font-family: "Inter";
  src: url("../fonts/static/Inter-ExtraLight.ttf");
}
* {
  margin: 0;
  box-sizing: border-box;
  font-family: Extra;
}
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>