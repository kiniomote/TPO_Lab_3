import os


class PathStorageService:
    def __init__(self):
        self.valid_paths = []
        self.invalid_paths = []

    def add_path(self, path):
        """ Add path to array """
        result_validation = self._validation_path(path)
        strip_path = path.strip()
        if result_validation:
            self.valid_paths.append(strip_path)
            return True
        else:
            self.invalid_paths.append(strip_path)
            return False

    def _validation_path(self, path):
        """ Return true if path is valid """
        if path.strip() is '':
            raise ValueError('Пустая строка!')
        return True if os.path.exists(path.strip()) else False

    def delete_valid_path(self, path):
        """ Delete path from array valid_paths """
        strip_path = path.strip()
        if strip_path in self.valid_paths:
            self.valid_paths.remove(strip_path)
        else:
            return False

    def delete_invalid_path(self, path):
        """ Delete path from array invalid_paths """
        strip_path = path.strip()
        if strip_path in self.invalid_paths:
            self.invalid_paths.remove(strip_path)
        else:
            return False

    def transport_path_to_invalid(self, path):
        """ Transport path from array valid_paths to invalid_paths """
        strip_path = path.strip()
        if strip_path in self.valid_paths:
            self.invalid_paths.append(strip_path)
            self.valid_paths.remove(strip_path)
        else:
            return False

    def pop_path_from_invalid(self, path):
        """ Return path from array invalid_paths and delete """
        strip_path = path.strip()
        if strip_path is '':
            raise ValueError('Вы не выбрали строку для повторной проверки!')
        if strip_path in self.invalid_paths:
            self.invalid_paths.remove(strip_path)
            return strip_path
        else:
            return False
