import pytest
from appium.webdriver.common.appiumby import AppiumBy


def test_sidebar_app_settings(user_login_fixture):
    user_login_fixture.login('qa.ajax.app.automation@gmail.com', 'qa_automation_password')
    hub = user_login_fixture.find_element(AppiumBy.ID, 'com.ajaxsystems:id/icNoHub')
    assert hub


@pytest.mark.parametrize(
    'by,test_item,expected_item',
    [
        pytest.param(AppiumBy.ID, 'com.ajaxsystems:id/settings', 'com.ajaxsystems:id/icon', id="test is settings work"),
        pytest.param(AppiumBy.ID, 'com.ajaxsystems:id/help', 'com.ajaxsystems:id/navigation', id="test is help work"),
        pytest.param(AppiumBy.ID, 'com.ajaxsystems:id/logs', 'com.ajaxsystems:id/content', id="test is report work"),
        pytest.param(AppiumBy.ID, 'com.ajaxsystems:id/addHub', 'com.ajaxsystems:id/title', id="test is add hub work")

    ]
)
def test_sidebar_for_components(user_login_fixture, by, test_item, expected_item):
    user_login_fixture.click_element(AppiumBy.ID, 'com.ajaxsystems:id/menuDrawer')
    user_login_fixture.click_element(by, test_item)
    expected = user_login_fixture.find_element(by, expected_item)
    assert expected
    user_login_fixture.driver.back()
