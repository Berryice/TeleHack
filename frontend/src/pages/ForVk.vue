<template>
    <form class="vk-page" @submit.prevent>
        <div class="message" v-show="isUser">
            <div class="input-user">
                <input-tag class="vk-input-user" v-model="this.userLink" required placeholder="Введите ссылку*"/>
                <button class="btn-user" @click="isUser=!isUser">{{ isUser?'Пользователь':'Паблик' }}</button>
                <input-button class="send-btn"  @click="sendUserLink($event)">Отправить</input-button>
            </div>
            <res-div class="results">Здесь будут данные о пользователе</res-div>
        </div>
        <div class="message" v-show="!isUser">
            <div class="input-public">
                <button class="btn-publ" @click="isUser=!isUser">{{ isUser?'Пользователь':'Паблик' }}</button>
                <input-tag class="vk-input-publ" v-model="this.publicLink" required placeholder="Введите ссылку*"/>
                <input-button class="send-btn" @click="sendPublicLink">Отправить</input-button>
            </div>
            <res-div class="results">Здесь будут данные о паблике</res-div>
        </div>
    </form>
</template>

<script>
export default {
    data() {
        return {
            userLink: '',
            publicLink: '',
            isUser: true
        }
    },
    methods: {
        sendPublicLink(event) {
            
        },
        sendUserLink(event) {
            
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