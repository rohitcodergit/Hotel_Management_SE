<?php

$server = "localhost:3308";  // Specify the port number after the hostname
$username = "root";
$password = "";  // Replace with your actual root password
$database = "HOTEL";

// Create connection
$conn = mysqli_connect($server, $username, $password, $database);

// Check connection
if (!$conn) {
    die("<script>alert('Connection failed: " . mysqli_connect_error() . "');</script>");
}

// Connection successful

?>
