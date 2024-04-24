import os
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy


def appium_setup():
    """
    appium 실행 전 환경변수를 설정해야 합니다.
    vi ~/.zshrc 명령어를 통해 해당 파일에 아래 스크립트를 추가합니다.
    단, java 버전이나 사용자 이름 같은 유동적인 값은 수정이 필요합니다.

    export JAVA_HOME=/Library/Java/JavaVirtualMachines/adoptopenjdk-16.jdk/Contents/Home
    export PATH=$PATH:JAVA_HOME/bin
    export ANDROID_SDK_ROOT=/Users/seunghoon/Library/Android/sdk
    export ANDROID_HOME=$ANDROID_SDK_ROOT
    export PATH=$ANDROID_SDK_ROOT:$PATH
    export PATH=$PATH:$ANDROID_SDK_ROOT/emulator
    export PATH=$PATH:$ANDROID_SDK_ROOT/tools
    export PATH=$PATH:$ANDROID_SDK_ROOT/tools/bin
    export PATH=$PATH:$ANDROID_SDK_ROOT/platform-tools
    :return:
    """
    try:
        appium_service = AppiumService()
        os.environ['ANDROID_HOME'] = '/Users/seunghoon/Library/Android/sdk'
        os.environ['ANDROID_SDK_ROOT'] = '/Users/seunghoon/Library/Android/sdk'
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
        URL = 'http://127.0.0.1:4723'
        apps = "naver.apk"
        app = os.path.join(BASE_DIR, 'apps', apps)
        print("baseDir = " + BASE_DIR)
        print("app = " + app)
        appium_service.start()
        capabilities = {
            "app": app,
            "platformName": "ANDROID",
            "appium:platformVersion": "14",
            "appium:automationName": "UiAutomator2",
            "appium:udid": "emulator-5554",
            "appium:bundleId": "com.nhn.android.search",
            "appium:appActivity": "com.nhn.android.search.ui.pages.SearchHomePage",
            "appium:appPackage": "com.nhn.android.search",
            "autoAcceptAlerts": "true",
        }

        appium_set = webdriver.Remote(command_executor=URL, desired_capabilities=capabilities)
        return appium_set
    except Exception as e:
        print(e)
        exit(1)

driver = appium_setup()

driver.find_element(
    AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]'
).click()