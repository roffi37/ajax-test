from appium.webdriver.common.appiumby import AppiumBy

from .page import Page


class LoginPage(Page):

    login_path = '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[1]/android.view.View/android.view.View/android.widget.Button'
    email_path = '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginEmail"]'
    password_path = '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginPassword"]'
    confirm_path = '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[4]/android.view.View/android.view.View/android.widget.Button'
    sign_out_button = '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[6]/android.view.View/android.view.View[1]'

    def login(self, login, password):
        self.click_element(AppiumBy.XPATH, self.login_path)
        self.clean_field(AppiumBy.XPATH, self.email_path)
        self.write_text_to_element(AppiumBy.XPATH, self.email_path, login)
        self.write_text_to_element(AppiumBy.XPATH, self.password_path, password)
        self.click_element(AppiumBy.XPATH, self.confirm_path)

    def sign_out(self):
        self.click_element(AppiumBy.ID, 'com.ajaxsystems:id/menuDrawer')
        self.click_element(AppiumBy.ID, 'com.ajaxsystems:id/settings')
        self.click_element(AppiumBy.XPATH, self.sign_out_button)
