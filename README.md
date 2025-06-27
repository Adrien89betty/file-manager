# FileManager

A lightweight macOS utility that automatically organizes your **Desktop** folder by sorting files into categories based on their extension (Images, Videos, Audios, PDFs, Text, Excel, Others).

---

## 📦 Features

- Scans `~/Desktop` and groups files into:
  - **Images** (`.jpg`, `.png`, `.gif`, …)
  - **Videos** (`.mp4`, `.mkv`, `.avi`, …)
  - **Audios** (`.mp3`, `.wav`, `.flac`, …)
  - **PDFs** (`.pdf`)
  - **Text** (`.txt`, `.md`, `.docx`, …)
  - **Excel** (`.xls`, `.xlsx`)
  - **Others** (unrecognized or no extension)
- Automatically creates destination folders if they don’t exist.
- Handles filename collisions by appending a numeric suffix (`file_1.ext`, `file_2.ext`, …).
- Universal2 executable (x86_64 + arm64): works natively on both Intel and Apple Silicon.
- Packaged as a single macOS app (`FileManager.app`) or a standalone CLI binary (`FileManager`).

---

## 🚀 Download and start using FileManager

### Download the Prebuilt Release

1. Go to the [Releases](https://github.com/Adrien89betty/file-manager/releases) page.
2. Download :
   **FileManager.app** (GUI application) — available as a ZIP.
3. Uncompress
4. Move it to your Application folder and run it !
