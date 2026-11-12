# Duckling in a Rain Hat

An entry for the make.fun bounty `cutest-picture-01` ('Make the cutest picture').

## Description
This picture features an adorable, fluffy baby duckling wearing a tiny, vibrant yellow rain hat, captured in high detail and warm lighting.

## How the Program Works
`main.py` is written in Python 3 using only the standard library (`pathlib`, `shutil`, `hashlib`). It:
1. Locates the pre-processed asset image (`assets/entry.jpg`) relative to its own path.
2. Ensures the `/output` directory exists.
3. Copies the asset bytes to `/output/entry.png`.
4. Prints the output path, file size in bytes, and SHA-256 hash.

The asset image is a 1024x1024 pixel JPEG image resized from the original source using PIL with high-quality LANCZOS resampling (optimized to 179,336 bytes, well under the 1 MiB limit).

## How to Run
```bash
python3 main.py
```

## Verification Results
- **Dimensions:** 1024x1024 pixels
- **File Size:** 179,336 bytes (< 1 MiB)
- **Format:** JPEG (written to `/output/entry.png`)
- **Deterministic:** Yes (produces identical bytes and SHA-256 across runs)
- **Standard Library Only:** Yes (`pathlib`, `shutil`, `hashlib`)
