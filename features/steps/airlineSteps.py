from behave import when, then


@when('"왕복" 탭을 클릭한다.')
def step_impl(context):
    context.alp.click_roundtrip_tap()

@when('출발 장소 드롭다운 메뉴를 클릭한다.')
def step_impl(context):
    context.alp.click_departure_menu()

@when('검색 필드에 "인천" 을 입력한다.')
def step_impl(context):
    context.alp.input_departure_place()

@when('검색 결과 인천 메뉴를 클릭한다.')
def step_impl(context):
    context.alp.click_departure_place()

@when('도착 장소 드롭다운 메뉴를 클릭한다.')
def step_impl(context):
    context.alp.click_arrival_menu()

@when('검색 필드에 "오사카" 를 입력한다.')
def step_impl(context):
    context.alp.input_arrival_place()

@when('검색 결과 오사카 메뉴를 클릭한다.')
def step_impl(context):
    context.alp.click_arrival_place()

@then('출발 장소, 도착 장소가 선택된다.')
def step_impl(context):
    context.alp.check_airline_setup()