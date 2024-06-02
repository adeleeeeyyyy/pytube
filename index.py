import pytube
import os

class YouTubeDownloader:
    def __init__(self, url):
        self.url = url
        self.youtube = pytube.YouTube(url)

    def download(self, file_extension):
        if file_extension == 'mp4':
            self.download_video()
        elif file_extension == 'mp3':
            self.download_audio()
        else:
            print("Ekstensi file tidak didukung. Silakan pilih 'mp4' atau 'mp3'.")

    def download_video(self):
        video_stream = self.youtube.streams.get_highest_resolution()
        output_path = video_stream.download()
        print(f"Video berhasil diunduh: {output_path}")

    def download_audio(self):
        audio_stream = self.youtube.streams.filter(only_audio=True).first()
        output_path = audio_stream.download()
        base, ext = os.path.splitext(output_path)
        new_file = base + '.mp3'
        os.rename(output_path, new_file)
        print(f"Audio berhasil diunduh: {new_file}")

if __name__ == "__main__":
    url = input("Masukkan URL YouTube: ")
    file_extension = input("Pilih ekstensi file (mp4/mp3): ").lower()

    downloader = YouTubeDownloader(url)
    downloader.download(file_extension)

