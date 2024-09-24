var formulario = document.getElementById('formulario');
var tablaNotas = document.getElementById('tabla_notas');

window.addEventListener('load', function() {
    cargarProfesores();
    cargarEstudiantes();
    cargarNotas();
});

function cargarProfesores() {
    fetch('control/controllers.php?view=1', { method: 'POST' })
    .then(resp => resp.json())
    .then(data => {
        if(data.status === 'success') {
            var profesor = document.getElementById('profesor');
            profesor.innerHTML = '<option value="">--Seleccione un profesor--</option>';
            data.profesores.forEach(prof => {
                profesor.innerHTML += `<option value="${prof.id}">${prof.nombre}</option>`;
            });
        } else {
            alert('Error al cargar los profesores');
        }
    }).catch(error => console.error('Error:', error));
}

function cargarEstudiantes() {
    fetch('control/controllers.php?view=2', { method: 'POST' })
    .then(resp => resp.json())
    .then(data => {
        if(data.status === 'success') {
            var estudiante = document.getElementById('estudiante');
            estudiante.innerHTML = '<option value="">--Seleccione un estudiante--</option>';
            data.estudiantes.forEach(est => {
                estudiante.innerHTML += `<option value="${est.id}">${est.nombre}</option>`;
            });
        } else {
            alert('Error al cargar los estudiantes');
        }
    }).catch(error => console.error('Error:', error));
}

function cargarNotas() {
    fetch('control/controllers.php?view=4', { method: 'POST' })
    .then(resp => resp.json())
    .then(data => {
        if(data.status === 'success') {
            tablaNotas.innerHTML = '';
            data.notas.forEach((nota, index) => {
                tablaNotas.innerHTML += `
                    <tr>
                        <td>${index + 1}</td>
                        <td>${nota.profesor}</td>
                        <td>${nota.estudiante}</td>
                        <td>${nota.nota}</td>
                        <td><button class="btn btn-danger btn-sm" onclick="verConsolidado(${index + 1}, '${nota.profesor}', '${nota.estudiante}', ${nota.nota})">Ver consolidado</button></td>
                    </tr>`;
            });
        } else {
            alert('Error al cargar las notas');
        }
    }).catch(error => console.error('Error:', error));
}

document.getElementById('btn_guardar').addEventListener('click', () => {
    var datos = new FormData(formulario);
    fetch('control/controllers.php?view=3', {
        method: 'POST',
        body: datos
    })
    .then(resp => resp.json())
    .then(data => {
        if(data.status === 'success') {
            alert("Nota guardada exitosamente");
            cargarNotas();
        } else {
            alert('Error al guardar la nota');
        }
    }).catch(error => console.error('Error:', error));
});

function verConsolidado(id, profesor, estudiante, nota) {
    alert(`Consolidado para el registro #${id}:\nProfesor: ${profesor}\nEstudiante: ${estudiante}\nNota: ${nota}`);
    // Aquí puedes implementar una lógica más avanzada en el futuro,
    // como abrir un modal o hacer una nueva petición al servidor para obtener más detalles.
}