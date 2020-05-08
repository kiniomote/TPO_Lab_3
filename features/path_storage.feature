# -- FILE: features/path_storage.feature
@path_storage
Feature: Testing desktop app Path Storage

  Scenario: Adding valid path to list
    Given we have opened main window
     When we enter "C:\\" to input
      And we click on button "Add"
     Then we will see "C:\\" in list of the valid paths

  Scenario: Adding invalid path to list
    Given we have opened main window
     When we enter "C:af\\" to input
      And we click on button "Add"
     Then we will see "C:af\\" in list of the invalid paths

   Scenario: Adding empty string to list
    Given we have opened main window
     When we click on button "Add" with empty input
     Then we will see error message "Пустая строка!"

   Scenario: Attempting to remove valid path if path is absent
    Given we have opened main window
     When we click on button "Удалить" under list of valid paths
     Then we will see that list of valid paths has not changed

   Scenario: Removing valid path from list
    Given we have opened main window
     When we click on "C:\\" in list of valid paths
      And we click on button "Удалить" under list of valid paths
     Then we will see that "C:\\" was removed from list of valid paths

   Scenario: Attempting to remove invalid path if path is absent
    Given we have opened main window
     When we click on button "Удалить" under list of invalid paths
     Then we will see that list of invalid paths has not changed

   Scenario: Removing invalid path from list
    Given we have opened main window
     When we click on "C:af\\" in list of invalid paths
      And we click on button "Удалить" under list of invalid paths
     Then we will see that "C:af\\" was removed from list of invalid paths

   Scenario: Attempting to transporting valid path from list of valid paths to list of invalid paths if path is absent
    Given we have opened main window
      And we have added path "C:\\" to list of valid paths
     When we click on button "Переместить" under list of valid paths
     Then we will see that list of invalid paths has not changed
      And we will see "C:\\" in list of the valid paths

   Scenario: Transporting valid path from list of valid paths to list of invalid paths
    Given we have opened main window
     When we click on "C:\\" in list of valid paths
      And we click on button "Переместить" under list of valid paths
     Then we will see "C:\\" in list of the invalid paths
      And we will see that "C:\\" was removed from list of valid paths

   Scenario: Attempting to take invalid path from list of invalid paths to input line if path is absent
    Given we have opened main window
     When we click on button "Вернуть" under list of invalid paths
     Then we will see error message "Вы не выбрали строку для повторной проверки!"

   Scenario: Taking invalid path from list of invalid paths to input line
    Given we have opened main window
     When we click on "C:\\" in list of invalid paths
      And we click on button "Вернуть" under list of invalid paths
     Then we will see that "C:\\" was removed from list of invalid paths
      And we will see "C:\\" in input line