import csv

with open('movies.csv', 'wb') as csvfile:
    movie_writer = csv.writer(csvfile)
    # Write the headers to the file
    headers = ['Name', 'IMDB', 'ReleaseYear']
    movie_writer.writerow(headers)
    # Write two rows of movies
    movie_writer.writerow(["Top Gun", 6.8, 1986])
    movie_writer.writerow(["The Usual Suspects", 8.7, 1995])