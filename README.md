# 🖼️ Duplicate Image Finder

A Python script to detect duplicate image files in your Downloads folder.

## ✨ Features

- 🔍 **Automatic Scanning**: Automatically scans Downloads folder and subfolders
- 🎯 **Multiple Format Support**: JPG, PNG, GIF, BMP, WEBP, TIFF, SVG and more
- 🔐 **Hash-Based Comparison**: Uses MD5 hash for 100% accurate detection
- 📊 **Detailed Reporting**: Duplicate groups, file sizes, and wasted disk space
- 💾 **Disk Space Savings**: Shows how much space you can save by removing duplicates
- 🪟 **Windows Compatible**: UTF-8 encoding support, no character issues

## 📦 Installation

### Requirements

- Python 3.12 or higher
- Windows operating system

### Using Python

```bash
# Clone the repository
git clone https://github.com/xdeust/DuplicateImageFinder.git
cd duplicate-image-finder

# Run the script
python find_duplicate_images.py
```

### Using EXE File

No Python installation required! Just download `DuplicateImageFinder.exe` and double-click to run.

## 🚀 Usage

When the script runs, it automatically:
1. Finds your Downloads folder
2. Scans all image files
3. Detects duplicate groups
4. Presents a detailed report

### Example Output

```
================================================================================
🔍 RESULTS
================================================================================
📊 Found 1 duplicates in 1 different image groups.

────────────────────────────────────────────────────────────────────────────────
Group 1: 2 copies (67.97 KB each)
Wasted space: 67.97 KB
Hash: 36cde6c14aba8ce1...
────────────────────────────────────────────────────────────────────────────────
  📌 ~/Downloads\image.jpg
  📄 ~/Downloads\image (1).jpg

================================================================================
💾 Total wasted disk space: 67.97 KB
================================================================================
```

## 🛠️ Building EXE File

To create your own EXE file:

```bash
# Install PyInstaller
pip install pyinstaller

# Build the EXE
pyinstaller --onefile --name "DuplicateImageFinder" --console find_duplicate_images.py

# The EXE will be created in the dist/ folder
```

## 📋 Supported Formats

- `.jpg` / `.jpeg`
- `.png`
- `.gif`
- `.bmp`
- `.webp`
- `.tiff` / `.tif`
- `.ico`
- `.svg`

## 🔒 Security

- The script only performs read operations, never deletes or modifies files
- All operations are performed locally on your computer
- No internet connection required

## 💡 Tips

- 📌 marker indicates the group leader (usually the original)
- 📄 marker indicates duplicates
- Files with identical hash values are 100% identical
- Manual verification is recommended before deletion

## 🤝 Contributing

Contributions are welcome! Feel free to submit pull requests.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👨‍💻 Developer

xDeust

## 🐛 Bug Reports

If you encounter any issues, please report them on the [Issues](https://github.com/xdeust/duplicate-image-finder/issues) page.

---

⭐ If you like this project, don't forget to give it a star!


