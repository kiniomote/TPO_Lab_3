from PyQt5.QtWidgets import QMessageBox


def show_message_error(function):
    """ Show message for user if function raise Exception """
    def catch_error(self):
        try:
            function(self)
        except Exception as error:
            self.message_box = QMessageBox()
            self.message_box.setIcon(QMessageBox.Critical)
            self.message_box.setWindowTitle('Ошибка')
            self.message_box.setText(error.__str__())
            self.message_box.setStandardButtons(QMessageBox.Ok)
            self.message_box.show()
    return catch_error
