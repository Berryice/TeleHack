<template>
    <ul class="navigation">
        <router-link to="/" class="navigation-li map"><li><font-awesome-icon icon="fa-solid fa-map-location-dot"/></li></router-link>
        <router-link to="/for-vk" class="navigation-li vk"><li><font-awesome-icon icon="fa-brands fa-vk"/></li></router-link>
        <router-link to="/for-tg" class="navigation-li tg"><li><font-awesome-icon icon="fa-brands fa-telegram"/></li></router-link>
    </ul>
</template>

<script>
import router from '@/router/router';

export default {
    name: 'nav-bar'
}
</script>

<style scoped>
.navigation {
    justify-content: space-around;
    display: flex;
    list-style: none;
    margin-bottom: 2%;
}
.navigation:first-child {
    padding: 0;
}
.map {
    padding: 20px 20px;
}
.tg {
    padding: 20px 25px;
}
.vk {
    padding: 20px 27px;
}
.navigation-li {
    color: #0d6efd;
    background: none;
    border: solid 3px #0d6efd;
    border-radius: 50%;
    font-size: 50px;
    width: 100px;
    height: 100px;
    margin: 1% 0;
    transition-property: color, background-color, border-color;
    transition-duration: 0.5s, 0.5s, 0.5s;
}
.navigation-li:hover {
    transition-property: color, background-color, border-color;
    transition-duration: 0.5s, 0.5s, 0.5s;
    border-color: white;
    background-color: #0d6efd;
    color: white;
}
.router-link-active {
    background-color:#0d6efd!important;
    color: white !important;
    border-color: white;
}
</style>