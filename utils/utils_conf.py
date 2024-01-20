import subprocess


def get_udid_from_abd():
    result = subprocess.run(["adb", 'devices', '-l'], shell=True, text=True, capture_output=True)
    return result.stdout.split()[4]
