#!/bin/bash
# 사용: ./rec_start.sh data/action/wave.csv  (녹화 시작, 서버 준비되면 시각 출력)
cd ~/eg2-lab
p=$(pgrep -f "^/home/jiwon934/eg2/bin/python pose_app.py"); [ -n "$p" ] && kill $p; sleep 2
rm -f "$1"
(nohup ~/eg2/bin/python pose_app.py --cam http://127.0.0.1:8090/stream --record "$1" > pose_rec.log 2>&1 < /dev/null &)
for i in $(seq 1 40); do curl -s -m 2 -o /dev/null http://127.0.0.1:8002/ && break; sleep 2; done
date +%T
