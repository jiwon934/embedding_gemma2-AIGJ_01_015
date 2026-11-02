# 실시간 앱 그대로 재현: 영상 하나를 반복 스트림(8097)으로 내보내고 앱(8012)이 처리한 동작 기록을 모은다
# 사용: bash live_repro.sh <앱 파일> <결과 jsonl> <영상...>
cd ~/eg2-lab && source ~/eg2/bin/activate
APP=$1; OUT=$2; shift 2
for v in "$@"; do
  a=$(free -m | awk "/^메모리|^Mem/{print \$7}"); [ "$a" -lt 1500 ] && { echo "LOWMEM $a skip $v"; continue; }
  dur=$(python -c "import cv2,sys; c=cv2.VideoCapture(sys.argv[1]); print(int(c.get(7)/max(c.get(5),1))+1)" "$v")
  tmux new -d -s eg2rep_vid "cd ~/eg2-lab && source ~/eg2/bin/activate && VS_PORT=8097 python runs/step9_hs/video_stream_port.py $v > /dev/null 2>&1"
  sleep 3
  tmux new -d -s eg2rep_app "cd ~/eg2-lab && source ~/eg2/bin/activate && python $APP $APP_ARGS --port 8012 --cam http://127.0.0.1:8097/stream > /dev/null 2>&1"
  for i in $(seq 1 40); do curl -s -m2 -o /dev/null http://127.0.0.1:8012/ && break; sleep 2; done
  sleep $(( dur * 2 + 10 ))
  curl -s -m5 http://127.0.0.1:8012/events | python -c "import json,sys; d=json.load(sys.stdin); print(json.dumps({\"video\": sys.argv[1].split(\"/\")[-1], \"loops\": 2, \"fps\": round(d[\"stats\"][\"fps\"],1), \"counts\": d[\"counts\"], \"events\": [(e[\"who\"], e[\"label\"]) for e in d[\"events\"]]}, ensure_ascii=False))" "$v" | tee -a $OUT
  tmux kill-session -t eg2rep_app; tmux kill-session -t eg2rep_vid; sleep 3
done
echo ALLDONE
