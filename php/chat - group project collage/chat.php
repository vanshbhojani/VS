    <?php
    include 'db.php';
    session_start();

    if (!isset($_SESSION['user_id'])) {
        header("Location: login.php");
        exit();
    }

    $user_id = $_SESSION['user_id'];
    $user_name = $_SESSION['user_name'];

    // Function to create a new user-specific message table
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

    // Function to store a message
    function store_message($conn, $sender_id, $receiver_id, $message) {
        // Get sender's username
        $stmt = $conn->prepare("SELECT username FROM users WHERE id = ?");
        $stmt->bind_param("i", $sender_id);
        $stmt->execute();
        $result = $stmt->get_result();
        $sender = $result->fetch_assoc();
        $sender_username = $sender['username'];
        $stmt->close();

        // Create or use existing table for sender
        $sender_table = "messages_" . preg_replace('/[^a-zA-Z0-9_]/', '_', $sender_username);
        create_user_message_table($conn, $sender_username);

        // Insert message into sender's table
        $stmt = $conn->prepare("INSERT INTO $sender_table (sender_id, receiver_id, message) VALUES (?, ?, ?)");
        $stmt->bind_param("iis", $sender_id, $receiver_id, $message);
        $stmt->execute();
        $stmt->close();

        // Get receiver's username
        $stmt = $conn->prepare("SELECT username FROM users WHERE id = ?");
        $stmt->bind_param("i", $receiver_id);
        $stmt->execute();
        $result = $stmt->get_result();
        $receiver = $result->fetch_assoc();
        $receiver_username = $receiver['username'];
        $stmt->close();

        // Create or use existing table for receiver
        $receiver_table = "messages_" . preg_replace('/[^a-zA-Z0-9_]/', '_', $receiver_username);
        create_user_message_table($conn, $receiver_username);

        // Insert message into receiver's table
        $stmt = $conn->prepare("INSERT INTO $receiver_table (sender_id, receiver_id, message) VALUES (?, ?, ?)");
        $stmt->bind_param("iis", $sender_id, $receiver_id, $message);
        $stmt->execute();
        $stmt->close();
    }

    // Handle message sending
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['message']) && isset($_POST['receiver_id'])) {
        $message = trim($_POST['message']);
        $receiver_id = intval($_POST['receiver_id']);
        
        if (!empty($message) && $receiver_id > 0) {
            store_message($conn, $user_id, $receiver_id, $message);
            echo json_encode(['status' => 'success']);
        } else {
            echo json_encode(['status' => 'error', 'message' => 'Invalid message or receiver']);
        }
        exit();
    }

    // Fetch user list for personal chat
    $sql = "SELECT id, username FROM users WHERE id != ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $user_id);
    $stmt->execute();
    $user_list = $stmt->get_result();
    $stmt->close();
    ?>

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Company Chat Group</title>
        <style>

            .current-user {
                background-color: var(--primary-color);
                color: white;
                padding: 15px;
                margin-bottom: 20px;
                border-radius: 5px;
                font-weight: bold;
            }

            .user-list li.active {
                background-color: #e0e0e0;
            }

            :root {
                --primary-color: #3498db;
                --secondary-color: #2c3e50;
                --bg-color: #ecf0f1;
                --text-color: #34495e;
            }

            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: 'Arial', sans-serif;
                height: 100vh;
                display: flex;
                flex-direction: column;
                background-color: var(--bg-color);
                color: var(--text-color);
            }

            header {
                background-color: black;
                color: white;
                padding: 15px 20px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }

            nav {
                display: flex;
                justify-content: flex-start;
            }

            nav a {
                color: white;
                text-decoration: none;
                padding: 10px 15px;
                margin-right: 10px;
                transition: background-color 0.3s;
                border-radius: 5px;
            }

            nav a:hover {
                background-color: rgba(255,255,255,0.1);
            }

            .login-signup {
                margin-left: auto;
            }

            .chat-container {
                display: flex;
                flex-grow: 1;
                overflow: hidden;
            }

            .sidebar {
                width: 20%;
                background-color: lightgrey;
                padding: 20px;
                overflow-y: auto;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }

            .user-list {
                list-style-type: none;
            }

            .user-list li {
                padding: 10px;
                border-bottom: 1px solid #eee;
                cursor: pointer;
                transition: background-color 0.3s;
            }

            .user-list li:hover {
                background-color: #f0f0f0;
            }

            .chat-area {
                width: 60%;
                display: flex;
                flex-direction: column;
                background-color: lightblue;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }

            .chat-messages {
                flex-grow: 1;
                overflow-y: auto;
                padding: 20px;
                display: flex;
                flex-direction: column;
            }

            .message {
                margin-bottom: 15px;
                padding: 10px;
                border-radius: 5px;
                max-width: 70%;
                position: relative;
            }

            .message.sent {
                background-color: var(--primary-color);
                color: white;
                align-self: flex-end;
                text-align: right;
            }

            .message.received {
                background-color: #f0f0f0;
                align-self: flex-start;
                text-align: left;
            }

            .chat-input {
                padding: 20px;
                background-color: #f9f9f9;
                display: flex;
            }

            .chat-input input {
                flex-grow: 1;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }

            .chat-input button {
                padding: 10px 20px;
                background-color: var(--primary-color);
                color: white;
                border: none;
                border-radius: 5px;
                margin-left: 10px;
                cursor: pointer;
                transition: background-color 0.3s;
            }

            .chat-input button:hover {
                background-color: #2980b9;
            }

            .right-sidebar .user-profile {
                padding: 20px;
            }

            .user-profile h2 {
                margin-bottom: 15px;
                color: var(--secondary-color);
            }

            .user-profile p {
                margin-bottom: 10px;
            }
        </style>
    </head>
    <body>
        <header>
            <nav>
                <a href="#home">Home</a>
                <a href="profile.php">Profile</a>
                <div class="login-signup">
                    <span><?php echo htmlspecialchars($user_name); ?></span>
                    <a href="logout.php">Logout</a>
                </div>
            </nav>
        </header>
        <div class="chat-container">
            <div class="sidebar left-sidebar">
                <div class="current-user">
                    You: <?php echo htmlspecialchars($user_name); ?>
                </div>
                <ul class="user-list" id="userList">
                    <?php
                    while ($user = $user_list->fetch_assoc()) {
                        echo "<li data-user-id='" . $user['id'] . "'>" . htmlspecialchars($user['username']) . "</li>";
                    }
                    ?>
                </ul>
            </div>

            <div class="chat-area">
                <div class="chat-messages" id="chatMessages">
                    <!-- Chat messages will be populated by JavaScript -->
                </div>
                <div class="chat-input">
                    <input type="text" id="messageInput" placeholder="Type your message...">
                    <button id="sendButton">Send</button>
                </div>
            </div>

            <div class="sidebar right-sidebar">
                <div class="user-profile" align="center">
                    <h2>User Profile</h2>
                    <p>Name: <span id="profileName"><?php echo htmlspecialchars($user_name); ?></span></p>
                    <p>Email: <span id="profileEmail"><?php echo htmlspecialchars($_SESSION['user_email']); ?></span></p>
                </div>
            </div>
        </div>

        
        <script>
            const currentUserId = <?php echo $user_id; ?>;
            const currentUserName = "<?php echo addslashes($user_name); ?>";
            let selectedUserId = null;

            // DOM elements
            const userList = document.getElementById('userList');
            const chatMessages = document.getElementById('chatMessages');
            const messageInput = document.getElementById('messageInput');
            const sendButton = document.getElementById('sendButton');

            // Select user to chat with
            function selectUser(userId, userName) {
                selectedUserId = userId;
                chatMessages.innerHTML = ''; // Clear chat
                const message = document.createElement('div');
                message.textContent = `You are now chatting with ${userName}`;
                message.className = 'message received';
                chatMessages.appendChild(message);
                
                // Remove active class from all users
                userList.querySelectorAll('li').forEach(li => li.classList.remove('active'));
                
                // Add active class to selected user
                userList.querySelector(`li[data-user-id="${userId}"]`).classList.add('active');
                
                // Load previous messages for this user
                loadMessages(userId);
            }

            // Add click event listeners to user list
            userList.querySelectorAll('li').forEach(li => {
                li.addEventListener('click', () => {
                    const userId = li.getAttribute('data-user-id');
                    const userName = li.textContent;
                    selectUser(userId, userName);
                });
            });

            // Send message
            function sendMessage() {
                const text = messageInput.value.trim();
                if (text && selectedUserId) {
                    fetch('chat.php', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded',
                        },
                        body: `message=${encodeURIComponent(text)}&receiver_id=${selectedUserId}`
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.status === 'success') {
                            const message = document.createElement('div');
                            message.textContent = text;
                            message.className = 'message sent';
                            chatMessages.appendChild(message);
                            messageInput.value = '';
                            chatMessages.scrollTop = chatMessages.scrollHeight;
                        } else {
                            console.error('Error sending message:', data.message);
                        }
                    })
                    .catch(error => console.error('Error:', error));
                }
            }

            sendButton.addEventListener('click', sendMessage);
            messageInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') sendMessage();
            });

            // Load messages for a specific user
            function loadMessages(userId) {
                fetch(`get_messages.php?receiver_id=${userId}`)
                .then(response => response.json())
                .then(messages => {
                    chatMessages.innerHTML = ''; // Clear existing messages
                    messages.forEach(msg => {
                        const message = document.createElement('div');
                        message.textContent = msg.message;
                        if (msg.sender_id == currentUserId) {
                            message.className = 'message sent';
                            message.style.alignSelf = 'flex-end';
                        } else {
                            message.className = 'message received';
                            message.style.alignSelf = 'flex-start';
                        }
                    chatMessages.appendChild(message);
                    });
                    chatMessages.scrollTop = chatMessages.scrollHeight;
                })
                .catch(error => console.error('Error loading messages:', error));
                }

            // Initially load the first user's chat
            if (userList.firstElementChild) {
                const firstUserId = userList.firstElementChild.getAttribute('data-user-id');
                const firstUserName = userList.firstElementChild.textContent;
                selectUser(firstUserId, firstUserName);
            }
        </script>
    </body>
    </html>    
   