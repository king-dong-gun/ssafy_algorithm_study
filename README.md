# SSAFY 16기 코테/알고리즘 스터디

2026.08 ~ ing

## 최초 환경 설정

VS Code 또는 IntelliJ의 터미널에서 아래 명령어를 실행합니다.

```bash
# 1. 저장소 복제
git clone https://github.com/king-dong-gun/ssafy_algorithm_study.git

# 2. 저장소로 이동
cd ssafy_algorithm_study

# 3. 본인 폴더만 보이도록 설정
git sparse-checkout init --cone
git sparse-checkout set <본인이름>

# 4. 본인 브랜치로 이동
git switch <본인이름>

# 5. 본인 폴더로 이동
cd <본인이름>

# 주차별 폴더 생성: 스터디 진행 후 week01, week02, week03......과 같이 생성
# 예: 1주차
mkdir week01
cd week01

# 문제 풀이 후 Commit / Push
# 변경된 파일 추가
git add .
# 변경분이 많은데 한 문제만 올릴 경우
git add 파일명

# 한 문제를 풀었을 경우
git commit -m "날짜_문제제목"

# 여러 문제를 풀었을 경우
git commit -m "날짜_문제제목 외 n문제"

# 최초 1회 Push
git push --set-upstream origin <본인이름>
# 최초 Push 이후부터는 아래 명령어만 사용
git push
```
```text
※ master 브랜치에는 직접 Push하지 않습니다.
주차별 문제 풀이가 끝나면 본인 브랜치에서 master 브랜치로 PR을 생성합니다.
```

GitHub 저장소 접속

GitHub의 ssafy_algorithm_study 저장소에 접속합니다.

Push 직후 저장소 상단에 아래와 같이 Compare & pull request 버튼이 나타나면 클릭합니다.

Compare & pull request
📷 이미지
![Compare & pull request](./images/pr01.png)
PR 브랜치 확인

Pull Request 생성 화면에서 브랜치가 다음과 같이 설정되어 있는지 확인합니다.

base: master  ←  compare: <본인이름>

예:

base: master  ←  compare: donggun
base : 최종적으로 코드를 합칠 브랜치
compare : 내가 작업한 브랜치

즉,

본인 브랜치
      ↓
    master

방향으로 설정합니다.

📷 이미지
![PR 브랜치 설정](./images/pr02.png)
PR 작성

PR 제목은 아래와 같이 작성합니다.

날짜_주차

예:

260813_week01

내용에는 이번 주에 해결한 문제를 간단하게 작성합니다.

예:

## 문제 풀이

- 문자열 출력하기
- 문자열 섞기
- 문자열 겹쳐쓰기
- 홀짝 구분하기

작성 후 Create pull request 버튼을 클릭합니다.

📷 이미지
![Create pull request](./images/pr03.png)
팀장 PR Merge

스터디원이 PR을 생성하면 팀장이 내용을 확인합니다.

Pull requests
→ 해당 PR 선택
→ Files changed 확인

문제가 없다면 아래 버튼을 클릭합니다.

Merge pull request

이후

Confirm merge

를 클릭하면 본인 브랜치의 변경사항이 master 브랜치에 반영됩니다.

전체 흐름
본인 브랜치에서 문제 풀이
        ↓
git add .
        ↓
git commit
        ↓
git push
        ↓
Pull Request 생성
        ↓
본인 브랜치 → master
        ↓
팀장 확인
        ↓
Merge
        ↓
master 반영

⚠️ 개인 작업은 항상 본인 브랜치에서 진행하고, master 반영은 Pull Request를 통해 진행합니다.
