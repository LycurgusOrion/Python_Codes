import cx_Oracle as ox

conn = ox.connect("ADMIN/q2GWExrEGYz9JKM@db201902191526_low")

print(conn.version)

conn.close()