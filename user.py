# noinspection PyInterpreter
print''' Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>USER REGISTRATION FORM</title>
</head>
<body  bgcolor= "#faebd7">
<h2 align="center">USER REGISTRATION</h2>
<form name="frm" align="center" method="post" action="user_code.py">
    <table align="center" cellpadding="15">
       
        <tr>
            <td><mark>Firstname</mark></td>
            <td><input type="text" name="F_name"></td>
            <td><mark>Lastname</mark></td> 
            <td><input type="text" name="L_name"></td>       
        </tr>
        <tr>
            <td><mark>E-mail</mark></td>
            <td><input type="mail" name="email" required></td>
        </tr>
        <tr>
            <td><mark>Password</mark></td>
            <td><input type="password" name="Password" required></td>
        <tr>
        <tr>
            <td><mark>Address</mark></td>
            <td><input type="text" name="Address" required></td>        
        
        </tr>
        <tr>
            <td><mark>Mobile No.</mark></td>
            <td><input type="Phone" name="mobile" required></td>
        </tr>
         <tr>
            <td><mark>City</mark></td>
            <td><input type="text" name="city" required></td>
        </tr>
         <tr>
            <td><mark>Pin no.</mark></td>
            <td><input type="text" name="pin"></td>
        </tr>
        <tr>
        <td>&nbsp</td>
        <td>
            <input type="submit" name="ok"value="save">
        </td>
    </tr>
    </table>
</form>
</body>
</html>
'''