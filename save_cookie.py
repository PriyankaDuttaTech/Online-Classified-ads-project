import Cookie
c=Cookie.SimpleCookie() #create the cookie
value=['Hello','World'] #assign a value to the cookie
c['sss']=value
c['sss']['expires']=60*60*24 #set the expiry time
#print the header starting with the cookie
print c
print "Content-type: text/html\n"
print "" #empty lines so that the browser knows what the header is
print ""
print '''
<html>
<body>
    <h1>Cookie has been set</h1>
</body>
</html>'''
