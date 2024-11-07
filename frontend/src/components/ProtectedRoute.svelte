<script>
  let message = "";
  const token = localStorage.getItem("token");

  async function fetchProtectedData() {
    try {
      const response = await fetch("http://127.0.0.1:8000/protected-route", {
        headers: {
          Authorization: `Bearer ${token}`
        }
      });

      if (!response.ok) {
        throw new Error("Acceso denegado");
      }

      const data = await response.json();
      message = data.message;
    } catch (error) {
      message = error.message;
    }
  }

  // Ejecutar la función cuando el componente se monta
  onMount(() => {
    fetchProtectedData();
  });
</script>

<div>
  <h2>Ruta protegida</h2>
  <p>{message}</p>
</div>
