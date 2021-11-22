<?php 
 
$command = escapeshellcmd('test.py'); //Chuyển mã trong tập tin test.py thành các lệnh
$output = shell_exec($command); // Lấy kết quả trả về biến $output
echo $output; // Xuất kết quả
 
?>