---
marp: true
---

## MVC pattern

![](/Chapter2/imgs/mvc_pattern.png)
    * Model(models.py): Database를 의미( 혹은 DB와 연결하는 객체)
    * View([Template(HTML)](/Chapter2/ToDoList/my_to_do_app/templates/)): 사용자에게 보여지는 UI로 보통 프론트엔드(HTML, js)
    * Control(view.py): UI를 통해서 내부 제어를 하기 위한 객체

---
## Django에서의 경로

**서버로 들어오는 domain은 제외하고 서버 내에서의 상대경로만 취급**

* \urls.py
    ![](/JSS/Chapter2/imgs/root_urls_py.png)
    * path('', ~~): url을 include내의 경로로 확장
* \app_name\urls.py
    ![](/JSS/Chapter2/imgs/app_urls_py.png)
    * path('', ~~): url의 메인(index) view를 보여주도록
    
---

## Django View(Control)

* render: 주어진 템플릿을 context와 결합하여 객체를 반환시키는 함수
* HttpResponse: 인자로 받은 문자열을 사용자에게 보여주는 함수
    * Tag 사용하여 반환도 가능
        ```python
        response = HttpResponse()
        response.write("<p>Here's the text of the web page.</p>")
        ```

---

## Django View(Control)
* HttpResponseRedirect: HttpResponse의 subclass
    * 매개변수로 Redirect될 주소를 입력
    * Redirect: re + direct -> 서버에서 다시 요청할 주소를 알려주는것(페이지 이동)
    * URL 입력 가능
    ```html
    https://www.yahoo.com/search/
    /search/
    search/
    ```
* reverse: 서버 코드에서 url처럼 사용 할 수 있는 함수
    * url에서 name을 이용하여 search
    ![](/JSS/Chapter2/imgs/app_urls_py.png)

---

## SQLite, MySQL, PostgreSQL...
**기본적으로 설정된 SQLite**
* dbshell: SQLite 커맨드라인을 실행하기 위한 명령어
    * `.help`, `.tables` 등을 사용
* 다른 DB 사용 시
    * `python manage.py --database DATABASE`
    * setting.py 에서 `DATABASES` 설정 필요

---

## Django template(View)

* 별도의 Template을 사용 할 수 있음
* Default는 `Django Template Language`

    1. Variable
        ```html
        {{ variable }} (O)
        {{ vari_able }} (O)
        {{ _variable }} (X)
        {{ vari.able }} (X)
        ```
        * `.`은 변수의 속성에 Access
    2. For 구문
        ```html
        {% for story in story_list %}
        <h2> 이 구문도 for에 적용이 됩니다 </h2>
        {% endfor %}
        ```
    
---

## Django template(View)
* **Reference**
    1. [Django template language](https://docs.djangoproject.com/en/4.0/ref/templates/language/)
    2. [template tag 정리](https://goodmorningcody.wordpress.com/tag/django/)

---
## ```{%csrf_token%}``` - 책에서 제공된 index.html에 포함된 코드
### CSRF(Cross Site Request Forgery)
* 웹사이트 취약점 공격
* 사용자가 자신의 의지와 무관하게 CRUD하여 웹사이트에 요청하게 하는 공격  

---

### POST 요청에 대해서만 csrf token발급, 체크
![](/JSS/Chapter2/imgs/html_post_csrf_token.png)
* `<form>`태그 안에 `{% csrf_token %}` 태그를 사용
* 동작과정
    ```
    1. 페이지에 접속하면 Django에서 자동으로 csrf_token을 클라이언트로 전송, cookie에 저장
    2. 사용자가 form 제출버튼 클릭
    3. form의 정보와 함께 cookie의 csrf_token정보 전송(POST)
    4. 유효성 검증 후 검증된 경우에만 요청 처리
    ```
---

## .Gitignore
* 일반적인 ignore
    * abc.txt
    * /exclude/
    * /notimport/abc.txt
    * *.py

* Migrations folder 무시하기
    * path: /TodoList/my_to_do_app/migrations/*.*
    * `/migrations/`: Root 기준 mirgrations만 제외
    * `*/migrations/`: 반응 없음

* `**/migrations/`: **하위폴더 내에 있는 migrations 폴더 무시**

---

## 이미 추적중인 파일 Gitignore 시키기
