class Languages:
    def __init__(self,title,stars,language, link, resume,className):
        self.title = title
        self.stars = stars
        self.language = language
        self.link = link
        self.resume = resume
        self.className = className
        # 
        self.data = []
    
    def getLanguage(self):
        return str("title:" +  self.title) 
    
    @staticmethod
    def Addlanguage(self, lng):
        self.data.append(lng)


