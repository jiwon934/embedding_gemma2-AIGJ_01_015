#!/bin/bash
# 사용: ./rec_stop.sh data/action/wave.csv 32  (N초 뒤 녹화 종료, 줄 수와 규칙 라벨 분포 출력)
cd ~/eg2-lab
sleep "${2:-32}"
p=$(pgrep -f "^/home/jiwon934/eg2/bin/python pose_app.py"); [ -n "$p" ] && kill $p; sleep 1
wc -l "$1"; cut -d, -f2,3 "$1" | sort | uniq -c | sort -rn | head -6
