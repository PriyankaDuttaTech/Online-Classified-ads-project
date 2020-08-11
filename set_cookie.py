import os
import Cookie
print '''
<html>
<body>
    <h1>Check the cookie</h1>'''
if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    c=Cookie.SimpleCookie()
    c.load(cookie_string)
    if (c['sss'].value):
        print "COOKIE ACHE KINTU DEKHABO NAA<br>"
    try:
        data=c['sss'].value
        lst=c['sss'].value.split(',')
        print "COOKIE DATA: "+lst[0]+"<br>"
    except KeyError:
        print "THE COOKIE IS NOT SET OR EXPIRED<br>"
else:
    print 'NOT PRESENT'
print '''
</body>
</html>'''