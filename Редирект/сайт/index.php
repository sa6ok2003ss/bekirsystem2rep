<?php
// Подключение к базе данных
$servername = "mysql.cd33ca7a60b5.hosting.myjino.ru";
$username = "j8732740_system";
$password = "196924Ll!";
$dbname = "j8732740_system";

$conn = new mysqli($servername, $username, $password, $dbname);

// Проверка соединения
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Получение параметра state из GET-запроса
$state = isset($_GET['state']) ? $_GET['state'] : null;

// Проверка значения state и обновление базы данных
if ($state == 7) {
    $sql = "SELECT * FROM users WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $_GET['id']);
    $stmt->execute();
    $result = $stmt->get_result();
    
    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        if ($row['state7'] == 0) {
            $sql = "UPDATE users SET state7 = 1 WHERE id = ?";
            $stmt = $conn->prepare($sql);
            $stmt->bind_param("i", $_GET['id']);
            $stmt->execute();
        }
    } else {
        $sql = "INSERT INTO users (id, state7, state8) VALUES (?, 1, 0)";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("i", $_GET['id']);
        $stmt->execute();
    }
    
    header("Location: https://t.me/StealthSystem");
} elseif ($state == 8) {
    $sql = "SELECT * FROM users WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $_GET['id']);
    $stmt->execute();
    $result = $stmt->get_result();
    
    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        if ($row['state8'] == 0) {
            $sql = "UPDATE users SET state8 = 1 WHERE id = ?";
            $stmt = $conn->prepare($sql);
            $stmt->bind_param("i", $_GET['id']);
            $stmt->execute();
        }
    } else {
        $sql = "INSERT INTO users (id, state7, state8) VALUES (?, 0, 1)";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("i", $_GET['id']);
        $stmt->execute();
    }
    
    header("Location: https://t.me/BekirOtzivi");
} else {
    // Если параметр state не равен 7 или 8, можно добавить дополнительную логику
}

$conn->close();
?>