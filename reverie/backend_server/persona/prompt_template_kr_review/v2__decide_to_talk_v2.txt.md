# 검수: `v2/decide_to_talk_v2.txt`

- 원본: 508자
- 번역: 386자
- 보존된 코드 표식: 11/12

## MISSING 마커 (자동 검출)
- "no"

## 원본
```
decide_to_talk_v1.txt

<commentblockmarker>###</commentblockmarker>
Task -- given context, determine whether the subject will initiate a conversation with another. 
Format: 
Context: []
Question: []
Reasoning: []
Answer in "yes" or "no": []
---
Context: !<INPUT 0>! 
Right now, it is !<INPUT 1>!. !<INPUT 2>! and !<INPUT 3>! last chatted at !<INPUT 4>! about !<INPUT 5>!. 
!<INPUT 6>! 
!<INPUT 7>! 

Question: Would !<INPUT 8>! initiate a conversation with !<INPUT 9>!? 

Reasoning: Let's think step by step.
```

## 번역
```
decide_to_talk_v1.txt

<commentblockmarker>###</commentblockmarker>
작업 -- 주어진 컨텍스트를 바탕으로 대상이 다른 사람과 대화를 시작할지 여부를 판단하세요.
형식:
컨텍스트: []
질문: []
추론: []
답변을 "yes" 또는 "no" 로 출력하세요: []
---
컨텍스트: !<INPUT 0>!
현재는 !<INPUT 1>! 입니다. !<INPUT 2>!와 !<INPUT 3>!는 마지막으로 !<INPUT 4>!에 !<INPUT 5>!에 대해 대화했습니다.
!<INPUT 6>!
!<INPUT 7>!

질문: !<INPUT 8>!가 !<INPUT 9>!와 대화를 시작할까요?

추론: 단계별로 생각해 보겠습니다.
=== 끝 ===

```
