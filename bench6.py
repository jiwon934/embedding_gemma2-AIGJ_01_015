# 6단계 측정: 구성 하나를 로드해 RAM·지연(두 번째 실행)·GPU 사용률을 잰다
# 사용: python bench6.py text|vision|audio|full
import glob, re, subprocess, sys, threading, time
import torch
from eg2 import load

def ram_used_mb():
    m = dict(l.split(":") for l in open("/proc/meminfo"))
    kb = lambda k: int(m[k].split()[0])
    return (kb("MemTotal") - kb("MemAvailable")) // 1024

cfg = sys.argv[1]
images = sorted(glob.glob("media/scene_*.jpg"))
wavs = ["media/speech.wav", "media/beep.wav", "media/noise.wav"]
queries = ["수업 중에 졸리고 머리가 맑지 않아요", "여름에 냉방 몇 도로 맞춰야 하나요?"]

if cfg == "text":
    kw, label = {}, "질의 2개"
    work = lambda m: m.encode(queries, prompt_name="SearchQuery")
elif cfg == "vision":
    kw, label = {"vision": True}, f"이미지 {len(images)}장"
    work = lambda m: m.encode([{"image": p} for p in images])
elif cfg == "audio":
    kw, label = {"audio": True}, "WAV 3개"
    work = lambda m: m.encode([{"audio": w} for w in wavs])
else:
    kw, label = {"vision": True, "audio": True}, f"질의2+이미지{len(images)}+WAV3"
    work = lambda m: (m.encode(queries, prompt_name="SearchQuery"),
                      m.encode([{"image": p} for p in images]),
                      m.encode([{"audio": w} for w in wavs]))

before = ram_used_mb()
t = time.perf_counter(); model = load(**kw); load_s = time.perf_counter() - t
after = ram_used_mb()

work(model)  # 첫 실행 (CUDA 초기화 포함) 은 버린다
torch.cuda.synchronize()

gpu = []
p = subprocess.Popen(["tegrastats", "--interval", "100"], stdout=subprocess.PIPE, text=True)
def rd():
    for line in p.stdout:
        g = re.search(r"GR3D_FREQ (\d+)%", line)
        if g: gpu.append(int(g.group(1)))
threading.Thread(target=rd, daemon=True).start()
time.sleep(0.3)
t = time.perf_counter(); work(model); torch.cuda.synchronize(); ms = (time.perf_counter() - t) * 1000
time.sleep(0.3); p.terminate()
peak = ram_used_mb()
print(f"RESULT|{cfg}|{label}|로드 {load_s:.1f}s|로드 전 {before}MB|로드 후 {after}MB (+{after-before})|실행 중 {peak}MB|지연 {ms:.0f}ms|GPU 최대 {max(gpu) if gpu else 0}% 평균 {sum(gpu)//max(1,len(gpu))}%|GPU메모리 {torch.cuda.max_memory_allocated()/1e9:.2f}GB")
