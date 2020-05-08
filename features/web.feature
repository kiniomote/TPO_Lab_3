# -- FILE: features/web.feature
@website_wiki
Feature: testing web-site https://en.wikipedia.org

  Scenario: Check russian language in article
    Given we are on the website https://en.wikipedia.org
     When we enter in search field "NUnit"
     Then we will see article about NUnit
      And we will see russian language in language list
