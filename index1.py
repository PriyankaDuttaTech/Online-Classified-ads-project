import cgi,cgitb
frm=cgi.FieldStorage()
msg=frm.getvalue('msg')
print''' Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<center>
<body bgcolor= "#faebd7">
<h2>User Login</h2>
<form name="frm" method="post" action="userlogin.py">
    <table cellpadding="15">
        
        <tr>
            <td><mark>Email-id</mark></td>
            <td><input type="mail" name="email" required></td>
        </tr>
        <tr>
            <td><mark>Password</mark></td>
            <td><input type="password" name="Password" required></td>
        <tr>
        <td>&nbsp</td>
        <td>
            <input type="submit" name="ok"value="login">
        </td>
        
        </tr>
    </table>
</form>'''
print '''<form name="frm" method="post" action="user.py">
    <table cellpadding="15">
        
        <td>&nbsp</td>
            <td><mark>New seller?<mark></td>
            <td><input type="submit" name="ok" value="click here"></td>
            
        </tr>
    </table>
</form>
</center>'''
if msg:
    print msg+"<br>"
print '''</body>
</html>
'''