import pymysql

# Open database connection
db = pymysql.connect(host='10.151.129.23', port=3306, user='minds', passwd='ggoggoma', db='disa3',charset='utf8',autocommit=True)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT word FROM disa_mean WHERE id = 2769922")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database value : %s " % data)
# print("conn")

# disconnect from server
db.close()


