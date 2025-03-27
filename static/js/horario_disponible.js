document.addEventListener("DOMContentLoaded", function() {
    const barberSelect = document.getElementById("barber");
    const dateInput = document.getElementById("date");
    const timeSelect = document.getElementById("time");

    function actualizarHorarios() {
        const barbero = barberSelect.value;
        const fecha = dateInput.value;

        if (barbero && fecha) {
            fetch(`/horarios_disponibles?barbero=${barbero}&fecha=${fecha}`)
                .then(response => response.json())
                .then(data => {
                    timeSelect.innerHTML = '<option value="" selected disabled>Selecciona un horario</option>';
                    data.forEach(horario => {
                        const option = document.createElement("option");
                        option.value = horario;
                        option.textContent = horario;
                        timeSelect.appendChild(option);
                    });
                })
                .catch(error => console.error("Error al obtener horarios:", error));
        }
    }

    barberSelect.addEventListener("change", actualizarHorarios);
    dateInput.addEventListener("change", actualizarHorarios);
});
