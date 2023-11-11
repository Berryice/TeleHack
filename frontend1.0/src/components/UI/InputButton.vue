<template>
    <button class="input-button">
        <slot></slot>
    </button>
</template>

<script>
export default {
    name: 'input-button'
}
</script>

<style scoped>
.input-button {
    font-family: "Inter";
    border: #0d6efd 3px solid;
    border-radius: 20px;
    background-color: #fff;
    color: #0d6efd;
    margin-left: 2%;
    height: 40px;
    transition-property: color, background-color, border-color;
    transition-duration: 0.5s, 0.5s, 0.5s;
}
.input-button:hover {
    transition-property: color, background-color, border-color;
    transition-duration: 0.5s, 0.5s, 0.5s;
    background-color: #0d6efd;
    color: #fff;
}
</style>