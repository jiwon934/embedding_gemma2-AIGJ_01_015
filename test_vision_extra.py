import glob, time
from eg2 import load

model = load(vision=True)

images = sorted(glob.glob("media/*.jpg"))
t = time.perf_counter()
img_emb = model.encode([{"image": p} for p in images], normalize_embeddings=True)
print(f"이미지 {len(images)}장: {(time.perf_counter()-t)*1000:.0f} ms")

t = time.perf_counter()
# vid_emb = model.encode({"video": "media/clip.mp4"}, normalize_embeddings=True)
# print(f"동영상 1개: {(time.perf_counter()-t)*1000:.0f} ms")

queries = ["천장의 조명", "코드가 띄워진 모니터", "창문과 블라인드", "강의실 앞쪽 스크린", "책상에 앉아 있는 사람"]
q = model.encode(queries, prompt_name="SearchQuery", normalize_embeddings=True)

sim = q @ img_emb.T
for qi, row in zip(queries, sim):
    order = row.argsort()[::-1][:3]
    print(qi, "->", [(images[i].split("/")[-1], round(float(row[i]), 3)) for i in order])

# print("질의-동영상 유사도:", (q @ vid_emb).round(3))
