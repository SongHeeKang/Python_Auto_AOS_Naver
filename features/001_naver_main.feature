Feature: 네이버 메인 페이지

    Background: 초기화
        Given 테스트 수행 전 초기화한다.

    Scenario: 네이버 앱 튜토리얼 진행하기
        When "네이버 시작하기" 버튼을 클릭한다.
        And "나중에 로그인" 버튼을 클릭한다.
        And 두 번째 "네이버 시작하기" 버튼을 클릭한다.
        And 튜토리얼 페이지에서 화면 중앙을 클릭한다.
        Then 네이버 메인 페이지로 이동한다.

    Scenario: 네이버 검색 필드에 네이버 항공권 입력하기
        When 네이버 검색 필드를 클릭한다.
        And "네이버 항공권" 을 입력한다.
        And 검색 아이콘을 클릭한다.
        Then 네이버 항공권 검색 결과 페이지로 이동한다.

    Scenario: 네이버 항공권 페이지로 이동하기
        When 네이버 항공권 검색 결과에서 링크 텍스트를 클릭한다.
        Then 네이버 항공권 페이지로 이동한다.