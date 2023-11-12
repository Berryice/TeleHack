<template>
    <form class="telegram-page" @submit.prevent>
        <div class="data-inputs">
            <input-tag
                v-model="this.tgcLink"
                class="input-tgc id"
                placeholder="Введите идентификатор телеграм-канала*"
                required
            />
            <input-tag v-show="keyWords.length !== 0"
                v-model="this.tgcUserName"
                class="input-tgc user"
                placeholder="Введите имя пользователя*"
                required
            />
            <input-tag v-show="keyWords.length === 0"
                v-model="this.tgcUserName"
                class="input-tgc user"
                placeholder="Введите имя пользователя"
            />
            <input-tag
                v-model="this.keyWords"
                class="input-tgc key-words"
                placeholder="Введите ключевые слова"
            />
        </div>
        <input-button class="btn" @click="submit">Отправить</input-button>
        <res-div class="results">
            <div v-if=" res !== '' ">
                <div v-for="message, index in this.res" :key="index" class="messages">
                    <div>
                        {{ message }}
                    </div>
                </div>
            </div>
            <div v-else class="messages">
                <div>
                    Нет данных
                </div>
            </div>
        </res-div>
    </form>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            tgcLink: '',
            tgcUserName: '',
            keyWords: '',
            res:""
        }
    },
    methods: {
        submit(){
            if(this.tgcLink !== ""){
                if(this.tgcUserName !== "") {
                    console.log(this.keyWords)
                    axios.get('http://localhost:8000/telegram/',
                    {
                        params: {
                            gname: this.tgcLink, 
                            search: this.keyWords, 
                            username: this.tgcUserName
                        }
                    })
                    .then(response => {
                        console.log(response)
                        if (response.data.posts){
                            this.res = response.data.posts
                        } else {
                            this.res = ""
                        }
                        this.tgcLink = ""
                        this.tgcUserName = ""
                        this.keyWords = ""
                    }
                )
                .catch(err => {
                    console.log(err)
                    this.tgcLink = ""
                    this.tgcUserName = ""
                    this.keyWords = ""
                })
            } else if(this.keyWords === "") {
                    axios.get('http://localhost:8000/telegram/', {params: { gname: this.tgcLink}})
                    .then(response => {
                        if (response.data.posts){
                            this.res = response.data.posts
                        } else {
                            this.res = ""
                        }
                        this.tgcLink = ""
                        this.tgcUserName = ""
                        this.keyWords = ""
                    }
                )
                .catch(err => {
                    console.log(err)
                    this.tgcLink = ""
                    this.tgcUserName = ""
                    this.keyWords = ""
                })
                }
            } else {
                this.tgcLink = ""
                this.tgcUserName = ""
                this.keyWords = ""
            }
        }
    }
}
</script>

<style scoped>
.input-tgc {
    width: 25%;
    margin-left: 6%;
    margin-bottom: 1%;
    height: 40px;
}
.btn {
    float: right;
    margin-right: 7%;
}
.results {
    border-radius: 20px 0 0 20px;
    width: 80%;
    margin: 4% auto 0;
    height: 400px;
    overflow-y: scroll;
    scroll-behavior: smooth;
}
.messages div{
    font-family: "Inter";
    margin-top: 4px;
}
</style>