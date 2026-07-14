# 검수: `v1/action_location_sector_v1.txt`

- 원본: 2110자
- 번역: 326자
- 보존된 코드 표식: 11/13

## MISSING 마커 (자동 검출)
- !<INPUT 11>!
- !<INPUT 10>!

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
!<INPUT 0>! -- 페르소나 이름
!<INPUT 1>! -- 미로의 모든 가능한 구역
!<INPUT 2>! -- 페르소나 이름
!<INPUT 3>! -- 페르소나 거주 구역
!<INPUT 4>! -- 페르소나 거주 구역 시설
!<INPUT 5>! -- 페르소나 이름
!<INPUT 6>! -- 페르소나 현재 구역
!<INPUT 7>! -- 페르소나 현재 구역 시설
!<INPUT 8>! -- 현재 행동 설명
!<INPUT 9>! -- 페르소나 이름
<commentblockmarker>###</commentblockmarker>
Task -- 현재 과제

```
