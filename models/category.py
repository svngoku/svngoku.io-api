categories = []
   

def setCategory(id, name):
    categories.append({id, name})


def getCategory(tags):
   for catg in tags:
       print(catg)


aws = setCategory(1, "Amazon Web Server")

getCategory(categories)

