import subprocess

pipeline = "gst-launch-1.0 rtspsrc location=rtsp://localhost:8554/input protocols=tcp latency=0 ! rtph264depay ! decodebin ! x264enc bitrate=2048 ! rtspclientsink location=rtsp://localhost:8554/output protocols=tcp"

subprocess.run(pipeline, shell=True)