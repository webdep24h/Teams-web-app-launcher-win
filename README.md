# 🧠 Microsoft Teams Web Launcher — One Device, Multiple Users

✨ Đăng nhập Microsoft Teams Web riêng biệt cho từng người, **tự động đăng xuất khi tắt Teams**.  
Phù hợp với mô hình: **1 máy tính được nhiều người dùng chung**, như tại quầy, văn phòng, trung tâm, nhà máy...

---
## 🛠️ Tải xuống và cài đặt

[![Click để tải](https://raw.githubusercontent.com/webdep24h/PingMonitorTool/main/images/Download.png)](https://github.com/webdep24h/Teams-web-app-launcher-win/raw/main/Microsoft-Teams-Web-App-Setup.rar)

Download tool tại: [Microsoft-Teams-Web-App](https://github.com/webdep24h/Teams-web-app-launcher-win/raw/main/Microsoft-Teams-Web-App-Setup.rar)

## 📦 TÍNH NĂNG NỔI BẬT

✅ Mỗi người dùng có 1 phiên làm việc riêng biệt (tạm thời)  
✅ Khi tắt cửa sổ Teams, dữ liệu đăng nhập sẽ **tự động bị xóa**  
✅ Cho phép **đăng nhập lại bằng tài khoản khác ngay sau đó**  
✅ Không cần cài ứng dụng Microsoft Teams Desktop  
✅ Sử dụng Chrome làm nền — nhanh, nhẹ, nhiều hỗ trợ  
✅ Có hỗ trợ thông báo popup nếu người dùng cho phép  
✅ Tự động tạo session tạm thời, không lưu trữ lâu dài  
✅ Có thể build thành `.exe` gắn icon chuyên nghiệp  
✅ Có trình cài đặt `.exe` bằng Inno Setup

---

## 🧱 KIẾN TRÚC HOẠT ĐỘNG

1. Ứng dụng tạo thư mục tạm `C:\TeamsWebTemp\TeamsUser_xxxxx`
2. Mở Chrome với `--user-data-dir` trỏ đến thư mục tạm
3. Mở trang web Teams: `https://teams.microsoft.com/v2/`
4. Khi tắt trình duyệt, thư mục sẽ bị **xoá hoàn toàn**
5. Người dùng tiếp theo có thể đăng nhập bằng tài khoản mới

---

## 🖥️ YÊU CẦU HỆ THỐNG

- Windows 10 hoặc 11
- Cài đặt Google Chrome
- Không yêu cầu Microsoft Teams Desktop
- Python 3.10+ (nếu build thủ công bằng PyInstaller)

---

## 🚀 CÁCH SỬ DỤNG (CHẠY TỪ PYTHON)

1. Clone project:
```bash
   git clone https://github.com/webdep24h/Teams-web-app-launcher-win.git
   cd Teams-web-app-launcher-win
```

2. Cài thư viện cần thiết:
```bash
 pip  install pyqt6 pywin32 winshell
 ```

3. Chạy:
```bash
 python microsoft_teams_launcher.py
 ```
## 🧰 BUILD EXE BẰNG PYINSTALLER

1. Cài PyInstaller:
```bash
 pip install pyinstaller
```

2. Build file `.exe`:
```bash
 pyinstaller --onefile --windowed --icon=Teams.ico --add-data "Teams.ico;." --name "Microsoft Teams" microsoft_teams_launcher.py
```
🟢 Kết quả: file .exe nằm trong thư mục `dist/`

## 🧳 ĐÓNG GÓI CÀI ĐẶT BẰNG INNO SETUP
Để đóng gói file .exe thành trình cài đặt chuyên nghiệp:
1. Tải Inno Setup [Inno Setup](https://jrsoftware.org/isdl.php)
2. Dùng file `installer.iss` trong repo
3. Gắn icon bằng dòng:
```bash
 SetupIconFile=dist\Teams.ico
```
4. Compile → tạo file `MicrosoftTeamsSetup.exe`

## 🧳 HƯỚNG PHÁT TRIỂN THÊM TÍNH NĂNG

1. Cho phép chọn thời gian timeout (15p, 30p, 1h) nếu không sử dụng.
2. Gửi log đăng xuất vào file `.txt`
3. Cho phép mở GUI quản lý người dùng
4. Chỉ theo dõi Chrome nếu đang mở Teams
5. Trước khi chạy kiểm tra `TeamsUser_xxxxx` có không, nếu có xóa tạo mới (Giúp giải phóng dung lượng)