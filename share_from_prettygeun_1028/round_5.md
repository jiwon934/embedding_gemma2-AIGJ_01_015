# 라운드 5: 실제 앱(pose_app_v4.py --model models/action_r2m.pt)에서 GRU 오판정

가설: 학습과 같은 15fps 안팎에서 돌리면 GRU 오판정이 줄어 실시간 화면에 켤 수 있다.
측정: runs/step9_hs/live_repro.sh로 영상 하나를 2번 반복 재생하며 앱의 동작 기록을 셈. 앱에서는 GRU 판정이 규칙 판정을 덮어씀.

| 영상 | 기대 | 앱 fps | 동작 기록 (2회 반복) |
| --- | --- | --- | --- |
| mk29963_arms_crossed_woman_livingroom.mp4 | 팔짱 | 15.1 | arms_crossed 1 |
| applause_wikiconvention.webm | 박수 | 12.9 | clap 10, wave 8, 만세 5, 한팔들기 1, 손흔들기 1 |
| jumping_jacks_burpees.webm | 팔벌려뛰기 (4동작 아님) | 18.1 | clap 13, wave 7, 만세 4, 한팔들기 1 |
| handshake_tv.ogv | 악수 (4동작 아님) | 20.9 | clap 11, wave 4, 손흔들기 1 |
| mk35968_classroom_raise_hands_b.mp4 | 손 들기 (4동작 아님) | 12.7 | wave 3, 한팔들기 1 |
| vtest.avi | 걷기 (4동작 아님) | 19.9 | 0 |
| wave_example.webm | 손 흔들기 3명 | 14.1 | clap 8, 손흔들기 2 |

결과: 팔짱(1)·걷기(0)는 맞지만 4동작이 아닌 영상에서 오판정이 많음(팔벌려뛰기 clap 13·wave 7, 악수 TV clap 11·wave 4), 손 흔들기 영상도 clap 8. 규칙만 쓸 때보다 훨씬 나쁨 → 실시간 화면에 GRU(--model)를 켜지 않음.
개선 없음 3회 연속(라운드 3·4·5) → 반복 개선 멈춤.
