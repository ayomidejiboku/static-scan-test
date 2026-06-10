import subprocess
import pickle
import yaml
import hashlib
import os

# Command injection
subprocess.run("ls -la; cat /etc/passwd", shell=True)

# Insecure YAML load
yaml.load("!!python/object/apply:os.system ['echo hacked']", Loader=yaml.Loader)

# Insecure pickle
pickle.loads(b"cos\nsystem\n(S'echo hacked'\ntR.")

# Weak hashing
hashlib.md5(b"password").hexdigest()

# Arbitrary file write
open("/tmp/pwned.txt", "w").write("owned")
