# 깃

개발이나 버전관리 할 게 없으면, 깃을 안쓰는 거임

마케팅 팀 프로젝트 , 연합동아리 프로젝트, 인턴십 개발 프로젝트

`git init`  깃은 내가 어떤 프로젝트 버전관리를 하고자 했을 때

버전 관리 시작 ?

그래서 데스크 탑이랑 오늘 아침에 나왔던 질문인데 





.git 삭제하면 모든 버전이 삭제가 된다



## 로컬 저장소 만들기 (연습)

### 1,프로젝트 폴더 

- 0706 폴더 생성하기

### 2. 해당 폴더에서 Git 버전 관리 시작하기

```bas
$ git init
```



### 3. 작업

- 별도의 빈 파일 하나 생성
- status도 확인하기 !

### 4. 작업이 완료되면 커밋하기





### 5.자유롭게 파일 만들고 수정하고 삭제하면서 커밋 3개 더 쌓아보기

- 총 커밋 4개





`git remote add orign https://github.com/kkinter/{}.git`

로컬 저장소에는 한번만 설정 해주면 된다. Origin 이름

`git remote -v`

원경저장소 이름



`git push origin master`

$ git push <원격저장소이름> <브랜치이름>

-원격 저장소로 로컬 저장소 변경 사항(커밋)을 올림 (push)

-로컬 폴더의 파일/폴더가 아닌 저장소의 버전(커밋)이 올라감





`Q. 저 파일 다섯개거든요.. 근데 깃 안됩니다.`

> 무엇을 잘못한 걸까요?
>
> > 커밋을 안했기 때문에



눈에 보이는 파일은 그냥 최신버전 커밋의 상태를 표현할 뿐,

절대로 파일/폴더를 관리하는 것이 아니라 버전 관리입니다 !!