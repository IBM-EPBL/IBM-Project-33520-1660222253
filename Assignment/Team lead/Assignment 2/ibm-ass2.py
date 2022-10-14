import ibm_db

hostname="b0aebb68-94fa-46ec-a1fc-1c999edb6187.c3n41cmd0nqnrk39u98g.databases.appdomain.clo
uid="dqy22047"
pwd="acnIjckvjcWkruJe"
driver="{IBM DB2 ODBC DRIVER}"
db="bludb"
port="31249"
protocol="TCPIP"
cert="certificate.crt"

dsn=(
    "DRIVER = {0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "UID={4};"
    "SECURITY=SSL;"
    "SSLServercertificate={5};"
    "PWD={6};"
).format(db,hostname,port,uid,cert,pwd,driver,protocol)
print(dsn)
try:
    db2=ibm_db.connect(dsn,"","")
    print("connectd to database")
except:
    print("unable to connect",ibm_db.conn_errormsg())

