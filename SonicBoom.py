import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp
import os

class YouTubeMP3Downloader:
    def __init__(self, root):
        self.root = root
        self.root.title("SonicBoom")
        self.root.geometry("500x250")
        self.root.resizable(False, False)

        # URL Entry
        tk.Label(root, text="YouTube URL:").pack(pady=10)
        self.url_entry = tk.Entry(root, width=60)
        self.url_entry.pack(pady=5)

        # Output Folder
        tk.Label(root, text="Output Folder:").pack(pady=10)
        self.folder_entry = tk.Entry(root, width=60)
        self.folder_entry.pack(pady=5)
        tk.Button(root, text="Browse", command=self.browse_folder).pack(pady=5)

        # Download Button
        tk.Button(root, text="Download MP3", command=self.download_mp3, width=20).pack(pady=20)

        # Status Label
        self.status_label = tk.Label(root, text="")
        self.status_label.pack(pady=10)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, folder)

    def download_mp3(self):
        url = self.url_entry.get().strip()
        output_path = self.folder_entry.get().strip()

        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return
        if not output_path:
            messagebox.showerror("Error", "Please select an output folder")
            return

        self.status_label.config(text="Downloading... Please wait.")
        self.root.update()

        # Use a relative path to ffmpeg.exe in the same folder as the script
        ffmpeg_path = os.path.join(os.path.dirname(__file__), 'ffmpeg.exe')

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': ffmpeg_path,  # Points to ffmpeg.exe in the same folder
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.status_label.config(text="Download completed!")
            messagebox.showinfo("Success", "MP3 downloaded successfully!")
        except Exception as e:
            self.status_label.config(text="Download failed!")
            messagebox.showerror("Error", f"Failed to download: {str(e)}")

def main():
    root = tk.Tk()
    app = YouTubeMP3Downloader(root)
    root.mainloop()

if __name__ == "__main__":
    main()
