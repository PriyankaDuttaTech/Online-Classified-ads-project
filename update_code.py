print '''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body> '''
import cgi,config
import check_cookie
frm=cgi.FieldStorage()
pname=frm.getvalue('pname')
pkey=frm.getvalue('pkey')
pprice=frm.getvalue('pprice')
User_id = check_cookie.lst[0]

try:
    cursor=config.db.cursor()
    upd="UPDATE post_table SET pname='{}',pkey='{}',pprice='{}' WHERE User_id='{}'".format(pname,pkey,pprice,User_id)
    if cursor.execute(upd):
        config.db.commit()
        config.db.close()
        print"""
                <html>
                       <body>
                         <script>
                         window.location='view_posts.py?msg=Update sucessful'
                            </script>
                        </body>
                        </html>     """

except Exception as e:
    print """ <html>
                <body>
                    <script>
                       window.location='view_posts.py?msg=Update unsuccessful'
                    </script>
                </body>
            </html>"""
print '''</body>
</html>'''

