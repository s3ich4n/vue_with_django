# Django Templates

이것도 [공식 docs]()를 보면 좋다.

* 현재 구조

* `base.html`: 문서들의 뼈대. 나머지 것들이 이 파일을 `extend`한다.
    * `vue_main.html`: 메인화면
    * `todo_confirm_delete.html`: 삭제확인 관련 로직.
    * `todo_form.html`: to-do 추가용 form
    * `todo_list.html`: to-do 리스트뷰
    * `home.html`: 메인 경로의 화면