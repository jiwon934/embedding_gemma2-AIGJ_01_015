# 정확도 개선 2차 라운드 2: 2단계 판정(문지기 + 동작 종류)과 판정 거부

가설: other 클래스가 있는 l2r1은 "동작인지 아닌지"를 잘 가리고, r2m은 팔짱을 잘 맞힌다. l2r1을 문지기로, r2m을 동작 종류 판정에 쓰면 둘의 장점을 합칠 수 있다.
앱: pose_app_v6.py (pose_app_v5.py 복사본 + --gate-model). 문지기가 idle/other라고 확률 0.5 이상으로 말하면 r2m 판정을 버림.
- gate: --model action_r2m.pt --gate-model action_l2r1.pt --gate-th 0.5
- gate_strict: gate + --ml-only arms_crossed,clap(손 흔들기는 규칙만) --ml-margin 0.3(1·2위 확률 차이) --ml-vote 3(3번 연속 같은 예측, 약 1초) --ml-rule(박수는 '박수 치는 사람'일 때만, 팔짱은 손목이 반대쪽 팔꿈치 근처일 때만)

## 실제 앱 재현 (영상 2번 반복, GRU가 낸 판정 횟수)
| 영상 | 기대 | l2r1 단독(라운드 1) | gate | gate_strict |
| --- | --- | --- | --- | --- |
| jumping_jacks_burpees.webm | 동작 아님 | 0 | wave 6 | 0 |
| mk35968_classroom_raise_hands_b.mp4 | 동작 아님 | wave 3 | wave 2 | 0 |
| mk11553_raise_hand_question.mp4 | 동작 아님 | wave 4, clap 2 | clap 6 | 0 |
| vtest.avi | 동작 아님 | 0 | 0 | 0 |
| e8_s3_v1.avi | 동작 아님 | 0 | 0 | 0 |
| e8_s3_v3.avi | 동작 아님 | wave 3 | wave 4, clap 1 | 0 |
| mk29963_arms_crossed_woman_livingroom.mp4 | 팔짱 | arms_crossed 3, clap 2 | **arms_crossed 13** | 0 |
| applause_wikiconvention.webm | 박수 | clap 7, wave 8 | clap 9, wave 8 | **clap 3** |
| wave_example.webm | 손 흔들기(규칙이 맡음) | wave 8, clap 12 | clap 9 | 0 (규칙 손흔들기 11) |
| **동작 아닌 영상 6개의 GRU 오판정** | | 12 | 19 | **0** |
| 맞힌 / 틀린 GRU 판정 (팔짱·박수·손 흔들기 영상) | | 18 / 22 | 22 / 17 | 3 / 0 |

결과
- gate: 팔짱을 13번 맞혀 가장 잘 잡지만, 동작 아닌 영상의 오판정이 19로 l2r1 단독(12)보다 많음.
- gate_strict: GRU 오판정 0으로 규칙만 쓸 때와 같으면서 박수를 3번 맞힘 → 처음으로 "규칙보다 오판정이 많지 않고 박수를 맞히는" 조합. 단 팔짱은 0(놓침).
- 최고 갱신: gate_strict (오판정 0 유지하며 박수 검출 추가).
다음: 팔짱을 놓친 원인(팔짱 규칙 확인, 3번 연속 조건, 확률 차이 조건 중 무엇인지)을 하나씩 풀어 보기.
