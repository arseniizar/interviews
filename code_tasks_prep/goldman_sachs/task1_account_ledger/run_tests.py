#!/usr/bin/env python3
import subprocess
import os
import glob
import xml.etree.ElementTree as ET

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
CYAN = "\033[96m"
RESET = "\033[0m"

def main():
    # Automatically locate project directory where pom.xml lives
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)

    print(f"\n{BOLD}{CYAN}🚀 Running Goldman Sachs Test Suite (HackerRank Style)...{RESET}\n")

    res = subprocess.run(["mvn", "test", "-Dspring.main.banner-mode=off"], capture_output=True, text=True, cwd=project_dir)

    report_dir = os.path.join(project_dir, "target/surefire-reports")
    xml_files = glob.glob(os.path.join(report_dir, "TEST-*.xml"))

    if not xml_files:
        print(f"{RED}{BOLD}❌ BUILD / COMPILATION FAILED!{RESET}")
        for line in res.stdout.splitlines():
            if "[ERROR]" in line and "Failed to execute" not in line:
                print(f"  {RED}{line}{RESET}")
        return

    # Check for application context failure in text report
    txt_files = glob.glob(os.path.join(report_dir, "*.txt"))
    root_cause = None
    for tf in txt_files:
        with open(tf, "r") as f:
            content = f.read()
            if "Caused by:" in content:
                for line in content.splitlines():
                    if "Caused by:" in line and "Ambiguous" in line:
                        root_cause = line.split("Caused by:")[-1].strip()
                        break
                    elif "Caused by:" in line and ("BeanCreationException" in line or "IllegalStateException" in line or "BeanInstantiationException" in line):
                        root_cause = line.split("Caused by:")[-1].strip()

    total = 0
    passed = 0
    failed = 0
    errors = 0
    failures_details = []

    for xml_file in xml_files:
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            for tc in root.findall("testcase"):
                total += 1
                name = tc.get("name", "unknown")
                failure = tc.find("failure")
                error = tc.find("error")

                if failure is not None:
                    failed += 1
                    msg = failure.get("message", "Assertion failed")
                    failures_details.append((name, msg))
                    print(f"  {RED}✖ FAIL:{RESET} {name}")
                elif error is not None:
                    errors += 1
                    msg = error.get("message", "Error during execution")
                    if root_cause:
                        msg = root_cause
                    failures_details.append((name, msg))
                    print(f"  {RED}✖ ERROR:{RESET} {name}")
                else:
                    passed += 1
                    print(f"  {GREEN}✔ PASS:{RESET} {name}")
        except Exception:
            pass

    print(f"\n{BOLD}{'='*55}{RESET}")
    print(f"{BOLD}📊 RESULTS: {GREEN}{passed} Passed{RESET} | {RED}{failed + errors} Failed{RESET} | {total} Total")
    print(f"{BOLD}{'='*55}{RESET}\n")

    if failures_details:
        print(f"{BOLD}{YELLOW}🔍 WHAT FAILED & WHY:{RESET}")
        if root_cause:
            print(f"  {RED}{BOLD}🚨 SPRING CONFIG ERROR:{RESET} {RED}{root_cause}{RESET}\n")
        else:
            for idx, (name, msg) in enumerate(failures_details, 1):
                clean_msg = msg.replace("java.lang.AssertionError: ", "").strip()
                print(f"  {idx}. {BOLD}{name}{RESET}")
                print(f"     {RED}↳ {clean_msg}{RESET}\n")

if __name__ == "__main__":
    main()
