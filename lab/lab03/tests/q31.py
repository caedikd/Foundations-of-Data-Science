test = {
  'name': 'q31',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(top_10_movies) == tables.Table
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> top_10_movies.select('Rating', 'Name')
          Rating | Name
          9.2    | The Shawshank Redemption (1994)
          9.2    | The Godfather (1972)
          9      | The Godfather: Part II (1974)
          8.9    | Pulp Fiction (1994)
          8.9    | Schindler's List (1993)
          8.9    | The Lord of the Rings: The Return of the King (2003)
          8.9    | 12 Angry Men (1957)
          8.9    | The Dark Knight (2008)
          8.9    | Il buono, il brutto, il cattivo (1966)
          8.8    | The Lord of the Rings: The Fellowship of the Ring (2001)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
