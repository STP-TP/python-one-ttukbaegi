---
marp: true
---

## Why Project -> App?

**App 구조화를 통한 재활용성**

* 시스템 리팩토링, 유지보수 용이
* App을 패키징화 하여 다른 프로젝트에서 사용

---

## MVC Pattern
![](/KJM/Chapter2/imgs/MVC.jpg)
* Model : 데이터(DB), 어플리케이션에서 사용되는 데이터와 그를 처리하는 부분
* View : 모델에 포함된 데이터의 시각화, 모델을 이용하여 화면을 출력
* Controller : 사용자의 입력(Input)을 받아 처리


---

## MVC Pattern
**장점**
1. 유연성이 높고 유지보수 용이
2. 개발자와 디자이너의 작업 영역을 분리

**단점**
1. 프로젝트의 규모가 커질수록 컨트롤러가 비대화
2. 뷰와 모델 사이의 높은 의존성


---

## 그래서?

**MVP**
* Controller 대신 Presenter를 사용  
  * Presenter에서만 데이터를 통제하도록!
 -> View와 Presenter의 의존성이 높아져버렸다..

**MVVM(ViewModel)**
* View와 Controller/Presenter의 높은 의존성을 완화해주는 디자인 패턴


---

## 아무튼 장고에서는?

**MTV - 골자는 MVC 패턴과 동일하지만..**
* Model : DB에 저장되는 데이터
  * Class로 정의되며 하나의 클래스가 각각 하나의 DB Table
  * ORM(Object Relational Mapping) 기능을 통해 SQL 대신 파이썬 코드로 DB를 조작할 수 있다
* Template : MVC패턴의 View와 같은 기능
  * View에서 로직을 처리한 후 html파일을 context와 함께 렌더링
    -> 장고 자체의 Django Template 문법 덕분에 html 파일 내에서 context로 받은 데이터를 활용할 수 있다


---

## 아무튼 장고에서는?

**MTV - 골자는 MVC 패턴과 동일하지만..**
* View : MVC패턴의 Controller에 대응
  * 요청에 따라 적절한 로직을 수행하여 결과를 템플릿으로 렌더링하며 응답
* URLConf(URL 설계) : 플러스 알파..?
  * URL 패턴을 정의하여 해당 URL과 View를 매핑하는 단계
  ```python
  from django.urls import path
  from . import views

  app_name = 'project'

  urlpatterns = [
      path('', views.HomeView.as_view(), name='home'),
      path('login/', views.LoginView.as_view(), name='login'),
  ]
  ```


---

## 아무튼 장고에서는?

**MTV - 골자는 MVC 패턴과 동일하지만..**
![](/KJM/Chapter2/imgs/MTV.jpg)
1. 유저가 특정 url로 요청을 보냄
2. URLConf를 통해 해당 url과 매핑된 View를 호출
3. 호출된 View는 요청에 따라 적절한 로직을 수행해 Model에게 CRUD를 지시
4. Model은 ORM을 통해 DB와 소통하여 CRUD를 수행
5. ~6. View는 지정된 Template를 렌더링하고 유저에게 반환

---

## CRUD
|**이름**|**조작(기능)**|**SQL**|
|:--:|:--:|:--:|
| Create | 생성 | INSERT |
| Read | 읽기 | SELECT |
| Update | 갱신, 수정 | UPDATE |
| Delete | 삭제 | DELETE |


---

## CRUD
|**기능**|**URI**|
|:--:|:--:|
| Create | 기본 도메인/create<br/>  기본 도메인/write|
| Read | 기본 도메인/read<br/> 기본 도메인/  |
| Update | 기본 도메인/update<br/> 기본 도메인/modify |
| Delete | 기본 도메인/delete<br/> 기본 도메인/remove|


---

## Post or Get
* 서버에 뭔가를 전달할 때 파라미터를 숨기냐 숨기지 않냐의 차이
* POST는 GET에 비해 보안에 우수하고 데이터 길이 제한이 없지만(GET의 경우 256바이트) 전송속도가 느린 편
* POST는 Create, Update, Delete에 관련된 것, GET은 Read에 관련된 것으로 생각하면 편하다. 

