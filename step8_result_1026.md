# 8단계 결과 2차 (2026-10-26, USB 웹캠 C920 1280x720 MJPG, app.py 포트 8002)
카메라: IP 카메라가 책상 높이·천장 쪽을 비춰 화각이 맞지 않아 USB 웹캠(`--cam 0`)으로 다시 진행. 세탁기는 노트북·모니터에 띄운 사진, 건전지는 듀라셀 AA 낱개와 AAA 블리스터 포장으로 확인.
코드 변경: 영상 JPEG 화질 75→95. LABELS 수정(아래 2차 실행부터 적용).

## 1차: 기존 LABELS (10:36~10:58)

| 물체 | yolo 라벨 | relabel 라벨 (점수) | yoloe 라벨 | 비고 |
| --- | --- | --- | --- | --- |
| 건전지 낱개 (COCO 밖) | cell phone (오인식) | 건전지 (0.73~0.75) | cell phone (오인식) | relabel만 해결 |
| 건전지 포장 (COCO 밖) | 미검출 | 미검출 | 미검출 | 세 모드 모두 실패 |
| 드럼 세탁기 사진 (COCO 밖) | microwave (오인식) | 통돌이 세탁기 (0.70~0.71, 종류 오답) | drum washing machine (정답) | yoloe가 가장 정확 |
| 통돌이 세탁기 사진 (COCO 밖) | 미검출 | 미확인 | cell phone (오인식) | 위에서 찍은 사진이 휴대폰처럼 보임 |
| 컵 | cup (정답) | 컵 (0.64~0.72) | 미검출 | |
| 휴대폰 | cell phone (정답) | 휴대폰 (0.70~0.72) | cell phone (정답) | yoloe는 노트북 모서리도 cell phone으로 잡음 |
| 화면 속 사진 전체 | tv, refrigerator | 모니터, 컵 | microwave, refrigerator | 화면 전체가 큰 가전으로 잡힘 |

| 모드 | 검출 fps | 임베딩 ms/개 | 저장 크롭 수 |
| --- | --- | --- | --- |
| yolo | 16.0 | 599 | 60 |
| relabel | 16.4 | 591 | 101 |
| yoloe | 12.2 | 620 | 38 |

텍스트 검색: 세 모드 모두 라벨이 틀려도 이미지 임베딩으로 건전지·세탁기 크롭을 상위에 찾음 (yolo 기준 "세탁기" 1위 = 드럼 세탁기 사진 0.778, "건전지" 1위 = 듀라셀 AA 0.708). 크롭이 작으면(70px 안팎) 검색 실패.

## 2차: LABELS 수정 후 (11:04, 13:03, yoloe)
수정: `top-load washing machine` → `top loading washing machine with open lid`, `battery pack` → `blister pack of batteries`, `AAA battery` 추가.

| 물체 | yoloe 라벨 | 비고 |
| --- | --- | --- |
| 건전지 포장 | blister pack of batteries (2회) | 1차에서 놓친 물체를 새로 잡음 |
| 통돌이 세탁기 사진 | 미검출 | 여전히 실패 |
| 드럼 세탁기 사진 | drum washing machine 4회, microwave 5회 | 화면 전체·흔들린 크롭은 microwave |
| 건전지 낱개 | AA battery (2회) | 정답 |
| 컵 | cup (8회) | 정답 |
| cell phone | 9회 | 대부분 노트북 모서리·충전기 오검출 |

## 정리
COCO 밖 물체 중 건전지는 relabel이, 드럼 세탁기는 yoloe가 바로잡아 두 개선 방법이 서로 다른 물체에서 강하다. yoloe는 라벨 문구를 구체적으로 바꾸는 것만으로 건전지 포장을 새로 잡았지만, `cell phone`이 네모난 물체를 끌어가는 문제와 통돌이 세탁기 미검출이 남았다. relabel은 LABEL_MIN 0.20이 낮아 의자·마우스처럼 맞는 라벨까지 바꾸는 부작용이 23일과 같이 나타났다 (0.7 근처 권장, 다만 세탁기 점수 0.70~0.71이 경계). LABELS 수정 후 relabel 재실행은 하지 않음(1차 결과로 갈음).
