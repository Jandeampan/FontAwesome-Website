#!/usr/bin/env python

# app.py

# Import necessary modules
from flask import Flask, render_template, send_from_directory, abort, request, jsonify
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Render index.html from public folder
@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

# Serve static files from public folder
@app.route('/<path:path>')
def serve_static(path):
    try:
        return send_from_directory('public', path)
    except FileNotFoundError:
        abort(404)

# Serve js and css files from src folder
@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('src', 'js/' + filename)

@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('src', 'css/' + filename)

# Handle hybridaction requests
@app.route('/hybridaction/<action>', methods=['GET', 'POST'])
def handle_hybrid_action(action):
    if action == 'zybTrackerStatisticsAction':
        # Here you should implement the logic for zybTrackerStatisticsAction
        # For now, we'll just return a dummy response
        return jsonify({"status": "success", "message": "zybTrackerStatisticsAction handled"})
    else:
        abort(404)

# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Start the Flask app
if __name__ == '__main__':
    try:
        PORT = int(os.environ['PORT'])
        app.run(host='0.0.0.0', port=PORT, debug=True)
    except (KeyError, ValueError):
        print("Error: Please set a valid PORT environment variable.")
        exit(1)
