<?php
$url = "http://127.0.0.1:5000/Students";
$response = file_get_contents($url);

#decodage du tableau JSON en php
$students = json_decode($response, true); 
#json_decode : Transforme le JSON en PHP
#True : Retourne un tableau associatif au lieu d'un objet

echo "<pre>";
print_r($students); //Affiche le tableau des étudiants de manière lisible
echo "</pre>";
#Une fois que'on a le résultat sous forme d'un tableau, on peut améliore ( par exmple l'affichage)
?>
