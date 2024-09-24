<?php
require_once '../modelo/modelo.php';
header('Content-Type: application/json');
if(isset($_GET['view'])){
    $type = $_GET['view'];
    switch($type){
        case 1:
            $modelo = new Modelo();
            $rta = $modelo->get_profesor();
            echo $rta;
            break;
        case 2:
            $modelo = new Modelo();
            $rta = $modelo->get_estudiante();
            echo $rta;
            break;
        case 3:
            $profesor = filter_var($_POST['profesor'],FILTER_SANITIZE_SPECIAL_CHARS);
            $estudiante =
            filter_var($_POST['estudiante'],FILTER_SANITIZE_SPECIAL_CHARS);
            $nota = filter_var($_POST['nota'],FILTER_SANITIZE_SPECIAL_CHARS);
            $modelo = new Modelo();
            $rta = $modelo->guardar($profesor, $estudiante, $nota);
            echo $rta;
            break;
        case 4:
            $modelo = new Modelo();
            $rta = $modelo->get_notas();
            echo $rta;
            break;
                
        }
    }