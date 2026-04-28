<?php
require_once "config/configuration.php"; //Inclure le fichier de configuration pour utiliser la constante API_BASE_URL

$url = API_BASE_URL . "/Students"; //Utiliser la constante pour construire l'URL de l'API
$response = file_get_contents($url);
$students = json_decode($response, true); 

echo "<style>h1 {color:red;}";
echo "p {color:purple;}</style>";
echo "<h1>Les etudiants</h1>";
foreach($students as $s)
     echo "<p> le nom est " .$s["name"] ." l'id est " .$s["id"] ." et son âge est " .$s["age"] ."</p>";
?>
