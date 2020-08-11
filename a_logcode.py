import cgi
import config
frm=cgi.FieldStorage()
a_mail=frm.getvalue('a_mail')
a_pass=frm.getvalue('a_pass')
cursor=config.db.cursor()
cursor.execute("SELECT * FROM admin WHERE a_mail='{}' AND a_pass='{}'".format(a_mail,a_pass))
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
            window.location='ADMIN.html?msg=Logout sucessful'
        </script>
        </body>
    </html>"""
else:
    print"""
    <html>
        <body>
        <script>
            window.location = 'a_login.py?msg=Login error'
        </script>
        </body>
    </html>"""


