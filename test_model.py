import unittest
from model import model

class Testmodel(unittest.TestCase):
    def test_add_movie(self):
        title =model(input())
        director = model(kk)
        year = model(2002)
        genre = model(horror)

        self.assertEqual(title, x)
        self.assertEqual(director, kk)
        self.assertEqual(year, 2002)
        self.assertEqual(genre, horror)

    def test_list_movies(self):
        title = model(x)
        director = model(kk)
        year = model(2002)
        genre = model(horror)

        self.assertEqual(quantity, 1)
    def test_find_title(self):
        search_title = model(x)

        self.assertEqual(director, kk)
        self.assertEqual(year, 2002)
        self.assertEqual(genre, horror)
    def test_find_director(self):
        search_director=model(kk)

        self.assertEqual(title, x)
        self.assertEqual(year, 2002)
        self.assertEqual(genre, horror)
    def test_find_genre(self):
        search_genre=model(horror)

        self.assertEqual(title, x)
        self.assertEqual(director, kk)
        self.assertEqual(year, 2002)

if __name__ == "__main__":
    unittest.main()













































































print("ok")