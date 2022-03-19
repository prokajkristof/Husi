<?php
    //database connection
    $user = //select count(*) from user where username = uname and password = pwd;
    //No password in db :(
?>
<script>
    var value = "<?php echo $user; ?>";
    if(value == 0){
        document.getElementsByName("login")[0].disabled = true;
    }

function validate(){
if (value>0){
alert ("Logged in successfully");
window.location = "#"; // page to redirect
}
else{
    alert("E-mail or password is incorrect");
}
}
</script>