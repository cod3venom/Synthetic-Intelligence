<?php


namespace Kernel\Database;


use Kernel\Config\Constants;
use Kernel\Security\FileSystem;

class QueryFactory extends FileSystem
{
    public function getQuery($num)
    {
        $Content = $this->readFile(Constants::DB_QUERIES);
        if(strpos($Content, Constants::NEWLINE)!==false && strpos($Content, Constants::DOLLAR)){
            $Lines = explode(Constants::NEWLINE,$Content);
            for ($i=0; $i < count($Lines);$i++){

                if (strpos($Lines[$i], Constants::HASHTAG) === false)
                {
                    $stack = explode(Constants::DOLLAR,$Lines[$i]);
                    if((int)$stack[0] === (int)$num)
                    {
                        return $stack[1];
                    }
                }
            }
        }
        return Constants::_EMPTY;
    }
}