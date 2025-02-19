from datetime import datetime
# Create favorite movies list
siteWhereSource:r"https://www.imdb.com/user/ur189045662/watchlist/"
favourite_movies = [
    {
        "title": "Inception",
        "year": 2010,
        "rating": 8.8,
        "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
        "directors": ["Christopher Nolan"],
        "writers": ["Christopher Nolan"],
        "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
        "genres": ["Action", "Adventure", "Sci-Fi"]
    },
    {
        "title": "The Matrix",
        "year": 1999,
        "rating": 8.7,
        "description": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
        "directors": ["Lana Wachowski", "Lilly Wachowski"],
        "writers": ["Lana Wachowski", "Lilly Wachowski"],
        "actors": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"],
        "genres": ["Action", "Sci-Fi"]
    },
    {
        "title": "Interstellar",
        "year": 2014,
        "rating": 8.6,
        "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
        "directors": ["Christopher Nolan"],
        "writers": ["Jonathan Nolan", "Christopher Nolan"],
        "actors": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"],
        "genres": ["Adventure", "Drama", "Sci-Fi"]
    },
    {
        "title": "The Dark Knight",
        "year": 2008,
        "rating": 9.0,
        "description": "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.",
        "directors": ["Christopher Nolan"],
        "writers": ["Jonathan Nolan", "Christopher Nolan"],
        "actors": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
        "genres": ["Action", "Crime", "Drama"]
    }
]

print(favourite_movies)

# Display the required pieces of data
print("Title of the first movie:", favourite_movies[0]["title"])
print("Year of the second movie:", favourite_movies[1]["year"])
print("Rating of the third movie:", favourite_movies[2]["rating"])
print("Description of the fourth movie:", favourite_movies[3]["description"])

# Display the required pieces of data with context
print("The title of the first movie is:", favourite_movies[0]["title"])
print("The release year of the second movie is:", favourite_movies[1]["year"])
print("The IMDB rating of the third movie is:", favourite_movies[2]["rating"])
print("The short description of the fourth movie is:", favourite_movies[3]["description"])

# Display the required pieces of new data with context
print("The lead director of the first movie is:", favourite_movies[0]["directors"][0])
print("The lead writer of the second movie is:", favourite_movies[1]["writers"][0])
print("The lead star of the third movie is:", favourite_movies[2]["actors"][0])
print("The main genre of the fourth movie is:", favourite_movies[3]["genres"][0])

# Calculate the average rating
total_rating = sum(movie["rating"] for movie in favourite_movies)
average_rating = total_rating / len(favourite_movies)

print("The average rating of the movies is:", average_rating)

# Calculate the average rating
total_rating = sum(movie["rating"] for movie in favourite_movies)
average_rating = total_rating / len(favourite_movies)

print("The average rating of the movies is:", average_rating)






