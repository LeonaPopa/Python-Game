import unittest
from unittest.mock import Mock

from service.service import Service


class TestService(unittest.TestCase):
    def test_valid(self):
        repository = Mock()
        repository.get_value.return_value = 0
        service = Service(repository, 10)
        self.assertTrue(service.valid(5, 5))

        repository.get_value.return_value = 1
        self.assertFalse(service.valid(5, 5))

    def test_game_complete(self):
        repository = Mock()
        repository.get_value.return_value = 0
        service = Service(repository, 10)
        self.assertFalse(service.game_complete())

        repository.get_value.return_value = 1
        self.assertTrue(service.game_complete())

    def test_display_game(self):
        repository = Mock()
        repository.get_value.side_effect = [1, 0, 0, 0, 1, 0, 0, 0, 1]
        service = Service(repository, 3)
        # Verify output of display_game method
        # Output should be:

        #    | 1 | 2 | 3 |
        # -----------------
        # A  | x |   |   |
        # -----------------
        # B  | x |   |   |
        # -----------------
        # C  | x |   |   |
        # -----------------

    def test_add_value_to_grid(self):
        repository = Mock()
        service = Service(repository, 10)
        service.add_value_to_grid(5, 5, 'x')
        repository.add_value_to_grid.assert_called_with(5, 5, 'x')

    def test_make_gray_part(self):
        repository = Mock()
        service = Service(repository, 10)
        service.make_gray_part(5, 5)
        repository.make_gray_part.assert_called_with(5, 5)

    def test_computer_response(self):
        repository = Mock()
        repository.get_value.return_value = 0
        service = Service(repository, 10)
        self.assertTrue(service.computer_response(False, None))
        repository.add_value_to_grid.assert_called_with(1, 1, "o")
        repository.make_gray_part.assert_called_with(1, 1)

        repository.reset_mock()
        repository.get_value.return_value = 1
        self.assertFalse(service.computer_response(False, None))
        repository.add_value_to_grid.assert_not_called()
        repository.make_gray_part.assert_not_called()

