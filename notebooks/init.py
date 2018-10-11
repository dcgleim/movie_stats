# section 1 functions
import ast

def movie_is_comedy(genre_json):
    genre_data= ast.literal_eval(genre_json)
    for genre in list(genre_data):
        if genre['name'] == 'Comedy':
            return 1
    return 0

# section 2 functions - fun with json and multi-value columns
import json

def json_pluck(arr, key):
    """ map values in json at `key` to a sorted list. """
    return [sorted([r[key] for r in json.loads(d)]) for d in arr]

DEFAULT_COLUMNS_PLUCK = dict(
    genres='name',
    keywords='name',
    production_companies='name',
    production_countries='iso_3166_1',
    spoken_languages='iso_639_1'
)

def parse_movie_df_json(df, **columns_pluck):
    """ map json colums in `columns_pluck` to a flat list of sorted values. """
    columns_pluck = columns_pluck or DEFAULT_COLUMNS_PLUCK
          
    for column, pluck in columns_pluck.items():
        df[column] = json_pluck(df[column].values, pluck)
    
    return df

def _norm_cols(col, vals):
    """ Helper used by contains to normalize field arguments. """
    expect = True
    if col.startswith('not_'):
        expect = False
        col = col[4:]
    
    if type(vals) is not tuple:
        vals = [vals]
    
    return expect, col, vals

def contains(df, **cols):
    """
    `apply` a test to a dataframe, based on columns containing given values.
    
    Columns defined by `cols` may be prefixed with `not_` to reverse test,
    and each column may be assigned to a single value, or tuple of values.
    
    Example:
    
    contains(df_movies,
         genres=('Crime', 'Thriller'),
         not_genres='Action',
         production_countries='GB')
    """
    cols = [_norm_cols(col, vals) for col, vals in cols.items()]

    def tester(r):
        for expect, col, vals in cols:
            for v in vals:
                if expect != (v in r[col]):
                    return False
        return True

    return df.apply(tester, axis=1)
   
# section 3 functions

# section 4 functions

# section 5 functions

# section 6 functions

# section 7 functions

# sections 8 functions

# sections 9 functions

# sections 10 functions