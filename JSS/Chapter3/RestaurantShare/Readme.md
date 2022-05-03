---
marp: false
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

* DB의 참조 무결성을 해 지원하는 값
* `ForeignKey Field`가 바라보는 값이 삭제될 때 해당 요소를 처리하는 방법을 지정한다.
* Ex) `Category A`가 삭제되었다면, Restaurant FK중 `Category A`를 가지는 값에 대한 처리

| on_delete | 내용 |
|:--:|:--:|
|SET_DEFAULT | default로 설정해둔 field로 바꿔준다.|
|CASCADE|참조되는 모든 요소 삭제|
|PROTECT| 삭제되지 말아야 하는 곳에 사용하면 될듯, ProtectedError 발생|
|SET_NULL| 참조값을 null로 바꾼다. |