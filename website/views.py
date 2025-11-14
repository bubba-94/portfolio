from django.conf import settings
from django.shortcuts import render
from django.http import FileResponse
import plotly.express as px

def home(request):
    tech_categories = [
        {
            "title": "Languages",
            "icons": [
                {"name": "C++", "src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg"},
                {"name": "C", "src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg"},
                {"name": "Python", "src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg"},
                {"name": "Bash", "src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg"},
                {"name": "C#", "src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg"},
                {"name": "HTML5", "src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"},
            ],
        },
        {
            "title": "Tools",
            "icons": [
                {"name": "VS Code", "src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg"},
                {"name": "Linux", "src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg"},
                {"name": "Git", "src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"},
                {"name": "Docker", "src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg"},
                {"name": "CMake", "src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cmake/cmake-original.svg"},
            ],
        },
        {
            "title": "Embedded",
            "icons": [
                {"name": "Arduino", "src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/arduino/arduino-original.svg"},
                {"name": "Raspberry Pi", "src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/raspberrypi/raspberrypi-original.svg"},
                {"name": "PlatformIO", "src": "https://cdn.simpleicons.org/platformio/F5822B"},
            ],
        },
        {
            "title": "Cloud & DevOps ",
            "icons": [
                {"name": "Azure", "src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/azure/azure-original.svg"},
                {"name": "Kubernetes", "src": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kubernetes/kubernetes-plain.svg"},
                {"name": "MySQL", "src": "https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg"},
            ],
        },
    ]

    return render(request, 'website/home.html', {"tech_categories": tech_categories})