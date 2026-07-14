# 검수: `v2/generate_next_convo_line_v1.txt`

- 원본: 537자
- 번역: 447자
- 보존된 코드 표식: 9/9

## 원본
```
generate_next_convo_line_v1.txt

Variables: 
!<INPUT 0>! -- agent name
!<INPUT 1>! -- agent iss
!<INPUT 2>! -- agent name
!<INPUT 3>! -- interlocutor name and description
!<INPUT 4>! -- prev convo
!<INPUT 5>! -- retrieve summary
!<INPUT 6>! -- agent name

<commentblockmarker>###</commentblockmarker>
Here is some basic information about !<INPUT 0>!.
!<INPUT 1>!

=== 
Following is a conversation between !<INPUT 2>! and !<INPUT 3>!. 

!<INPUT 4>!

(Note -- This is the only information that !<INPUT 5>! has: !<INPUT 6>!)

!<INPUT 7>!: "
```

## 번역
```
generate_next_convo_line_v1.txt

Variables: 
!<INPUT 0>! -- 에이전트 이름
!<INPUT 1>! -- 에이전트 ISS
!<INPUT 2>! -- 에이전트 이름
!<INPUT 3>! -- 대화 상대 이름 및 설명
!<INPUT 4>! -- 이전 대화
!<INPUT 5>! -- 요약 가져오기
!<INPUT 6>! -- 에이전트 이름

<commentblockmarker>###</commentblockmarker>
!<INPUT 0>!에 대한 기본 정보는 다음과 같습니다.
!<INPUT 1>!

=== 
!<INPUT 2>!와 !<INPUT 3>! 사이의 대화는 다음과 같습니다. 

!<INPUT 4>!

(참고 -- 이것은 !<INPUT 5>!가 가지고 있는 유일한 정보입니다: !<INPUT 6>!)

!<INPUT 7>!: "
=== 끝 ===

```
