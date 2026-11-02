# 정확도 개선 2차 라운드 3: gate_strict에서 팔짱을 놓친 원인 찾기

가설: gate_strict의 조건 중 하나가 팔짱을 막는다. 조건을 하나씩 풀어 원인을 찾는다.
공통: --model action_r2m.pt --gate-model action_l2r1.pt --gate-th 0.5 --ml-only arms_crossed,clap --ml-margin 0.3
- norule: 규칙 확인(--ml-rule) 없이 3번 연속
- vote2: 규칙 확인 있음, 연속 조건 3 → 2번

## 실제 앱 재현 (영상 2번 반복, GRU 판정 횟수)
| 영상 | 기대 | gate_strict (라운드 2) | norule | vote2 |
| --- | --- | --- | --- | --- |
| jumping_jacks_burpees.webm | 동작 아님 | 0 | 0 | 0 |
| mk35968_classroom_raise_hands_b.mp4 | 동작 아님 | 0 | 0 | 0 |
| mk11553_raise_hand_question.mp4 | 동작 아님 | 0 | clap 5 | 0 |
| vtest.avi | 동작 아님 | 0 | 0 | 0 |
| e8_s3_v1.avi | 동작 아님 | 0 | 0 | 0 |
| e8_s3_v3.avi | 동작 아님 | 0 | 0 | 0 |
| mk29963_arms_crossed_woman_livingroom.mp4 | 팔짱 | 0 | **arms_crossed 9** | 0 |
| applause_wikiconvention.webm | 박수 | clap 3 | clap 6 | clap 4 |
| wave_example.webm | 손 흔들기(규칙) | 0 | clap 7 | 0 |
| **GRU 오판정 합** | | 0 | 12 | 0 |
| **맞힌 팔짱·박수** | | 3 | 15 | 4 |

결과
- 팔짱을 막은 건 팔짱 규칙 확인(손목이 반대쪽 팔꿈치 아래팔 0.7배 안)이었다. 빼면 팔짱 9번을 맞힘. 이 영상에서는 팔짱 낀 손목이 팔꿈치 근처까지 안 가거나 가려져 있음.
- 반대로 박수 규칙 확인('박수 치는 사람'일 때만)은 질문 손 들기·손 흔들기 영상의 박수 오판정(12번)을 막아 주는 핵심 조건.
- 연속 조건 3 → 2는 팔짱 문제를 풀지 못함.
- 최고는 라운드 2의 gate_strict 유지(오판정 0). 개선 없음 1회.
다음: 규칙 확인을 박수에만 적용(--ml-rule-labels clap).
