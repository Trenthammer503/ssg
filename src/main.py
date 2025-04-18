from textnode import *
import os
import shutil

def copy_recursive(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copy_recursive(s, d)
        else:
            shutil.copy2(s, d)
            print(f"Copied: {d}")

def main():
    source_dir = "static"
    dest_dir = "public"
    copy_recursive(source_dir, dest_dir)

main()