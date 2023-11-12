<template>
    <form class="vk-page" @submit.prevent>
        <div class="message" v-show="isUser">
            <div class="input-user">
                <input-tag class="vk-input-user" v-model="this.userLink" required placeholder="Введите идентификатор пользователя*"/>
                <button class="btn-user" @click="isUser=!isUser">{{ isUser?'Пользователь':'Паблик' }}</button>
                <input-button class="send-btn"  @click="sendUserLink($event)">Отправить</input-button>
            </div>
            <div v-if="this.resUser !== '' ">
                <res-div class="results">
                    <div>
                        ID: {{ this.resUser.id }}<br>
                        First Name: {{ this.resUser.first_name }}<br>
                        Last Name: {{ this.resUser.last_name }}<br>
                        Folowers: <br>
                        <div v-for="usr in this.resUser.folowers" :key="usr.id">
                            {{ usr.first_name }} {{ usr.last_name }}<br>
                        </div>
                    </div>
                </res-div>
            </div>
            <div v-else>
                <res-div class="results">
                    Данных нет
                </res-div>
            </div>
        </div>
        <div class="message" v-show="!isUser">
            <div class="input-public">
                <button class="btn-publ" @click="isUser=!isUser">{{ isUser?'Пользователь':'Паблик' }}</button>
                <input-tag class="vk-input-publ" v-model="this.publicLink" required placeholder="Введите идентификатор паблика*"/>
                <input-button class="send-btn" @click="sendPublicLink">Отправить</input-button>
            </div>
            <div v-if="this.resPublic !== '' ">
                <res-div class="results">
                    ID: {{ this.resPublic.id }}<br>
                    Name: {{ this.resPublic.name }}<br>
                    Closed: {{ Boolean(this.resPublic.is_closed) }}
                </res-div>
            </div>
            <div v-else>
                <res-div class="results">
                    Данных нет
                </res-div>
            </div>
        </div>
    </form>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            userLink: '',
            publicLink: '',
            isUser: true, 
            resUser: "",
            resPublic: ""
        }
    },
    methods: {
        sendPublicLink(event) {
            if(this.publicLink !== ""){
                axios.post('http://localhost:8000/task2/group/',
                    {
                        'name':this.publicLink
                    }
                ).then(response => {
                    var data = response.data
                    if(data.id){
                        this.resPublic = {
                            id: data.id,
                            name: data.name,
                            is_closed: data.is_closed
                        }
                    } else {
                        this.resPublic = ""
                    }
                    this.publicLink = ""
                }
                ).catch(err => {
                    console.log(err)
                    this.resPublic = ""
                    this.publicLink = ""
                })
            }
        },
        sendUserLink(event) {
            if(this.userLink !== ""){
                axios.post('http://localhost:8000/task2/user/',
                    {
                        'name':this.userLink
                    }
                ).then(response => {
                    var data = response.data
                    if (data.user_info){
                        this.resUser = {
                            id: data.user_info.id,
                            first_name: data.user_info.first_name,
                            last_name: data.user_info.last_name,
                            folowers: data.followers
                        }
                    } else {
                        this.resUser = ""
                    }
                    this.userLink = ""
                }
                ).catch(err => {
                    console.log(err)
                    this.resUser = ""
                    this.userLink = ""
                })
            }
        }
    }
}
</script>

<style scoped>
.vk-page {
    margin-left: 2%;
}
.input-user .input-public {
    display: flex;
}
.results {
    width: 95%;
    margin-top: 2%;
    height: 400px;
}
.results div{
    font-family: 'Inter';
}
.results div div{
    margin-left: 30px;
}
.btn-user {
    font-family: 'Inter';
    height: 40px;
    border: #0d6efd 3px solid;
    border-radius: 0 20px 20px 0;
    background-color: #0d6efd;
    color: rgb(30, 30, 30);
    width: 10%;
    transition-property: color, background-color, border-color;
    transition-duration: 0.5s, 0.5s, 0.5s;
}
.btn-user:hover {
    background-color: rgb(30, 30, 30);
    color: #0d6efd;
    border-color: #fff;
    transition-property: color, background-color, border-color;
    transition-duration: 0.5s, 0.5s, 0.5s;
}
.vk-input-user {
    height: 40px;
    width: 50%;
    border-radius: 20px 0 0 20px;
}
.btn-publ {
    font-family: 'Inter';
    height: 40px;
    border: #0d6efd 3px solid;
    border-radius: 20px 0 0 20px;
    background-color: #0d6efd;
    color: #1e1e1e;
    width: 10%;
    transition-property: color, background-color, border-color;
    transition-duration: 0.5s, 0.5s, 0.5s;
}
.btn-publ:hover {
    background-color: rgb(30, 30, 30);
    color: #0d6efd;
    border-color: #fff;
    transition-property: color, background-color, border-color;
    transition-duration: 0.5s, 0.5s, 0.5s;
}
.vk-input-publ {
    height: 40px;
    width: 50%;
    border-radius: 0 20px 20px 0;
}
</style>