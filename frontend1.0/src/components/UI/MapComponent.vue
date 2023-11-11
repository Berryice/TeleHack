<template>
    <div id="map" style="height: 500px; border: solid 3px #0d6efd; min-width: 80%; border-radius: 20px;">
    </div>
</template>

<script>
import L from 'leaflet'
    
    export default {
        name: 'MapComponent',
        data(){
            return {
                theMap: null,
                circle: null,
                mark: null
            }
        },
        props: {
            x: {
                type: Number,
                required: true
            },
            y: {
                type: Number,
                required: true
            },
            newRadius: {
                type: Number,
                required: true
            }
        },
        mounted(){
            this.init()
        },
        watch: {
            x(newx) {
                this.theMap.removeLayer(this.mark)
                this.theMap.setView([newx, this.y], 13)
                this.mark = L.marker([newx, this.y]).addTo(this.theMap);
            },
            y(newy) {
                this.theMap.removeLayer(this.mark)
                this.theMap.setView([this.x, newy], 13)
                this.mark = L.marker([this.x, newy]).addTo(this.theMap);
            },
            newRadius(newradius) {
                this.theMap.removeLayer(this.circle)
                this.circle = L.circle([this.x, this.y], {
                    color: '#1e1e1e',
                    fillColor: '#0d6efd',
                    fillOpacity: 0.5,
                    radius: newradius
                }).addTo(this.theMap);
            }
        },
        methods:{
            init(){
                this.theMap = L.map("map")
                this.theMap.setView([this.x, this.y], 13)
                L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 19,
                    attribution: ''
                }).addTo(this.theMap);
                this.mark = L.marker([this.x, this.y]).addTo(this.theMap);
                this.circle = L.circle([this.x, this.y], {
                    color: '#1e1e1e',
                    fillColor: '#0d6efd',
                    fillOpacity: 0.5,
                    radius: this.newRadius
                }).addTo(this.theMap);
            }
        },
    }
</script>
<style src="leaflet/dist/leaflet.css"></style>