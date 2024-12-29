from flask import Flask, render_template, request, redirect, url_for
from google.cloud import storage
import os

# Initialize Flask app
app = Flask(__name__)

# Set the GCS bucket name (replace with your bucket name)
GCS_BUCKET_NAME = 'bkt-emp-attrition-data'

# Set up Google Cloud Storage Client
storage_client = storage.Client()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    # Upload file to GCS
    upload_to_gcs(file)
    return 'File uploaded successfully'

def upload_to_gcs(file):
    bucket = storage_client.bucket(GCS_BUCKET_NAME)
    blob = bucket.blob(file.filename)
    blob.upload_from_file(file)

if __name__ == '__main__':
    app.run(debug=True)

