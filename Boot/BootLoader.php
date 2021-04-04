<?php

    CONST STATUS_PREFIX = '[STATRTUP] ====> ';
    CONST BACKSLASH = '\\';
    CONST SLASH = '//';
    CONST PHP = '.php';

    spl_autoload_register(function ($component) {
        Debug(1,STATUS_PREFIX.$component."</br>");
        BootLoader($component);
    });

    function BootLoader($component)
    {
        if(!empty($component))
        {
            $component = $component.PHP;
            $component = str_replace(BACKSLASH,SLASH,$component);
            include_once $component;
        }
    }

    function Debug($status,$data)
    {
        //echo $data;
    }
?>