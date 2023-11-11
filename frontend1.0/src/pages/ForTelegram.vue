<template>
    <form class="telegram-page" @submit.prevent>
        <div class="data-inputs">
            <input-tag
                v-model="this.tgcLink"
                class="input-tgc id"
                placeholder="Введите ссылку на телеграм-канал*"
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
        <input-button class="btn">Отправить</input-button>
        <res-div class="results">Lorem ipsum dolor sit amet consectetur adipisicing elit. Perferendis ab neque maxime debitis a, architecto, et beatae dicta atque, itaque omnis? Temporibus fuga est nulla ipsa vero ullam autem aliquid soluta iusto fugiat, in ipsum reprehenderit adipisci maiores aperiam excepturi veritatis cupiditate sit tempora. Animi, similique suscipit! Explicabo ad culpa, debitis commodi labore a repellat, numquam pariatur aperiam hic repellendus quasi perferendis, aut consequuntur? Repellendus asperiores accusamus inventore. Dolore ut asperiores distinctio? Magnam animi facilis tempore eos sapiente. Error repellat hic obcaecati quam natus? Molestias impedit, quidem autem ipsum placeat dolores alias officiis, delectus, soluta quo sequi provident quae iure. Aliquid dolores earum impedit voluptatum, quaerat dolorem. Cumque molestiae quaerat quae velit cum eligendi reiciendis, incidunt accusantium quasi voluptas ratione iusto quis quam optio dolor repellat nemo quo ipsam fugit rem, placeat saepe neque explicabo amet. At neque ab eum nostrum repudiandae officia tempora omnis voluptas, ad, maiores error nesciunt iusto, temporibus quaerat architecto molestiae impedit dolores enim quibusdam voluptatibus. Mollitia dignissimos praesentium id repudiandae ex architecto ea voluptatem exercitationem ipsam qui labore recusandae similique magnam voluptatum porro natus soluta debitis fugit, fugiat illo provident consequatur officiis accusantium! At dolor saepe architecto! Nostrum natus placeat iste possimus esse harum, corrupti deleniti suscipit voluptate dolor iusto voluptatem expedita, aut quidem aliquam quod voluptatum magnam quisquam repellendus sed quos omnis reprehenderit eius non! Animi perferendis officiis voluptatum fuga vel aperiam quidem accusantium soluta, quas repellendus dolorum facilis nam possimus quasi commodi culpa temporibus necessitatibus atque! Voluptas obcaecati laborum pariatur eum ad quidem sapiente veritatis dolorum expedita quasi rerum, ab fugiat quo omnis mollitia voluptate qui alias corrupti iusto, praesentium facere aliquid ullam! Eius velit officiis, soluta sapiente sequi ipsa, eos veniam, aliquid impedit amet doloremque deleniti cumque consequuntur doloribus natus voluptate excepturi similique aperiam! Officia, cupiditate explicabo! Assumenda cupiditate sit alias provident unde harum omnis, porro sed atque suscipit quis praesentium voluptatum necessitatibus consequatur ad incidunt quisquam aspernatur aperiam laudantium aliquam nam ut molestiae? Repellendus quos accusamus repellat quasi voluptatem ipsum consequatur minima eos fugiat nobis? Itaque sint libero praesentium alias ullam facilis error numquam, perferendis eos unde excepturi dolore, dolor veritatis inventore exercitationem incidunt nesciunt? Soluta asperiores quos impedit odit explicabo aperiam officia voluptas eos minus natus accusamus, sapiente veniam reprehenderit similique corrupti ipsum architecto animi praesentium. Officiis autem expedita dolor deserunt atque id eaque quibusdam dolore, perferendis non, sed earum modi eligendi. Eos, laboriosam fuga modi in dolorum reiciendis maxime nemo corrupti illum eligendi! Dignissimos distinctio, inventore ut iste officia placeat laborum modi? Sequi illo aut dicta quia sed eaque ab non quisquam ducimus quaerat accusamus velit sit doloremque expedita tenetur deserunt quis adipisci, esse aspernatur id quos sint at. Vero magnam dignissimos ipsam pariatur recusandae sit nesciunt! Nobis assumenda ipsam ea reprehenderit quas et eaque minus? Facere ut iure consequatur voluptatem cumque, beatae hic deleniti reprehenderit molestias quis quia similique quod ab voluptatibus maiores ullam, excepturi animi vel reiciendis consectetur corrupti sapiente dolor eaque. Voluptate quaerat maxime placeat voluptatem aperiam! Dolorem quia dicta numquam ab dolor atque quo autem.</res-div>
    </form>
</template>

<script>
export default {
    data() {
        return {
            tgcLink: '',
            tgcUserName: '',
            keyWords: ''
        }
    },
    methods: {
        
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
</style>