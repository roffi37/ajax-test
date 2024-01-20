from utils.utils_conf import get_udid_from_abd


def android_get_desired_capabilities():
    result = {'autoGrantPermissions': True, 'automationName': 'uiautomator2', 'newCommandTimeout': 500, 'noSign': True,
              'platformName': 'Android', 'platformVersion': '11', 'resetKeyboard': True, 'takesScreenshot': True,
              'appPackage': 'com.ajaxsystems',
              'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity', "udid": get_udid_from_abd()}
    return result
