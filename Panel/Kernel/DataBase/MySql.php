<?php


namespace Kernel\DataBase;


class MySql extends DButill
{
    protected  $Connection;
    protected  $QueryFactory;
    protected  $stmt;

    public function __construct()
    {
        parent::__construct();
        $this->Connection = mysqli_connect($this->DB_HOSTNAME, $this->DB_USERNAME, $this->DB_PASSWORD, $this->DB_NAME);
        $this->QueryFactory = new QueryFactory();
    }

    public function CreateStatement($num){
        $query = $this->QueryFactory->getQuery($num);
        echo $query;
        if($this->Connection && !empty($query)){
            $this->stmt = mysqli_stmt_init($this->Connection);
            if(!$this->stmt->prepare($query)){
                echo mysqli_stmt_error($this->stmt);
            }else{
                $this->stmt->prepare($query);
                return $this->stmt;
            }
        }
        return false;
    }


    public function CreateStatementWithQuery($query){
        if($this->Connection && !empty($query)){
            $this->stmt = mysqli_stmt_init($this->Connection);
            if(!$this->stmt->prepare($query)){
                echo $query;
                echo mysqli_stmt_error($this->stmt);
            }else{
                $this->stmt->prepare($query);
                return $this->stmt;
            }
        }
        return false;
    }

    public function Insert(){
        try {
            if($this->stmt){
                if($this->stmt->execute()) {
                    $this->stmt->store_result();
                }
            }
        }
        catch (\Exception $ex){
            echo $ex;
        }
    }

    public function Select(){
        if($this->stmt){
            if($this->stmt->execute()){
                return $this->stmt->get_result();
            }
        }
        return false;
    }

    public function Delete(){
        if($this->stmt){
            return $this->stmt->execute();
        }
        return false;
    }


    public function Count(){
        if($this->stmt){
            if($this->stmt->execute()){
                $this->stmt->store_result();
                return $this->stmt->num_rows();
            }
        }
    }

    private function CloseConnection(){
        if($this->Connection){
            $this->stmt->close();
            $this->Connection->close();
        }
    }

    function JSDebug($status,$data)
    {
        global $count;
        $count +=1;
        $code = '<script>console.log("[#]*");</script>';
        $code = str_replace("#",$count, $code);
        $code = str_replace("*",$data,$code);
        #echo $code;
    }
}