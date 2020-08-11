import os
import Cookie
print "Content-type: text/html\r\n\r\n"
print """ 
<html> 
<body> 
"""
if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    c=Cookie.SimpleCookie()
    c.load(cookie_string)

    '''if(c['info1'].value):
        print 'cookie is present'''
    try:
        data=c['info1'].value
        lst = c['info1'].value.split(',')
        #print "cookie data: "+lst[0]+"<br>"

    except KeyError:
        print "The cookie was not set or has expired<br>"

else:
    print''' 
    <script> window.location='index1.py?msg=Please login yourself' 
    </script>'''
print """ 
</body> 
</html> """