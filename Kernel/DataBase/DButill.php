<?php


namespace Kernel\Classes\Database;


use Kernel\Classes\Config\Constants;
use Kernel\Classes\Security\FileSystem;

class DButill extends FileSystem
{
    public $DB_HOSTNAME = 'DB_HOSTNAME';
    public $DB_USERNAME = 'DB_USERNAME';
    public $DB_PASSWORD = 'DB_PASSWORD';
    public $DB_NAME = 'DB_NAME';

    public function __construct()
    {

        $Config = $this::readFile(Constants::DB_ACCESS);
        $unJson = json_decode($Config, true);
        foreach ($unJson as $json){
            foreach ($json as $jsn){
                $this->DB_HOSTNAME = $jsn[$this->DB_HOSTNAME];
                $this->DB_USERNAME = $jsn[$this->DB_USERNAME];
                $this->DB_PASSWORD = $jsn[$this->DB_PASSWORD];
                $this->DB_NAME = $jsn[$this->DB_NAME];
                return true;
            }
        }
        return false;
    }
}