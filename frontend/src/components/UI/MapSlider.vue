<template>
    <div>
        <input type="range" min="1" max="1000" class="slider">
    </div>
</template>

<script>
export default {
    name: 'map-slider'
}
</script>

<style>
.slider {
    position: absolute;
    left: 120%;
    top: 2000%;
    width: 50%;
    opacity: 0.7;
    transition: opacity .2s;
}
.slider:hover {
    opacity: 1;
}
</style>