# OrangeHRM Enterprise Automation Framework

This folder contains a Page Object Model framework for OrangeHRM login and dashboard validation.

## What is included

- `config/` for runtime settings and environment helpers
- `core/` for reusable browser and wait factories
- `pages/` for page objects
- `tests/` for login and dashboard scenarios
- `utilities/` for logging, screenshots, and helper functions
- `main.py` and `ui_runner.py` for local execution entry points

## How to run

Install dependencies from `requirements.txt`, then run one of the following commands from this folder:

```bash
pytest
python main.py
python ui_runner.py
```

### UI/API mode selection

- Running `python main.py` now prompts for mode selection: `ui`, `api`, or `all`.
- You can also pass mode explicitly:

```bash
python main.py --mode ui
python main.py --mode api
python main.py --mode all
```

- Direct pytest execution supports the same mode option:

```bash
pytest --mode ui
pytest --mode api
pytest --mode all
```

- In non-interactive execution (such as CI), if mode is not provided, default mode is `ui`.

## Notes

- The framework uses the demo OrangeHRM site from the upstream README.
- Selenium Manager is used for Chrome driver resolution.
- Screenshots are written to `screenshots/` when a test fails.

# OrangeHRM Enterprise Automation Framework

Target application: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

This document describes a complete Page Object Model (POM) framework design for UI automation of the OrangeHRM login flow, dashboard validation, and related positive, negative, and edge scenarios.

## 1. Framework Goal

Build a maintainable test automation framework that:

- Separates page actions from test logic using POM.
- Covers login, dashboard, and logout journeys.
- Supports positive, negative, and edge-case validation.
- Produces readable test reports and screenshots on failure.
- Is easy to extend for more modules such as admin, pim, leave, and time.

## 2. Recommended Tech Stack

- Python 3.11+
- Pytest for test execution
- Selenium WebDriver for browser automation
- WebDriverManager or local driver management
- PyYAML or configparser for environment configuration
- Allure or HTML reporting
- Logging via the standard logging module

## 3. Proposed Folder Structure

```text
OrangeHRM_Enterprise_Automation_Framework/
├── config/
│   ├── config.yaml
│   └── env.py
├── core/
│   ├── base_page.py
│   ├── browser_factory.py
│   └── wait_factory.py
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── base_page.py
├── tests/
│   ├── test_login_positive.py
│   ├── test_login_negative.py
│   ├── test_login_edge.py
│   └── test_dashboard.py
├── testdata/
│   ├── login_data.yaml
│   └── users.json
├── utilities/
│   ├── logger.py
│   ├── helpers.py
│   ├── screenshot.py
│   └── assertions.py
├── reports/
├── screenshots/
├── logs/
├── conftest.py
├── main.py
├── ui_runner.py
├── pytest.ini
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
└── README.md
```

## 4. POM Design

### 4.1 Base Page

The base page should contain reusable browser actions used by all pages.

Responsibilities:

- Open URLs
- Click elements
- Enter text
- Clear text fields
- Get text and attribute values
- Wait for visibility/clickability
- Scroll to elements

### 4.2 Login Page

The login page should hold only login-screen locators and login actions.

Suggested methods:

- `open_login_page()`
- `enter_username(username)`
- `enter_password(password)`
- `click_login()`
- `login(username, password)`
- `get_error_message()`
- `is_login_button_enabled()`
- `is_username_field_visible()`
- `is_password_field_visible()`

Key locators:

- Username input
- Password input
- Login button
- Error message area
- Required field validation messages

### 4.3 Dashboard Page

The dashboard page should validate the landing page after successful login.

Suggested methods:

- `is_dashboard_loaded()`
- `get_page_header()`
- `get_profile_menu_text()`
- `open_profile_menu()`
- `logout()`
- `is_sidebar_visible()`

Key locators:

- Dashboard header or title
- User profile dropdown
- Side navigation panel
- Logout option

