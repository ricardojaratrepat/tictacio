<script>
    let username = localStorage.getItem("username") || "usuario"; // Puedes almacenar el nombre al iniciar sesión
</script>

<main>
    <h1>¡Bienvenido a Tictacio, {username}!</h1>
    <p>Estamos contentos de tenerte aquí.</p>
</main>

<style>
    main {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        text-align: center;
    }

    h1 {
        color: #007bff;
        font-size: 2em;
    }
</style>
