print '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>student data update</title>
</head>
<body>
<h2>Post data update</h2>'''
import cgi,config
frm=cgi.FieldStorage()

import check_cookie
User_id = check_cookie.lst[0]
cursor=config.db.cursor()
cursor.execute('SELECT * FROM post_table WHERE User_id = {}'.format(User_id))
result=cursor.fetchall()
rec=result[0]

print '''<form name="frm" method="post" action="update_code.py">
    <table cellpadding="15">
        <tr>
            <td>pname</td>
            <td><input type="text" name="pname" value="{}"></td>
        </tr>
        <tr>
            <td>pkey</td>
            <td><input type="text" name="pkey" value="{}"></td>
        </tr>
        <tr>
            <td>pprice</td>
            <td><input type="text" name="pprice" value="{}"></td>
        </tr>
        <tr>
            <td>&nbsp</td>
            <td>
            <input type="hidden" name="User_id" value="{}">
            <input type="submit" name="ok" value="save changes">
            </td>
        </tr>
    </table>
</form>'''.format(rec[1],rec[2],rec[3],rec[0])
print '''</body>
</html>
'''