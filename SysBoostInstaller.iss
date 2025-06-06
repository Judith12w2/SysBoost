; Script de Inno Setup para SysBoost
[Setup]
AppName=SysBoost
AppVersion=1.0
DefaultDirName={pf}\SysBoost
DefaultGroupName=SysBoost
UninstallDisplayIcon={app}\main.exe
OutputDir=dist
OutputBaseFilename=SysBoost_Installer
Compression=lzma
SolidCompression=yes
WizardStyle=modern
SetupIconFile=data\logo.ico


[Files]
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "data\*"; DestDir: "{app}\data"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\SysBoost"; Filename: "{app}\main.exe"
Name: "{commondesktop}\SysBoost"; Filename: "{app}\main.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Crear acceso directo en el escritorio"; GroupDescription: "Iconos adicionales:"
