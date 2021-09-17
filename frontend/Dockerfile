FROM node:16-alpine
WORKDIR /app
COPY ./package.json .
COPY ./package-lock.json .

RUN npm install
CMD [ "npm", "run", "start" ]