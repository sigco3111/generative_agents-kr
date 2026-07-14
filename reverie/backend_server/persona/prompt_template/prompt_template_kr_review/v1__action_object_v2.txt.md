# 검수: `v1/action_object_v2.txt`

- 원본: 1127자
- 번역: 798자
- 보존된 코드 표식: 3/3

## 원본
```
Variables: 
!<INPUT 0>! -- curr action seq
!<INPUT 1>! -- Objects available

<commentblockmarker>###</commentblockmarker>
Current activity: sleep in bed
Objects available: {bed, easel, closet, painting}
Pick ONE most relevant object from the objects available: bed
---
Current activity: painting
Objects available: {easel, closet, sink, microwave}
Pick ONE most relevant object from the objects available: easel
---
Current activity: cooking
Objects available: {stove, sink, fridge, counter}
Pick ONE most relevant object from the objects available: stove
---
Current activity: watch TV
Objects available: {couch, TV, remote, coffee table}
Pick ONE most relevant object from the objects available: TV
---
Current activity: study
Objects available: {desk, computer, chair, bookshelf}
Pick ONE most relevant object from the objects available: desk
---
Current activity: talk on the phone
Objects available: {phone, charger, bed, nightstand}
Pick ONE most relevant object from the objects available: phone
---
Current activity: !<INPUT 0>!
Objects available: {!<INPUT 1>!}
Pick ONE most relevant object from the objects available:
```

## 번역
```
Variables: 
!<INPUT 0>! -- 현재 행동 순서
!<INPUT 1>! -- 사용 가능한 객체

<commentblockmarker>###</commentblockmarker>
현재 활동: 침대에서 잠자기
사용 가능한 객체: {bed, easel, closet, painting}
사용 가능한 객체 중 가장 관련성이 높은 하나를 선택하세요: bed
---
현재 활동: 그림 그리기
사용 가능한 객체: {easel, closet, sink, microwave}
사용 가능한 객체 중 가장 관련성이 높은 하나를 선택하세요: easel
---
현재 활동: 요리하기
사용 가능한 객체: {stove, sink, fridge, counter}
사용 가능한 객체 중 가장 관련성이 높은 하나를 선택하세요: stove
---
현재 활동: TV 시청
사용 가능한 객체: {couch, TV, remote, coffee table}
사용 가능한 객체 중 가장 관련성이 높은 하나를 선택하세요: TV
---
현재 활동: 공부하기
사용 가능한 객체: {desk, computer, chair, bookshelf}
사용 가능한 객체 중 가장 관련성이 높은 하나를 선택하세요: desk
---
현재 활동: 전화 통화
사용 가능한 객체: {phone, charger, bed, nightstand}
사용 가능한 객체 중 가장 관련성이 높은 하나를 선택하세요: phone
---
현재 활동: !<INPUT 0>!
사용 가능한 객체: {!<INPUT 1>!}
사용 가능한 객체 중 가장 관련성이 높은 하나를 선택하세요: 
=== 끝 ===

```
