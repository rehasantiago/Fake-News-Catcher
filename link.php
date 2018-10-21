<?php
$input=$_POST['input'];
$my_file = 'input.txt';
$handle = fopen($my_file, 'w') or die('Cannot open file:  '.$my_file);
$data = $input;
fwrite($handle, $data);
$pyscript='C:\\xampp\\htdocs\\CodeByters-Enroot\\google.py';//path of python file
$cmd="$pyscript";
$links=array();
$final=array();
exec("$cmd",$output);
foreach($output as $value){
	echo $value;
}
?>