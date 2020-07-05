<?php
echo "\n";
echo "\x1b[00m[ Web target ]=> ";
$target = trim(fgets(STDIN));
$list = "pagelist.txt";
if(!preg_match("/^http:\/\//",$target) AND !preg_match("/^https:\/\//",$target)){
$url = "http://$target";
}else{
	$url = $target;
}

$open = fopen("$list","r");
$size = filesize("$list");
$read = fread($open,$size);
$lists = explode("\r\n",$read);
echo "\n\x1b[34;1m[+]\x1b[00m Trying to find Admin login page";
sleep(1);
echo "\n\x1b[34;1m[+]\x1b[00m Wordlist detected in list $size \n";

foreach($lists as $login){
	$link = "$url/$login";
	$web = curl_init("$link");
	curl_setopt($web, CURLOPT_FOLLOWLOCATION, 1);
	curl_setopt($web, CURLOPT_RETURNTRANSFER, 1);
	curl_exec($web);
	$httpcode = curl_getinfo($web, CURLINFO_HTTP_CODE);
	curl_close($web);
	if($httpcode == 200){
		 $handle = fopen("result_adminfinder.txt", "a+");
		fwrite($handle, "$link\n");
		print "\n\x1b[00m[\x1b[0;30m\033[42m ADMIN LOGIN \033[00m]:\x1b[33;1m $link\x1b[00m \n";
		exit(0);
	}else{
		print "\n\033[31;1m[!NOT FOUND]\033[00m $link Page not Found";
	}
}

?>
