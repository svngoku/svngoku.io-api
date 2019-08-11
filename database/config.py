import pymysql

# Etablit la connexion avec le serveur de bases de données
connexion = pymysql.connect(host='127.0.0.1',port=3306, user='root',passwd='root', db='mysql')

# cursor renvoie un objet curseur utilisable pour émettre des requetes MYSQL .
crs = connexion.cursor()

# use required database
crs.execute("USE svngokuApi;")

print("query executed")

# func to show articles 
def showArticles():
    crs.execute("SELECT * FROM article;")
    for article in crs.fetchall():
        return article

# end