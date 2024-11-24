import { spawn } from 'child_process';
import svelte from 'rollup-plugin-svelte';
import commonjs from '@rollup/plugin-commonjs';
import terser from '@rollup/plugin-terser';
import resolve from '@rollup/plugin-node-resolve';
import livereload from 'rollup-plugin-livereload';
import css from 'rollup-plugin-css-only';
import dotenv from 'dotenv';
import replace from '@rollup/plugin-replace';

dotenv.config();

const production = !process.env.ROLLUP_WATCH;

function serve() {
	let server;

	function toExit() {
		if (server) server.kill(0);
	}

	return {
		writeBundle() {
			if (server) return;
			server = spawn('npm', ['run', 'start', '--', '--dev'], {
				stdio: ['ignore', 'inherit', 'inherit'],
				shell: true
			});

			process.on('SIGTERM', toExit);
			process.on('exit', toExit);
		}
	};
}

export default {
	input: 'src/main.js',
	output: {
		sourcemap: true,
		format: 'iife',
		name: 'app',
		file: 'public/build/bundle.js'
	},
	plugins: [
		svelte({
			compilerOptions: {
				dev: !production // Habilitar verificaciones en tiempo de ejecución si no es producción
			}
		}),
		// Extraer CSS en un archivo separado
		css({ output: 'bundle.css' }),

		// Reemplazar las variables de entorno en tiempo de compilación
		replace({
			preventAssignment: true, // Prevenir advertencias de asignación
			'process.env.API_BASE_URL': JSON.stringify(process.env.API_BASE_URL || 'http://localhost:8000') // Valor predeterminado
		}),

		// Resolver dependencias de npm
		resolve({
			browser: true,
			dedupe: ['svelte'],
			exportConditions: ['svelte']
		}),
		commonjs(),

		// Ejecutar el servidor de desarrollo en modo dev
		!production && serve(),

		// Recargar el navegador en cambios si no es producción
		!production && livereload('public'),

		// Minificar si es producción
		production && terser()
	],
	watch: {
		clearScreen: false
	}
};
