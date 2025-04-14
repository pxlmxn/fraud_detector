FROM node:23.11-bookworm AS build
WORKDIR /vue
ENV PATH /vue/node_modules/.bin:$PATH
COPY package.json /vue/package.json
RUN npm install --silent
RUN npm install @vue/cli -g
COPY . /vue
RUN npm run build

FROM nginx:1.27.4-bookworm
COPY --from=build /vue/dist /usr/share/nginx/html
