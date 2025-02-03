def average_imdb(category):
    total_score = 0
    count = 0
    for movie in movies:
        if movie["category"] == category:
            total_score += movie["imdb"]
            count += 1
    if count == 0:
        return 0
    return total_score / count
# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

category = "Romance" 
print("The average IMDB score for", category, "movies is", average_imdb(category))
category = "Action"
print("The average IMDB score for", category, "movies is", average_imdb(category))
category = "Thriller"
print("The average IMDB score for", category, "movies is", average_imdb(category))
category = "Drama"
print("The average IMDB score for", category, "movies is", average_imdb(category))
category = "Adventure"
print("The average IMDB score for", category, "movies is", average_imdb(category))
category = "Suspense"
print("The average IMDB score for", category, "movies is", average_imdb(category))
category = "Crime"
print("The average IMDB score for", category, "movies is", average_imdb(category))