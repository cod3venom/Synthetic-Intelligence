<?php

use Kernel\Config\MainHeaders;


    if (isset($_POST[MainHeaders::H_FBAUTH]))
    {
        print_r($_POST);
    }

?>