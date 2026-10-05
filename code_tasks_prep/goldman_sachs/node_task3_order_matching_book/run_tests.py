#!/usr/bin/env python3
import subprocess
import json
import sys

def main():
    print("🚀 Running Node.js Test Suite (HackerRank Style)...\n")
    proc = subprocess.run(
        ["npx", "mocha", "test/orders.spec.js", "--reporter", "json", "--exit"],
        capture_output=True,
        text=True
    )
    
    output = proc.stdout
    json_start = output.find('{')
    if json_start == -1:
        print("❌ FAILED TO EXECUTE TESTS:")
        print(proc.stderr or proc.stdout)
        sys.exit(1)
        
    try:
        data = json.loads(output[json_start:])
    except Exception as e:
        print("❌ Error parsing test output:")
        print(output)
        sys.exit(1)

    passes = data.get("passes", [])
    failures = data.get("failures", [])
    
    for p in passes:
        print(f"  ✔ PASS: {p.get('fullTitle')}")
        
    for f in failures:
        print(f"  ✖ FAIL: {f.get('fullTitle')}")
        err = f.get("err", {})
        msg = err.get("message", "Assertion failed")
        print(f"      → {msg}")
        
    total = len(passes) + len(failures)
    print("\n=======================================================")
    print(f"📊 RESULTS: {len(passes)} Passed | {len(failures)} Failed | {total} Total")
    print("=======================================================\n")
    
    if failures:
        sys.exit(1)

if __name__ == "__main__":
    main()
