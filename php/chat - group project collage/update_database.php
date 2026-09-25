<?php
include 'db.php';

$sql = "ALTER TABLE users ADD profile_pic VARCHAR(255) DEFAULT 'default.png'";

if ($conn->query($sql) === TRUE) {
    echo "Table users updated successfully";
} else {
    echo "Error updating table: " . $conn->error;
}

// $conn->close();
?>
