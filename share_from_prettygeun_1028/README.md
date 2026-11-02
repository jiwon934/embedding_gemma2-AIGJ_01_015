# 9단계 사람 동작 인식 전체 결과 공유 (박창근 → 정지원님, 2026-10-28)

읽기 전용 복사본이에요. 필요한 파일은 자기 폴더로 복사해서 쓰세요.
`cp -r /var/tmp/eg2-share-prettygeun ~/eg2-lab/share_from_prettygeun`
원본은 `/home/prettygeun/eg2-lab/`에 있지만 홈 폴더 권한 때문에 직접은 못 열어요. 10월 27일에 공유한 첫 README는 `README_1027.md`로 남겨 두었어요.

## 9단계를 무엇으로 했나
웹캠 대신 인터넷 샘플 영상(Wikimedia Commons, Mixkit, WVU·OpenCV 공개 데이터, 출처는 SOURCES.txt)으로 했어요. 영상 파일은 크기·라이선스 때문에 넣지 않았어요(위치는 아래).

| 단계 | 한 것 | 결과 문서 |
| --- | --- | --- |
| 9-1 raw 판정 | 샘플 영상으로 pose_app.py --raw, 프레임마다 판정이 깜빡이는 문제 확인 | step9_result.md |
| 9-2 안정화 | 0.6초 다수결 + 손 흔들기 규칙. 이후 규칙을 v2~v4로 개선 | step9_result.md, step9_improve.md 2·5·6절 |
| 9-3 --record 녹화 | **안 함.** 대신 영상에서 같은 형식의 특징 CSV를 뽑는 extract_feats.py 사용 | - |
| 9-4 비교 | raw / smooth / GRU 횟수 비교표, 정면·측면(WVU 다시점) 비교 | step9_result.md, step9_improve.md 4절 |
| 9-5 행동 패턴 | --behavior 규칙(지나감·힐끗 봄·관심 있음·머무름)을 영상 13개로 확인 | step9_behavior.md |
| 9-6 GRU | 동작 모델: 지원님 action.pt 데이터 + 인터넷 영상으로 여러 번 다시 학습. 행동 모델: behavior_v1.pt | step9_improve.md 1·3·6·7절, step9_behavior.md |

## 핵심 결과
**규칙**
- 손 흔들기(v3, angleC): 손목 x 대신 팔꿈치 기준 아래팔 각도의 흔들림으로 판정. 손 흔들기 영상 31개 중 검출 11 → 23개(측면 2/6 → 4/6). 오판정 6 → 10회.
- 악수(v4): 박수 치는 사람·손 흔드는 사람·둘 다 카메라 정면을 보는 경우는 제외. 나란히 서서 박수 치는 옆 사람끼리 악수로 세던 문제(사무실 박수 영상 2번 반복에 5회 → 0회). 악수 TV는 3회 그대로 잡음.
- 측면: 측면에서는 어깨 너비가 정면의 1/2~1/8로 줄어 어깨 너비 단위 규칙이 흔들림(WVU 다시점 데이터로 확인).

**GRU 최종 조합 (step9_improve.md 7절)**
- 문지기 모델 action_l2r1.pt("그 밖의 움직임(other)" 클래스 포함)가 "동작 아님"이라고 하면 버리고, 동작 종류는 action_r2m.pt가 판정. GRU는 팔짱·박수만 맡고 손 흔들기는 규칙.
- 1·2위 확률 차이 0.3 이상, 3번 연속 같은 예측, 박수는 실제로 손을 붙였다 뗄 때만 인정.
- 실제 앱 재현(영상 2번 반복): 팔벌려뛰기·손 들기·걷기·악수 등 동작 아닌 영상 7개에서 GRU 오판정 0회(규칙만 쓸 때와 같음), 팔짱 10회·박수 3회 맞힘. 원래 action.pt는 다른 영상에서 확률 0.7을 넘는 판정이 없었어요(웹캠 한 대·한 사람 데이터라).

**9-5 행동 패턴 규칙**: 영상 13개 중 10개 맞음. 카메라를 보고 멈춰 있으면 관심 있음, 화면을 가로지르면 지나감이 잘 나와요.
**9-6 행동 모델(behavior_v1.pt)**: 학습에 안 쓴 영상에서 81%(관심 있음 89%, 머무름 52%, 지나감 82%)지만, 확률이 0.5 안팎이라 앱 기준(0.7)을 넘는 판정이 없음. README 설정(창 80)은 샘플 영상이 짧아 학습이 안 돼서 창 30으로 학습.

