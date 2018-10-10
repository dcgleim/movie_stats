# section 1 functions
import ast

def movie_is_comedy(genre_json):
    genre_data= ast.literal_eval(genre_json)
    for genre in list(genre_data):
        if genre['name'] == 'Comedy':
            return 1
    return 0

# section 2 functions

# section 3 functions

# section 4 functions

# section 5 functions

# section 6 functions

# section 7 functions

# sections 8 functions

# sections 9 functions

# sections 10 functions