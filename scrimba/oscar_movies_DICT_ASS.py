oscar_movies={
    'title':['MahaAvtar Narsimha','Dashavtar','Kalki','Kantara'],
    'release':[2025,2024,2023,2020],
    'budget':[100,20,300,16]
}
# First method
# for i,title in enumerate(oscar_movies['title']):
#     print(f"Title: {title} , Release : {oscar_movies['release'][i]} , Budget : {oscar_movies['budget'][i]} Cr")
    
# Second method
# for title, release, budget in zip(
#     oscar_movies['title'],oscar_movies['release'],oscar_movies['budget']
# ):
#     print(f"\nFilm No : {i} ")
#     print(f"Title: {title} ")
#     print(f" Release : {release}")
#     print(f" Budget : {budget} Cr")\
    
 # Third method   
    
for i,(title,release,budget) in enumerate(zip(
   oscar_movies['title'],
   oscar_movies['release'],
   oscar_movies['budget']),
   start=1):  
    print(f"Film Number : {i}")
    print(f"Title : {title}")
    print(f"Release : {release}")
    print(f"Budget : {budget} Cr")
    
print('\n\n\n')
oscar_movies['cast']=['Bhakt Prahlad','Babuli kaka','Prabhas','Rishabh Shetty']
# print(oscar_movies)
for i,(title,release,budget,cast) in enumerate(zip(
   oscar_movies['title'],
   oscar_movies['release'],
   oscar_movies['budget'],
   oscar_movies['cast']),
   start=1):  
    print(f"Film Number : {i}")
    print(f"Title : {title}")
    print(f"Casts : {cast}")
    print(f"Release : {release}")
    print(f"Budget : {budget} Cr")
    # print(f"Casts : {cast}")
    print('\n\n')


oscar_movies['cast'][1]='Dilip Prabhavalkar'
print(oscar_movies)

# del oscar_movies['cast']   #use to delete a key value pair
# casts=oscar_movies.pop('cast')
# print(casts)
print(oscar_movies)
print(len(oscar_movies))
print(oscar_movies.keys())
print(oscar_movies.values())
print(oscar_movies.items())

