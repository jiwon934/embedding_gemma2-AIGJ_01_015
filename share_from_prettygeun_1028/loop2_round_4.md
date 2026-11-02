# 정확도 개선 2차 라운드 4: 규칙 확인을 박수에만 적용

가설: 팔짱 규칙 확인이 팔짱을 막고, 박수 규칙 확인이 오판정을 막는다(라운드 3). 박수에만 적용하면 둘 다 얻는다.
앱: pose_app_v6.py --model models/action_r2m.pt --gate-model models/action_l2r1.pt --gate-th 0.5 --ml-only arms_crossed,clap --ml-margin 0.3 --ml-vote 3 --ml-rule --ml-rule-labels clap
평가 영상에 팔짱 끼는 모델(mk50643), 회의 박수(mk24214, 학습에 쓴 영상이라 참고), 악수 TV를 더함.

## 실제 앱 재현 (영상 2번 반복)
| 영상 | 기대 | GRU 판정 | 규칙 판정(참고) |
| --- | --- | --- | --- |
| jumping_jacks_burpees.webm | 동작 아님 | 0 | 만세 11, 한팔들기 2, 손흔들기 2 |
| mk35968_classroom_raise_hands_b.mp4 | 동작 아님 | 0 | 한팔들기 3, 만세 2 |
| mk11553_raise_hand_question.mp4 | 동작 아님 | 0 | 만세 2, 한팔들기 1, 손흔들기 1 |
| vtest.avi | 동작 아님 | 0 | 한팔들기 1 |
| e8_s3_v1.avi | 동작 아님 | 0 | 만세 4 |
| e8_s3_v3.avi | 동작 아님 | 0 | 만세 3 |
| handshake_tv.ogv | 동작 아님(악수) | 0 | 악수 3, 손흔들기 5, 한팔들기 2 |
| mk29963_arms_crossed_woman_livingroom.mp4 | 팔짱 | **arms_crossed 8** | 0 |
| mk50643_arms_crossed_model.mp4 | 팔짱(끼고 푸는 동작) | arms_crossed 2, **clap 3(틀림)** | 한팔들기 8 |
| applause_wikiconvention.webm | 박수 | **clap 3** | 만세 7, 손흔들기 5, 한팔들기 2 |
| mk24214_clap_conference.mp4 | 박수(학습에 씀) | clap 11 | 손흔들기 11 |
| wave_example.webm | 손 흔들기(규칙) | 0 | 손흔들기 10 |

- 동작 아닌 영상 7개의 GRU 오판정: **0** (규칙만 쓸 때와 같음)
- 맞힌 팔짱·박수: 팔짱 10, 박수 3(+학습 영상 11). 틀린 GRU 판정: 3(팔짱 끼는 동작을 박수로)

결과: 개선. 오판정 0을 유지하면서 팔짱(라운드 2: 0 → 10)과 박수를 함께 맞힘 → 최고 갱신.
남은 문제: 팔짱을 끼고 푸는 동작 중 두 팔이 가슴 앞에서 움직일 때 박수로 3번 판정. 규칙 판정(만세·한팔들기)은 팔벌려뛰기·박수 영상에서 여전히 많음(GRU와 별개, 5·6절의 규칙 한계).
