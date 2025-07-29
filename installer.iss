[Setup]
AppName=Microsoft Teams Web
AppVersion=1.0
DefaultDirName={autopf}\Microsoft Teams Web
DefaultGroupName=Microsoft Teams Web
UninstallDisplayIcon={app}\Microsoft Teams.exe
OutputBaseFilename=MicrosoftTeamsSetup
SetupIconFile=dist\Teams.ico
Compression=lzma
SolidCompression=yes
DisableDirPage=yes

[Files]
Source: "dist\Microsoft Teams.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\Teams.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autodesktop}\Microsoft Teams"; Filename: "{app}\Microsoft Teams.exe"; IconFilename: "{app}\Teams.ico"; WorkingDir: "{app}"

[Run]
Filename: "{app}\Microsoft Teams.exe"; Description: "Khởi chạy Microsoft Teams"; Flags: nowait postinstall skipifsilent
