#!/usr/bin/env python3
# Entry: Duckling in a Rain Hat
# Approach: Deterministic file copy from assets/entry.jpg to /output/entry.png with strict output validation.
import os
import sys
import hashlib
import shutil

def main():
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    
    src_path = "assets/entry.jpg"
    dst_path = os.path.join(output_dir, "entry.png")
    
    shutil.copyfile(src_path, dst_path)
    
    # Output validation
    if not os.path.exists(dst_path):
        print(f"Error: Output file {dst_path} does not exist.", file=sys.stderr)
        sys.exit(1)
        
    file_size = os.path.getsize(dst_path)
    if not (0 < file_size < 1048576):
        print(f"Error: Output file size {file_size} bytes is invalid (must be > 0 and < 1048576 bytes).", file=sys.stderr)
        sys.exit(1)
        
    with open(dst_path, "rb") as f:
        header = f.read(3)
    if header != b'\xff\xd8\xff':
        print(f"Error: Output file magic bytes {header!r} do not match JPEG magic bytes b'\\xff\\xd8\\xff'.", file=sys.stderr)
        sys.exit(1)
        
    hasher = hashlib.sha256()
    with open(dst_path, "rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            hasher.update(chunk)
    sha256_hex = hasher.hexdigest()
    
    print(f"VALIDATION: OK | size={file_size} | SHA-256={sha256_hex}")
    print(f"Output path: {dst_path}")
    print(f"Byte size: {file_size}")
    print(f"SHA-256: {sha256_hex}")

if __name__ == "__main__":
    main()
