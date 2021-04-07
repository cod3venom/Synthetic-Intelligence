<?php
/*
 * @table=None
 * @author Levan Ostrowski
 * @project SILICON
 * @created 03/12/2020 - 12:57
 */

use \Kernel\Security\FileSystem;

$query = json_decode(file_get_contents("query.json"), true);

echo $query[1]['QUERY'];