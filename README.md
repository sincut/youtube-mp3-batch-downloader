# 🎵 YouTube MP3 Batch Downloader

Download audio dari YouTube secara batch menggunakan daftar URL dalam file `links.txt`. Dibangun dengan Python dan didukung oleh `yt-dlp` serta `FFmpeg` untuk proses ekstraksi dan konversi audio ke format MP3.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![yt-dlp](https://img.shields.io/badge/yt--dlp-Latest-orange.svg)

---

## ✨ Features

* Batch download dari file `links.txt`
* Support video YouTube biasa
* Support YouTube Shorts
* Support YouTube Playlist
* Konversi otomatis ke MP3
* Pilihan kualitas audio (128, 192, 256, 320 kbps)
* Progress download real-time
* Error handling yang stabil
* Output folder dapat dikustomisasi

---

## 📦 Requirements

* Python 3.8+
* FFmpeg
* yt-dlp

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/youtube-mp3-batch-downloader.git
cd youtube-mp3-batch-downloader
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Atau install manual:

```bash
pip install yt-dlp tqdm colorama mutagen validators
```

---

## 🎬 Install FFmpeg

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install ffmpeg -y
```

### macOS

```bash
brew install ffmpeg
```

### Windows

1. Download FFmpeg dari https://ffmpeg.org/download.html
2. Ekstrak ke folder, misalnya:

```text
C:\ffmpeg
```

3. Tambahkan:

```text
C:\ffmpeg\bin
```

ke Environment Variables (PATH)

4. Verifikasi:

```bash
ffmpeg -version
```

---

## 📖 Usage

### 1. Buat File links.txt

Contoh:

```text
# Video
https://www.youtube.com/watch?v=VIDEO_ID

# Shorts
https://www.youtube.com/shorts/VIDEO_ID

# Playlist
https://www.youtube.com/playlist?list=PLAYLIST_ID
```

### 2. Jalankan Program

```bash
python download_mp3.py
```

---

## ⚙️ Configuration

```python
download_batch(
    file_path="links.txt",
    output_folder="musik",
    quality="192"
)
```

### Available Quality

| Quality | Bitrate  |
| ------- | -------- |
| 128     | 128 kbps |
| 192     | 192 kbps |
| 256     | 256 kbps |
| 320     | 320 kbps |

---

## 📁 Project Structure

```text
youtube-mp3-batch-downloader/
│
├── download_mp3.py
├── requirements.txt
├── links.txt
├── README.md
├── downloads/
└── musik/
```

---

## 🛠 Troubleshooting

### FFmpeg Not Found

```bash
ffmpeg -version
```

Pastikan FFmpeg sudah terinstall dan berada di PATH sistem.

### yt-dlp Not Found

```bash
pip install yt-dlp
```

### Update yt-dlp

```bash
pip install --upgrade yt-dlp
```

### Permission Error

Gunakan virtual environment:

```bash
python -m venv venv
```

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

## 📋 Example links.txt

```text
https://youtu.be/Cl6N8Cwxtlg
https://youtu.be/9a1aFrNJ3T8
https://youtu.be/4oUki4W7DJM
https://youtu.be/WZwhFStJnyA
```

---

## 📚 Dependencies

### Core

* yt-dlp
* FFmpeg

### Optional

* tqdm
* colorama
* mutagen
* validators

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

1. Fork repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Coy / SINCUT**

Built with Python, yt-dlp, and FFmpeg.

If this project helps you, consider giving it a ⭐ on GitHub.