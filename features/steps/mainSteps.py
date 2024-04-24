from behave import when, then


@when('네이버 알림 팝업을 닫는다.')
def step_impl(context):
    context.mp.close_naver_noti_modal()

@when('"네이버 시작하기" 버튼을 클릭한다.')
def step_impl(context):
    context.mp.click_naver_first_start_button()

@when('"나중에 로그인" 버튼을 클릭한다.')
def step_impl(context):
    context.mp.click_later_login_button()

@when('두 번째 "네이버 시작하기" 버튼을 클릭한다.')
def step_impl(context):
    context.mp.click_naver_second_start_button()

@when('튜토리얼 페이지에서 화면 중앙을 클릭한다.')
def step_impl(context):
    context.mp.click_naver_tutorial_screen_center()

@then('네이버 메인 페이지로 이동한다.')
def step_impl(context):
    context.mp.check_naver_main_page()

@when('네이버 검색 필드를 클릭한다.')
def step_impl(context):
    context.mp.click_naver_search_field()

@when('"네이버 항공권" 을 입력한다.')
def step_impl(context):
    context.mp.input_naver_airline_text()

@when('검색 아이콘을 클릭한다.')
def step_impl(context):
    context.mp.click_search_icon()

@then('네이버 항공권 검색 결과 페이지로 이동한다.')
def step_impl(context):
    context.mp.check_naver_airline_search_result()

@when('네이버 항공권 검색 결과에서 링크 텍스트를 클릭한다.')
def step_impl(context):
    context.mp.click_naver_airline_link_text()

@then('네이버 항공권 페이지로 이동한다.')
def step_impl(context):
    context.mp.check_naver_airline_page()