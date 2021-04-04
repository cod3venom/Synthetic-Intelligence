<?php


namespace Kernel\Security;


class FileSystem
{
    public function readFile($path)
    {
        if(file_exists($path)){
            return file_get_contents($path);
        }else{
            echo $path;
        }
        return false;
    }
}