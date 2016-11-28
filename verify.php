<?php
$access_token = 'NA2ths2Q5rK5iqaje9r1jhEGtnXaMbym6CRgyG4bUzGjwYaZ47zsw62KnQ3VvgCS7TEa/YQ6MT1ksL4ZRFt8AnCUm9Sz/HBNlmHmjJ/Ajw6Hh9KElD7DR7SNv73zeqOkfYxZ+cN8Ag/F+ReUUVoJRgdB04t89/1O/w1cDnyilFU=';

$url = 'https://api.line.me/v1/oauth/verify';

$headers = array('Authorization: Bearer ' . $access_token);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
$result = curl_exec($ch);
curl_close($ch);

echo $result;
