# controllers.py
import requests
import qrcode
import yt_dlp
from flask import request, jsonify

# General API route logic
def get_data():
    return jsonify({"message": "API is working!"}), 200

# Create a TinyURL link (GET only)
def create_tinyurl():
    original_url = request.args.get("url")
    
    if not original_url:
        return jsonify({"error": "URL is required"}), 400
    
    try:
        response = requests.get(f"http://tinyurl.com/api-create.php?url={original_url}")
        tiny_url = response.text
        return jsonify({"tiny_url": tiny_url}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Generate a QR code for a given text (GET only)
def generate_qr_code():
    text = request.args.get("text")
    
    if not text:
        return jsonify({"error": "Text is required"}), 400
    
    try:
        # Generate QR code from any given text (URL, number, or generic string)
        img = qrcode.make(text)
        img.save("qrcode.png")  # Save the generated QR code locally
        return jsonify({"message": "QR code generated", "qr_code_path": "/static/qrcode.png"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# YouTube downloader functionality using yt-dlp (GET only)
def download_youtube():
    video_url = request.args.get("url")
    
    if not video_url:
        return jsonify({"error": "URL is required"}), 400

    try:
        ydl_opts = {
            'outtmpl': './downloads/%(title)s.%(ext)s',  # Save location
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])  # Download video

        return jsonify({"message": "Video downloaded successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
	    
