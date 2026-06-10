import subprocess

# BAD: using shell=True is dangerous
subprocess.run("ls -la", shell=True)
