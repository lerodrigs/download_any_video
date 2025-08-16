import yt_dlp
import sys

def download_video(url, output = '.'):
    # Configura as opções para o yt-dlp
    ydl_opts = {
        'format': 'best',  # Baixa a melhor qualidade de vídeo e áudio disponíveis
        'outtmpl': f'{output}/%(title)s.%(ext)s',  # Define o nome e o caminho de saída
    }

    try:
        # Cria a instância do yt_dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Iniciando o download do vídeo da URL: {url}")
            # Baixa o vídeo
            ydl.download([url])
            print("Download concluído com sucesso!")

    except yt_dlp.utils.DownloadError as e:
        print(f"Ocorreu um erro ao baixar o vídeo: {e}")
    except Exception as e:
        print(f"Um erro inesperado ocorreu: {e}")

if __name__ == "__main__": 
    url = input("passa a url ai, maluco:")
    download_video(url)