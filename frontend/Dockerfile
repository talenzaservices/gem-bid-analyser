FROM node:18-alpine

WORKDIR /app

COPY package.json package-lock.json* ./
RUN npm install

COPY . .

# Ensure Vite is available
RUN npm install -g vite

CMD ["npm", "run", "dev", "--", "--host"]
