import unittest
import life_game
import os


class TestLifeGame(unittest.TestCase):
    filename = 'parameters.json'
    visibility_parameter = False

    def test_visibility_type(self):
        life_obj = life_game.Life(self.filename, self.visibility_parameter)
        self.assertIsInstance(life_obj._visibility, bool)

    def test_length_type(self):
        life_obj = life_game.Life(self.filename, self.visibility_parameter)
        self.assertIsInstance(life_obj._length, int)

    def test_width_type(self):
        life_obj = life_game.Life(self.filename, self.visibility_parameter)
        self.assertIsInstance(life_obj._width, int)

    def test_the_beginnings_of_life_type(self):
        life_obj = life_game.Life(self.filename, self.visibility_parameter)
        self.assertIsInstance(life_obj._the_beginnings_of_life, list)

    def test_generation_type(self):
        life_obj = life_game.Life(self.filename, self.visibility_parameter)
        self.assertIsInstance(life_obj._generation, list)

    def test_live_cell_type(self):
        life_obj = life_game.Life(self.filename, self.visibility_parameter)
        self.assertIsInstance(life_obj._live_cell, str)

    def test_visibility_value(self):
        life_obj = life_game.Life(self.filename, self.visibility_parameter)
        self.assertEqual(life_obj._visibility, self.visibility_parameter)

    def test_size_generation(self):
        life_obj = life_game.Life(self.filename, self.visibility_parameter)
        self.assertEqual(len(life_obj._generation), life_obj._width)

    def test_empty_field_generator(self):
        # field must be empty on first iteration
        life_obj = life_game.Life(self.filename, self.visibility_parameter)
        for line in life_obj._get_empty_field():
            self.assertNotIn(life_obj._live_cell, line)

    def test_end_game(self):
        # condition of over the game is zero life cells
        life_obj = life_game.Life(self.filename, self.visibility_parameter)
        life_obj._generation = life_obj._get_empty_field()
        life_obj._end_game()
        self.assertEqual(life_obj._end_game(), True)

    def test_generation_generator(self):
        # next generation must be different
        life_obj = life_game.Life(self.filename, self.visibility_parameter)
        self.assertNotEqual(
            life_obj._generation, life_obj._get_next_generation()
        )

    def test_file_result_create(self):
        files_first = os.listdir(path='.')
        life_obj = life_game.Life(self.filename, self.visibility_parameter)
        life_obj.life_itself()
        files_second = os.listdir(path='.')
        self.assertIsNot(files_first, files_second)
        file_to_delete = list(set(files_first) ^ set(files_second))
        os.remove(file_to_delete[0])


if __name__ == '__main__':
    unittest.main()
