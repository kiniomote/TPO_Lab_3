from PyQt5 import QtCore, QtWidgets, QtGui
from Views import FilePathTesterWindow
from Services.PathStorageService import PathStorageService
from Services.QtMessageErrorService import show_message_error
import sys


class FilePathTesterViewModel(QtWidgets.QWidget, FilePathTesterWindow.Ui_FilePathTesterForm):
    def __init__(self, parent=None):
        super(FilePathTesterViewModel, self).__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
        self._file_path_tester = PathStorageService()
        self.message_box = None

        # Events
        self.add_button.clicked.connect(self._add_path)
        self.delete_valid_path_button.clicked.connect(self._delete_valid_path)
        self.transport_button.clicked.connect(self._transport_path)
        self.delete_invalid_path_button.clicked.connect(self._delete_invalid_path)
        self.return_button.clicked.connect(self._return_invalid_path)

    @show_message_error
    def _add_path(self):
        """ Click on add_button """
        if self._file_path_tester.add_path(self.path_line_edit.text()) is True:
            self.list_valid_paths.addItem(self.path_line_edit.text())
        else:
            self.list_invalid_paths.addItem(self.path_line_edit.text())
        self.path_line_edit.setText('')

    def _delete_valid_path(self):
        """" Click on delete_valid_path_button """
        if self.list_valid_paths.currentItem() is None:
            return
        if self._file_path_tester.delete_valid_path(self.list_valid_paths.currentItem().text()) is False:
            return
        self.list_valid_paths.takeItem(self.list_valid_paths.currentRow())

    def _transport_path(self):
        """" Click on transport_button """
        if self.list_valid_paths.currentItem() is None:
            return
        if self._file_path_tester.transport_path_to_invalid(self.list_valid_paths.currentItem().text()) is False:
            return
        self.list_invalid_paths.addItem(self.list_valid_paths.currentItem().text())
        self.list_valid_paths.takeItem(self.list_valid_paths.currentRow())

    def _delete_invalid_path(self):
        """" Click on delete_invalid_path_button """
        if self.list_invalid_paths.currentItem() is None:
            return
        if self._file_path_tester.delete_invalid_path(self.list_invalid_paths.currentItem().text()) is False:
            return
        self.list_invalid_paths.takeItem(self.list_invalid_paths.currentRow())

    @show_message_error
    def _return_invalid_path(self):
        """" Click on return_button """
        if self.list_invalid_paths.currentItem() is None:
            current_item = ''
        else:
            current_item = self.list_invalid_paths.currentItem().text()
        path = self._file_path_tester.pop_path_from_invalid(current_item)
        if path is False:
            return
        self.path_line_edit.setText(path)
        self.list_invalid_paths.takeItem(self.list_invalid_paths.currentRow())


def show_window():
    app = QtWidgets.QApplication(sys.argv)
    window = FilePathTesterViewModel()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    show_window()
