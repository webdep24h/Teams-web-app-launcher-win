import os
import sys
import subprocess
import shutil
import time

def base_path():
    return getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

def get_icon_temp():
    src = os.path.join(base_path(), "Teams.ico")
    dst = os.path.join("C:\\TeamsWebTemp", "Teams.ico")
    try:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if os.path.exists(src):
            shutil.copy(src, dst)
    except Exception as e:
        print(f"[⚠️] Không thể copy icon: {e}")
    return dst

def find_chrome():
    paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    ]
    return next((p for p in paths if os.path.exists(p)), None)

def run_teams_web_app():
    chrome = find_chrome()
    if not chrome:
        print("❌ Không tìm thấy Google Chrome.")
        return

    # Tạo thư mục session tạm
    base_dir = r"C:\TeamsWebTemp"
    os.makedirs(base_dir, exist_ok=True)
    profile_dir = os.path.join(base_dir, f"TeamsUser_{int(time.time())}")
    os.makedirs(profile_dir, exist_ok=True)

    teams_url = "https://teams.microsoft.com/v2/"

    args = [
        chrome,
        f'--user-data-dir={profile_dir}',
        f'--app={teams_url}',
        '--no-first-run',
        '--no-default-browser-check',
        '--disable-background-mode',
        '--disable-plugins-discovery',
        '--disable-extensions',
        '--disable-features=TranslateUI'
    ]

    print(f"[🚀] Đang chạy Teams Web App...")
    proc = subprocess.Popen(args)

    try:
        while proc.poll() is None:
            time.sleep(1)
    finally:
        print("[🧹] Đóng Teams. Xoá session...")
        shutil.rmtree(profile_dir, ignore_errors=True)
        print("[✅] Hoàn tất.")

if __name__ == "__main__":
    get_icon_temp()
    run_teams_web_app()
