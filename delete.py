print''' Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Delete</title>
</head>
<body>'''
import cgi,config
frm=cgi.FieldStorage()
post_id=frm.getvalue('post_id')
User_id=frm.getvalue('User_id')
try:
    cursor=config.db.cursor()
    sql="DELETE FROM post_table WHERE post_id={}".format(post_id)
    if cursor.execute(sql):
        config.db.commit()
        config.db.close()
       # print'Deletion successful'
        print'''
        <script>
        window.location='ADMIN.html?msg= Data Delete Successful'
        </script>'''
except Exception as e:
    print e

print''' </body>
</html>'''
