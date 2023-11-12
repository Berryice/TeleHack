<template>
    <form @submit.prevent>
        <div class="map-form">
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
                <div class="for-radius">{{ this.radius }}</div>
                <input-button @click="printResults" class="btn">Отправить</input-button>
            </div>
            <res-div class="results" >
                <div v-if="addresses.length !== 0">
                    <div v-for="address in addresses">
                        <div class="address-entity">
                            <p class="address-entity__text">{{ address.unrestricted_value }}</p>
                        </div>
                    </div>
                </div>
                <div v-else>
                    <div>
                        <p class="address-entity__empty">Данных нет</p>
                    </div>
                </div>
            </res-div>
        </div>
    </form>
</template>

<script>
import MapComponent from "@/components/UI/MapComponent"
import axios from 'axios';

export default {
    components: {
        MapComponent
    },
    data() {
        return {
            radius: 0,
            coords: {
                x: 56.8349,
                y: 60.538743
            },
            addresses: []
        }
    },
    methods: {
        printResults() {
            axios.get("http://localhost:8000/geo/", { params: { long: this.coords.y, lat: this.coords.x, radius: this.radius } })
                .then(response => {
                    this.addresses = response.data.adresses
                }
                )
                .catch(err => console.log(err))
        },
        newRadius(event) {
            this.radius = event.target.valueAsNumber
        },
    }
}
</script>

<style scoped>
.map-form {
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
.for-radius {
    text-align: center;
    width: 10%;
    height: 22px;
    z-index: 9999;
    position: absolute;
    left: 180%;
    top: 2000%;
    color: #0d6efd;
    border: 3px solid #0d6efd;
    border-radius: 20px;
    background-color: white;
}
.results {
    font-size: 14px;
    width: 18%;
    height: 670px;
    overflow-y: auto;
}
.address-entity {
    margin-bottom: 15px;
}
.address-entity__text {
    font-family: "Inter";
}
.address-entity__empty {
    font-family: "Inter";
    margin-left: 35%;
    margin-top: 20%;
    font-size: large;
}
</style>