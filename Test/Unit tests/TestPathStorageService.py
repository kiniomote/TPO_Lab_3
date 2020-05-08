import unittest
from Services.PathStorageService import PathStorageService


class TestPathStorageService(unittest.TestCase):
    """ Unit-tests for module PathStorageService.py """

    @classmethod
    def setUpClass(cls):
        cls.valid_path = 'C:/Windows'
        cls.valid_path_not_found = 'C:/Program Files'
        cls.invalid_path = 'C:/4SSSS'
        cls.invalid_path_not_found = 'C:/t1351'
        cls.empty_path = ''

    def setUp(self):
        self.storage = PathStorageService()

    def test_add_valid_path(self):
        """ Test adding valid path to storage """
        self.storage.add_path(self.valid_path)
        self.assertIn(self.valid_path, self.storage.valid_paths)

    def test_add_invalid_path(self):
        """ Test adding invalid path to storage """
        self.storage.add_path(self.invalid_path)
        self.assertIn(self.invalid_path, self.storage.invalid_paths)

    @unittest.expectedFailure
    def test_add_empty_string(self):
        """ Test attempting to add empty string to storage """
        self.assertRaises(ValueError, self.storage.add_path(self.empty_path))

    def test_delete_valid_path(self):
        """ Test removing valid path from storage """
        self.storage.add_path(self.valid_path)
        self.storage.delete_valid_path(self.valid_path)
        self.assertNotIn(self.valid_path, self.storage.valid_paths)

    def test_delete_valid_path_not_found(self):
        """ Test attempting to remove valid path from storage if path is absent """
        self.assertEqual(self.storage.delete_valid_path(self.valid_path), False)

    def test_delete_invalid_path(self):
        """ Test removing invalid path from storage """
        self.storage.add_path(self.invalid_path)
        self.storage.delete_invalid_path(self.invalid_path)
        self.assertNotIn(self.invalid_path, self.storage.invalid_paths)

    def test_delete_invalid_path_not_found(self):
        """ Test attempting to remove invalid path from storage if path is absent """
        self.assertEqual(self.storage.delete_invalid_path(self.invalid_path), False)

    def test_transport_path_to_invalid(self):
        """ Test transporting valid path from valid_paths to invalid_paths storage """
        self.storage.add_path(self.valid_path)
        self.storage.transport_path_to_invalid(self.valid_path)
        not_in_valid = True if self.valid_path not in self.storage.valid_paths else False
        in_invalid = True if self.valid_path in self.storage.invalid_paths else False
        self.assertEqual(True, not_in_valid, in_invalid)

    def test_transport_path_to_invalid_not_found(self):
        """ Test attempting to transport valid path from valid_paths to invalid_paths storage if path is absent """
        self.assertEqual(False, self.storage.transport_path_to_invalid(self.valid_path))

    def test_pop_invalid_path(self):
        """ Test taking invalid path from invalid_paths storage """
        self.storage.add_path(self.invalid_path)
        is_path = True if self.storage.pop_path_from_invalid(self.invalid_path) is self.invalid_path else False
        not_in_invalid = True if self.invalid_path not in self.storage.invalid_paths else False
        self.assertEqual(True, is_path, not_in_invalid)

    @unittest.expectedFailure
    def test_pop_invalid_empty_path(self):
        """ Test attempting to take empty string to storage """
        self.assertRaises(ValueError, self.storage.pop_path_from_invalid(self.empty_path))
