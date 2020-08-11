import cgi
frm=cgi.FieldStorage();
print '''Content-type:text/html\r\n\r\n
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>File Uploading</title>
</head>

<body>
<form name="frm" method="post" action="upload_code.py" enctype="multipart/form-data">
<table cellpadding="10">
<tr>
	<td>Select File</td>
    <td><input type="file" name="file"></td>
</tr>
	<td><input type="submit" name="ok" value="Upload"></td>
</tr>
</table>
</form>'''
if frm.getvalue('msg'):
    print frm.getvalue('msg')
print'''</body>
</html>'''
