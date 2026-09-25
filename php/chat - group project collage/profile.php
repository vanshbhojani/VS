<?php
session_start();
$servername = "localhost";
$username = "root";  // Default XAMPP MySQL username
$password = "";      // Default XAMPP MySQL password (blank)
$dbname = "company_chat";


$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if user is logged in
if (!isset($_SESSION['user_id'])) {
    header("Location: login.php"); // Redirect to login page if not logged in
    exit();
}

$user_id = $_SESSION['user_id'];

// Fetch user data from database
$stmt = $conn->prepare("SELECT username, email, password FROM users WHERE id = ?");
$stmt->bind_param("i", $user_id);
$stmt->execute();
$result = $stmt->get_result();

if ($result->num_rows > 0) {
    $user = $result->fetch_assoc();
    $name = $user['username'];
    $email = $user['email'];
    $hashed_password = $user['password'];
} else {
    die("User not found");
}

$stmt->close();

// Handle form submissions
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['profile_submit'])) {
        // Handle profile update
        $new_name = $_POST['name'];
        $new_email = $_POST['email'];
        $new_password = $_POST['new_password'];
        
        $update_stmt = $conn->prepare("UPDATE users SET username = ?, email = ? WHERE id = ?");
        $update_stmt->bind_param("ssi", $new_name, $new_email, $user_id);
        
        if ($update_stmt->execute()) {
            $name = $new_name;
            $email = $new_email;
            $message = "Profile updated successfully!";
            
            // Update password if provided
            if (!empty($new_password)) {
                $hashed_new_password = password_hash($new_password, PASSWORD_DEFAULT);
                $password_update_stmt = $conn->prepare("UPDATE users SET password = ? WHERE id = ?");
                $password_update_stmt->bind_param("si", $hashed_new_password, $user_id);
                if ($password_update_stmt->execute()) {
                    $hashed_password = $hashed_new_password;
                    $message .= " Password updated successfully!";
                } else {
                    $error = "Error updating password: " . $conn->error;
                }
                $password_update_stmt->close();
            }
            
            // Redirect to chat.php after successful update
            header("Location: chat.php");
            exit();
        } else {
            $error = "Error updating profile: " . $conn->error;
        }
        $update_stmt->close();
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile Page</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100">
    <div class="container mx-auto p-6 space-y-6">
        <?php if (isset($message)): ?>
            <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline"><?php echo $message; ?></span>
            </div>
        <?php endif; ?>
        <?php if (isset($error)): ?>
            <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline"><?php echo $error; ?></span>
            </div>
        <?php endif; ?>

        <div class="bg-white shadow rounded-lg">
            <div class="p-6">
                <h2 class="text-2xl font-bold">Profile Information</h2>
                <p class="text-gray-500">Update your account's profile information, email address, and password.</p>
            </div>
            <div class="p-6 border-t border-gray-200">
                <form method="POST" class="space-y-4">
                    <div>
                        <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
                        <input type="text" id="name" name="name" value="<?php echo htmlspecialchars($name); ?>" 
                               class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                    </div>
                    <div>
                        <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
                        <input type="email" id="email" name="email" value="<?php echo htmlspecialchars($email); ?>" 
                               class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                    </div>
                    <div>
                        <label for="current_password" class="block text-sm font-medium text-gray-700">Current Password (Hashed)</label>
                        <input type="text" id="current_password" value="<?php echo htmlspecialchars($hashed_password); ?>" readonly
                               class="mt-1 block w-full rounded-md border-gray-300 bg-gray-100 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                    </div>
                    <div>
                        <label for="new_password" class="block text-sm font-medium text-gray-700">New Password (leave blank to keep current password)</label>
                        <input type="password" id="new_password" name="new_password"
                               class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                    </div>
                    <button type="submit" name="profile_submit" 
                            class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                        Save and Go to Chat
                    </button>
                </form>
            </div>
        </div>
    </div>
</body>
</html>