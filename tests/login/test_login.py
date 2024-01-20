import pytest
from appium.webdriver.common.appiumby import AppiumBy


@pytest.mark.parametrize(
    "login,password",
    [
        pytest.param("abcd", "1234", id="login with invalid email"),
        pytest.param("qa.ajax.app.automation@gmail.com", "1234", id="login with wrong password")
    ]
    )
def test_user_login_with_wrong_credentials(user_login_fixture, login, password):
    user_login_fixture.login(login, password)
    snack_bar = user_login_fixture.find_element(AppiumBy.ID, 'com.ajaxsystems:id/snackbar_text')
    assert snack_bar
    user_login_fixture.driver.back()


def test_success_user_login(user_login_fixture):
    user_login_fixture.login('qa.ajax.app.automation@gmail.com', 'qa_automation_password')
    hub = user_login_fixture.find_element(AppiumBy.ID, 'com.ajaxsystems:id/icNoHub')
    assert hub


def test_success_sign_out(user_login_fixture):
    user_login_fixture.sign_out()
    login_path = '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[1]/android.view.View/android.view.View/android.widget.Button'
    assert login_path
