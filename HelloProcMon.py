__author__ = 'Justin Dearing <zippy1981@gmail.com>'
# Tested on Python 3.4

import win32file

GENERIC_WRITE = 0x40000000
OPEN_EXISTING = 3
FILE_WRITE_ACCESS = 0x0002
FILE_SHARE_WRITE = 0x00000002
FILE_ATTRIBUTE_NORMAL = 0x00000080
METHOD_BUFFERED = 0
FILE_DEVICE_PROCMON_LOG = 0x00009535
PROCMON_DEBUGGER_HANDLER = r"\\.\Global\ProcmonDebugLogger"
IOCTL_EXTERNAL_LOG_DEBUGOUT = 2503311876 # Why: https://github.com/zippy1981/ProcMon.LINQpad/blob/master/ProcMonDebugOutput.linq

msg = "Hello ProcMon!"
msgLen = 2 * len(msg)
handle = win32file.CreateFile(PROCMON_DEBUGGER_HANDLER, GENERIC_WRITE, FILE_SHARE_WRITE, None, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL,0)
print("handle %x" % handle)
win32file.DeviceIoControl(handle, IOCTL_EXTERNAL_LOG_DEBUGOUT, bytes(msg, 'UTF-16'), None)


win32file.CloseHandle(handle)