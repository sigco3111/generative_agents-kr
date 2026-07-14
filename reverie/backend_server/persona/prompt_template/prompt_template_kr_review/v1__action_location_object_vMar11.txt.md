# 검수: `v1/action_location_object_vMar11.txt`

- 원본: 1450자
- 번역: 1152자
- 보존된 코드 표식: 10/10

## 원본
```
Variables: 
!<INPUT 0>! -- Persona name
!<INPUT 1>! -- Persona's current arena
!<INPUT 2>! -- Persona's current sector
!<INPUT 3>! -- Persona name
!<INPUT 4>! -- target sector
!<INPUT 5>! -- Persona's sector's all arenas (minus no access)
!<INPUT 6>! -- Curr action seq
!<INPUT 7>! -- Persona name
!<INPUT 8>! -- Persona's current sector

<commentblockmarker>###</commentblockmarker>
Jane Anderson is in kitchen in Jane Anderson's house.
Jane Anderson is going to Jane Anderson's house that has the following areas: {kitchen,  bedroom, bathroom}
Stay in the current area if the activity can be done there. Never go into other people's rooms unless necessary.
For cooking, Jane Anderson should go to the following area in Jane Anderson's house:
Answer: {kitchen}
---
Tom Watson is in common room in Tom Watson's apartment. 
Tom Watson is going to Hobbs Cafe that has the following areas: {cafe}
Stay in the current area if the activity can be done there. Never go into other people's rooms unless necessary.
For getting coffee, Tom Watson should go to the following area in Hobbs Cafe:
Answer: {cafe}
---

!<INPUT 0>! is going to !<INPUT 1>! that has the following areas: {!<INPUT 2>!}
* Stay in the current area if the activity can be done there. 
* NEVER go into other people's rooms unless necessary.
!<INPUT 3>! is !<INPUT 4>!. For !<INPUT 5>!, !<INPUT 6>! should go to the following area in !<INPUT 7>! (MUST pick one of {!<INPUT 8>!}):
Answer: {
```

## 번역
```
Variables: 
!<INPUT 0>! -- Persona name
!<INPUT 1>! -- Persona's current arena
!<INPUT 2>! -- Persona's current sector
!<INPUT 3>! -- Persona name
!<INPUT 4>! -- target sector
!<INPUT 5>! -- Persona's sector's all arenas (minus no access)
!<INPUT 6>! -- Curr action seq
!<INPUT 7>! -- Persona name
!<INPUT 8>! -- Persona's current sector

<commentblockmarker>###</commentblockmarker>
Jane Anderson은 Jane Anderson의 집에 있는 주방에 있습니다.
Jane Anderson은 다음 구역을 가진 Jane Anderson의 집으로 이동합니다: {kitchen,  bedroom, bathroom}
활동을 현재 구역에서 수행할 수 있다면 그곳에 머무르세요. 필요하지 않은 경우 타인의 방에 들어가지 마세요.
요리를 위해 Jane Anderson은 Jane Anderson의 집에서 다음 구역으로 이동해야 합니다:
Answer: {kitchen}
---
Tom Watson은 Tom Watson의 아파트에 있는 공용실에 있습니다.
Tom Watson은 다음 구역을 가진 Hobbs Cafe로 이동합니다: {cafe}
활동을 현재 구역에서 수행할 수 있다면 그곳에 머무르세요. 필요하지 않은 경우 타인의 방에 들어가지 마세요.
커피를 얻기 위해 Tom Watson은 Hobbs Cafe에서 다음 구역으로 이동해야 합니다:
Answer: {cafe}
---

!<INPUT 0>!은 다음 구역을 가진 !<INPUT 1>!으로 이동합니다: {!<INPUT 2>!}
* 활동을 현재 구역에서 수행할 수 있다면 그곳에 머무르세요. 
* 필요하지 않은 경우 타인의 방에 절대 들어가지 마세요.
!<INPUT 3>!은 !<INPUT 4>!입니다. !<INPUT 5>!에 대해, !<INPUT 6>!은 !<INPUT 7>!에서 다음 구역으로 이동해야 합니다 (다음 중 하나를 반드시 선택하세요: {!<INPUT 8>!}):
Answer: {
=== 끝 ===

```
