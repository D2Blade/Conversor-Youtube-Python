import os
import youtube_dl

def baixar_audio(url, qualidade):
    opcoes = {
        'format': 'bestaudio/best',
        'outtmpl': 'musica/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': qualidade,
        }],
    }

    if not os.path.exists('musica'):
        os.makedirs('musica')

    with youtube_dl.YoutubeDL(opcoes) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    link = input("Digite o link do vídeo do YouTube: ")
    qualidade = input("Digite a qualidade desejada (ex: 128, 192, 256): ")
    baixar_audio(link, qualidade)

