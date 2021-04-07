<?php


namespace Kernel\DataOperations;


class JSON
{
    public static function PrettyConverter($json){
        return json_encode($json,JSON_PRETTY_PRINT);
    }
    public static function setJsonHeader(){
        header('Content-Type: application/json');
    }
    public static function setTextHeader(){
        header('Content-Type: html/text');
    }
}