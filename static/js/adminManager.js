function filtroCitas(){

  const filtroBarbero = document.getElementById('filtroBarbero');
  const filtroHora = document.getElementById('filtroHora');
  const filtroFecha = document.getElementById('filtroFecha');
  const btnLimpiarFiltros = document.getElementById('limpiarFiltros');
  const citas = document.querySelectorAll('.cita-card');
  const mensajeNoResultados = document.getElementById('mensajeNoResultados');

  function filtrarCitas() {
  const barbero = filtroBarbero.value.toLowerCase();
  const hora = filtroHora.value;
  const fecha = filtroFecha.value;

  let hayResultados = false;

  citas.forEach(cita => {
    const citaBarbero = cita.getAttribute('data-barbero');
    const citaHora = cita.getAttribute('data-hora').substring(0, 5); // <<< cortar solo HH:MM
    const citaFecha = cita.getAttribute('data-fecha');

    const matchBarbero = !barbero || citaBarbero.toLowerCase() === barbero;
    const matchHora = !hora || citaHora === hora;
    const matchFecha = !fecha || citaFecha === fecha;

    if (matchBarbero && matchHora && matchFecha) {
      cita.style.display = 'block';
      hayResultados = true;
    } else {
      cita.style.display = 'none';
    }
  });

  mensajeNoResultados.style.display = hayResultados ? 'none' : 'block';

  }

  filtroBarbero.addEventListener('change', filtrarCitas);
  filtroHora.addEventListener('change', filtrarCitas);
  filtroFecha.addEventListener('input', filtrarCitas);

  btnLimpiarFiltros.addEventListener('click', () => {
    filtroBarbero.value = '';
    filtroHora.value = '';
    filtroFecha.value = '';
    filtrarCitas();
  });
}


function configModal() {
  const botonesFinalizar = document.querySelectorAll('.btn-finalizar');

  botonesFinalizar.forEach(btn => {
    btn.addEventListener('click', () => {
      const cliente = btn.dataset.cliente;
      const barbero = btn.dataset.barbero;
      const servicio = btn.dataset.servicio;
      const monto = btn.dataset.monto;

      document.getElementById('modalCliente').textContent = cliente;
      document.getElementById('modalBarbero').textContent = barbero;
      document.getElementById('modalServicio').textContent = servicio;
      document.getElementById('modalMonto').textContent = monto;
    });
  });
}
