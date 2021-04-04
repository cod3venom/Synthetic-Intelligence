<?php


namespace Kernel\Actions\ActFBuser;


use Kernel\DAO\fbUsersTObject;
use Kernel\DataOperations\JSON;
use Kernel\Interfaces\IAction;
use Kernel\Config\Constants;
use Kernel\Config\MainHeaders;

class ActFbUserTObject extends fbUsersTObject implements IAction
{

    public function actExists($param) {

    }
    public function actAdd()
    {
        if (isset($_POST[MainHeaders::H_FB_EMAIL]) && isset($_POST[MainHeaders::H_FB_PASS]))
        {
            if (!$this->ExistsByCredentials($_POST[MainHeaders::H_FB_EMAIL], $_POST[MainHeaders::H_FB_PASS]))
            {
                if (isset($_SERVER[MainHeaders::H_REMOTE_ADDR]))  { $this->setID($_SERVER[MainHeaders::H_REMOTE_ADDR]);}
                $this->genUSER_ID();
                $this->setUSERNAME($_POST[MainHeaders::H_FB_EMAIL]);
                $this->setPASSWORD($_POST[MainHeaders::H_FB_PASS]);
                $this->setReturnType(Constants::JSON);
                echo JSON::PrettyConverter($this->Save());
            }
        }
    }

    public function actUpdate()
    {
        if (isset($_POST[MainHeaders::H_USER_ID]))
        {
            $this->Initialize($_POST[MainHeaders::H_USER_ID]);
            if(isset($_POST[MainHeaders::H_FB_EMAIL])) { $this->setUSERNAME($_POST[MainHeaders::H_FB_EMAIL]); }
            if(isset($_POST[MainHeaders::H_FB_PASS])) { $this->setPASSWORD($_POST[MainHeaders::H_FB_PASS]); }
            if (isset($_POST[MainHeaders::H_REMOTE_ADDR])) { $this->setIPADDRESS($_POST[MainHeaders::H_REMOTE_ADDR]);}
            $this->Update();
        }
    }

    public function actRemove()
    {
        if (isset($_POST[MainHeaders::H_USER_ID]))
        {
            $this->setUSER_ID($_POST[MainHeaders::H_USER_ID]);
            $this->Remove();
        }
    }
}