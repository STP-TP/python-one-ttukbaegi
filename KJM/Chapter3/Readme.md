---
marp: true
---

## url.py 경로잡을 때 주의!
```
urlpatterns = [
    ...
    path('restaurantDetail/updatePage/update', views.update_restaurant, name='resUpdate'),
    path('restaurantDetail/updatePage/<str:res_id>', views.restaurant_update, name='resUpdatePage'),
    ...
]
```
 - ./updatePage/update 경로가 updatePage/str:res_id 보다 아래에 있으면 에러 발생
 - urlpattern이 발생할 때 updatePage/까지 간 뒤 update로 넘어가지 않고 res_id로 처리될 수 있기 때문!

---
 
 ## ASK

 - 장고 모델 구성 때 다른 요소를 참조하는 요소는 무엇으로 정의되는가?
   - 외래키(Foreign Key)
     - 자기 자신 참조 가능 : 자기참조 or 재귀적 외래키
     - 하나의 테이블이 여러개의 외래키 포함 가능
   ```python
   class Restaurant(models.Model):
       category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=3)
       restaurnat_name = models.CharField(max_length = 100)
       ...
   ```


---

 ## ASK

 - 장고 모델 구성 때 다른 요소를 참조하는 요소를 정의할 때 함께 사용되는 on_delete 속성에 대한 기댓값으로는 어떠한 것들이 존재하며, 그 쓰임새는 어떻게 되는가?

   - CASCADE : 해당 데이터를 참조하는 요소 모두 삭제
   - RESTRICT : 참조하는 요소가 있을 경우 에러 발생
   - SET NULL : 참조하는 요소를 전부 NULL로
   - SET_DEFAULT : 참조하는 요소를 전부 DEFAULT 값으로(DEFAULT 지정 필수)
   - NO ACTION : 아무것도 하지 않음(DBMS에서 참조 무결성 검사 -> 성공시 실행, 실패시 캔슬)

---

 ## ASK

 - 장고 모델 대신 SQL의 경우

   - CASCADE : 해당 데이터를 참조하는 요소 모두 삭제
   - PROTECT : 참조하는 요소가 있을 경우 에러 발생
   - SET_NULL : 참조하는 요소를 전부 NULL로
   - SET_DEFAULT : 참조하는 요소를 전부 DEFAULT 값으로(DEFAULT 지정 필수)
   - SET() : SET에 설정된 함수 실행시켜 참조
   - DO_NOTHING : 아무것도 하지 않음

---

 ## ASK

 - 이메일 발송 기능을 구현하는 데 Django.core와 관련된 라이브러리 이전에 사용한 라이브러리는 어떤 것인가?
   - SMTPlib (Simpoe Mail Transfer Protocol)
<p>

 - 프로젝트를 진행 중 Page not Found(404)에러가 발생했다. 어떤 문제에 의해서 발생할 가능성이 있을까?
   - '참조하는 url에 대한 정보가 없을 때'가 가장 높은 확률
<p>

 - 배포할 때 형상관리 툴(ex, git)을 이용하는 이유는 무엇인가?
   - 시스템 유지보수, 수정 및 배포 용이

---

 ## ASK

 - 다음 코드는 특정 모델의 데이터를 삭제하는 함수이다. 빈칸의 코드를 완성해보자
 ```python
 def Delete_restaurant(request):
     res_id = request.POST['resId']
     #
     # 이곳에 들어갈 코드를 구현하시오.
     #
     return HttpResponseRedirect(reverse('index'))
 ```

 ---

  ## ASK

 - 다음 코드는 특정 모델의 데이터를 삭제하는 함수이다. 빈칸의 코드를 완성해보자
 ```python
 def Delete_restaurant(request):
     res_id = request.POST['resId']
     restaurant = Restaurant.objects.get(id = res_id)
     restaurant.delete()
     return HttpResponseRedirect(reverse('index'))
 ```

 ---
 