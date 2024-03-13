class Movie:
    def __init__(self, title, actor, actress):
        self.title = title
        self.actor = actor 
        self.actress = actress
    
    def info(self):
        print("Movie name: ", self.title)
        print("Actor name:", self.actor)
        print("Actress name: ", self.actress)

list_of_movies = []
while True:
    title = input("Enter the title of the movie: ")
    lead_actor = input("Enter the actor name: ")
    lead_actress = input("Enter the actress name: ")
    m = Movie(title, lead_actor, lead_actress)
    list_of_movies.append(m) 
    print("Movie added to the list successfully")
    option = input("Do you want to add one more movie: [Yes/No]: ")
    if option.lower() == "no":
        break

print("All movies information")
print("#" * 40)
for movie in list_of_movies:
    movie.info()

