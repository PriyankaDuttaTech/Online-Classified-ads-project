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
id = frm.getvalue('User_id')
cursor.execute('SELECT u.*,p.* FROM userdata u INNER JOIN post_table p ON u.User_id=p.User_id')
result = cursor.fetchall()
if result:

    print'''<table cellpadding="5" cellspacing="0" border="1">
        <thead>
            <tr>
            <th>pname</th>
            <th>pkey</th>
            <th>pprice</th>
            <th>pfile</th>
            <th>pbrand</th>
            <th>pdate</th>
            
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
                <td>{}</td>
                <td>{}</td>

         </tr>'''.format(j[1], j[2], j[3], j[4], j[5], j[6])

    print'''
            </tbody>
            </table>'''
else:
    print "No data found"
print '''<a href="http://localhost:63342/project/tryprtoject/index.html?_ijt=ljea5bpj65av2e5egbophmuelr">Back to home</a>'''
print '</body>'
print '</html>'

