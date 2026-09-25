<?php
include 'db.php';
session_start();

if (!isset($_SESSION['user_id'])) {
    echo json_encode(['error' => 'User not authenticated']);
    exit();
}

$current_user_id = $_SESSION['user_id'];
$other_user_id = isset($_GET['receiver_id']) ? intval($_GET['receiver_id']) : 0;

if ($other_user_id === 0) {
    echo json_encode(['error' => 'Invalid receiver ID']);
    exit();
}

// Get current user's username
$stmt = $conn->prepare("SELECT username FROM users WHERE id = ?");
$stmt->bind_param("i", $current_user_id);
$stmt->execute();
$result = $stmt->get_result();
$current_user = $result->fetch_assoc();
$current_username = $current_user['username'];
$stmt->close();

// Get messages from both users' tables
$current_user_table = "messages_" . preg_replace('/[^a-zA-Z0-9_]/', '_', $current_username);

$sql = "SELECT * FROM $current_user_table 
        WHERE (sender_id = ? AND receiver_id = ?) OR (sender_id = ? AND receiver_id = ?)
        ORDER BY timestamp ASC";

$stmt = $conn->prepare($sql);
$stmt->bind_param("iiii", $current_user_id, $other_user_id, $other_user_id, $current_user_id);
$stmt->execute();
$result = $stmt->get_result();

$messages = [];
while ($row = $result->fetch_assoc()) {
    $messages[] = $row;
}

echo json_encode($messages);
$stmt->close();
?>