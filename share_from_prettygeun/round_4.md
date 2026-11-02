# 라운드 4: 규칙+GRU 결합 (손 흔들기=규칙 angleC, 팔짱·박수=GRU r2m), 이어지는 영상

가설: GRU가 약한 손 흔들기를 규칙에 맡기면 이어지는 영상의 잘못된 판정이 줄어든다.
측정: pose_eval_v2.py로 영상 전체를 돌려 확률 0.7 이상 판정 횟수(기대 동작과 다른 판정을 셈). 규칙 손흔들기 횟수는 pose_eval_v3.py 3차 결과(runs/step9_wave/stock3·wvu3.jsonl).

| 영상 | 기대 | GRU r2m 단독 (@0.7) | GRU v6u 단독 (@0.7) | 결합: 팔짱·박수=r2m, 손 흔들기=규칙 angleC |
| --- | --- | --- | --- | --- |
| mk29963_arms_crossed_woman_livingroom.mp4 | arms_crossed | arms_crossed 1 | clap 1 | arms_crossed 1 |
| mk50643_arms_crossed_model.mp4 | arms_crossed | clap 3, wave 4 | clap 6 | clap 3 |
| applause_wikiconvention.webm | clap | clap 5, wave 3 | clap 3 | clap 5, wave(규칙) 2 |
| clapping_nhs.webm | clap(학습에 씀) | clap 2 | clap 2 | clap 2 |
| mk24214_clap_conference.mp4 | clap(학습에 씀) | clap 3, wave 1 | clap 1 | clap 3, wave(규칙) 2 |
| vtest.avi | idle(4동작 아님) | 0 | clap 2 | 0 |
| mk4519_idle_students_walking.mp4 | idle(4동작 아님) | 0 | clap 4 | 0 |
| mk460_idle_standing_woman.mp4 | idle(4동작 아님) | wave 1 | 0 | 0 |
| mk35954_classroom_raise_hands_a.mp4 | idle(4동작 아님) | wave 2 | clap 6 | wave(규칙) 1 |
| mk35968_classroom_raise_hands_b.mp4 | idle(4동작 아님) | clap 1, wave 1 | clap 7 | clap 1, wave(규칙) 2 |
| mk11553_raise_hand_question.mp4 | idle(4동작 아님) | clap 2, wave 1 | clap 4 | clap 2 |
| jumping_jacks_burpees.webm | idle(4동작 아님) | clap 7, wave 5 | arms_crossed 5, clap 6, wave 5 | clap 7, wave(규칙) 1 |
| handshake_tv.ogv | idle(4동작 아님) | clap 5, wave 4 | clap 7 | clap 5, wave(규칙) 2 |
| wave_example.webm | wave | clap 3 | clap 2 | clap 3, wave(규칙) 3 |
| wave_couch_2-5.5s.avi | wave | clap 1 | 0 | clap 1 |
| mk48998_wave_elderly_couple.mp4 | wave | wave 2 | clap 2 | wave(규칙) 1 |
| children_waving.webm | wave | clap 13, wave 23 | clap 17 | clap 13, wave(규칙) 2 |
| e1_s3_v1.avi | idle(4동작 아님) | 0 | 0 | 0 |
| e1_s3_v3.avi | idle(4동작 아님) | 0 | clap 1 | 0 |
| e3_s3_v1.avi | clap | clap 1 | 0 | clap 1 |
| e3_s3_v3.avi | clap | clap 1 | clap 1 | clap 1 |
| e4_s3_v1.avi | wave | wave 1 | 0 | wave(규칙) 1 |
| e4_s3_v3.avi | wave | wave 1 | clap 1 | wave(규칙) 1 |
| **기대와 다른 판정 합** | | 57 | 76 | 45 |

결과: 기대와 다른 판정이 r2m 단독 57 → 결합 45 (v6u 단독 76). 결합이 낫지만 팔벌려뛰기·악수 TV·교실 손 들기·아이들 손 흔들기에서 박수 오판정이 여전히 많음.
주의: 이 측정은 30fps 영상을 모든 프레임 그대로 GRU에 넣었는데, 모델은 15fps(30프레임=2초)로 학습함 → 실제 앱(초당 약 15장)보다 나쁘게 나왔을 수 있음. 라운드 5에서 실제 앱으로 다시 잼.
종합 점수 개선 없음 (라운드 3에 이어 2회 연속).
