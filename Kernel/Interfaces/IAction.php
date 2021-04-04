<?php


namespace Kernel\Interfaces;


interface IAction
{
    public function actExists($param);
    public function actAdd();
    public function actUpdate();
    public function actRemove();
}