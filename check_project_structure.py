import os

def check_structure():
    base_files = ["main.py"]
    view_files = ["stock_info_view.py", "ui_stock_info.py", "stock_info.ui", "__init__.py"]

    print("🔍 Checking project structure...\n")

    # בדוק קבצים בתיקייה הראשית
    for f in base_files:
        if not os.path.isfile(f):
            print(f"❌ Missing file: {f}")
        else:
            print(f"✅ Found: {f}")

    # בדוק קיום תיקיית view
    if not os.path.isdir("view"):
        print("❌ Missing folder: view")
        return

    print("\n🔍 Checking 'view' folder...")

    for f in view_files:
        if not os.path.isfile(os.path.join("view", f)):
            print(f"❌ Missing in view/: {f}")
        else:
            print(f"✅ Found in view/: {f}")

    print("\n✅ Structure check complete!")

if __name__ == "__main__":
    check_structure()
