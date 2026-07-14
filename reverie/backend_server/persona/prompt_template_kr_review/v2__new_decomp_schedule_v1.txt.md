# 검수: `v2/new_decomp_schedule_v1.txt`

- 원본: 739자
- 번역: 605자
- 보존된 코드 표식: 13/13

## 원본
```
new_decomp_schedule_v1.txt

Variables: 
!<INPUT 0>! -- persona name 
!<INPUT 1>! -- start hour
!<INPUT 2>! -- end hour 
!<INPUT 3>! -- original plan
!<INPUT 4>! -- persona name
!<INPUT 5>! -- new event
!<INPUT 6>! -- new event duration
!<INPUT 7>! -- persona name 
!<INPUT 8>! -- start hour
!<INPUT 9>! -- end hour 
!<INPUT 10>! -- end hour 
!<INPUT 11>! -- new schedule init 


<commentblockmarker>###</commentblockmarker>
Here was !<INPUT 0>!'s originally planned schedule from !<INPUT 1>! to !<INPUT 2>!. 
!<INPUT 3>!

But !<INPUT 4>! unexpectedly ended up !<INPUT 5>! for !<INPUT 6>! minutes. Revise !<INPUT 7>!'s schedule from !<INPUT 8>! to !<INPUT 9>! accordingly (it has to end by !<INPUT 10>!). 
The revised schedule:
!<INPUT 11>!
```

## 번역
```
new_decomp_schedule_v1.txt

Variables: 
!<INPUT 0>! -- 페르소나 이름
!<INPUT 1>! -- 시작 시간
!<INPUT 2>! -- 종료 시간
!<INPUT 3>! -- 원래 계획
!<INPUT 4>! -- 페르소나 이름
!<INPUT 5>! -- 새 이벤트
!<INPUT 6>! -- 새 이벤트 기간
!<INPUT 7>! -- 페르소나 이름
!<INPUT 8>! -- 시작 시간
!<INPUT 9>! -- 종료 시간
!<INPUT 10>! -- 종료 시간
!<INPUT 11>! -- 새 일정 초기화


<commentblockmarker>###</commentblockmarker>
다음은 !<INPUT 0>!의 원래 계획된 일정으로, !<INPUT 1>!부터 !<INPUT 2>!까지입니다. 
!<INPUT 3>!

하지만 !<INPUT 4>!가 예상치 못하게 !<INPUT 5>!를 !<INPUT 6>!분 동안 진행했습니다. !<INPUT 7>!의 일정을 !<INPUT 8>!부터 !<INPUT 9>!까지에 맞게 수정하세요 ( !<INPUT 10>!까지 끝나야 합니다). 
수정된 일정:
!<INPUT 11>!
=== 끝 ===

```
