<script>
    import Login from "./components/Login.svelte";
    import Register from "./components/Register.svelte";
    import ProtectedRoute from "./components/ProtectedRoute.svelte";

    let token = localStorage.getItem("token"); // Para saber si el usuario está autenticado
    let currentView = "login"; // Vista actual: "login" o "register"

    function goToRegister() {
        currentView = "register";
    }

    function goToLogin() {
        currentView = "login";
    }
</script>

<main>
    {#if token}
        <ProtectedRoute />
    {:else}
        <!-- Mostrar el componente adecuado según la vista actual -->
        {#if currentView === "login"}
            <Login />
            <p>¿No tienes una cuenta? <a href="#" on:click={goToRegister}>Regístrate aquí</a></p>
        {:else if currentView === "register"}
            <Register />
            <p>¿Ya tienes una cuenta? <a href="#" on:click={goToLogin}>Inicia sesión aquí</a></p>
        {/if}
    {/if}
</main>
