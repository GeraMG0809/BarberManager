document.addEventListener("DOMContentLoaded", function () {
    console.log("funcion entra")
    const barberSelect = document.getElementById("barber");
    const dateInput = document.getElementById("date");
    const timeSelect = document.getElementById("time");

    function fetchAvailableTimes() {
        const barber = barberSelect.value;
        const date = dateInput.value;

        if (barber && date) {
            fetch(`/horarios_disponibles?barbero=${barber}&fecha=${date}`)
                .then(response => response.json())
                .then(data => {
                    timeSelect.innerHTML = '<option value="" selected disabled>Selecciona un horario</option>';
                    data.forEach(hora => {
                        const option = document.createElement("option");
                        option.value = hora;
                        option.textContent = hora;
                        timeSelect.appendChild(option);
                    });
                })
                .catch(error => console.error("Error al obtener horarios:", error));
        }
    }

    barberSelect.addEventListener("change", fetchAvailableTimes);
    dateInput.addEventListener("change", fetchAvailableTimes);
});
