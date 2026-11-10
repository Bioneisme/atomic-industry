"""Builds dist/atomic_industry-<version>.hpack from horizon-modpack.toml and overrides/.

Checks first that every listed mod is that exact version, with that hash, in the Horizon registry.
The zip is reproducible: sorted entries, fixed timestamps.

    python tools/build.py            # build, checking against the registry index
    python tools/build.py --offline  # build without the check
"""
import hashlib
import json
import pathlib
import sys
import tomllib
import urllib.request
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = "https://horizon-rust.github.io/horizon-mods/index.json"
STAMP = (2026, 1, 1, 0, 0, 0)


def check(manifest):
    with urllib.request.urlopen(INDEX) as r:
        index = json.load(r)
    known = {(p["id"], v["version"]): v["file"]["sha256"]
             for p in index["projects"] for v in p.get("versions", [])}
    revoked = index.get("revoked", [])
    bad = []
    for m in manifest["mods"]:
        sha = known.get((m["id"], m["version"]))
        if sha is None:
            bad.append(f'{m["id"]} {m["version"]}: not in the registry')
        elif sha != m["sha256"]:
            bad.append(f'{m["id"]} {m["version"]}: the registry has another sha256')
        for r in revoked:
            if r["id"] == m["id"] and r.get("sha256") in (None, m["sha256"]):
                bad.append(f'{m["id"]}: revoked ({r["reason"]})')
    if bad:
        sys.exit("refused:\n  " + "\n  ".join(bad))


def main():
    manifest_path = ROOT / "horizon-modpack.toml"
    manifest = tomllib.loads(manifest_path.read_text(encoding="utf-8"))
    if "--offline" not in sys.argv:
        check(manifest)
    files = [("horizon-modpack.toml", manifest_path)]
    overrides = ROOT / "overrides"
    if overrides.is_dir():
        files += sorted((p.relative_to(ROOT).as_posix(), p) for p in overrides.rglob("*") if p.is_file())
    out = ROOT / "dist" / f'{manifest["id"]}-{manifest["version"]}.hpack'
    out.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for name, path in files:
            info = zipfile.ZipInfo(name, STAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, path.read_bytes())
    data = out.read_bytes()
    print(f"{out.relative_to(ROOT)}  {len(manifest['mods'])} mods  {len(data)} bytes  "
          f"sha256 {hashlib.sha256(data).hexdigest()}")


if __name__ == "__main__":
    main()
