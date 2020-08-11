print "Content-type:text/html\r\n\r\n"
print '<!DOCTYPE HTML>'
print '<html>'
print '<head>'
print '<title>User Registration Form</title>'
print '</head>'
print '<body>'
import cgi,cgitb,config
frm=cgi.FieldStorage()
F_name=frm.getvalue('F_name')
L_name=frm.getvalue('L_name')
Password=frm.getvalue('Password')
Address=frm.getvalue('Address')
mobile=frm.getvalue('mobile')
city=frm.getvalue('city')
pin=frm.getvalue('pin')
email=frm.getvalue('email')

try:
    cursor=config.db.cursor()
    #cursor is function which is used to execute the SQL query written as a string
# config to save the retrieve data
    #to close connectivity of database
    sql="INSERT INTO userdata (F_name,L_name,Password,Address,mobile,city,pin,email) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" %(F_name,L_name,Password,Address,mobile,city,pin,email)
    if cursor.execute(sql):
        config.db.commit()
        config.db.close()
        print '''<script>
               window.location="index1.py?msg=Registration successfull"
               </script>
               '''
except Exception as e:
    print '''<script>
                   window.location="index1.py?msg=Registration unsuccessfull"
                   </script> '''



print '</body>'
print'</html>'
