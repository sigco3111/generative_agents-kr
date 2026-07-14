# 검수: `v2/convo_to_thoughts_v1.txt`

- 원본: 479자
- 번역: 354자
- 보존된 코드 표식: 6/6

## 원본
```
convo_to_thoughts_v1.txt

Variables: 
!<INPUT 0>! -- init persona name
!<INPUT 1>! -- target persona name
!<INPUT 2>! -- convo string
!<INPUT 3>! -- init persona name
!<INPUT 4>! -- target persona name or "the conversation"

<commentblockmarker>###</commentblockmarker>
Here is the conversation that happened between !<INPUT 0>! and !<INPUT 1>!. 

!<INPUT 2>!

Summarize what !<INPUT 3>! thought about !<INPUT 4>! in one short sentence. The sentence needs to be in third person:

```

## 번역
```
convo_to_thoughts_v1.txt

Variables: 
!<INPUT 0>! -- 초기 인물 이름
!<INPUT 1>! -- 대상 인물 이름
!<INPUT 2>! -- 대화 문자열
!<INPUT 3>! -- 초기 인물 이름
!<INPUT 4>! -- 대상 인물 이름 또는 "대화"

<commentblockmarker>###</commentblockmarker>
!<INPUT 0>!와 !<INPUT 1>! 사이에서 일어난 대화는 다음과 같습니다.

!<INPUT 2>!

!<INPUT 3>!가 !<INPUT 4>!에 대해 생각한 내용을 한 문장으로 요약하세요. 문장은 3인칭으로 작성해야 합니다.

=== 끝 ===

```
