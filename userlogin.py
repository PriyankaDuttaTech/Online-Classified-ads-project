import cgi
import config
frm=cgi.FieldStorage()
email=frm.getvalue('email')
Password=frm.getvalue('Password')
cursor=config.db.cursor()
cursor.execute("SELECT * FROM userdata WHERE email='{}' AND Password='{}'".format(email,Password))
r=cursor.fetchall()
if r:
    import Cookie
    c=Cookie.SimpleCookie()
    for j in r:
        c['info1']=j[0]
    c['info1']['expires']=60*60*24
    print c
    print "Content-type:text/html\n"

    print"""
    <html>
        <body>
        <script>
            window.location='view_data1.html?msg=Login sucessful'
        </script>
        </body>
    </html>"""
else:
    print"""
    <html>
        <body>
        <script>
            window.location = 'index1.py?msg=Login error'
        </script>
        </body>
    </html>"""


