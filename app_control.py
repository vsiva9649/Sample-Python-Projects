# -*- coding: utf-8 -*-
import subprocess
import sys

def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True).strip()
    except subprocess.CalledProcessError as e:
        print(e.output)
        sys.exit(1)

def ensure_device():
    out = run("adb devices")
    lines = [l for l in out.splitlines()[1:] if l.strip()]
    if not lines:
        print("❌ No device. Connect phone & enable USB debugging.")
        sys.exit(1)

def start_app(package, activity=None):
    ensure_device()
    if activity:
        run(f"adb shell am start -n {package}/{activity}")
        print(f"Started {package}/{activity}")
    else:
        run(f"adb shell monkey -p {package} -c android.intent.category.LAUNCHER 1")
        print(f"Started {package}")

def stop_app(package):
    ensure_device()
    run(f"adb shell am force-stop {package}")
    print(f"Stopped {package}")

# --- Apps List ---
APPS = {
    "1": ("WhatsApp", "com.whatsapp", None),
    "2": ("NP Manager", "com.wn.app.np", None),
    "3": ("MT Manager", "bin.mt.plus", None)
}

# store last opened package globally
last_opened_package = None

def menu():
    global last_opened_package
    while True:
        print("\n=== Android App Controller ===")
        for key, (name, _, _) in APPS.items():
            print(f"{key}. Open {name}")
        print("4. Close Last Opened App")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice in APPS:
            name, pkg, act = APPS[choice]
            start_app(pkg, act)
            last_opened_package = pkg  # store package name

        elif choice == "4":
            if last_opened_package:
                stop_app(last_opened_package)
                last_opened_package = None
            else:
                print("❌ No app has been opened yet!")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    menu()
