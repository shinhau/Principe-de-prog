<?php

$url = "http://127.0.0.1:5000/Students";
$response = file_get_contents($url);
$students = json_decode($response, true); 

echo "<style>h1 {color:red;}";
echo "p {color:purple;}</style>";
echo "<h1>Les etudiants</h1>";
foreach($students as $s)
     echo "<p> le nom est " .$s["name"] ." l'id est " .$s["id"] ." et son âge est " .$s["age"] ."</p>";
?>