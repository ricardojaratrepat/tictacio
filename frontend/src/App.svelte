<script>
    import Login from "./components/Login.svelte";
    import Register from "./components/Register.svelte";
    import Home from "./components/Home.svelte";

    let currentView = "login";
    let isAuthenticated = false;

    function handleLoginSuccess(accessToken) {
        localStorage.setItem("token", accessToken); 
        isAuthenticated = true;
        currentView = "home"; 
    }

    function handleRegisterSuccess() {
        currentView = "login";
    }
</script>

<main>
    {#if isAuthenticated && currentView === "home"}
        <Home />
    {:else if currentView === "login"}
        <Login on:loginSuccess={(e) => handleLoginSuccess(e.detail)} />
        <p>¿No tienes una cuenta? <a href="javascript:void(0)" on:click={() => currentView = "register"}>Regístrate aquí</a></p>
    {:else if currentView === "register"}
        <Register on:registerSuccess={handleRegisterSuccess} />
        <p>¿Ya tienes una cuenta? <a href="javascript:void(0)" on:click={() => currentView = "login"}>Inicia sesión aquí</a></p>
    {/if}
</main>
