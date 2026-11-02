"""큰 zip을 통째로 받지 않고 HTTP Range로 목록과 필요한 파일만 꺼낸다 (영상 파일만, 실행하지 않음).
사용: python3 remote_zip.py <zip URL> list
      python3 remote_zip.py <zip URL> get <출력 폴더> <패턴(정규식)>
"""
import io, os, re, sys, urllib.request, zipfile

class HttpFile(io.RawIOBase):
    def __init__(self, url):
        self.url, self.pos = url, 0
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=60) as r:
            self.url, self.size = r.geturl(), int(r.headers["Content-Length"])
    def seekable(self): return True
    def readable(self): return True
    def tell(self): return self.pos
    def seek(self, off, whence=0):
        self.pos = off if whence == 0 else self.pos + off if whence == 1 else self.size + off
        return self.pos
    def read(self, n=-1):
        if n is None or n < 0:
            n = self.size - self.pos
        if n == 0 or self.pos >= self.size:
            return b""
        end = min(self.pos + n, self.size) - 1
        for t in range(10):
            try:
                req = urllib.request.Request(self.url, headers={"Range": f"bytes={self.pos}-{end}"})
                with urllib.request.urlopen(req, timeout=120) as r:
                    data = r.read()
                if len(data) == end - self.pos + 1:
                    break
            except OSError:
                pass
        else:
            raise IOError("range read failed")
        self.pos += len(data)
        return data
    def readinto(self, b):
        d = self.read(len(b)); b[:len(d)] = d; return len(d)

url, cmd = sys.argv[1], sys.argv[2]
z = zipfile.ZipFile(io.BufferedReader(HttpFile(url), buffer_size=4 << 20))
if cmd == "list":
    for i in z.infolist():
        print(i.filename, i.file_size)
else:
    out, pat = sys.argv[3], re.compile(sys.argv[4])
    os.makedirs(out, exist_ok=True)
    for i in z.infolist():
        name = os.path.basename(i.filename)
        if i.is_dir() or not pat.search(i.filename) or not name.lower().endswith((".avi", ".mp4", ".mpg", ".mov", ".jpg")):
            continue
        dst = os.path.join(out, i.filename.replace("/", "_"))   # 장면 사진은 train3_view1_10.jpg처럼 경로를 이름에 넣음
        if os.path.exists(dst):
            print("EXISTS", dst); continue
        with z.open(i) as src, open(dst, "wb") as f:
            while True:
                b = src.read(1 << 20)
                if not b: break
                f.write(b)
        print("got", i.filename, i.file_size, flush=True)
