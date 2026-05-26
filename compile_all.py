import subprocess
import sys
import os

print("=" * 60)
print("  COMPILING ALL BIOCHEMISTRY NOTES MODULES (1 - 10)")
print("=" * 60)

failed = []
success = []

for i in range(1, 11):
    print(f"\n[START] Module {i:02d}...")
    res = subprocess.run(["python", "generate_pdf.py", "--module", str(i), "--edition", "both"])
    if res.returncode == 0:
        print(f"[OK] Module {i:02d} completed successfully.")
        success.append(i)
    else:
        print(f"[FAIL] Module {i:02d} failed with exit code {res.returncode}.")
        failed.append(i)

print("\n" + "=" * 60)
print("  COMPILATION SUMMARY")
print("=" * 60)
print(f"  Successfully compiled: {len(success)} / 10 modules")
if success:
    print(f"    Modules: {', '.join(map(str, success))}")
if failed:
    print(f"  Failed: {len(failed)} / 10 modules")
    print(f"    Modules: {', '.join(map(str, failed))}")
print("=" * 60)

if failed:
    sys.exit(1)
sys.exit(0)
