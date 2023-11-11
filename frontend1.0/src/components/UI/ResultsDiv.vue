<template>
    <div class="results">
        <slot></slot>
    </div>
</template>

<script>
export default {
    name: 'res-div'
}
</script>

<style>
.results {
    font-family: "Inter";
    border: solid 3px #0d6efd;
    border-radius: 20px;
    padding: 10px;
    background-color: white;
}
</style>