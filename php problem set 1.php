<?php

$i = gunun_saatleri;

if(strotime($i>=06:00 && $i<10:00))
{
	echo("Günaydın")
}

elseif(strtotime($i>=10:00 && $i<17:00))
{
	echo("İyi akşamlar")
}

elseif(strtotime($i>=17:00 && $i<20:00))
{
	echo("İyi akşamlar")
}

elseif(strtotime($i>=20:00 && $i<00:00))
{
	echo("İyi geceler")
}
else:
{
	echo("Esenlikler dilerim")
}

?>
