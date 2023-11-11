<template>
    <input 
        required
        :value="modelValue" 
        @input="updateInput" 
        class="input"
    >
</template>

<script>
export default {
    name: 'input-tag',
    props: {
        modelValue: [String, Number]
    },
    methods: {
        updateInput(event) {
            this.$emit('update:modelValue', event.target.value)
        }
    }
}
</script>

<style scoped>
input {
    font-family: "Inter";
    border: #0d6efd 3px solid;
    border-radius: 20px;
    padding-left: 10px;
}
</style>