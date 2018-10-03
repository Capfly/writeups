<?php   
    // include $flag for ninjas
    include 'flag.php';
    
    // we are oddly specific on the number required to extract this flag
    function check_val($val){
        return (is_numeric($val) && strlen($val) === 5 && $val > 2431 && $val < 2433);
    }
    
    // give me those vars
    if(isset($_GET['x'],$_GET['y'],$_GET['z'])){
        if($_GET['x'] !== $_GET['y'] && $_GET['x'] !== $_GET['z'] && $_GET['y'] !== $_GET['z']){
            if(check_val($_GET['x']) && check_val($_GET['y']) && check_val($_GET['z'])){
                die($flag);
            }
        }
    }
    
    // share the source cause we are nice guys
    show_source(basename(__FILE__));
?>