## 5. Test Layer Design

### 5.1 Positive Scenarios

Use valid credentials and verify successful navigation to the dashboard.

Examples:

- Valid username and valid password should log in successfully.
- After login, dashboard page title or header should be visible.
- Profile menu should be accessible after login.
- Logout should return the user to the login page.

### 5.2 Negative Scenarios

Validate that the application rejects invalid or incomplete input.

Examples:

- Invalid username and valid password.
- Valid username and invalid password.
- Invalid username and invalid password.
- Blank username and blank password.
- Blank username with valid password.
- Valid username with blank password.
- Locked or restricted user credentials, if applicable.
- Username with leading or trailing spaces.
- Password with leading or trailing spaces.

Expected results:

- Login should fail.
- Proper error message should be displayed.
- Dashboard should not load.

### 5.3 Edge Scenarios

Validate boundary and unusual input behavior.

Examples:

- Very long username or password values.
- Special characters in username and password.
- Numeric-only username or password.
- Unicode or mixed-language characters.
- Copy-paste input with accidental whitespace.
- Empty spaces only in input fields.
- Repeated login attempts with invalid data.
- Browser refresh on login page and dashboard page.

## 6. Test Data Strategy

Store data outside the test code so scenarios remain readable and easy to maintain.

Suggested files:

- `testdata/login_data.yaml` for credential sets and expected messages.
- `testdata/users.json` for structured test user profiles.

Recommended data groups:

- `valid_user`
- `invalid_user`
- `blank_user`
- `locked_user`
- `edge_long_input`

## 7. Pytest Structure

Use Pytest fixtures in `conftest.py` for browser setup and teardown.

Recommended fixtures:

- `driver` fixture for WebDriver lifecycle.
- `login_page` fixture for login page object.
- `dashboard_page` fixture for dashboard page object.
- `base_url` fixture for environment URL handling.

Recommended markers:

- `smoke`
- `regression`
- `positive`
- `negative`
- `edge`

## 8. Execution Flow

1. Load configuration from `config/config.yaml`.
2. Launch browser from `core/browser_factory.py`.
3. Create page object instance for the login page.
4. Open the OrangeHRM login URL.
5. Run the selected scenario set.
6. Validate dashboard or error state depending on the test.
7. Capture screenshot and logs on failure.
8. Close browser and generate report.

## 9. Suggested Assertions

- Login success should be confirmed by dashboard visibility.
- Login failure should be confirmed by exact or partial error text.
- UI elements should be visible, enabled, and clickable before interaction.
- Logout should bring the user back to the login page.
- Fields should preserve expected validation behavior.

## 10. Reporting and Diagnostics

The framework should capture:

- Screenshots on failure
- Browser logs if available
- Test execution logs
- HTML or Allure report output

## 11. CI and Run Support

Recommended entry points:

- `main.py` for local execution orchestration
- `ui_runner.py` for UI suite execution
- `pytest.ini` for markers and default options
- `Jenkinsfile` for CI pipeline execution
- `Dockerfile` for containerized runs

## 12. Example Module Responsibilities

- `core/base_page.py`: shared browser actions
- `pages/login_page.py`: login screen actions and validations
- `pages/dashboard_page.py`: dashboard validations and logout flow
- `utilities/logger.py`: structured logging
- `utilities/screenshot.py`: failure screenshots
- `tests/test_login_positive.py`: valid credential flow
- `tests/test_login_negative.py`: invalid credential flow
- `tests/test_login_edge.py`: boundary input flow

## 13. Minimum Coverage Recommendation

For a solid starter suite, implement at least:

- 3 positive login tests
- 5 negative login tests
- 5 edge login tests
- 2 dashboard verification tests
- 1 logout test

## 14. Next Build Step

If you want to turn this design into implementation, the next step is to create the actual POM files and test files under `OrangeHRM_Enterprise_Automation_Framework/` using the structure above.