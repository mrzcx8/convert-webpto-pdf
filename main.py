from flask import Flask, render_template, request, send_file
from PIL import Image
import os
import re
import uuid
import time
from datetime import datetime, timedelta

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FOLDER = 'output'
ALLOWED_EXTENSIONS = ['.webp', '.png', '.jpg', '.jpeg']
LOG_FILE = 'log.txt'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def natural_key(text):
    return [
        int(s) if s.isdigit() else s.lower() for s in re.split(r'(\d+)', text)
    ]


def cleanup_old_sessions(folder, max_age_hours=1):
    now = time.time()
    for root, dirs, files in os.walk(folder):
        for dir in dirs:
            path = os.path.join(root, dir)
            if os.stat(path).st_mtime < now - max_age_hours * 3600:
                os.system(f"rm -rf '{path}'")


def log_activity(session_id, num_files):
    with open(LOG_FILE, 'a') as log:
        log.write(
            f"{datetime.now()} - Session: {session_id} - Files: {num_files}\n")


def allowed_file(filename):
    return os.path.splitext(filename.lower())[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    cleanup_old_sessions(UPLOAD_FOLDER)

    if request.method == 'POST':
        uploaded_files = request.files.getlist("images")
        session_id = str(uuid.uuid4())
        session_folder = os.path.join(UPLOAD_FOLDER, session_id)
        os.makedirs(session_folder, exist_ok=True)

        jpg_paths = []
        for file in uploaded_files:
            if allowed_file(file.filename):
                filename = file.filename.rsplit(".", 1)[0] + ".jpg"
                save_path = os.path.join(session_folder, filename)
                try:
                    img = Image.open(file.stream).convert("RGB")
                    img.save(save_path, "JPEG")
                    jpg_paths.append(save_path)
                except Exception as e:
                    print(f"Error: {e}")

        jpg_paths.sort(key=lambda x: natural_key(os.path.basename(x)))

        if jpg_paths:
            log_activity(session_id, len(jpg_paths))
            images = [Image.open(p).convert("RGB") for p in jpg_paths]
            pdf_filename = f"{session_id}.pdf"
            pdf_path = os.path.join(OUTPUT_FOLDER, pdf_filename)
            images[0].save(pdf_path, save_all=True, append_images=images[1:])
            return send_file(pdf_path, as_attachment=True)

    return render_template('index.html')


app.run(host='0.0.0.0', port=5000)
