print "Content-type:text/html\r\n\r\n"
print '<!DOCTYPE HTML>'
print '<html>'
print '<head>'
print '<title>USER POSTS</title>'
print '</head>'
print '<body>'
import config, cgi, cgitb
frm = cgi.FieldStorage()
cursor = config.db.cursor()
id=frm.getvalue('User_id')
cursor.execute('SELECT * FROM post_table WHERE cat_id=1')
result = cursor.fetchall()
if result:

    print'''<table cellpadding="5" cellspacing="0" border="1">
        <thead>
            <tr>
            <th>pname</th>
            <th>pkey</th>
            <th>pprice</th>
            <th>pbrand</th>
            <th>Update</th>
            <th>Delete</th>
            </tr>

        </thead>
        <tbody>'''
    for j in result:
        print'''
                <tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td><a href="update.py?id={}"><img src="images2/b_edit.png"></a></td>
            <td><a href="delete.py?id={}"><img src="images2/b_drop.png"></a></td>
         </tr>'''.format(j[1],j[2], j[3], j[4],j[0],j[0])

    print'''
            </tbody>
            </table>'''
else:
    print "No data found"
print '''<a href="http://localhost:90/project/EXPO/ADMIN.html">Back to home</a>'''
print '</body>'
print '</html>'

