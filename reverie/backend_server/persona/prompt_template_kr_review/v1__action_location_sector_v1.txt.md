# 검수: `v1/action_location_sector_v1.txt`

- 원본: 2110자
- 번역: 1624자
- 보존된 코드 표식: 13/13

## 어색한 한국어 (자동 검출)
- 번역 안 된 'and' 발견 `...ouse, The Rose and Crown Pub, Hobb...`
- 번역 안 된 'and' 발견 `...Willows Market and Pharmacy}.
* 활동...`
- 번역 안 된 'and' 발견 `...tory, The Rose and Crown Pub, Hobb...`
- 번역 안 된 'and' 발견 `...Willows Market and Pharmacy}. 
* 활...`

## 원본
```
Variables: 
!<INPUT 0>! -- Persona name
!<INPUT 1>! -- Maze all possible sectors
!<INPUT 2>! -- Persona name
!<INPUT 3>! -- Persona living sector
!<INPUT 4>! -- Persona living sector arenas
!<INPUT 5>! -- Persona name
!<INPUT 6>! -- Persona current sector
!<INPUT 7>! -- Persona current sector arenas
!<INPUT 8>! -- curr action description
!<INPUT 9>! -- Persona name
<commentblockmarker>###</commentblockmarker>
Task -- choose an appropriate area  from the area options for a task at hand. 

Sam Kim lives in {Sam Kim's house} that has Sam Kim's room, bathroom, kitchen.
Sam Kim is currently in {Sam Kim's house} that has Sam Kim's room, bathroom, kitchen. 
Area options: {Sam Kim's house, The Rose and Crown Pub, Hobbs Cafe, Oak Hill College, Johnson Park, Harvey Oak Supply Store, The Willows Market and Pharmacy}.
* Stay in the current area if the activity can be done there. Only go out if the activity needs to take place in another place.
* Must be one of the "Area options," verbatim.
For taking a walk, Sam Kim should go to the following area: {Johnson Park}
---
Jane Anderson lives in {Oak Hill College Student Dormatory} that has Jane Anderson's room.
Jane Anderson is currently in {Oak Hill College} that has a classroom, library
Area options: {Oak Hill College Student Dormatory, The Rose and Crown Pub, Hobbs Cafe, Oak Hill College, Johnson Park, Harvey Oak Supply Store, The Willows Market and Pharmacy}. 
* Stay in the current area if the activity can be done there. Only go out if the activity needs to take place in another place.
* Must be one of the "Area options," verbatim.
For eating dinner, Jane Anderson should go to the following area: {Hobbs Cafe}
---
!<INPUT 0>! lives in {!<INPUT 1>!} that has !<INPUT 2>!.
!<INPUT 3>! is currently in {!<INPUT 4>!} that has !<INPUT 5>!. !<INPUT 6>!
Area options: {!<INPUT 7>!}. 
* Stay in the current area if the activity can be done there. Only go out if the activity needs to take place in another place.
* Must be one of the "Area options," verbatim.
!<INPUT 8>! is !<INPUT 9>!. For !<INPUT 10>!, !<INPUT 11>! should go to the following area: {
```

## 번역
```
Variables: 
!<INPUT 0>! -- 인물 이름
!<INPUT 1>! -- 미로 전체 가능한 구역
!<INPUT 2>! -- 인물 이름
!<INPUT 3>! -- 인물이 거주하는 구역
!<INPUT 4>! -- 인물이 거주하는 구역의 구역들
!<INPUT 5>! -- 인물 이름
!<INPUT 6>! -- 인물이 현재 있는 구역
!<INPUT 7>! -- 인물이 현재 있는 구역의 구역들
!<INPUT 8>! -- 현재 행동 설명
!<INPUT 9>! -- 인물 이름
<commentblockmarker>###</commentblockmarker>
Task -- 현재 작업에 맞는 적절한 지역을 영역 옵션 중에서 선택하세요. 

Sam Kim은 {Sam Kim's house}에 거주하며, 그 안에는 Sam Kim의 방, 욕실, 주방이 있습니다.
Sam Kim은 현재 {Sam Kim's house}에 있으며, 그 안에는 Sam Kim의 방, 욕실, 주방이 있습니다. 
지역 옵션: {Sam Kim's house, The Rose and Crown Pub, Hobbs Cafe, Oak Hill College, Johnson Park, Harvey Oak Supply Store, The Willows Market and Pharmacy}.
* 활동을 현재 지역에서 할 수 있으면 그곳에 머무르세요. 다른 장소에서 해야 할 경우에만 나가세요.
* 반드시 "Area options"에 있는 항목 중 하나여야 합니다.
산책을 위해서는 Sam Kim이 다음 지역으로 이동해야 합니다: {Johnson Park}
---
Jane Anderson은 {Oak Hill College Student Dormatory}에 거주하며, 그 안에는 Jane Anderson의 방이 있습니다.
Jane Anderson은 현재 {Oak Hill College}에 있으며, 그 안에는 강의실, 도서관이 있습니다.
지역 옵션: {Oak Hill College Student Dormatory, The Rose and Crown Pub, Hobbs Cafe, Oak Hill College, Johnson Park, Harvey Oak Supply Store, The Willows Market and Pharmacy}. 
* 활동을 현재 지역에서 할 수 있으면 그곳에 머무르세요. 다른 장소에서 해야 할 경우에만 나가세요.
* 반드시 "Area options"에 있는 항목 중 하나여야 합니다.
저녁을 먹기 위해서는 Jane Anderson이 다음 지역으로 이동해야 합니다: {Hobbs Cafe}
---
!<INPUT 0>!은 {!<INPUT 1>!}에 거주하며, 그 안에는 !<INPUT 2>!이(가) 있습니다.
!<INPUT 3>!은 현재 {!<INPUT 4>!}에 있으며, 그 안에는 !<INPUT 5>!이(가) 있습니다. !<INPUT 6>!
지역 옵션: {!<INPUT 7>!}. 
* 활동을 현재 지역에서 할 수 있으면 그곳에 머무르세요. 다른 장소에서 해야 할 경우에만 나가세요.
* 반드시 "Area options"에 있는 항목 중 하나여야 합니다.
!<INPUT 8>!은 !<INPUT 9>!입니다. !<INPUT 10>!을(를) 위해, !<INPUT 11>!은 다음 지역으로 이동해야 합니다: {

```
