---
marp: true
---

### 가상환경 세팅 및 requirements
 1. 터미널(cmd창)에서 cd명령어를 통해 적절한 위치로 이동, mkdir 명령어를 통해 프로젝트를 진행할 폴더 생성
 2. 아나콘다를 사용할 경우 conda create -n [env이름] [python=3.x.x]를 통해 가상환경 생성, active를 통해 진입
 3. pip install 명령어를 통해 필요한 라이브러리 설치 ex) django, pandas..
 4. pip freeze를 통해 설치된 라이브러리와 버전을 확인할 수 있으며 pip freeze > requirements.txt로 해당 목록을 txt파일로 뽑아낼 수 있다.
 5. 추후 다른 환경에서 가상환경을 설치하거나 배포할 때, 해당 위치에 requirements.txt를 옮긴 뒤 pip install -r requirements.txt를 입력하면 목록의 모든 라이브러리가 한번에 설치된다.
    
- pycharm 내부의 기능이나 가상환경을 사용할 경우 터미널, 아나콘다의 기능은 대체될 수 있다.
- 라이브러리 교체가 있어 requirements를 변경해야할 경우 pip freeze > requirements.txt를 다시 실행하면 수정 가능

---

### HttpResponseRedirect, redirect
- ResponseRedirect는 첫번째 인자로 단순히 url만 입력될 수 있다
  - reverse를 이용해 특정 url의 이름을 통해 url을 가져와 전달
  ```
  return HttpResponseRedirect(reverse('index'))
  return HttpResponseRedirect(reverse('resDetailPage', kwargs={'res_id': resId}))
  ```
- redirect는 model, view, url 등 다양한 것을 인자로 전달해 줄 수 있다
  ```
  return redirect('main_index')
  ```

-> 일반적으로 redirect가 더 간결하게 사용될 수 있다

---

