from behave import given, when, then
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt, QTimer

# ___________________Given___________________
# -------------------------------------------
#
@given('we have opened main window')
def step_impl(context):
    context.window.path_line_edit.setText('')
    context.window.list_valid_paths.clearSelection()
    context.window.list_invalid_paths.clearSelection()
    context.window.valid_path_count = context.window.list_valid_paths.count()
    context.window.invalid_path_count = context.window.list_invalid_paths.count()


@given('we have added path "{path}" to list of valid paths')
def step_impl(context, path):
    QTest.keyClicks(context.window.path_line_edit, path)
    QTest.mouseClick(context.window.add_button, Qt.LeftButton)
# ___________________When___________________
# ------------------------------------------
#
@when('we enter "{path}" to input')
def step_impl(context, path):
    QTest.keyClicks(context.window.path_line_edit, path)


@when('we click on button "Add"')
def step_impl(context):
    QTest.mouseClick(context.window.add_button, Qt.LeftButton)


@when('we click on button "Add" with empty input')
def step_impl(context):
    def close_message_box():
        context.window.message_box.close()
    QTimer.singleShot(100, close_message_box)
    QTest.mouseClick(context.window.add_button, Qt.LeftButton)


@when('we click on button "Удалить" under list of valid paths')
def step_impl(context):
    QTest.mouseClick(context.window.delete_valid_path_button, Qt.LeftButton)


@when('we click on "{path}" in list of valid paths')
def step_impl(context, path):
    item = context.window.list_valid_paths.item(context.window.list_valid_paths.count() - 1)
    context.window.list_valid_paths.setCurrentItem(item)


@when('we click on button "Удалить" under list of invalid paths')
def step_impl(context):
    QTest.mouseClick(context.window.delete_invalid_path_button, Qt.LeftButton)


@when('we click on "{path}" in list of invalid paths')
def step_impl(context, path):
    item = context.window.list_invalid_paths.item(context.window.list_invalid_paths.count() - 1)
    context.window.list_invalid_paths.setCurrentItem(item)


@when('we click on button "Переместить" under list of valid paths')
def step_impl(context):
    QTest.mouseClick(context.window.transport_button, Qt.LeftButton)


@when('we click on button "Вернуть" under list of invalid paths')
def step_impl(context):
    QTest.mouseClick(context.window.return_button, Qt.LeftButton)

# ___________________Then___________________
# ------------------------------------------
#
@then('we will see "{path}" in list of the valid paths')
def step_impl(context, path):
    assert context.window.list_valid_paths.item(context.window.list_valid_paths.count() - 1).text() == path


@then('we will see "{path}" in list of the invalid paths')
def step_impl(context, path):
    assert context.window.list_invalid_paths.item(context.window.list_invalid_paths.count() - 1).text() == path


@then('we will see error message "{message}"')
def step_impl(context, message):
    assert context.window.message_box.text() == message


@then('we will see that list of valid paths has not changed')
def step_impl(context):
    assert context.window.list_valid_paths.count() is context.window.valid_path_count


@then('we will see that "{path}" was removed from list of valid paths')
def step_impl(context, path):
    assert context.window.list_valid_paths.item(context.window.list_valid_paths.count() - 1) is None


@then('we will see that list of invalid paths has not changed')
def step_impl(context):
    assert context.window.list_invalid_paths.count() is context.window.invalid_path_count


@then('we will see that "{path}" was removed from list of invalid paths')
def step_impl(context, path):
    assert context.window.list_invalid_paths.item(context.window.list_invalid_paths.count() - 1) is None


@then('we will see that input line has not changed')
def step_impl(context):
    assert context.window.path_line_edit.text() == ''


@then('we will see "{path}" in input line')
def step_impl(context, path):
    assert context.window.path_line_edit.text() == path

