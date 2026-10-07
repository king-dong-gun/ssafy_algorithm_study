# SSAFY 16기 코테/알고리즘 스터디

2026.08 ~ ing

스터디원: `김동건`, `김동준`, `정승원`, `최윤석`

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

<details>
<summary>📌 Issue 생성 방법 보기</summary>

## 1. Issues 탭 클릭
![issue01.png](./images/issue03.png)
## 2. New issue 클릭
![issue01.png](./images/issue02.png)
## 3. Issue 작성
> 이슈 제목, 이슈 설명 작성 이후 create

![issue01.png](./images/issue01.png)

## 4. Issue 생성 후 생성된 Issue 번호를 확인
![issue01.png](./images/issue04.png)
> 위의 이슈는 #30이므로 #30 기준으로 작성하겠음

## 5. 알고리즘 구현 및 작업 후 `git add.`

## 6. 이후 커밋메시지 작성 시 
### `Resolves #이슈 번호/feat: 날짜_문제번호_문제제목`
> 위의 이슈가 #30이므로 #30기준으로 리드미 작성하겠음
> 
> 1. `git add.`
> 
> 2. `git commit -m "Resolves #이슈 번호/feat: 날짜_문제번호_문제제목 외 n문제"`
> 
> 3. `git push origin 자신의 브랜치`

![issue01.png](./images/issue05.png)

## 7. 평소처럼 pr 생성화면이 나오면 머지하면 이슈는 알아서 닫힌다. 만약 자기 로컬에 메인에 없는 기록이 있으면 아래 사진처럼 뜨므로 여기서 pr를 생성하면 된다.

![issue01.png](./images/issue06.png)

## 8. 이후 pr을 생성 후 머지하면 이슈는 닫힌다.
제목은 알아서 커밋메세지로 들어간다.

![issue01.png](./images/issue07.png)

![issue01.png](./images/issue08.png)

## 9. 이후 이슈에 들어가보면 닫힌걸 확인이 가능하다.
![issue01.png](./images/issue09.png)

</details>

<details>
<summary>📌 PR 생성 방법 보기</summary>

## 1. Compare & pull request 클릭

![Compare & pull request](./images/pr01.png)

## 2. 브랜치 확인

![PR 브랜치 설정](./images/pr07.png)
> 반드시 자신의 브랜치에서 해야함
> 브랜치명 왼쪽에 `*` 떠 있으면 현재 브랜치
> 

## 3. 기능 담당자 설정
![Assignees](./images/pr02.png)
![Assignees](./images/pr03.png)


> 라벨은 추후 수정함 일단은 feature 사용
> 
## 4. Create pull request 클릭

![Create pull request](./images/pr04.png)

## 5. Merge pull request 클릭
![Merge pull request](./images/pr05.png)

## 6. Merge가 됐는지 확인
![Merged](./images/pr06.png)
</details>

### 만약 잘 안되면 `김동건`한테 mm이나 카톡 주셈
