# embedding_gemma2-AIGJ_01_015

Google **EmbeddingGemma 2** 멀티모달 임베딩 모델을 Jetson Orin Nano Super(8GB)에서 돌려 본 과제입니다. 텍스트·이미지·오디오 임베딩 검색과 자원 측정, 강의실 도메인 데이터로 미세 조정, YOLO 검출 + 임베딩 재라벨링 카메라 앱, 자세(pose) 기반 동작 인식, 카메라 2대로 사람의 접근을 감지하는 앱까지 1~10단계 코드와 결과 기록을 담았습니다.

## 단계별 파일

| 단계 | 파일 | 내용 |
|---|---|---|
| 1~5 환경·기본 검색 | `check.py`, `eg2.py`, `test_text.py`, `test_vision*.py`, `test_audio.py` | 패키지·CUDA 확인, 모델 로드(`eg2.load()`), 텍스트·이미지·오디오 임베딩 검색 시험 |
| 6 자원 측정 | `bench6.py`, `bench6_result.md` | 텍스트/비전/오디오/전체 구성별 로드 시간·RAM·지연·GPU 사용률 |
| 7 미세 조정 | `make_data.py`, `train_ft.py`, `eval_ir.py`, `eg2_ft.py`, `test_text_ft.py`, `step7_result.md`, `models/eg2-classroom/`(설정·모델 카드만), `runs/eg2-classroom/`(평가 CSV, trainer_state) | 강의실 환경 질의-문서 쌍을 만들어 MatryoshkaLoss로 미세 조정, accuracy@1 0.833 → 0.850 |
| 8 카메라 물체 인식 | `app.py`, `result_8_*.json`, `step8_result.md`, `step8_result_1026.md` | YOLO 검출 결과를 임베딩으로 재라벨링(relabel)하거나 YOLOE(open-vocabulary)로 COCO 밖 물체 인식 비교 |
| 9 동작 인식 | `pose_app.py`, `pose_model.py`, `train_pose.py`, `rec_start.sh`, `rec_stop.sh`, `data/action/*.csv`, `result_9_*.json`, `step9_result.md`, `step9_result_1027.md` | YOLO pose 관절로 만세·한팔들기·손흔들기 판정(raw → 시간 다수결 smooth), 관절 특징 CSV로 GRU 동작 분류 학습 |
| 10 접근 감지 | `prox/` | USB 카메라 2대 보정(`calib_intrinsics*.py`, `calib_extrinsics.py`, `calib/*.json`), 삼각측량(`stereo.py`), 발목 1대/스테레오/융합 방식 접근 감지 앱(`proximity_app*.py`), 로그 기록·요약(`state_logger.py`, `summarize_log.py`). 결과는 `prox/runs/step10_results.md`, `10-8_results.md` 등 |
| 팀원 공유 | `share_from_prettygeun/`, `share_from_prettygeun_1028/` | 팀원 **prettygeun**(박창근)이 공유한 9단계 작업(샘플 영상으로 동작 판정 개선 pose_app_v4~v6, GRU 평가, 라운드별 기록). `step9_result_1027.md`가 이 결과를 인용합니다 |

## 실행 방법 (Jetson, 가상환경 `~/eg2`)

```bash
source ~/eg2/bin/activate        # torch(CUDA), transformers, sentence-transformers>=6.1, ultralytics, fastapi
python check.py
python test_text.py
python bench6.py text|vision|audio|full
python make_data.py && python train_ft.py && python eval_ir.py
python app.py --cam 0            # 브라우저 http://<Jetson IP>:8002
python pose_app.py --cam 0
python train_pose.py --data data/action --task action --window 30 --out models/action.pt
cd prox && python proximity_app.py --cams 2 0 --mode fused   # 브라우저 :8020
```

## 올리지 않은 것

사진·영상·오디오 샘플, 크롭 이미지, 데이터셋(coco128), 모델 가중치(`*.pt`, `*.safetensors`, `mobileclip_blt.ts`, 미세 조정 체크포인트, 30MB `tokenizer.json`), 실행 로그는 크기·저작권 때문에 일부러 뺐습니다. IP 카메라 계정 같은 비밀 정보는 코드에 없고 보드의 별도 파일에서 읽습니다.
