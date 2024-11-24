import adapter from '@sveltejs/adapter-static';

export default {
  kit: {
    adapter: adapter({
      pages: 'public',  // Carpeta donde se generan los archivos estáticos
      assets: 'build', // Carpeta para los activos como CSS y JS
      fallback: null,  // Archivo HTML que se usará en caso de rutas no encontradas
    }),
    paths: {
      base: '/tictacio/', // Configuración adicional si tu proyecto usa un subdirectorio
    },
    prerender: {
      default: true, // Habilita la pre-renderización para generar contenido estático
    },
  },
};
