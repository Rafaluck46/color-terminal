import winreg

RELATIVE_PATH=r"\console"
DWORD_KEY=r"VirtualTerminalLevel"

def verify_register():
	print("Try to connect with registry...")
	connect_registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
	handle = winreg.OpenKey(connect_registry,"Console")
	if(handle):
		print("connected!")
	print(winreg.QueryValueEx(handle,"VirtualTerminalLevel"))
