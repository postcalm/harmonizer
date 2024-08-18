from subprocess import check_output

import psutil


def get_pid(name: str) -> int:
    output = str(check_output(f"tasklist | findstr {name}", shell=True))
    pid = int(output.split()[1])
    return pid


def get_exe_by_pid(pid: int) -> str:
    return psutil.Process(pid).exe()
