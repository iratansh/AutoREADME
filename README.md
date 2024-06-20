# AutoREADME

The provided code is a full-stack web application designed for a Google Chrome extension. It integrates a frontend implemented in HTML, CSS, and JavaScript with a backend powered by FastAPI. The application utilizes OpenAI's GPT-3.5 model to generate GitHub READMEs based on code snippets provided by users.

1. **JavaScript (popup.js)**:
   - Executes when the DOM content is fully loaded (`DOMContentLoaded` event).
   - Listens for a click event on the button with id `generateButton`.
   - Upon button click, retrieves the code entered in the textarea (`inputBox`), sends it as a POST request to `http://localhost:5002/generate_readme` (the FastAPI endpoint), and expects a JSON response containing the generated README.
   - Displays the generated README in the element with id `output`.

2. **HTML (index.html)**:
   - Provides the structure for the README generator web application.
   - Includes a textarea (`inputBox`) for entering code snippets, a button (`generateButton`) to trigger README generation, and a div (`output`) to display the generated README.
   - Defines additional styling and references to external JavaScript (`popup.js`).

3. **FastAPI Server (app.py)**:
   - Initializes a FastAPI application.
   - Configures CORS middleware to allow requests from a specific origin (a Chrome extension).
   - Defines a POST endpoint `/generate_readme` that expects a JSON payload containing a `code` field.
   - Utilizes the OpenAI API (via `openai` Python package) to generate a GitHub README based on the provided code snippet (`code`).
   - Returns the generated README as JSON in the response.

#### Technologies Used:
- **FastAPI**: FastAPI is a high-performance web framework for building APIs with Python 3.7+.
- **HTML/CSS/JavaScript**: Frontend technologies used to create the user interface and interaction for the README generator web application.
- **OpenAI API**: Provides natural language processing capabilities, specifically generating human-like text based on input prompts.
- **uvicorn**: Uvicorn is an ASGI server implementation used to run the FastAPI application.
- **pydantic**: Pydantic is employed for data validation and settings management within the FastAPI application, ensuring incoming data adheres to specified schemas.

#### Application Context:
- **Google Chrome Extension**: This application is designed to serve as a backend for a Google Chrome extension. Users can input code snippets through the extension's interface, which then communicates with the FastAPI server to generate GitHub READMEs using AI-powered text generation.
- **Full Stack Program**: Combines both frontend (HTML, CSS, JavaScript) and backend (FastAPI, OpenAI API) components to create a complete web application. Users interact with the frontend to initiate README generation, while the backend handles processing and responds with the generated content.

### How to Use:
1. **Setup**:
   - Install required Python packages (`fastapi`, `uvicorn`, `openai`, `pydantic`).
   - Replace `'INPUT_YOUR_OPEN_AI_API_KEY'` in `app.py` with your actual OpenAI API key.

2. **Running the Application**:
   - Start the FastAPI server by running `uvicorn app:app --reload`.
   - The server will run on `http://localhost:5002` by default.

3. **Using the Web Application**:
   - Open `index.html` in a web browser.
   - Enter a code snippet in the textarea and click `Generate README`.
   - The generated README will be displayed in the output section (`output` div) of the web application.

This setup provides a seamless integration between a frontend interface, powered by HTML/JavaScript, and a backend API implemented with FastAPI, utilizing OpenAI's GPT-3.5 model for automated GitHub README generation.

<img width="1580" alt="image" src="https://github.com/iratansh/AutoREADME/assets/151393106/76bfcdd4-749e-4735-92c4-5d3a868d6153">
