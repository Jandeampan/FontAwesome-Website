# Setup Instructions

1. Ensure you have Python installed on your system.

2. Install the required Python packages:

```bash
pip install flask python-dotenv
```

3. Create the following directory structure:

```plaintext
project_root/
├── public/
│   └── index.html
├── src/
│   ├── css/
│   │   └── index.css
│   └── js/
│       └── index.js
├── templates/
│   └── 404.html
├── .env
└── app.py
```

4. Copy the contents of each file into their respective locations:
   - `public/index.html`: Contains the main HTML structure of the website
   - `src/css/index.css`: Includes all the styles for the website
   - `src/js/index.js`: Contains JavaScript functionality, including the code copying feature
   - `templates/404.html`: Custom 404 error page
   - `.env`: Stores environment variables (e.g., PORT=5000)
   - `app.py`: Flask application code that serves the website and handles routes

5. Ensure all files are in their correct locations as per the directory structure.

6. Run the Flask application:

```bash
python app.py
```

7. Open a web browser and navigate to `http://localhost:5000` to view the website.

## File Descriptions

- `public/index.html`: The main page of the Font Awesome website, showcasing various icons and their usage.
- `src/css/index.css`: Styles the website, including responsive design and animations for a modern look.
- `src/js/index.js`: Implements the functionality to copy icon code to the clipboard.
- `templates/404.html`: A custom 404 error page for better user experience when a page is not found.
- `.env`: Contains environment variables, currently setting the PORT for the application.
- `app.py`: The Flask application that serves the static files and handles routing.

**Note**: Make sure to keep the directory structure intact and all files in their designated locations for the application to function correctly.
