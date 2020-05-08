# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\S\C#\TPO\Lab_3\Ui\FilePathTesterWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FilePathTesterForm(object):
    def setupUi(self, FilePathTesterForm):
        FilePathTesterForm.setObjectName("FilePathTesterForm")
        FilePathTesterForm.resize(430, 280)
        self.gridLayout = QtWidgets.QGridLayout(FilePathTesterForm)
        self.gridLayout.setObjectName("gridLayout")
        self.path_line_edit = QtWidgets.QLineEdit(FilePathTesterForm)
        self.path_line_edit.setObjectName("path_line_edit")
        self.gridLayout.addWidget(self.path_line_edit, 0, 1, 1, 3)
        self.add_button = QtWidgets.QPushButton(FilePathTesterForm)
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 0, 4, 1, 1)
        self.delete_valid_path_button = QtWidgets.QPushButton(FilePathTesterForm)
        self.delete_valid_path_button.setObjectName("delete_valid_path_button")
        self.gridLayout.addWidget(self.delete_valid_path_button, 2, 1, 1, 1)
        self.transport_button = QtWidgets.QPushButton(FilePathTesterForm)
        self.transport_button.setObjectName("transport_button")
        self.gridLayout.addWidget(self.transport_button, 2, 2, 1, 1)
        self.delete_invalid_path_button = QtWidgets.QPushButton(FilePathTesterForm)
        self.delete_invalid_path_button.setObjectName("delete_invalid_path_button")
        self.gridLayout.addWidget(self.delete_invalid_path_button, 2, 3, 1, 1)
        self.return_button = QtWidgets.QPushButton(FilePathTesterForm)
        self.return_button.setObjectName("return_button")
        self.gridLayout.addWidget(self.return_button, 2, 4, 1, 1)
        self.list_invalid_paths = QtWidgets.QListWidget(FilePathTesterForm)
        self.list_invalid_paths.setObjectName("list_invalid_paths")
        self.gridLayout.addWidget(self.list_invalid_paths, 1, 3, 1, 2)
        self.list_valid_paths = QtWidgets.QListWidget(FilePathTesterForm)
        self.list_valid_paths.setObjectName("list_valid_paths")
        self.gridLayout.addWidget(self.list_valid_paths, 1, 1, 1, 2)

        self.retranslateUi(FilePathTesterForm)
        QtCore.QMetaObject.connectSlotsByName(FilePathTesterForm)

    def retranslateUi(self, FilePathTesterForm):
        _translate = QtCore.QCoreApplication.translate
        FilePathTesterForm.setWindowTitle(_translate("FilePathTesterForm", "FilePathTester"))
        self.add_button.setText(_translate("FilePathTesterForm", "Добавить"))
        self.delete_valid_path_button.setText(_translate("FilePathTesterForm", "Удалить"))
        self.transport_button.setText(_translate("FilePathTesterForm", "Переместить"))
        self.delete_invalid_path_button.setText(_translate("FilePathTesterForm", "Удалить"))
        self.return_button.setText(_translate("FilePathTesterForm", "Вернуть"))
