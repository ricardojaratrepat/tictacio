<script>
  let message = "";
  const token = localStorage.getItem("token");
  const API_BASE_URL = process.env.API_BASE_URL;

  async function fetchProtectedData() {
    try {
      const protectedRouteEndpoint = `${API_BASE_URL}/protected-route`;
      const response = await fetch(protectedRouteEndpoint, {
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
