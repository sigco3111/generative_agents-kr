# 검수: `v2/create_conversation_v2.txt`

- 원본: 1071자
- 번역: 847자
- 보존된 코드 표식: 17/17

## 어색한 한국어 (자동 검출)
- 조사 어색: ~을이 연속 `...있습니다. 지금 그들은 무엇을 이야기할까요?

!<INPUT...`

## 원본
```
create_conversation_v2.txt

Variables: 
!<INPUT 0>! -- init_persona iss
!<INPUT 1>! -- target_persona iss

!<INPUT 2>! -- init_persona_name
!<INPUT 3>! -- target_persona_name
!<INPUT 4>! -- init_persona's thoughts

!<INPUT 5>! -- target_persona_name
!<INPUT 6>! -- init_persona_name
!<INPUT 7>! -- target_persona's thoughts

!<INPUT 8>! -- current time
!<INPUT 9>! -- init_persona curr action description
!<INPUT 10>! -- target_persona curr action description

!<INPUT 11>! -- previous convo

!<INPUT 12>! -- init_persona_name
!<INPUT 13>! -- target_persona_name
!<INPUT 14>! -- curr_location name
!<INPUT 15>! -- init_persona_name

<commentblockmarker>###</commentblockmarker>
We have two characters. 

Character 1. 
!<INPUT 0>!

Character 2. 
!<INPUT 1>!
---
Context: 
Here is what !<INPUT 2>! thinks about !<INPUT 3>!: 
!<INPUT 4>!
Here is what !<INPUT 5>! thinks about !<INPUT 6>!:
!<INPUT 7>!
Currently, it is !<INPUT 8>!
-- !<INPUT 9>!
-- !<INPUT 10>!
!<INPUT 11>!

!<INPUT 12>! and !<INPUT 13>! are in !<INPUT 14>!. What would they talk about now?

!<INPUT 15>!: "
```

## 번역
```
create_conversation_v2.txt

Variables: 
!<INPUT 0>! -- 초기 페르소나 iss
!<INPUT 1>! -- 목표 페르소나 iss

!<INPUT 2>! -- 초기 페르소나 이름
!<INPUT 3>! -- 목표 페르소나 이름
!<INPUT 4>! -- 초기 페르소나의 생각

!<INPUT 5>! -- 목표 페르소나 이름
!<INPUT 6>! -- 초기 페르소나 이름
!<INPUT 7>! -- 목표 페르소나의 생각

!<INPUT 8>! -- 현재 시간
!<INPUT 9>! -- 초기 페르소나 현재 행동 설명
!<INPUT 10>! -- 목표 페르소나 현재 행동 설명

!<INPUT 11>! -- 이전 대화

!<INPUT 12>! -- 초기 페르소나 이름
!<INPUT 13>! -- 목표 페르소나 이름
!<INPUT 14>! -- 현재 위치 이름
!<INPUT 15>! -- 초기 페르소나 이름

<commentblockmarker>###</commentblockmarker>
두 명의 인물이 있습니다. 

인물 1. 
!<INPUT 0>!

인물 2. 
!<INPUT 1>!
---
상황: 
다음은 !<INPUT 2>!가 !<INPUT 3>!에 대해 생각하는 내용입니다: 
!<INPUT 4>!
다음은 !<INPUT 5>!가 !<INPUT 6>!에 대해 생각하는 내용입니다:
!<INPUT 7>!
현재 시각은 !<INPUT 8>!입니다.
-- !<INPUT 9>!
-- !<INPUT 10>!
!<INPUT 11>!

!<INPUT 12>!와 !<INPUT 13>!은 !<INPUT 14>!에 있습니다. 지금 그들은 무엇을 이야기할까요?

!<INPUT 15>!:

```
