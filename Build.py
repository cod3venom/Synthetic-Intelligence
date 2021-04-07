import os

linux_dir = "/usr/bin/FBView"

if os.path.isdir(linux_dir):
    os.system(f"cp -r {linux_dir} Linux/")
    print("BUILD SUCCESSFULLY")