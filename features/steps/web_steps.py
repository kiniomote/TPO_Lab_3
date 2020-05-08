from behave import given, when, then


@given('we are on the website https://en.wikipedia.org')
def step_impl(context):
    context.browser.get('https://www.google.com/')
    element = context.browser.find_element_by_name('q')
    element.send_keys('unit testing')
    element.submit()
    x_path = "//a[@href='https://en.wikipedia.org/wiki/Unit_testing']"
    context.browser.find_element_by_xpath(x_path).click()


@when('we enter in search field "{article}"')
def step_impl(context, article):
    search = context.browser.find_element_by_xpath("//input[@id='searchInput']")
    search.send_keys('NUnit')
    search.submit()


@then('we will see article about NUnit')
def step_impl(context):
    url = 'https://en.wikipedia.org/wiki/NUnit'
    assert context.browser.current_url == url


@then('we will see russian language in language list')
def step_impl(context):
    assert context.browser.find_element_by_xpath("//*[@title='NUnit – Russian']").text == 'Русский'
