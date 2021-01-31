<?php
	$i=0; 
	$sum=0; 
	while($sum<=3) 
	{
		$i++; 
		$isum=0;
		for($k=1;$k<$i;$k++) 
		{
			
			if($i  % $k == 0) 
			{
				$isum+=$k; 
			}
		}
		if($isum==$i) 
		{
			echo "$i <br />";
			$sum++;
		}
	}
	?>
