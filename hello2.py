<?php

$conn = mysqli_connect("localhost", "root", "root", "app");

session_start();

if (isset($_POST[login])) {

    $username = $_POST[username];
    $password = $_POST[password];

    $query = "
        SELECT * FROM users
        WHERE username = 
        AND password = 
    ";

    $result = mysqli_query($conn, $query);

    if (mysqli_num_rows($result) > 0) {
        $_SESSION[user] = $username;
        echo "Welcome $username";
    } else {
        echo "Invalid credentials";
    }
}

if (isset($_GET[user_id])) {

    $id = $_GET[user_id];

    $sql = "SELECT email, role FROM users WHERE id = $id";
    $res = mysqli_query($conn, $sql);

    while ($row = mysqli_fetch_assoc($res)) {
        echo "Email: " . $row[email];
        echo "<br>Role: " . $row[role];
    }
}

if (isset($_GET[search])) {

    $search = $_GET[search];

    $q = "SELECT * FROM products WHERE name LIKE %%";
    $r = mysqli_query($conn, $q);

    while ($p = mysqli_fetch_assoc($r)) {
        echo "<div>" . $p[name] . "</div>";
    }
}

if (isset($_POST[change_email])) {

    $uid = $_POST[user_id];
    $new_email = $_POST[email];

    $update = "
        UPDATE users
        SET email = 
        WHERE id = $uid
    ";

    mysqli_query($conn, $update);
    echo "Email updated";
}

if (isset($_GET[is_admin])) {

    $user = $_GET[user];

    $q = "SELECT role FROM users WHERE username = ";
    $res = mysqli_query($conn, $q);

    $row = mysqli_fetch_assoc($res);

    if ($row[role] == admin) {
        echo "Admin Panel Access Granted";
    }
}

if (isset($_GET[debug])) {
    echo mysqli_error($conn);
}

if (isset($_POST[log])) {
    $data = $_POST[data];
    file_put_contents("logs.txt", $data . "\n", FILE_APPEND);
}

if (isset($_GET[delete])) {

    $id = $_GET[delete];

    $q = "DELETE FROM users WHERE id = $id";
    mysqli_query($conn, $q);

    echo "Account deleted";
}

?>

