# !/usr/bin/python
print '''content-type:text/html\r\n\r\n'''
import cgi, os
import cgitb; cgitb.enable()
import config
import check_cookie
try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

form = cgi.FieldStorage()

# Generator to buffer file chunks
def fbuffer(f, chunk_size=10000):
    while True:
        chunk = f.read(chunk_size)
        if not chunk: break
        yield chunk

# A nested FieldStorage instance holds the file
fileitem = form['file']

User_id = check_cookie.lst[0]

cat_id=form.getvalue('cat_id')
pname=form.getvalue('pname')
pkey=form.getvalue('pkey')
pprice=form.getvalue('pprice')
pbrand=form.getvalue('pbrand')
pdate=form.getvalue('pdate')
approve=form.getvalue('approve')
# Test if the file was uploaded
if fileitem.filename:

    # strip leading path from file name to avoid directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    # print fn
    fpath ='images2/' + fn
    f = open('project/' + fpath, 'wb', 10000)

    # Read the file in chunks
    for chunk in fbuffer(fileitem.file):
        f.write(chunk)
    f.close()
    cursor =config.db.cursor()
    sql ="INSERT INTO post_table (pname,pkey,pprice,pbrand,pdate,cat_id,User_id,approve,fpath)VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(pname,pkey,pprice,pbrand,pdate,cat_id,User_id,approve,fpath)
    if cursor.execute(sql):
        config.db.commit()
        config.db.close()
        print '''<script>
            window.location='productinsertion.py?msg=file upload successfully'
            </script>'''
    # message = 'The file "' + fn + '" was uploaded successfully'

else:
    print '''<script>
            window.location='productinsertion.py?msg=file not upload successfully'
            </script>'''