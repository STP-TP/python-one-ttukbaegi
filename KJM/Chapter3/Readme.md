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

## 장고 모델 구성 중 on_delete 속성은 어떤 것이 있는가

 - CASCADE : 해당 데이터를 참조하는 요소 모두 삭제
 - PROTECT : 참조하는 요소가 있을 경우 에러 발생
 - SET_NULL : 참조하는 요소를 전부 NULL로
 - SET_DEFAULT : 참조하는 요소를 전부 DEFAULT 값으로(DEFAULT 지정 필수)
 - SET() : SET에 설정된 함수 실행시켜 참조
 - DO_NOTHING : 아무것도 하지 않음
 
 ---
 
 