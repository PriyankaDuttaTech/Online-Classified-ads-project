import cgi,config
cursor = config.db.cursor()
frm = cgi.FieldStorage()
print ''' Content-type:text/html\r\n\r\n
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>file upload</title>
</head>

<body>
<form name="frm" method="post" action="upload_code.py" enctype="multipart/form-data">
    <table cellpadding="10">
        <tr>
            <td><mark>Product name</mark></td>
            <td><input type="text" name="pname" ></td>
        </tr>
         <tr>
            <td><mark>pkey</mark></td>
            <td><input type="text" name="pkey"></td>
        </tr>
        <tr>
            <td><mark>Product Price</mark></td>
            <td><input type="text" name="pprice"></td>        

        </tr>
        <tr>
            <td><mark>category</mark></td>
            <td colspan="2" align="center">
                <select name="cat_id">
                <option value="" selected>select category</option>'''
cursor.execute('SELECT * FROM category')
result = cursor.fetchall()
for rec in result:
    print '''<option value="{}">{}</option>'''.format(rec[0], rec[1])
print ''' </select>
            </td>

        </tr>


        <tr>
            <td><mark>Product Brand</mark></td>
            <td><input type="text" name="pbrand"></td>


        </tr>
        <tr>
            <td><mark>Approval</mark></td>
            <td><input type="text" name="approve"></td>


        </tr>
        <tr>
            <td><mark>pdate</mark></td>
            <td><input type="date" name="pdate"></td>        

        </tr>
        <tr>
            <td><mark>pimage</mark></td>
            <td><input type="file" name="file"></td>        

        </tr>
        <tr>
	        <td></td>
	        <td><input type="submit" name="Insert"></td>

        </tr>         
    </table>
</form>'''
if frm.getvalue('msg'):
    print frm.getvalue('msg')
print'''</body>
 </html>'''