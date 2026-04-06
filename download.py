import os
import sys
import shutil
import yt_dlp


def tem_ffmpeg():
    """Verifica se o ffmpeg está disponível no sistema"""
    return shutil.which("ffmpeg") is not None


def baixar(url, modo="video", formato=None):
    pasta_saida = "downloads"
    os.makedirs(pasta_saida, exist_ok=True)

    ffmpeg_instalado = tem_ffmpeg()

    print(f"FFmpeg instalado: {ffmpeg_instalado}")

    if modo == "audio":
        if not formato:
            formato = "mp3"

        if ffmpeg_instalado:
            # Melhor qualidade com conversão
            opcoes = {
                "format": "bestaudio/best",
                "outtmpl": os.path.join(pasta_saida, "%(title)s.%(ext)s"),
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": formato,
                        "preferredquality": "192",
                    }
                ],
            }
        else:
            # Sem ffmpeg → baixa áudio direto (sem conversão)
            print("⚠️ FFmpeg não encontrado. Baixando áudio sem conversão...")
            opcoes = {
                "format": "bestaudio[ext=m4a]/bestaudio",
                "outtmpl": os.path.join(pasta_saida, "%(title)s.%(ext)s"),
            }

    else:  # modo == "video"
        if not formato:
            formato = "mp4"

        if ffmpeg_instalado:
            # Melhor qualidade (vídeo + áudio separados → merge)
            opcoes = {
                "format": "bestvideo+bestaudio/best",
                "merge_output_format": formato,
                "outtmpl": os.path.join(pasta_saida, "%(title)s.%(ext)s"),
            }
        else:
            # Sem ffmpeg → baixa mp4 já com áudio
            print("⚠️ FFmpeg não encontrado. Baixando versão com áudio embutido...")
            opcoes = {
                "format": "best[ext=mp4]/best",
                "outtmpl": os.path.join(pasta_saida, "%(title)s.%(ext)s"),
            }

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url])
        print("✅ Download concluído!")
    except Exception as e:
        print(f"❌ Erro: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso:")
        print("  python baixar.py <URL> <modo: video|audio> [formato]")
        print("\nExemplos:")
        print("  python baixar.py <URL> video mp4")
        print("  python baixar.py <URL> audio mp3")
        sys.exit(1)

    url = sys.argv[1]
    modo = sys.argv[2]
    formato = sys.argv[3] if len(sys.argv) > 3 else None

    baixar(url, modo, formato)