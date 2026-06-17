import json
import os
import glob

def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()

code_str  = read("/tmp/fongmi_code.txt")
name      = read("/tmp/fongmi_name.txt")
raw       = read("/tmp/fongmi_raw.txt")
out_dir   = read("/tmp/fongmi_dir.txt")
branch    = read("/tmp/fongmi_branch.txt")
tag       = read("/tmp/fongmi_tag.txt")
repo_url  = read("/tmp/fongmi_repo.txt")

code  = int(code_str) if code_str else 0
lines = [l.strip() for l in raw.splitlines() if l.strip()]
desc  = "\n".join(f"* {l}" for l in lines) if lines else f"* {name}"

os.makedirs(out_dir, exist_ok=True)

for keyword, json_name in (("mobile", "mobile.json"), ("leanback", "leanback.json")):
    matches = glob.glob(os.path.join(out_dir, f"*{keyword}*.apk"))
    if not matches:
        print(f"Warning: no {keyword} apk found, skipping {json_name}")
        continue

    apk_file = os.path.basename(matches[0])
    url = f"{repo_url}/releases/download/{tag}/{apk_file}"
    payload = {"code": code, "name": name, "desc": desc, "url": url}

    path = os.path.join(out_dir, json_name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Written {path}:")
    print(json.dumps(payload, ensure_ascii=False, indent=2))