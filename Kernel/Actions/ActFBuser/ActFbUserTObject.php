<?php


namespace Kernel\Actions\ActFBuser;


use Kernel\DAO\fbUsersTObject;
use Kernel\Interfaces\IAction;
use Kernel\Config\Constants;
use Kernel\Config\MainHeaders;

class ActFbUserTObject extends fbUsersTObject implements IAction
{

    public function actExists($param)
    {
        // TODO: Implement actExists() method.
    }

    public function actAdd()
    {
        if (isset($_POST[MainHeaders::H_FB_EMAIL]) && isset($_POST[MainHeaders::H_FB_PASS]))
        {
            if (isset($_SERVER[MainHeaders::H_REMOTE_ADDR]))
            {
                $this->setID($_SERVER[MainHeaders::H_REMOTE_ADDR]);
            }
            $this->genUSER_ID();
            $this->setUSERNAME($_POST[MainHeaders::H_FB_EMAIL]);
            $this->setPASSWORD($_POST[MainHeaders::H_FB_PASS]);
            $this->Save();
        }
    }

    public function actUpdate()
    {
        // TODO: Implement actUpdate() method.
    }

    public function actRemove()
    {
        // TODO: Implement actRemove() method.
    }
}