<script>
    import { onMount } from "svelte";
    let username = "";
    let password = "";
    let message = "";
  
    async function handleLogin() {
      try {
        const response = await fetch("http://127.0.0.1:8000/login", {
          method: "POST",
          headers: {
                "Accept": "application/json",         
                "Content-Type": "application/json"
          },
          body: JSON.stringify({ username, password })
        });
  
        if (!response.ok) {
          throw new Error("Inicio de sesión fallido");
        }
  
        const data = await response.json();
        localStorage.setItem("token", data.access_token);  // Guardar el token en el navegador
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
  