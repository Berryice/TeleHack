<template>
    <form @submit.prevent>
        <div class="mail-form">
            <map-component 
                :x="this.coords.x"
                :y="this.coords.y"
                :newRadius="this.radius"
            />
            <div class="coord-input">
                <input-tag
                    v-model.number="coords.x"
                    placeholder="Введите X*"
                    required
                    class="input-tag"
                />
                <input-tag
                    v-model.number="coords.y"
                    placeholder="Введите Y*"
                    required
                    class="input-tag"
                />
                <map-slider @input="newRadius"/>
                <input-button @click="printResults" class="btn">Отправить</input-button>
            </div>
            <res-div class="results">Здесь будут данные о зданиях</res-div>
        </div>
    </form>
</template>

<script>
import MapComponent from "@/components/UI/MapComponent"
export default {
    components: {
        MapComponent
    },
    data() {
        return {
            radius: 0,
            coords: {
                x:  56.790846,
                y: 60.509152
            }
        }
    },
    methods: {
        printResults(event) {
            document.querySelector('.results').innerHTML = "lorem"
        },
        newRadius(event) {
            this.radius = event.target.valueAsNumber
        },
    }
}
</script>

<style scoped>
.mail-form {
    justify-content: space-between;
    margin: 0 1%;
    position: relative;
    display: flex;
}
.coord-input {
    display: flex;
    font-family: "Inter";
    margin: 1% 5%;
    position: absolute;
    background: none;
    z-index: 9999;
}
.input-tag {
    margin: 0 1% 0 0;
}
.btn {
    height: 30px;
}
.slider:hover {
    opacity: 1;
}

.results {
    font-size: 14px;
    width: 18%;
}
</style>