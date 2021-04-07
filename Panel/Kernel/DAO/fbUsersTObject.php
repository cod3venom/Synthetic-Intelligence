<?php

namespace Kernel\DAO;

use Kernel\Config\Constants;
use Kernel\DataBase\MySql;
use Kernel\Interfaces\IDataObject;

class fbUsersTObject extends MySql implements  IDataObject {

    protected $ID;
    protected $USER_ID;
    protected $USERNAME;
    protected $PASSWORD;
    protected $IPADDRESS;
    protected $FLAG;
    protected $DATE;
    protected $RETURN_TYPE; 
    public function __construct()
    {
         parent::__construct();
    }
    private function CopyObjects($Result, $certain = true)
    {
        $copy = array();
        if($this->getReturnType() === Constants::JSON)
        {
            foreach ($Result as $object)
            {
               if(!$certain)
               {
                    $id = $object['ID'];
                    $copy[$id] = $object;
               }
               else
               {
                    $copy = $object;
               }
            }
            return $copy;
        }
        foreach ($Result as $object){
            $this->setID($object["ID"]);
            $this->setUSER_ID($object["USER_ID"]); 
            $this->setUSERNAME($object["USERNAME"]); 
            $this->setPASSWORD($object["PASSWORD"]); 
            $this->setIPADDRESS($object["IPADDRESS"]); 
            $this->setFLAG($object["FLAG"]); 
            $this->setDATE($object["DATE"]);
        }
    }
    private function Reset()
    {
        $this->setID("");
        $this->setUSER_ID("");
        $this->setUSERNAME("");
        $this->setPASSWORD("");
        $this->setIPADDRESS("");
        $this->setFLAG("");
        $this->setDATE("");
    }
    public function setID($ID){ $this->ID = $ID; }
    public function setUSER_ID($USER_ID){ $this->USER_ID = $USER_ID; }
    public function genUSER_ID(){ $this->USER_ID = md5(microtime()); }
    public function setUSERNAME($USERNAME){ $this->USERNAME = $USERNAME; }
    public function setPASSWORD($PASSWORD){ $this->PASSWORD = $PASSWORD; }
    public function setIPADDRESS($IPADDRESS){ $this->IPADDRESS = $IPADDRESS; }
    public function setFLAG($FLAG){ $this->FLAG = $FLAG; }
    private function setDATE($DATE){ $this->DATE = $DATE; }
    public function setReturnType($type){ $this->RETURN_TYPE = $type;}public function getID(){ return $this->ID; }
    public function getUSER_ID(){ return $this->USER_ID; }
    public function getUSERNAME(){ return $this->USERNAME; }
    public function getPASSWORD(){ return $this->PASSWORD; }
    public function getIPADDRESS(){ return $this->IPADDRESS; }
    public function getFLAG(){ return $this->FLAG; }
    public function getDATE(){ return $this->DATE; }
    public function getReturnType(){ return $this->RETURN_TYPE;}

    public function Initialize($USER_ID)
    {
        $this->CreateStatement(5)->bind_param("s", $USER_ID);
        return $this->CopyObjects($this->Select());
    }
    public function InitializeByCredentials()
    {
        $this->CreateStatement(1)->bind_param("ss", $this->USERNAME, $this->PASSWORD);
        return $this->CopyObjects($this->Select());
    }

    public function InitializeAll()
    {

    }
    public function Exists()
    {

    }
    public  function ExistsByCredentials($username, $password)
    {
        $this->CreateStatement(1)->bind_param("ss", $username, $password);
        $this->CopyObjects($this->Select());
        return !empty($this->USER_ID);
    }
    public function Save()
    {
        $this->CreateStatement(2)->bind_param("sssss", $this->USER_ID, $this->USERNAME, $this->PASSWORD, $this->IPADDRESS, $this->FLAG);
        $this->Insert();
        return $this->Initialize($this->USER_ID);
    }
    public function Update()
    {
        if (!empty($Class->USER_ID))
        {
            $this->CreateStatement(4)->bind_param("sssss",  $this->USERNAME, $this->PASSWORD, $this->IPADDRESS, $this->FLAG, $this->USER_ID);
            $this->Insert();
            return $this->Initialize($Class->USER_ID);
        }
        return false;
    }
    public function Remove(){
        $this->CreateStatement(6)->bind_param("s",  $this->USER_ID);
        $this->Insert();
        return $this->Initialize($this->USER_ID);
    }
}
     
