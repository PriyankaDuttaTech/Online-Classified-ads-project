print '''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>BLOCKED POST</title>
</head>
<body>'''
import cgi, config
frm = cgi.FieldStorage()
id = frm.getvalue('id')

try:
    cursor = config.db.cursor()
     #function which is used to execute the sql query written as a string
     #config to save the retieve data
    sql = "DELETE FROM std WHERE id = {}".format(id)
    if cursor.execute(sql):
        config.db.commit()
        config.db.close()
        #print 'DELETE Successful'
        print '''
        <script>
        window.location='view_data.py?msg=DELETE SUCCESSFUL'
        </script>'''
except Exception as e :
    print e
print '''</body>
</html>'''
