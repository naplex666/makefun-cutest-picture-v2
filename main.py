#!/usr/bin/env python3
import hashlib
from pathlib import Path
import shutil

def main():
    script_dir = Path(__file__).resolve().parent
    asset_path = script_dir / 'assets' / 'entry.jpg'
    
    output_dir = Path('/output')
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / 'entry.png'
    
    shutil.copyfile(asset_path, output_path)
    
    byte_size = output_path.stat().st_size
    sha256_hash = hashlib.sha256(output_path.read_bytes()).hexdigest()
    
    print(f"Output Path: {output_path}")
    print(f"Byte Size: {byte_size}")
    print(f"SHA-256: {sha256_hash}")

if __name__ == '__main__':
    main()
