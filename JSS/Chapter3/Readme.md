---
marp: true
---

## Views.py 만들때 팁

* Function의 Return 결과를 바로 만드려고 하지 말것.
* `HttpResponse`를 통해서 간단한 text 출력으로 결과를 본 뒤 수정 시작
    * 결과를 보면서 차근차근히 진행 가능
    * 생각지 못한 에러 잡을 수 있음
---

## 보이지 않는 Hidden 값

* Html만 사용하면서 어쩔 수 없이 `hidden input tag` 사용
* Javascript 사용하면 내부 변수 저장 가능

---

## on_delete

* DB의 참조 무결성을 지원하는 값
* `ForeignKey Field`가 바라보는 값이 삭제될 때 해당 요소를 처리하는 방법을 지정한다.
* Ex) `Category A`가 삭제되었다면, FK중 `Category A`를 가지는 값에 대한 처리

| on_delete | 내용 |
|:--:|:--:|
|SET_DEFAULT | default로 설정해둔 field로 바꿔준다.|
|CASCADE|참조되는 모든 요소 삭제|
|PROTECT| 삭제되지 말아야 하는 곳에 사용하면 될듯, ProtectedError 발생|
|SET_NULL| 참조값을 null로 바꾼다. |

---

## input에서 js 값 사용

* `index.html`에서 아래와 같은 구문을 통해 Javascript를 호출하여 판단하는 로직이 존재
```html
<from onsubmit="return emailCheckFrom();"/>
```
![](/JSS/Chapter3/imgs/javascript_usable.png)

* JS의 console.log를 통해 Frontend의 여러 정보들을 찍어 볼 수 있음

---

## MIMEText, MIMEMultipart
* MIME(Multipurpose Internet Mail Extensions) - 전자우편을 위한 인터넷 표준
* SMTP는 7비트 아스키문자만 가능했었음(영어만 가능)
* 비영어권 언어도 전자메일을 사용하기 위해 MIME 사용

### MIMEText
* MIME로 아스키가 아닌 언어로 메일을 보내는 방식(텍스트여야 함)
### MIMEMultipart
* 이메일 메세지 컨테이너 생성자
* 자세한 설명이 없음..

---
## private info
* Github에 꼭 올리지 말아야 할 것들이 개인정보이다.
* AWS에서 이용하는 각종 token이나 로그인 정보들을 해킹하는 집단 존재(오픈소스인 점을 이용)
* 필수적으로 **외부 파일을 이용하여 사용**
```python
from sendEmail.env.mail_info import *
```

![](/JSS/Chapter3/imgs/private_info.png)

---

## Depandency injection
* **"A가 B를 의존한다"**
    * B가 변하면 A에 영향을 미친다.
    * A와 B의 결합 의존도가 높다
* 의존도를 낮추려면?
    * B의 개념을 Interface로 추상화 시킨 뒤
    * A에서는 Interface변수를 통해 B를 외부에서 주입받는다.
![](https://upload.wikimedia.org/wikipedia/commons/1/10/W3sDesign_Dependency_Injection_Design_Pattern_UML.jpg)

---

## DI의 실 사용 예시를 들어보자.
1. 어떤 기업에서 LiteSQL을 사용해서 백엔드 개발을 완료하고 서비스중이라고 가정
2. 모종의 이유로.. 데이터베이스를 MariaDB로 바꿔야 한다면?
    * 데이터 내용은 Migration이 잘 되어 있다.
    * 그렇다면 백엔드 코드는 전부 바꿔야 하는가?
        * SQL 명령어 테스트는? 데이터베이스 의존 코드는?

### DI를 사용함으로 인해 Unit test 를 하기 쉬워진다.
* 각 모듈의 의존성이 떨어지므로 별도의 객체로 볼 수 있다.

---

## Django의 DI는?
* Django, DRF(Django REST Framework)에서 내장된 DI프레임워크 존재
* Directory 이용해서 Injection시킴
![](/JSS/Chapter3/imgs/python_di.png)
* 그런데 프레임워크 종속된것보다는 `Dependency-injector` 파이썬 라이브러리 이용

---
## Ask
* 장고 모델 구성 때 다른 요소를 참조하는 요소는 무엇으로 정의되는가?
    * ForeignKey를 통해서 다른 테이블의 값을 참조한다.
* on_delete 속성에 대한 기댓값으로는 어떤것들이 존재하며, 그 쓰임새는?
    위 페이지에 정리
* 이메일 발송 기능을 구현하는데 Django.core와 관련된 라이브러리 이전에 사용한 라이브러리?
    * SMTPlib
* Page Not Found(404)에러가 발생, 어떤 문제에서 발생할 가능성이 있을까?
    * Page not found이므로 url을 잘못 작성하여 대상 페이지를 찾을 수 없을때 발생 할 것.
    * 하나의 특정 이유를 꼽기는 힘들지만 가장 단순한 이유 일 수 있음

---

* 특정 모델의 데이터를 삭제하는 코드이다. 빈칸의 코드 완성
```python
def Delete_restaurant(request):
    res_id = request.POST['resId']
    delete_target = Restaurant.object.get(id=res_id)
    delete_target.delete()
    return HttpResponseRedirect(reverse('index'))
```
* 배포할 때 형상 관리 툴(git)을 이용하는 이유는?
    * 코드의 형상관리를 통해 변경점을 기록하고 지속적인 시스템 유지 보수(CD)와 지속적인 통합(CI)을 달성하기 위해서 사용