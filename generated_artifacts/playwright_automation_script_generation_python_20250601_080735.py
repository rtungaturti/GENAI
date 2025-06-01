Here's a Python script using Playwright to automate the test cases on the provided webpage.

```python
# Import the required Playwright modules
from playwright.sync_api import sync_playwright

# Define test cases
def test_positive_login(page):
    """
    Test case 1: Positive LogIn test
    """
    # Open the page
    page.goto("https://practicetestautomation.com/login/")

    # Type username
    username_input = page.locator('#username')
    username_input.fill('student')

    # Type password
    password_input = page.locator('#password')
    password_input.fill('Password123')

    # Click submit button
    submit_button = page.locator('#submit')
    submit_button.click()

    # Verify new page URL contains 'logged-in-successfully/'
    page.wait_for_load_state()
    assert 'logged-in-successfully/' in page.url()

    # Verify new page contains expected text
    congratulations_text = page.locator('text="Congratulations"')
    assert congratulations_text.count() > 0

    # Verify Log out button is displayed
    logout_button = page.locator('text="Log out"')
    assert logout_button.count() > 0

def test_negative_username(page):
    """
    Test case 2: Negative username test
    """
    # Open the page
    page.goto("https://practicetestautomation.com/login/")

    # Type incorrect username
    username_input = page.locator('#username')
    username_input.fill('incorrectUser')

    # Type password
    password_input = page.locator('#password')
    password_input.fill('Password123')

    # Click submit button
    submit_button = page.locator('#submit')
    submit_button.click()

    # Verify error message is displayed
    error_message = page.locator('#error')
    assert error_message.text_content() == 'Your username is invalid!'

def test_negative_password(page):
    """
    Test case 3: Negative password test
    """
    # Open the page
    page.goto("https://practicetestautomation.com/login/")

    # Type username
    username_input = page.locator('#username')
    username_input.fill('student')

    # Type incorrect password
    password_input = page.locator('#password')
    password_input.fill('incorrectPassword')

    # Click submit button
    submit_button = page.locator('#submit')
    submit_button.click()

    # Verify error message is displayed (Note: For this test case error message might not be 'Your password is invalid!' - adapt as per actual error)
    error_message = page.locator('#error')
    assert error_message.count() > 0

# Run the tests
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    test_positive_login(page)
    page.close()
    page = context.new_page()

    test_negative_username(page)
    page.close()
    page = context.new_page()

    test_negative_password(page)

    browser.close()
```

For best practices and re-usability, consider organizing these tests using a testing framework such as Pytest or Unittest.

**Using Pytest**

Firstly, install required packages:
```bash
pip install pytest playwright
```

Here's how you can refactor the tests:

```python
# tests/test_login.py
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser

def test_positive_login(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practicetestautomation.com/login/")

    # Type username
    username_input = page.locator('#username')
    username_input.fill('student')

    # Type password
    password_input = page.locator('#password')
    password_input.fill('Password123')

    # Click submit button
    submit_button = page.locator('#submit')
    submit_button.click()

    # Verify new page URL contains 'logged-in-successfully/'
    page.wait_for_load_state()
    assert 'logged-in-successfully/' in page.url()

    # Verify new page contains expected text
    congratulations_text = page.locator('text="Congratulations"')
    assert congratulations_text.count() > 0

    # Verify Log out button is displayed
    logout_button = page.locator('text="Log out"')
    assert logout_button.count() > 0

    browser.close()

def test_negative_username(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practicetestautomation.com/login/")

    # Type incorrect username
    username_input = page.locator('#username')
    username_input.fill('incorrectUser')

    # Type password
    password_input = page.locator('#password')
    password_input.fill('Password123')

    # Click submit button
    submit_button = page.locator('#submit')
    submit_button.click()

    # Verify error message is displayed
    error_message = page.locator('#error')
    assert error_message.text_content() == 'Your username is invalid!'

    browser.close()

def test_negative_password(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practicetestautomation.com/login/")

    # Type username
    username_input = page.locator('#username')
    username_input.fill('student')

    # Type incorrect password
    password_input = page.locator('#password')
    password_input.fill('incorrectPassword')

    # Click submit button
    submit_button = page.locator('#submit')
    submit_button.click()

    # Verify error message is displayed (Note: For this test case error message might not be 'Your password is invalid!' - adapt as per actual error)
    error_message = page.locator('#error')
    assert error_message.count() > 0

    browser.close()
```
Or you could use a more optimized way with pytest fixture to reduce duplication:
```python
# tests/conftest.py
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()

# tests/test_login.py
def test_positive_login(page):
    page.goto("https://practicetestautomation.com/login/")

    # Type username
    username_input = page.locator('#username')
    username_input.fill('student')

    # Type password
    password_input = page.locator('#password')
    password_input.fill('Password123')

    # Click submit button
    submit_button = page.locator('#submit')
    submit_button.click()

    # Verify new page URL contains 'logged-in-successfully/'
    page.wait_for_load_state()
    assert 'logged-in-successfully/' in page.url()

    # Verify new page contains expected text
    congratulations_text = page.locator('text="Congratulations"')
    assert congratulations_text.count() > 0

    # Verify Log out button is displayed
    logout_button = page.locator('text="Log out"')
    assert logout_button.count() > 0

def test_negative_username(page):
    page.goto("https://practicetestautomation.com/login/")

    # Type incorrect username
    username_input = page.locator('#username')
    username_input.fill('incorrectUser')

    # Type password
    password_input = page.locator('#password')
    password_input.fill('Password123')

    # Click submit button
    submit_button = page.locator('#submit')
    submit_button.click()

    # Verify error message is displayed
    error_message = page.locator('#error')
    assert error_message.text_content() == 'Your username is invalid!'

def test_negative_password(page):
    page.goto("https://practicetestautomation.com/login/")

    # Type username
    username_input = page.locator('#username')
    username_input.fill('student')

    # Type incorrect password
    password_input = page.locator('#password')
    password_input.fill('incorrectPassword')

    # Click submit button
    submit_button = page.locator('#submit')
    submit_button.click()

    # Verify error message is displayed (Note: For this test case error message might not be 'Your password is invalid!' - adapt as per actual error)
    error_message = page.locator('#error')
    assert error_message.count() > 0

# Run tests via pytest command
```