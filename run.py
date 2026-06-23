import yt_dlp
import os

def download_batch(file_path="links.txt", output_folder="downloads", quality="192"):
    """Download MP3 dari daftar link di file txt"""
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    with open(file_path, 'r') as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    if not urls:
        print("❌ FILE KOSONG KONTOL!")
        return
    
    print(f"🔥 TOTAL LINK: {len(urls)}")
    
    for i, url in enumerate(urls, 1):
        print(f"\n📥 [{i}/{len(urls)}] {url}")
        
        ydl_opts = {
            'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': quality,
            }],
            'quiet': True,
            'no_warnings': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                print(f"✅ [{i}] BERHASIL")
        except Exception as e:
            print(f"❌ [{i}] ERROR: {e}")

# ======== PAKE ========
download_batch("links.txt", "musik", "192")