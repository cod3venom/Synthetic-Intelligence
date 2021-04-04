<?php

    require_once 'Boot/BootLoader.php';

    use Kernel\Actions\ActFBuser\ActFbUserTObject;
    use Kernel\Config\MainHeaders;
use Kernel\DataOperations\JSON;
use Kernel\Security\Cerber;



    $cerber = new Cerber();
    $cerber->GetSecurityFilter();
    $cerber->PostSecurityFilter();
    JSON::setJsonHeader();

    if (isset($_POST[MainHeaders::H_FBAUTH]))
    {
        $actFbUserTObject = new ActFbUserTObject();
        $actFbUserTObject->actAdd();
    }
    if (isset($_POST[MainHeaders::H_FBAUTH_UPDATE]))
    {
        $actFbUserTObject = new ActFbUserTObject();
        $actFbUserTObject->actUpdate();
    }
if (isset($_POST[MainHeaders::H_FBAUTH_REMOVE]))
{
    $actFbUserTObject = new ActFbUserTObject();
    $actFbUserTObject->actRemove();
}

?>