import datetime
categories = []

def setCategory(id, name, created_at):
    
    categories.append({
        "identifant": id, 
        "categorie" : name,
        "created at": created_at
    })
# end 

def getCategory(tags):
   for catg in tags:
       print(catg)
# end


aws = setCategory(1, "Amazon Web Server",  datetime.date.today().isoformat())
javascript = setCategory(2, "Javascript", None)

getCategory(categories)

