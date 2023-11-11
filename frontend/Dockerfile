FROM node:20-alpine

RUN npm install -g http-server
RUN npm install -g @vue/cli-service --save-dev
WORKDIR /frontend

COPY package*.json ./

# устанавливаем зависимости проекта
RUN npm install
COPY . .
