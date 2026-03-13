import gi
gi.require_version("Gst", "1.0")
from gi.repository import Gst

Gst.init(None)

pipeline_str = """
rtspsrc location=rtsp://localhost:8554/input protocols=tcp latency=0 !
rtph264depay !
decodebin !
x264enc bitrate=2048 !
rtspclientsink location=rtsp://localhost:8554/output protocols=tcp
"""

pipeline = Gst.parse_launch(pipeline_str)

pipeline.set_state(Gst.State.PLAYING)

try:
    input("Pipeline running... Press Enter to stop\n")
finally:
    pipeline.set_state(Gst.State.NULL)