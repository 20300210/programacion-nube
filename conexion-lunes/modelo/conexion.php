<?php
class Conexion extends PDO {
private $host = 'localhost';
private $usuario = 'root';
private $contrasena = '';
private $nombreBD = 'practica_16_09_2024';
private $conn;
public function __construct() {
try {
    $this->conn = new PDO("mysql:host=$this->host;dbname=$this->nombreBD",
    $this->usuario,
    $this->contrasena);
//$this->conn = newPDO("pgsql:host=localhost;port=5432;dbname=ejercicio1_migracion;user=postgres;password=12345");
// Configurar el modo de error de PDO a excepciones
    $this->conn->setAttribute(PDO::ATTR_ERRMODE,
PDO::ERRMODE_EXCEPTION);
}catch (PDOException $e) {
    $this->conn->$e->getMessage();
}
}
public function getConexion() {
    return $this->conn;
}
}
?>