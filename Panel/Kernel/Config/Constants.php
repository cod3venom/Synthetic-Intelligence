<?php


namespace Kernel\Config;


class Constants
{
    const DB_ACCESS = "/usr/bin/SI/Settings/DbAccess.json";
    const DB_QUERIES = "/usr/bin/SI/QueryFactory/Queries.que";

    const _EMPTY = "";
    const NEWLINE = "\n";
    const DOLLAR = '$';
    const HASHTAG = '#';


    CONST NOT_EXISTS = 0;
    CONST EXISTS = 1;

    CONST JSON = 'JSON';
    CONST OBJECT = 'OBJECT';

    CONST HTML_ELEMENTS = array("!–- -–", "!DOCTYPE html","a","abbr","address","area","article","aside","audio","b","base", "bdi",
        "bdo","blockquote", "body","br","button","canvas","caption","cite","code","col","colgroup","data","datalist",
        "dd","del","details","dfn", "dialog","div","dl","dt","em","embed","fieldset","figure", "footer", "form",
        "h1", "h2","h3","h4","h5","h6","head","header","hgroup","hr","html","i","iframe","img","input","ins",
        "kbd","keygen","label","legend","li","link","main","map","mark","menu","menuitem","meta","meter", "nav","noscript",
        "object","ol","optgroup","option","output","p","param","pre","progress","q","rb","rp","rt", "rtc","ruby", "s",
        "samp","script","section","select","small","source","span", "strong","style", "sub","summary","sup","table", "tbody",
        "td","template","textarea","tfoot", "th", "thead","time","title","tr","track", "u","ul", "var", "video","wbr");
    CONST NOT_ALLOWED_CHARS =array(); #array('!','#','$','%','^','&','*','(',')','_','=','+',';',"'",'"');

    CONST NOT_ALLOWED_PHP   = array('<?','?>', 'php','<?php','<?php', 'system(','shell_exec','ls','dir', 'ls -l', 'chmod', 'chown');

    CONST URL_REGEX = '/^(http|https):\\/\\/[a-z0-9_]+([\\-\\.]{1}[a-z_0-9]+)*\\.[_a-z]{2,5}'.'((:[0-9]{1,5})?\\/.*)?$/i';


}
