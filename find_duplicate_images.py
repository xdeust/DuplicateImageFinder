#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Duplicate Image Finder
Finds and lists duplicate image files in the Downloads folder.
"""

import os
import hashlib
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set
import sys
import io

# Fix Windows console encoding issues
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Image file extensions
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff', '.tif', '.ico', '.svg'}

def get_downloads_folder() -> Path:
    """Returns the path to the Downloads folder."""
    return Path.home() / "Downloads"

def calculate_file_hash(file_path: Path, chunk_size: int = 8192) -> str:
    """Calculates the MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(chunk_size):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except (IOError, PermissionError) as e:
        print(f"⚠️  Could not read file ({file_path.name}): {e}")
        return None

def find_image_files(directory: Path) -> List[Path]:
    """Finds all image files in the specified directory."""
    image_files = []
    
    print(f"📁 Scanning directory: {directory}")
    print("=" * 80)
    
    try:
        for item in directory.rglob('*'):
            if item.is_file() and item.suffix.lower() in IMAGE_EXTENSIONS:
                image_files.append(item)
    except PermissionError as e:
        print(f"⚠️  Access denied: {e}")
    
    return image_files

def find_duplicates(image_files: List[Path]) -> Dict[str, List[Path]]:
    """Finds duplicates among image files."""
    hash_to_files = defaultdict(list)
    
    print(f"\n🔍 Checking {len(image_files)} image files...")
    print("=" * 80)
    
    for idx, file_path in enumerate(image_files, 1):
        if idx % 10 == 0 or idx == len(image_files):
            print(f"Processing: {idx}/{len(image_files)}", end='\r')
        
        file_hash = calculate_file_hash(file_path)
        if file_hash:
            hash_to_files[file_hash].append(file_path)
    
    print(f"\nProcessing: {len(image_files)}/{len(image_files)} ✓")
    
    # Return only hashes with 2 or more files (duplicates)
    duplicates = {h: files for h, files in hash_to_files.items() if len(files) > 1}
    
    return duplicates

def format_file_size(size_bytes: int) -> str:
    """Returns file size in readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"

def print_duplicates(duplicates: Dict[str, List[Path]]):
    """Prints duplicate files to screen."""
    if not duplicates:
        print("\n✅ No duplicate images found!")
        return
    
    total_duplicates = sum(len(files) - 1 for files in duplicates.values())
    total_wasted_space = 0
    
    print(f"\n{'='*80}")
    print(f"🔍 RESULTS")
    print(f"{'='*80}")
    print(f"📊 Found {total_duplicates} duplicates in {len(duplicates)} different image groups.\n")
    
    for idx, (file_hash, files) in enumerate(duplicates.items(), 1):
        # Get file size
        file_size = files[0].stat().st_size
        wasted_space = file_size * (len(files) - 1)
        total_wasted_space += wasted_space
        
        print(f"\n{'─'*80}")
        print(f"Group {idx}: {len(files)} copies ({format_file_size(file_size)} each)")
        print(f"Wasted space: {format_file_size(wasted_space)}")
        print(f"Hash: {file_hash[:16]}...")
        print(f"{'─'*80}")
        
        for file_idx, file_path in enumerate(sorted(files), 1):
            # Relative path
            try:
                rel_path = file_path.relative_to(Path.home())
                display_path = f"~/{rel_path}"
            except ValueError:
                display_path = str(file_path)
            
            marker = "📌" if file_idx == 1 else "📄"
            print(f"  {marker} {display_path}")
    
    print(f"\n{'='*80}")
    print(f"💾 Total wasted disk space: {format_file_size(total_wasted_space)}")
    print(f"{'='*80}\n")

def main():
    """Main program."""
    print("\n" + "="*80)
    print("🖼️  DUPLICATE IMAGE FINDER")
    print("="*80 + "\n")
    
    # Get Downloads folder
    downloads_folder = get_downloads_folder()
    
    if not downloads_folder.exists():
        print(f"❌ Error: Downloads folder not found: {downloads_folder}")
        sys.exit(1)
    
    # Find image files
    image_files = find_image_files(downloads_folder)
    
    if not image_files:
        print("❌ No image files found in Downloads folder.")
        sys.exit(0)
    
    # Find duplicates
    duplicates = find_duplicates(image_files)
    
    # Print results
    print_duplicates(duplicates)
    
    print("\n✨ Scan complete!\n")
    
    # Keep window open
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
