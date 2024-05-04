import os
from pytube import YouTube


def get_desktop_path():
    platform = os.name
    if platform == "nt":  # Windows
        return os.path.join(os.environ['USERPROFILE'], 'Desktop')
    else:  # Mac or Linux
        return os.path.expanduser("~/Desktop")


def download_video_from_youtube(url, save_path=None):
    if save_path is None:
        save_path = get_desktop_path()

    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        stream.download(save_path)
        print("Видео успешно скачано в", save_path)
    except Exception as e:
        print(f"Произошла ошибка при скачивании видео: {str(e)}")


if __name__ == "__main__":
    video_url = input("Введите URL видео на YouTube: ")
    download_video_from_youtube(video_url)
