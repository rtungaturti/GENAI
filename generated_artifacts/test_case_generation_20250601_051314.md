Test Cases for Test Login Page
==============================

### Test Case 1: Positive Login Test

* **Test Case ID:** TC_001
* **Description:** Successful login with valid credentials
* **Preconditions:** User is on the Test Login page
* **Steps:**
  1. Open the Test Login page
  2. Enter valid username (`student`) in the Username field
  3. Enter valid password (`Password123`) in the Password field
  4. Click the Submit button
  5. Verify the new page URL contains `practicetestautomation.com/logged-in-successfully/`
  6. Verify the new page contains expected text (`Congratulations` or `successfully logged in`)
  7. Verify the Log out button is displayed on the new page
* **Expected Result:** The user is logged in successfully and redirected to the expected page
* **Priority:** High
* **Category:** Functional

### Test Case 2: Negative Username Test

* **Test Case ID:** TC_002
* **Description:** Login with invalid username
* **Preconditions:** User is on the Test Login page
* **Steps:**
  1. Open the Test Login page
  2. Enter invalid username (`incorrectUser`) in the Username field
  3. Enter valid password (`Password123`) in the Password field
  4. Click the Submit button
  5. Verify an error message is displayed
  6. Verify the error message text is `Your username is invalid!`
* **Expected Result:** An error message is displayed with the correct text
* **Priority:** High
* **Category:** Functional

### Test Case 3: Negative Password Test

* **Test Case ID:** TC_003
* **Description:** Login with invalid password
* **Preconditions:** User is on the Test Login page
* **Steps:**
  1. Open the Test Login page
  2. Enter valid username (`student`) in the Username field
  3. Enter invalid password (`incorrectPassword`) in the Password field
  4. Click the Submit button
  5. Verify an error message is displayed
  6. Verify the error message text is `Your password is invalid!`
* **Expected Result:** An error message is displayed with the correct text
* **Priority:** High
* **Category:** Functional

### Test Case 4: Empty Username and Password Fields

* **Test Case ID:** TC_004
* **Description:** Login with empty username and password fields
* **Preconditions:** User is on the Test Login page
* **Steps:**
  1. Open the Test Login page
  2. Leave the Username field empty
  3. Leave the Password field empty
  4. Click the Submit button
  5. Verify an error message is displayed
* **Expected Result:** An error message is displayed
* **Priority:** Medium
* **Category:** Functional

### Test Case 5: SQL Injection Attack

* **Test Case ID:** TC_005
* **Description:** Attempt to inject SQL code in the username field
* **Preconditions:** User is on the Test Login page
* **Steps:**
  1. Open the Test Login page
  2. Enter SQL injection code in the Username field
  3. Enter valid password (`Password123`) in the Password field
  4. Click the Submit button
  5. Verify the application behaves as expected (e.g., error message or no login)
* **Expected Result:** The application prevents SQL injection and displays an error message
* **Priority:** High
* **Category:** Security

### Test Case 6: Cross-Site Scripting (XSS)

* **Test Case ID:** TC_006
* **Description:** Attempt to inject JavaScript code in the username field
* **Preconditions:** User is on the Test Login page
* **Steps:**
  1. Open the Test Login page
  2. Enter JavaScript code in the Username field
  3. Enter valid password (`Password123`) in the Password field
  4. Click the Submit button
  5. Verify the application behaves as expected (e.g., error message or no login)
* **Expected Result:** The application prevents XSS and displays an error message
* **Priority:** High
* **Category:** Security

### Test Case 7: Accessibility - Page Title

* **Test Case ID:** TC_007
* **Description:** Verify the page title is correct and descriptive
* **Preconditions:** User is on the Test Login page
* **Steps:**
  1. Open the Test Login page
  2. Verify the page title is `Test Login | Practice Test Automation`
* **Expected Result:** The page title is correct and descriptive
* **Priority:** Medium
* **Category:** Accessibility

### Test Case 8: Usability - Form Fields

* **Test Case ID:** TC_008
* **Description:** Verify form fields are properly labeled and easily usable
* **Preconditions:** User is on the Test Login page
* **Steps:**
  1. Open the Test Login page
  2. Verify the Username field has a label
  3. Verify the Password field has a label
  4. Verify the form fields are easily usable (e.g., correct keyboard navigation)
* **Expected Result:** The form fields are properly labeled and easily usable
* **Priority:** Medium
* **Category:** UI/UX

### Test Case 9: Usability - Error Messages

* **Test Case ID:** TC_009
* **Description:** Verify error messages are properly displayed and easy to understand
* **Preconditions:** User is on the Test Login page
* **Steps:**
  1. Open the Test Login page
  2. Trigger an error message (e.g., invalid username or password)
  3. Verify the error message is displayed
  4. Verify the error message text is clear and easy to understand
* **Expected Result:** Error messages are properly displayed and easy to understand
* **Priority:** Medium
* **Category:** UI/UX

### Test Case 10: Link Navigation

* **Test Case ID:** TC_010
* **Description:** Verify navigation links work as expected
* **Preconditions:** User is on the Test Login page
* **Steps:**
  1. Open the Test Login page
  2. Click on navigation links (e.g., Home, Practice, Courses, Blog, Contact)
  3. Verify the links navigate to the correct pages
* **Expected Result:** Navigation links work as expected
* **Priority:** Low
* **Category:** UI/UX

The complete test case list:
```markdown
### Test Cases

#### Functional Test Cases

* [TC_001: Positive Login Test](#test-case-1-positive-login-test)
* [TC_002: Negative Username Test](#test-case-2-negative-username-test)
* [TC_003: Negative Password Test](#test-case-3-negative-password-test)
* [TC_004: Empty Username and Password Fields](#test-case-4-empty-username-and-password-fields)
* [TC_005: SQL Injection Attack](#test-case-5-sql-injection-attack)
* [TC_006: Cross-Site Scripting (XSS)](#test-case-6-cross-site-scripting-xss)

#### Accessibility Test Cases

* [TC_007: Accessibility - Page Title](#test-case-7-accessibility---page-title)

#### UI/UX Test Cases

* [TC_008: Usability - Form Fields](#test-case-8-usability---form-fields)
* [TC_009: Usability - Error Messages](#test-case-9-usability---error-messages)
* [TC_010: Link Navigation](#test-case-10-link-navigation)
```