class anime:
    def __init__(self,name,category,ratings):
        self.__name=name
        self.__category=category
        self.__ratings=ratings

    def display(self):
        print(f"Anime name : {self.__name} \nGenre : {self.__category} \nRatings : {self.__ratings}")

class series(anime):
    def __init__(self, name, category, ratings,episodes):
        super().__init__(name, category, ratings)
        self.__episodes=episodes

    def display(self):
        super().display()
        print(f"Total episodes : {self.__episodes} \n")


s1=series("One Piece","Adventure",9.9,1155)
s2=series("Demon Slayer","Horror",9.7,60)
s3=series("My Hero Academia","Action",9.8,120)

s1.display()
s2.display()
s3.display()

