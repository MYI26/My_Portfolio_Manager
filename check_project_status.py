import os
import subprocess
import sys

def check_pyside6_version():
    try:
        output = subprocess.check_output([sys.executable, "-m", "pip", "show", "PySide6"], text=True)
        for line in output.splitlines():
            if line.startswith("Version:"):
                version = line.split(":")[1].strip()
                print(f"✅ PySide6 version installed: {version}")
                return
        print("❌ PySide6 is not installed properly.")
    except Exception as e:
        print(f"❌ Failed to check PySide6 version: {e}")

def check_main_file():
    if os.path.exists("main.py"):
        print("✅ Found 'main.py' - running from correct folder.")
    else:
        print("❌ 'main.py' not found! Make sure you are running from the project root.")

def check_ui_file():
    ui_path = os.path.join("view", "ui_stock_info.py")
    if os.path.exists(ui_path):
        print("✅ Found 'view/ui_stock_info.py'.")
    else:
        print("❌ Missing 'view/ui_stock_info.py'. Did you run pyside6-uic?")

def check_pycache():
    pycache_found = False
    for root, dirs, files in os.walk("."):
        for dir in dirs:
            if dir == "_pycache_":
                pycache_found = True
                print(f"⚠  Found _pycache_ folder at: {os.path.join(root, dir)}")
    if not pycache_found:
        print("✅ No _pycache_ folders found. (Good)")

def run_all_checks():
    print("\n🔍 Checking project environment...\n")
    check_main_file()
    check_pyside6_version()
    check_ui_file()
    check_pycache()
    print("\n✅ Environment check complete.\n")

if __name__ == "__main__":
    run_all_checks()