<?php
$file = fopen("/home/venom/links.txt","r");

while ($line = fgets($file)) {
  // <... Do your work with the line ...>
   echo "found ".$line;
}
fclose($fh);
