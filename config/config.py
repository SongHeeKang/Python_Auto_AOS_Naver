import os
BASE_DIR = os.getcwd()


# BasePage
WAIT_TIME = 10
PASS_SCREENSHOT = True

# appium
APP_FILE = "naver.apk"
# APP_FILE = "YouTube_19.14.43_Apkpure.apk"
# APP_FILE = "Naver Whale Browser_3.2.3.2_Apkpure.apk"
URL = 'http://127.0.0.1:4723'
PLATFORM_NAME = "ANDROID"
PLATFORM_VERSION = "14"
AUTOMATION_NAME = "UiAutomator2"
UDID = "emulator-5554" #"R3CW20T5XZB"
BUNDLE_ID = "com.nhn.android.search"
APP_ACTIVITY = "com.nhn.android.search.ui.pages.SearchHomePage"
APP_WAIT_ACTIVITY = "com.nhn.android.search.ui.pages.SearchHomePage, com.nhn.android.search.tutorial.TutorialActivity"
# BUNDLE_ID="com.google.android.youtube"
# BUNDLE_ID="com.naver.whale"
# XCODE_ORG_ID="G476VT3T47"


# threshold
# CONFIDENCE_THRESHOLD = 99.0
# DISTANCE_THRESHOLD = 0.3338
# ID_VERIFICATION_THRESHOLD = 1.0


# google
#https://console.cloud.google.com/apis/credentials 의 서비스 계정등록된 Json 파일 구글 문서에 권한을 추가해줘야함.(googleqaapi@alchera-d0790.iam.gserviceaccount.com)
# GOOGLE_AUTH_FILE_NAME= BASE_DIR + "/config/alchera-auth.json"
# GOOGLE_SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1_OPFRQ_e6OflL_VZZL5__lvafh_pKH5Mv85PYLbFxX4/edit#gid=0"
# GOOGLE_WORKSHEET="Result"