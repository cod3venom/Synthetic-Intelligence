<?php


namespace Kernel\Database;


use Kernel\Config\Constants;
use Kernel\Security\FileSystem;

class DButill extends FileSystem
{
    public $DB_HOSTNAME = 'DB_HOSTNAME';
    public $DB_USERNAME = 'DB_USERNAME';
    public $DB_PASSWORD = 'DB_PASSWORD';
    public $DB_NAME = 'DB_NAME';

    public function __construct()
    {

        $Config = $this::readFile(Constants::DB_ACCESS);
        $json = json_decode($Config, true);
        $this->DB_HOSTNAME = $json[$this->DB_HOSTNAME];
        $this->DB_USERNAME = $json[$this->DB_USERNAME];
        $this->DB_PASSWORD = $json[$this->DB_PASSWORD];
        $this->DB_NAME = $json[$this->DB_NAME];
    }
}