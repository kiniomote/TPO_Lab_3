# -- FILE: features/environment.py
from behave import fixture, use_fixture
from selenium import webdriver
from ViewModels.FilePathTesterViewModel import FilePathTesterViewModel
from PyQt5 import QtWidgets
import sys


@fixture
def selenium_browser_chrome(context):
    context.browser = webdriver.Chrome('D:\Program Files\Chrome\chromedriver')
    yield context.browser
    context.browser.quit()


@fixture
def path_storage_qt(context):
    app = QtWidgets.QApplication(sys.argv)
    window = FilePathTesterViewModel()
    window.show()
    context.window = window
    yield context.window
    # sys.exit(app.exec_())


def before_tag(context, tag):
    if tag == 'website_wiki':
        use_fixture(selenium_browser_chrome, context)
    if tag == 'path_storage':
        use_fixture(path_storage_qt, context)
