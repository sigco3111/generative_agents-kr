# 검수: `v3_ChatGPT/iterative_convo_v1.txt`

- 원본: 1110자
- 번역: 859자
- 보존된 코드 표식: 15/15

## 원본
```
iterative_convo_v1.txt

Variables: 
!<INPUT 0>! -- persona ISS
!<INPUT 1>! -- persona name
!<INPUT 2>! -- retrieved memory
!<INPUT 3>! -- past context
!<INPUT 4>! -- current location
!<INPUT 5>! -- current context
!<INPUT 6>! -- persona name
!<INPUT 7>! -- target persona name
!<INPUT 8>! -- curr convo
!<INPUT 9>! -- persona name
!<INPUT 10>! -- target persona name
!<INPUT 11>! -- persona name
!<INPUT 12>! -- persona name
!<INPUT 13>! -- persona name
<commentblockmarker>###</commentblockmarker>
Context for the task: 

PART 1. 
!<INPUT 0>!

Here is the memory that is in !<INPUT 1>!'s head: 
!<INPUT 2>!

PART 2. 
Past Context: 
!<INPUT 3>!

Current Location: !<INPUT 4>!

Current Context: 
!<INPUT 5>!

!<INPUT 6>! and !<INPUT 7>! are chatting. Here is their conversation so far: 
!<INPUT 8>!

---
Task: Given the above, what should !<INPUT 9>! say to !<INPUT 10>! next in the conversation? And did it end the conversation?

Output format: Output a json of the following format: 
{
"!<INPUT 11>!": "<!<INPUT 12>!'s utterance>",
"Did the conversation end with !<INPUT 13>!'s utterance?": "<json Boolean>"
}
```

## 번역
```
iterative_convo_v1.txt

Variables: 
!<INPUT 0>! -- 페르소나 ISS
!<INPUT 1>! -- 페르소나 이름
!<INPUT 2>! -- 검색된 기억
!<INPUT 3>! -- 과거 컨텍스트
!<INPUT 4>! -- 현재 위치
!<INPUT 5>! -- 현재 컨텍스트
!<INPUT 6>! -- 페르소나 이름
!<INPUT 7>! -- 대상 페르소나 이름
!<INPUT 8>! -- 현재 대화
!<INPUT 9>! -- 페르소나 이름
!<INPUT 10>! -- 대상 페르소나 이름
!<INPUT 11>! -- 페르소나 이름
!<INPUT 12>! -- 페르소나 이름
!<INPUT 13>! -- 페르소나 이름
<commentblockmarker>###</commentblockmarker>
작업을 위한 컨텍스트: 

파트 1. 
!<INPUT 0>!

!<INPUT 1>!의 머릿속에 있는 기억은 다음과 같습니다: 
!<INPUT 2>!

파트 2. 
과거 컨텍스트: 
!<INPUT 3>!

현재 위치: !<INPUT 4>!

현재 컨텍스트: 
!<INPUT 5>!

!<INPUT 6>!와 !<INPUT 7>!이 대화하고 있습니다. 지금까지의 대화 내용은 다음과 같습니다: 
!<INPUT 8>!

---
작업: 위 내용을 바탕으로, !<INPUT 9>!가 다음에 !<INPUT 10>!에게 무엇이라고 말해야 할까요? 그리고 대화가 종료되었나요?

출력 형식: 다음과 같은 형식의 json을 출력하세요: 
{
"!<INPUT 11>!": "<!<INPUT 12>!의 발언>",
"대화가 !<INPUT 13>!의 발언으로 종료되었나요?": "<json Boolean>"
}
=== 끝 ===

```
