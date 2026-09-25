<?php
include 'db.php';

function create_unique_username($conn, $base_username) {
    $username = $base_username;
    $counter = 1;

    // Check if the username exists
    $stmt = $conn->prepare("SELECT id FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->store_result();

    while ($stmt->num_rows > 0) {
        // If exists, append a number to create a unique username
        $username = $base_username . '_' . $counter;
        $counter++;

        $stmt->bind_param("s", $username);
        $stmt->execute();
        $stmt->store_result();
    }

    $stmt->close();
    return $username;
}

function create_user_message_table($conn, $username) {
    $table_name = "messages_" . preg_replace('/[^a-zA-Z0-9_]/', '_', $username);
    $sql = "CREATE TABLE IF NOT EXISTS $table_name (
        id INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        sender_id INT(11) NOT NULL,
        receiver_id INT(11) NOT NULL,
        message TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";
    return $conn->query($sql);
}


if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['username']) && isset($_POST['email']) && isset($_POST['password'])) {
    $username = trim($_POST['username']);
    $email = trim($_POST['email']);
    $password = password_hash(trim($_POST['password']), PASSWORD_BCRYPT);

    // Ensure the username is unique
    $username = create_unique_username($conn, $username);

    // Insert the new user into the database
    $stmt = $conn->prepare("INSERT INTO users (username,email,password) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $username, $email, $password);
    if ($stmt->execute()) {
        // Create a unique message table for the new user
        // create_user_message_table($conn, $username);
    
        // Redirect to chat.php
        header("Location: chat.php");
        exit(); // Ensure the script stops executing after the redirect
    } else {
        echo "Error: Could not register user.";
    }
    
    $stmt->close();
    $conn->close();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Signup - IT Company Chat Group</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .signup-container {
            background-color: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        h2 {
            text-align: center;
            color: #333;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        input {
            margin: 10px 0;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 10px;
        }
        button:hover {
            background-color: #0056b3;
        }
        .error {
            color: red;
            font-size: 14px;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="signup-container">
        <h2>Signup</h2>
        <!-- <?php if ($error_message): ?>
            <p class="error"><?php echo htmlspecialchars($error_message); ?></p>
        <?php endif; ?> -->
        <form action="signup.php" method="POST">
            <input type="text" name="username" placeholder="Name" required>
            <input type="email" name="email" placeholder="Email" required>
            <input type="password" name="password" placeholder="Password" required minlength="8">
            <button type="submit">Signup</button>
        </form>
        <p>Already have an account? <a href="login.php">Login here</a></p>
    </div>
</body>
</html>