import config
import check_cookie
import cgi
frm = cgi.FieldStorage()

cat_id=frm.getvalue('cat_id')
pname=frm.getvalue('pname')
pkey=frm.getvalue('pkey')
pprice=frm.getvalue('pprice')
pbrand=frm.getvalue('pbrand')
pdate=frm.getvalue('pdate')
approve=frm.getvalue('approve')


try:
    User_id = check_cookie.lst[0]

    cursor=config.db.cursor()

    r="INSERT INTO post_table (pname,pkey,pprice,pbrand,pdate,cat_id,User_id,approve) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" %(pname,pkey,pprice,pbrand,pdate,cat_id,User_id,approve)
    if cursor.execute(r):
        config.db.commit()
        config.db.close()
        r=cursor.fetchall()
        print"""
               <html>
               <body>
                 <script>
                 window.location='productinsertion.py?msg=Login sucessful'
                    </script>
                </body>
                </html>     """

except Exception as e:
    print"""
            <html>
                <body>
                    <script>
                       window.location='productinsertion.py?msg=Insertion unsuccessful'
                    </script>
                </body>
            </html>"""

