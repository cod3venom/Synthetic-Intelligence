<?php


namespace Kernel\Classes\Interfaces;


interface IDataObject
{
    public function Initialize($USER_ID);
    public function InitializeAll();
    public function Save();
}