import MySQLdb
import sys
try:
    db=MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='data')
except Exception as e:
    sys.exit(e)