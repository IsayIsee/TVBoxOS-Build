import json
import os

def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()

code_str = read("/tmp/fongmi_code.txt")
name     = read("/tmp/fongmi_name.txt")
raw      = read("/tmp/fongmi_raw.txt")
out_dir  = read("/tmp/fongmi_dir.txt")
branch   = read("/tmp/fongmi_branch.txt")

code  = int(code_str) if code_str else 0
lines = [l.strip() for l in raw.splitlines() if l.strip()]
desc  = "\n".join(f"* {l}" for l in lines) if lines else f"* {name}"

payload = {"code": code, "name": name, "desc": desc}

os.makedirs(out_dir, exist_ok=True)

for fname in ("mobile.json", "leanback.json"):
    path = os.path.join(out_dir, fname)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Written {path}:")
    print(json.dumps(payload, ensure_ascii=False, indent=2))