## 실행 방법
pose_model.py와 yolo11n-pose.pt가 있는 폴더(지원님 ~/eg2-lab)에 앱과 모델을 복사해서 실행하세요. 제 앱과 겹치지 않게 다른 포트를 쓰세요(지원님 10단계 앱이 8020을 쓰고 있으니 예: 8030).
```
cp /var/tmp/eg2-share-prettygeun/pose_app_v6.py ~/eg2-lab/
cp /var/tmp/eg2-share-prettygeun/models/action_r2m.pt /var/tmp/eg2-share-prettygeun/models/action_l2r1.pt ~/eg2-lab/models/
cd ~/eg2-lab && source ~/eg2/bin/activate

# 최종 조합 (규칙 + GRU 2단계)
python pose_app_v6.py --port 8030 --cam 0 \
  --model models/action_r2m.pt --gate-model models/action_l2r1.pt --gate-th 0.5 \
  --ml-only arms_crossed,clap --ml-margin 0.3 --ml-vote 3 --ml-rule --ml-rule-labels clap

# 규칙만 (GRU 없이)
python pose_app_v6.py --port 8030 --cam 0

# 행동 패턴 (9-5)
python pose_app_v6.py --port 8030 --cam 0 --behavior
```
- 웹캠은 한 번에 한 프로그램만 열 수 있어요. IP 카메라는 --cam http://127.0.0.1:8091/stream
- 영상 파일로 시험: video_stream.py로 영상을 반복 재생(127.0.0.1:8096)하고 --cam http://127.0.0.1:8096/stream. live_repro.sh는 영상 하나를 2번 반복 재생하며 앱 기록을 모으는 재현 스크립트(포트 8097·8012 사용, 안의 경로는 제 폴더 기준이라 고쳐서 쓰세요).
- 앱 하나가 메모리 약 1.5GB를 써요.

## 알려진 문제
- 팔짱을 끼고 푸는 동작(두 팔이 가슴 앞에서 움직임)을 박수로 판정할 때가 있어요(팔짱 끼는 모델 영상에서 2번 반복에 3회).
- 뒤에서 본 사람들이 나란히 걸을 때 손이 가까워져 악수로 잡힐 때가 있어요(대학생 걷기 영상에서 3회).
- 측면 악수는 뒤쪽 사람 손목이 가려져 자주 놓쳐요(요트·영접 악수 영상 0회).
- 규칙의 만세·한팔들기는 팔벌려뛰기·군중 박수에서 여전히 많이 나와요.
- 행동 패턴: 카메라가 사람을 따라가며 찍으면 "머무름", 종이를 보고 있어도 얼굴이 카메라 쪽이면 "관심 있음"으로 나와요.
- 행동 모델을 쓰려면 교실 카메라 앞에서 지나가기·머물기·쳐다보기를 10초 이상씩 직접 녹화(9-3 --record)한 데이터가 필요해요.

## 파일
| 파일 | 내용 |
| --- | --- |
| step9_result.md | 샘플 영상 첫 비교 |
| step9_improve.md | 개선 정리 전체(1~7절) |
| step9_behavior.md | 9-5 행동 패턴, 9-6 행동 모델 |
| round_1~5.md | 1차 반복 개선 기록 / loop2_round_1~4.md: 2차 반복 개선 기록 |
| summary3.md | 손 흔들기 규칙 비교표 |
| SOURCES.txt | 영상 출처·라이선스 |
| pose_app_v4.py | 규칙 v4(손 흔들기 angleC, 악수 v4) |
| pose_app_v5.py | v4 + GRU 판정 거부·라벨 제한·규칙 확인 옵션 |
| pose_app_v6.py | v5 + 문지기 모델(--gate-model), --ml-rule-labels (최종) |
| pose_model.py | 지원님 원본과 같음 |
| pose_eval_v2/v3/v4.py, pose_eval_beh.py | 영상 파일로 판정 횟수를 세는 비교 스크립트(v3 손 흔들기, v4 악수, beh 행동 패턴) |
| extract_feats.py | 영상 → --record 형식 특징 CSV |
| train_pose_v4.py | train_pose.py 개선판(--mirror 좌우 뒤집기, --lowdrop 하체 지우기, --balance). l2r1·r2m은 이걸로 학습(--mirror) |
| eval_gru.py | 학습에 안 쓴 영상 특징으로 GRU 정확도 비교 |
| video_stream.py, live_repro.sh | 영상 반복 재생, 실제 앱 재현 |
| remote_zip.py | 큰 zip에서 필요한 파일만 HTTP Range로 꺼냄(WVU 데이터) |
| models/action_r2m.pt | 동작 종류(팔짱·박수·기본·손 흔들기), 최종 조합의 주 모델 |
| models/action_l2r1.pt | other 클래스 포함, 최종 조합의 문지기 |
| models/behavior_v1.pt | 9-6 행동 모델(interested·linger·passing, 창 30) |
| models/action_v3m.pt, v5m, v6u | 이전 버전(10/27 공유분) |
| images/step9v7_gru_combo.jpg | 최종 앱 장면: 팔짱·박수·팔벌려뛰기·악수·손 흔들기·팔짱 끼는 모델 |
| images/step9v7_behavior.jpg | 9-5 행동 패턴 장면 |
| images/front_vs_side_wave.jpg | 정면·45도·측면 관절 비교 |
| images/live_8011_*.jpg 등 | 이전 실시간 화면 캡처, 정답 확인용 장면 모음 |

## 데이터 위치 (크기 때문에 복사 안 함, 필요하면 말해 주세요)
- 영상: /home/prettygeun/eg2-lab/media/pose/ (Wikimedia, mixkit/, wvu/, test_clips/)
- 특징 CSV: /home/prettygeun/eg2-lab/data/ (action_v2 ~ action_r2, action_l2r1, action_test_*, behavior_v1, behavior_test_v1)
