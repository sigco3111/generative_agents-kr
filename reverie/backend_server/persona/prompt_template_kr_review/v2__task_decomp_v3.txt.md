# 검수: `v2/task_decomp_v3.txt`

- 원본: 2584자
- 번역: 1420자
- 보존된 코드 표식: 9/9

## 원본
```
task_decomp_v2.txt

Variables: 
!<INPUT 0>! -- Commonset
!<INPUT 1>! -- Surrounding schedule description
!<INPUT 2>! -- Persona first name
!<INPUT 3>! -- Persona first name
!<INPUT 4>! -- Current action
!<INPUT 5>! -- curr time range
!<INPUT 6>! -- Current action duration in min
!<INPUT 7>! -- Persona first names

<commentblockmarker>###</commentblockmarker>
Describe subtasks in 5 min increments. 
---
Name: Kelly Bronson
Age: 35
Backstory: Kelly always wanted to be a teacher, and now she teaches kindergarten. During the week, she dedicates herself to her students, but on the weekends, she likes to try out new restaurants and hang out with friends. She is very warm and friendly, and loves caring for others.
Personality: sweet, gentle, meticulous
Location: Kelly is in an older condo that has the following areas: {kitchen, bedroom, dining, porch, office, bathroom, living room, hallway}.
Currently: Kelly is a teacher during the school year. She teaches at the school but works on lesson plans at home. She is currently living alone in a single bedroom condo.
Daily plan requirement: Kelly is planning to teach during the morning and work from home in the afternoon.s

Today is Saturday May 10. From 08:00am ~09:00am, Kelly is planning on having breakfast, from 09:00am ~ 12:00pm, Kelly is planning on working on the next day's kindergarten lesson plan, and from 12:00 ~ 13pm, Kelly is planning on taking a break. 
In 5 min increments, list the subtasks Kelly does when Kelly is working on the next day's kindergarten lesson plan from 09:00am ~ 12:00pm (total duration in minutes: 180):
1) Kelly is reviewing the kindergarten curriculum standards. (duration in minutes: 15, minutes left: 165)
2) Kelly is brainstorming ideas for the lesson. (duration in minutes: 30, minutes left: 135)
3) Kelly is creating the lesson plan. (duration in minutes: 30, minutes left: 105)
4) Kelly is creating materials for the lesson. (duration in minutes: 30, minutes left: 75)
5) Kelly is taking a break. (duration in minutes: 15, minutes left: 60)
6) Kelly is reviewing the lesson plan. (duration in minutes: 30, minutes left: 30)
7) Kelly is making final changes to the lesson plan. (duration in minutes: 15, minutes left: 15)
8) Kelly is printing the lesson plan. (duration in minutes: 10, minutes left: 5)
9) Kelly is putting the lesson plan in her bag. (duration in minutes: 5, minutes left: 0)
---
!<INPUT 0>!
!<INPUT 1>!
In 5 min increments, list the subtasks !<INPUT 2>! does when !<INPUT 3>! is !<INPUT 4>! from !<INPUT 5>! (total duration in minutes !<INPUT 6>!): 
1) !<INPUT 7>! is
```

## 번역
```
task_decomp_v2.txt

변수:
!<INPUT 0>! -- 공통 컨텍스트
!<INPUT 1>! -- 주변 일정 설명
!<INPUT 2>! -- 페르소나 이름
!<INPUT 3>! -- 페르소나 이름
!<INPUT 4>! -- 현재 행동
!<INPUT 5>! -- 현재 시간 범위
!<INPUT 6>! -- 현재 행동 총 소요 시간 (분)
!<INPUT 7>! -- 페르소나 이름들

<commentblockmarker>###</commentblockmarker>
5분 단위로 하위 작업을 기술하세요.
---
이름: 이서연
나이: 27
배경: 이서연은 도시계획 석사과정 학생이며, 한강 자전거 동호회 회원이다. 평일에는 학교에서 공부하고, 주말에는 한강 자전거 라이딩을 즐긴다. 따뜻하고 사교적이며, 타인을 잘 챙기는 성격이다.
성격: 호기심 많음, 외향적, 세심함
위치: 이서연은 다음 구역이 있는 한강변 자전거 동호회 사무실에 있다: {사무실, 라커룸, 라운지, 옥상, 거실, 화장실}.
현재: 이서연은 도시계획 석사과정 중이며, 평일에는 학교에서 공부하고 주말에는 한강 자전거 코스를 라이딩한다. 현재 1인실 자취방에 혼자 살고 있다.
일일 계획 요구사항: 이서연은 평일 오전에는 학교에서 공부하고, 오후에는 집에서 논문을 작성하는 일과를 보낸다.

오늘은 5월 10일 토요일이다. 08:00 ~ 09:00에는 아침을 먹을 계획이고, 09:00 ~ 12:00에는 다음 학술 회의 발표 자료를 준비할 계획이며, 12:00 ~ 13:00에는 휴식할 계획이다.
이서연이 09:00 ~ 12:00에 다음 학술 회의 발표 자료를 준비할 때, 5분 단위로 수행하는 하위 작업을 나열하라 (총 소요 시간 180분):
1) 이서연은 학술 회의 발표 주제를 검토한다. (소요 시간: 15분, 남은 시간: 165분)
2) 이서연은 발표 아이디어를 브레인스토밍한다. (소요 시간: 30분, 남은 시간: 135분)
3) 이서연은 발표 개요를 작성한다. (소요 시간: 30분, 남은 시간: 105분)
4) 이서연은 발표 자료를 만든다. (소요 시간: 30분, 남은 시간: 75분)
5) 이서연은 잠시 휴식을 취한다. (소요 시간: 15분, 남은 시간: 60분)
6) 이서연은 발표 내용을 검토한다. (소요 시간: 30분, 남은 시간: 30분)
7) 이서연은 발표 자료의 최종 수정 작업을 한다. (소요 시간: 15분, 남은 시간: 15분)
8) 이서연은 발표 자료를 출력한다. (소요 시간: 10분, 남은 시간: 5분)
9) 이서연은 발표 자료를 가방에 넣는다. (소요 시간: 5분, 남은 시간: 0분)
---
!<INPUT 0>!
!<INPUT 1>!
5분 단위로, !<INPUT 2>!가 !<INPUT 5>!에 !<INPUT 4>!를 할 때 수행하는 하위 작업을 나열하라 (총 소요 시간 !<INPUT 6>!분):
1) !<INPUT 7>!는
```
