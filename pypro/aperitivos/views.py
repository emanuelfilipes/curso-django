from django.shortcuts import render


def video(request, slug):
    video = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 640497475},
        'instalacao-windows': {'titulo': 'Instalação Windows', 'vimeo_id': 640754710},
    }
    video = video[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
