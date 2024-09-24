<?php
require_once 'conexion.php';

class Modelo {
    private $conexion;

    public function __construct() {
        $c = new Conexion();
        $this->conexion = $c->getConexion();
    }

    public function get_profesor() {
        $datos = array();
        $sql = $this->conexion->prepare('SELECT id, nombre FROM profesor');
        $sql->execute();
        $resultados = $sql->fetchAll(PDO::FETCH_ASSOC);
        $t = count($resultados);
        $datos['t'] = $t;
        if ($t > 0) {
            $datos['profesores'] = $resultados;
            $datos['status'] = "success";
        } else {
            $datos['status'] = "error";
            $datos['rta'] = 0;
        }
        $this->conexion = null; // Cerrar la conexión
        return json_encode($datos);
    }

    public function get_estudiante() {
        $datos = array();
        $sql = $this->conexion->prepare('SELECT id, nombre FROM estudiante');
        $sql->execute();
        $resultados = $sql->fetchAll(PDO::FETCH_ASSOC);
        $t = count($resultados);
        $datos['t'] = $t;
        if ($t > 0) {
            $datos['estudiantes'] = $resultados; // Cambiado a "estudiantes" para mantener consistencia
            $datos['status'] = "success";
        } else {
            $datos['status'] = "error";
            $datos['rta'] = 0;
        }
        $this->conexion = null; // Cerrar la conexión
        return json_encode($datos);
    }

    public function guardar($profe, $estudiante, $nota) {
        $sql_x = 'INSERT INTO notas(id_estudiante, id_profesor, notas)
                  VALUES (:profe, :estudiante, :notas)';
        $sentencia = $this->conexion->prepare($sql_x);
        $sentencia->bindParam(':profe', $profe);
        $sentencia->bindParam(':estudiante', $estudiante);
        $sentencia->bindParam(':notas', $nota);
        $resul = $sentencia->execute();
        
        if ($resul) {
            $r['status'] = "success";
            $r['rta'] = 1;
        } else {
            $r['status'] = "error";
            $r['rta'] = 0;
        }
        $this->conexion = null; // Cerrar la conexión
        return json_encode($r);
    }

    public function get_notas() {
        $sql = $this->conexion->prepare('
            SELECT p.nombre AS profesor, e.nombre AS estudiante, n.notas AS nota 
            FROM notas n
            JOIN profesor p ON n.id_profesor = p.id
            JOIN estudiante e ON n.id_estudiante = e.id
        ');
        $sql->execute();
        $resultados = $sql->fetchAll(PDO::FETCH_ASSOC);

        if (count($resultados) > 0) {
            $datos['notas'] = $resultados;
            $datos['status'] = "success";
        } else {
            $datos['status'] = "error";
        }
        $this->conexion = null; // Cerrar la conexión
        return json_encode($datos);
    }
}