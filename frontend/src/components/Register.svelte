<script>
    import { onMount } from "svelte";
    let username = "";
    let password = "";
    let message = "";

    async function handleRegister() {
    try {
        const registerEndpoint = `${API_BASE_URL}/register`;
        const response = await fetch(registerEndpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        });

        if (!response.ok) {
            throw new Error("El nombre de usuario ya está registrado o hubo un error.");
        }

        message = "¡Usuario registrado exitosamente!";
    } catch (error) {
        message = error.message;
    }
}

</script>

<div>
    <h2>Registro</h2>
    <input bind:value={username} placeholder="Nombre de usuario" />
    <input type="password" bind:value={password} placeholder="Contraseña" />
    <button on:click={handleRegister}>Registrar</button>
    {#if message}
        <p>{message}</p>
    {/if}
</div>
