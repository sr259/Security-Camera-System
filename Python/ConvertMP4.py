import subprocess

class ConvertMP4:
    def convert(filename, output_file): #converts the mp4 to a viewable version so discord and other web platforms can read it without downloading
        subprocess.run(["ffmpeg", "-y", "-i", filename, "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "23",
        "-pix_fmt", "yuv420p",
        output_file
    ])

    def remove_file(filename):
        subprocess.run(["rm", filename])


if __name__ == "__main__":
    ConvertMP4.convert("output.mp4", "output_converted.mp4")
    ConvertMP4.remove_file("output.mp4")