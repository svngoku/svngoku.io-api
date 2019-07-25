import pymysql

# Etablit la connexion avec le serveur de bases de données
connexion = pymysql.connect(host='127.0.0.1',port=3306, user='root',passwd='root', db='mysql')

# cursor renvoie un objet curseur utilisable pour émettre des requetes MYSQL .
crs = connexion.cursor()

print("**** connexion au SGBD *****")

print("**** use database for API ****")
# use database query
crs.execute("USE svngokuApi;")

print("query executed")

crs.execute("SHOW tables;")
for unReg in crs:
    print(unReg, end=", ")