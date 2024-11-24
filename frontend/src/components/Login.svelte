<script>
    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();
    const API_BASE_URL = process.env.API_BASE_URL;
    let username = "";
    let password = "";
    let message = "";

    async function handleLogin() {
        try {
            const loginEndpoint = `${API_BASE_URL}/login`;
            const response = await fetch(loginEndpoint, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ username, password })
            });

            if (!response.ok) {
                throw new Error("Usuario o contraseña incorrectos");
            }

            const data = await response.json();
            dispatch("loginSuccess", data.access_token); 

            message = "Inicio de sesión exitoso!";
        } catch (error) {
            message = error.message;
        }
    }
</script>

<div>
    <h2>Iniciar sesión</h2>
    <input bind:value={username} placeholder="Usuario" />
    <input type="password" bind:value={password} placeholder="Contraseña" />
    <button on:click={handleLogin}>Iniciar sesión</button>
    {#if message}
        <p>{message}</p>
    {/if}
</div>
