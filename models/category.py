categories = []

def setCategory(id, name):
    categories.append({
        "identifant": id, 
        "categorie" : name
    })


def getCategory(tags):
   for catg in tags:
       print(catg)


aws = setCategory(1, "Amazon Web Server")
javascript = setCategory(2, "Javascript")

getCategory(categories)

