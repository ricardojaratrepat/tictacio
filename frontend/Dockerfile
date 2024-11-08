# Etapa 1: Construcción
FROM node:16 AS build

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de dependencias y luego instala
COPY package.json package-lock.json ./
RUN npm install

# Copia todo el código fuente de la aplicación
COPY . .

# Construye la aplicación para producción
RUN npm run build

# Etapa 2: Servidor web con nginx
FROM nginx:alpine

# Copia los archivos construidos desde la etapa de construcción
COPY --from=build /app/public /usr/share/nginx/html


# Copia la configuración de nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expone el puerto 80
EXPOSE 80

# Comando para iniciar nginx
CMD ["nginx", "-g", "daemon off;"]
