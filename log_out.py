import Cookie
import cgi # set the cookie to expire
c=Cookie.SimpleCookie()
c['info1']=''
c['info1']['expires']=60*60*0
#print the HTTP header
print c
print "Content-type: text/html\n\n"
print """ 
<html> 
<body>
    <script> window.location='index1.py?msg=Logout sucessfully' 
    </script>
</body> 
</html> """

