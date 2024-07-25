<?php
// $servername = "";
$username = "root";
$password = "D@8sep2002";
$dbname = "weather";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Query to retrieve data
$sql = "SELECT * FROM weather";
$result = $conn->query($sql);

// Fetch data as an associative array
$data = array();
while ($row = $result->fetch_assoc()) {
    $data["city"] = $row;
    $data["temperature"] = $row;

}

// Close connection
$conn->close();

// Return data as JSON
echo json_encode($data);
?>
