# 검수: `v2/generate_event_triple_v1.txt`

- 원본: 844자
- 번역: 717자
- 보존된 코드 표식: 4/4

## 원본
```
generate_event_triple_v1.txt

Variables: 
!<INPUT 0>! -- Persona's full name. 
!<INPUT 1>! -- Current action description
!<INPUT 2>! -- Persona's full name. 

<commentblockmarker>###</commentblockmarker>
Task: Turn the input into (subject, predicate, object). 

Input: Sam Johnson is eating breakfast. 
Output: (Dolores Murphy, eat, breakfast) 
--- 
Input: Joon Park is brewing coffee.
Output: (Joon Park, brew, coffee)
---
Input: Jane Cook is sleeping. 
Output: (Jane Cook, is, sleep)
---
Input: Michael Bernstein is writing email on a computer. 
Output: (Michael Bernstein, write, email)
---
Input: Percy Liang is teaching students in a classroom. 
Output: (Percy Liang, teach, students)
---
Input: Merrie Morris is running on a treadmill. 
Output: (Merrie Morris, run, treadmill)
---
Input: !<INPUT 0>! is !<INPUT 1>!. 
Output: (!<INPUT 2>!,
```

## 번역
```
generate_event_triple_v1.txt

Variables: 
!<INPUT 0>! -- 인물의 전체 이름. 
!<INPUT 1>! -- 현재 행동 설명
!<INPUT 2>! -- 인물의 전체 이름. 

<commentblockmarker>###</commentblockmarker>
Task: 입력을 (주어, 서술어, 목적어) 형태로 변환하세요. 

Input: Sam Johnson은 아침을 먹고 있습니다. 
Output: (Dolores Murphy, 먹다, 아침) 
--- 
Input: Joon Park은 커피를 끓이고 있습니다. 
Output: (Joon Park, 끓이다, 커피)
---
Input: Jane Cook은 자고 있습니다. 
Output: (Jane Cook, 있다, 자다)
---
Input: Michael Bernstein은 컴퓨터로 이메일을 쓰고 있습니다. 
Output: (Michael Bernstein, 쓰다, 이메일)
---
Input: Percy Liang은 교실에서 학생들을 가르치고 있습니다. 
Output: (Percy Liang, 가르치다, 학생들)
---
Input: Merrie Morris은 러닝머신 위에서 뛰고 있습니다. 
Output: (Merrie Morris, 달리다, 러닝머신)
---
Input: !<INPUT 0>!은 !<INPUT 1>!이다. 
Output: (!<INPUT 2>!,
=== 끝 ===

```
