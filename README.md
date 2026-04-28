Aqui está a versão mais formal e profissional do README:

---

# YouTube Downloader (Vídeo e Áudio)

Script em Python para download de vídeos ou extração de áudio do YouTube, com suporte aos seguintes formatos:

- Vídeo: MP4
- Áudio: MP3, AAC, M4A
- Detecção automática de FFmpeg

---

## 1. Pré-requisitos

### Instalar o Python

Baixe o Python a partir do site oficial:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

Durante a instalação, selecione a opção:

```
Add Python to PATH
```

---

### Instalar o yt-dlp

No terminal (PowerShell ou CMD), execute:

```
pip install yt-dlp
```

---

### Instalar o FFmpeg (Recomendado)

O FFmpeg é necessário para:

- Conversão de áudio (MP3, AAC)
- Junção de vídeo e áudio em alta qualidade

#### Passos de instalação:

1. Acesse:
   [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)

2. Baixe o arquivo:

```
ffmpeg-release-essentials.zip
```

3. Extraia para o diretório:

```
C:\ffmpeg
```

4. Adicione ao PATH do sistema:

```
C:\ffmpeg\bin
```

5. Verifique a instalação:

```
ffmpeg -version
```

---

## 2. Estrutura do Projeto

```
/projeto
 ├── baixar.py
 └── downloads/
```

---

## 3. Execução

No terminal, dentro da pasta do projeto:

### Download de vídeo (MP4)

```
python download.py "URL_DO_VIDEO" video mp4
```

---

### Download de áudio (MP3)

```
python download.py "URL_DO_VIDEO" audio mp3
```

---

### Download de áudio (AAC)

```
python download.py "URL_DO_VIDEO" audio aac
```

---

## 4. Exemplos

```
python download.py "https://www.youtube.com/watch?v=BXd62mMu1UY" video mp4

python download.py "https://www.youtube.com/watch?v=BXd62mMu1UY" audio mp3
```

---

## 5. Comportamento do Script

### Com FFmpeg instalado:

- Download na melhor qualidade disponível
- Junção automática de vídeo e áudio
- Conversão de formatos de áudio

### Sem FFmpeg:

- Download de vídeo com áudio incorporado (qualidade inferior)
- Download de áudio sem conversão (formato original, geralmente M4A)

---

## 6. Problemas Comuns

### Vídeo sem áudio

Instale o FFmpeg e execute novamente o script.

---

### 'ffmpeg' is not recognized

Verifique se o diretório `C:\ffmpeg\bin` foi corretamente adicionado ao PATH.

---

### Erro no yt-dlp

Atualize a biblioteca:

```
pip install -U yt-dlp
```

---

## 7. Possíveis Extensões

- Interface gráfica (Tkinter ou Electron)
- Suporte a download de playlists
- Seleção manual de qualidade
- Exposição como API (FastAPI)

---

## Autor

Mário Teixeira Varela - github.com/trupakufi  
Projeto desenvolvido para fins educacionais e práticos.
