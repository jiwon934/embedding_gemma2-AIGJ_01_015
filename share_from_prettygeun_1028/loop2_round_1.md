# 정확도 개선 2차 라운드 1: "그 밖의 움직임(other)"을 다섯 번째 클래스로 추가

가설: 4동작이 아닌 움직임을 박수·손 흔들기로 착각하는 건 모델이 "그 밖의 움직임"을 본 적이 없어서다. other 클래스를 따로 두면 착각이 줄어든다.
데이터: data/action_l2r1 = action_r2 (팔짱 954, 박수 5715, 기본 7447, 손 흔들기 4002행) + other 9008행
 - WVU Dataset 1의 끄덕이기(2)·주먹 지르기(6)·조깅(7)·차기(9)·줍기(10)·던지기(11)·볼링(12) × 사람 1·2 × 시점 1·2·3·7 (remote_zip.py로 필요한 장면만 받음)
 - Mixkit 13개: 길거리 안무, 힙합 그룹, 남성 춤, 발코니 스트레칭, 아침 스트레칭, 헬스장 스트레칭, 거실 운동, 줄넘기, 발표자 손짓, 말하는 남성, 가리키기, 화이트보드 설명, 무대 연설
테스트: data/action_test_l2 = action_test_v7 + other(WVU 같은 동작 × 사람 3 × 4시점, 학습에 안 씀)
모델: models/action_l2r1.pt (train_pose_v4.py --mirror, 라벨 arms_crossed·clap·idle·other·wave)

## 특징 테스트 (eval_gru.py)
| 모델 | 팔짱 | 박수 | 기본 | other | 손 흔들기 | WVU V1 | V2 | V3 | V7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| action_r2m | 100% | 44% | 100% | 0% (기본 127·박수 68·손 흔들기 57) | 0% | 81% | 100% | 100% | 81% |
| action_l2r1 | 12% (other 32) | 0% | 41% (other 20) | 88% | 44% | 42% | 56% | 75% | 75% |
- other와 기본은 앱에서 둘 다 "동작 아님"이라 서로 헷갈려도 문제없다. 합쳐서 보면 l2r1은 기본 테스트 100%, other 테스트 93%를 "동작 아님"으로 맞힘. r2m은 other 테스트의 50%만 "동작 아님"(나머지는 박수·손 흔들기로 착각).
- 대신 팔짱(12%)·박수(0%)를 거의 못 맞히고, WVU 정확도도 떨어짐(other 데이터 9천 행에 팔짱이 묻힘).

## 실제 앱 재현 (pose_app_v5.py, 영상 2번 반복, GRU가 낸 판정 횟수)
| 영상 | 기대 | 규칙만 | r2m | l2r1 |
| --- | --- | --- | --- | --- |
| jumping_jacks_burpees.webm | 동작 아님 | 0 | clap 12, wave 8 | 0 |
| mk35968_classroom_raise_hands_b.mp4 | 동작 아님 | 0 | wave 2 | wave 3 |
| mk11553_raise_hand_question.mp4 | 동작 아님 | 0 | clap 7, wave 1 | wave 4, clap 2 |
| vtest.avi | 동작 아님 | 0 | 0 | 0 |
| e8_s3_v1.avi (WVU 팔벌려뛰기 정면) | 동작 아님 | 0 | clap 4 | 0 |
| e8_s3_v3.avi (WVU 팔벌려뛰기 측면) | 동작 아님 | 0 | wave 4, clap 2 | wave 3 |
| mk29963_arms_crossed_woman_livingroom.mp4 | 팔짱 | 0 | arms_crossed 3 | arms_crossed 3, clap 2 |
| applause_wikiconvention.webm | 박수 | 0 | clap 9, wave 7 | clap 7, wave 8 |
| wave_example.webm | 손 흔들기 | (규칙 손흔들기 8) | clap 8 | wave 8, clap 12 |
| **동작 아닌 영상 6개의 GRU 오판정** | | 0 | **40** | **12** |
| 팔짱·박수·손 흔들기 영상에서 맞힌 / 틀린 GRU 판정 | | 0 / 0 | 12 / 15 | 18 / 22 |

결과: 실제 앱 기준으로 개선(오판정 40 → 12, 맞힘 12 → 18). 특히 팔벌려뛰기(정면·측면)를 박수로 착각하던 것이 사라짐. 하지만 규칙만 쓸 때(GRU 오판정 0)보다는 여전히 오판정이 많아 8011에는 켜지 않음.
최고 갱신: action_l2r1 (실제 앱 기준).
다음: 2단계 방식(l2r1이 "동작 아님"이라고 하면 버리고, 동작 종류는 팔짱에 강한 r2m이 판정) + 판정 거부.
