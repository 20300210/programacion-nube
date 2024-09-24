<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <title>Registro de Notas</title>
</head>
<body>
    <div class="container mt-5">
        <h2 class="text-center mb-4">REGISTRO NOTAS</h2>

        <form id="formulario" method="post" class="mb-4">
            <div class="row">
                <div class="col-md-4 mb-3">
                    <select class="form-control" name="profesor" id="profesor">
                        <option value="">--Seleccione un profesor--</option>
                    </select>
                </div>
                <div class="col-md-4 mb-3">
                    <select class="form-control" name="estudiante" id="estudiante">
                        <option value="">--Seleccione un estudiante--</option>
                    </select>
                </div>
                <div class="col-md-4 mb-3">
                    <input class="form-control" id="nota" name="nota" placeholder="Insertar nota">
                </div>
            </div>
            <div class="text-center">
                <button type="button" id="btn_guardar" class="btn btn-danger">Guardar nota</button>
            </div>
        </form>

        <table class="table table-dark">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>PROFESOR</th>
                    <th>ESTUDIANTE</th>
                    <th>NOTA</th>
                    <th>OPCIONES</th>
                </tr>
            </thead>
            <tbody id="tabla_notas">
                <!-- Aquí se llenarán los datos -->
            </tbody>
        </table>
    </div>
    <script src="js/script.js"></script>
</body>
</html>