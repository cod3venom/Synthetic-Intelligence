<?php


namespace Kernel\Interfaces;


interface IDataObject
{
    public function Initialize($USER_ID);
    public function InitializeAll();
    public function Save();
}