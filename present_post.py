import config
print '''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ADD POSTS</title>
</head>
<body>
<h2>PRODUCT DETAILS</h2>
<form name="frm" method="post" action="view_posts.py">
    <table>
        <tr>
           <td>SELECT</td>
            <td colspan="2" align="center">
                <select name="User_id">
                <option value="" selected>Username</option>'''
cursor=config.db.cursor()
cursor.execute('SELECT * FROM userdata')
result=cursor.fetchall()
for rec in result:
    print '''<option value="{}">{}</option>'''.format(rec[0],rec[1])
print ''' </select>
            </td>
            
        </tr>
               <tr>
            
            <td><input type="submit" name="ok" value="view posts"></td>        
        
        </tr>
    
    </table>
</form>
</body>
</html>
'''
