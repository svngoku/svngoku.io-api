import pymysql

# connect établit la connexion avec le serveur de bases de données
connexion = pymysql.connect(host='127.0.0.1',port=3306, user='root',passwd='root', db='mysql')

# cursor renvoie un objet curseur utilisable pour émettre des requetes MYSQL .
crs = connexion.cursor()

print("**** connexion au SGBD *****")
print("**** liste des différentes base de données")

crs.execute("SHOW DATABASES")
for unReg in crs:
    print(unReg, end=", ")