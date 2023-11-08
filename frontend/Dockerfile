FROM node:20-alpine

RUN npm install -g http-server

WORKDIR /frontend

COPY package*.json ./

# устанавливаем зависимости проекта
RUN npm install

COPY . .