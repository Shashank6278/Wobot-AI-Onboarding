FROM python:3.10

RUN apt-get update && apt-get install -y \
gstreamer1.0-tools \
gstreamer1.0-plugins-base \
gstreamer1.0-plugins-good \
gstreamer1.0-plugins-bad \
gstreamer1.0-plugins-ugly \
gstreamer1.0-libav \
gstreamer1.0-rtsp \
ffmpeg

WORKDIR /app

COPY app/ .

CMD ["python", "reproxy.py"]