# 9단계 사람 동작 인식 결과 공유 (박창근 → 정지원님, 2026-10-27)

읽기 전용 복사본이에요. 필요한 파일은 자기 폴더로 복사해서 쓰세요(`cp -r /var/tmp/eg2-share-prettygeun ~/eg2-lab/share_from_prettygeun`).
원본은 `/home/prettygeun/eg2-lab/`에 있지만 홈 폴더 권한 때문에 직접은 못 열어요.

## 핵심 결과
- **손 흔들기**: 어깨 너비 대신 팔꿈치 기준 아래팔 각도로 판정하도록 바꿈. 손 흔들기 영상 31개 중 검출 11개 → 23개(측면 6개 중 2 → 4개), 손 흔들기가 아닌 영상의 오판정 6 → 10회.
- **악수**: 나란히 서서 박수 치는 옆 사람끼리 악수로 세던 문제(사무실 박수 영상 2번 반복에 5회 → 0회). 박수 치는 사람·손 흔드는 사람·둘 다 카메라 정면을 보는 경우를 제외. 측면 악수는 손목이 가려져 아직 잘 못 잡음.
- **측면 시점**: 측면에서는 어깨 너비가 정면의 1/2~1/8로 줄어 어깨 너비 단위 규칙이 흔들림(WVU 다시점 데이터로 확인).
- **GRU**: 지원님 웹캠 데이터에 인터넷 영상 특징을 더해 다시 학습. action_r2m.pt가 학습에 안 쓴 영상에서 팔짱·기본 100%, 측면 평균 90.5%. 다만 실제 앱에서 팔벌려뛰기·악수·손 들기를 박수·손 흔들기로 자주 착각해서 실시간 화면에는 켜지 않았어요. 원래 action.pt는 다른 영상에서 확률 0.7을 넘는 판정이 없었어요(웹캠 한 대·한 사람 데이터라).
- 자세한 표와 해석은 `step9_improve.md`(1~6절), 라운드별 기록은 `round_1~5.md`.

## 파일
| 파일 | 내용 |
| --- | --- |
| step9_improve.md | 개선 정리 전체 (1 GRU 재학습, 2 규칙 개선, 4 측면 시점, 5 손 흔들기, 6 악수·반복 개선) |
| step9_result.md | 샘플 영상으로 처음 비교한 결과 |
| round_1~5.md, summary3.md | GRU 반복 개선 기록, 손 흔들기 규칙 비교 표 |
| SOURCES.txt | 영상 출처·라이선스 (Wikimedia Commons, Mixkit, WVU·UTD 연구용 공개 데이터) |
| pose_app_v4.py | 실시간 앱 최신판 (원래 pose_app.py에서 손 흔들기·악수 판정만 바꿈) |
| pose_model.py | 정지원님 원본과 같은 파일 (pose_app_v4.py가 씀) |
| pose_eval_v2/v3/v4.py | 영상 파일로 판정 횟수를 세는 비교 스크립트 (v3: 손 흔들기 방식 비교, v4: 악수 조건 비교) |
| extract_feats.py | 영상에서 --record와 같은 형식의 관절 특징 CSV 만들기 |
| train_pose_v4.py | train_pose.py 개선판 (--mirror 좌우 뒤집기, --lowdrop 하체 지우기, --balance) |
| eval_gru.py | 학습에 안 쓴 영상의 특징 CSV로 GRU 모델 정확도 비교 |
| video_stream.py | 영상 파일을 반복 재생해 웹캠처럼 MJPEG(127.0.0.1:8096)으로 내보냄 |
| remote_zip.py | 큰 zip을 통째로 받지 않고 필요한 파일만 HTTP Range로 꺼냄 (WVU 데이터에 사용) |
| models/action_r2m.pt | 추천(팔짱·기본·측면 강함), 실시간 화면에는 아직 비추천 |
| models/action_v3m.pt | 정면 스톡 영상 테스트에서 좋음, 측면 약함 |
| models/action_v5m.pt | 측면(WVU) 데이터 포함, 팔짱 약함 |
| models/action_v6u.pt | 하체를 지우고 상반신만 학습(손 흔들기 강함, 팔짱 약함). eval_gru.py로 평가할 때만 하체 지우기가 적용됨 |
| images/ | 정면·측면 관절 비교, 8011 화면 캡처, 정답 확인용 장면 모음 |

## 실행 방법
pose_model.py와 yolo11n-pose.pt가 있는 폴더(예: 지원님 ~/eg2-lab)에 pose_app_v4.py를 복사해서 실행하세요.
제 8011 화면(pose_app_v4)과 지원님이 전에 쓰던 8002와 겹치지 않게 다른 포트를 쓰세요.

```
cp /var/tmp/eg2-share-prettygeun/pose_app_v4.py ~/eg2-lab/
cd ~/eg2-lab && source ~/eg2/bin/activate
python pose_app_v4.py --port 8020 --cam 0                      # USB 웹캠
python pose_app_v4.py --port 8020 --cam http://127.0.0.1:8091/stream   # IP 카메라 뷰어
python pose_app_v4.py --port 8020 --cam 0 --wave v2           # 예전 손 흔들기 방식
python pose_app_v4.py --port 8020 --cam 0 --model models/action.pt   # GRU 켜기(GRU 판정이 규칙 판정을 덮어씀)
```
웹캠(/dev/video0)은 한 번에 한 프로그램만 열 수 있어요. 제 camview가 켜져 있으면 말해 주세요.

## 데이터 위치 (크기 때문에 복사 안 함)
- 영상: /home/prettygeun/eg2-lab/media/pose/ (Wikimedia, mixkit/, wvu/, test_clips/), 약 730MB
- 특징 CSV: /home/prettygeun/eg2-lab/data/action_v2 ~ action_r2, action_test_v6·v7, action_test_wvu
필요하면 말해 주세요. 따로 복사해 드릴게요.
