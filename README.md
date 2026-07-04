Email Productivity Tool
A web app built with React and Python that summarizes emails using the Gemini API. It classifies whether an email is read-only or needs a response, flags if a file attachment is likely required, and generates a concise summary of the original message.

________________________________________________________________________________________________________________________
Features


Paste any email into a text field and get an instant summary.    
Automatically classifies the email as read-only or requiring a response.    
Flags whether a response is likely to need a file attachment.    
Summarizes the email to roughly 20–50% of its original length while preserving the core message.    
Clean, minimal interface built with React.    

_________________________________________________________________________________________________________________________

Tech Stack


Frontend - React (Create React App)
Backend logic - Python
AI Model - Gemini 2.5 Flash


__________________________________________________________________________________________________________________________
Environment Variables


GEMINI_API_KEY for authenticating requests to the Gemini API.

_________________________________________________________________________________________________________________________

Project Structure


├── src/
            ├── App.js # Main React component    
            ├── App.css # App styling    
            ├── App.test.js # App tests    
            ├── index.js # React entry point    
            ├── index.css # Global styling    
            ├── reportWebVitals.js # Performance reporting    
            ├── setupTests.js # Test setup    
            └── logo.svg # App logo    
├── backend.py # Python backend / Gemini integration    
├── requirements.txt # Python dependencies    
├── README.md # (this file)    


_____________________________________________________________________________________________________________________________
How It Works


The user pastes an email into the input field.    
The email text is sent to the Gemini 2.5 Flash model with a structured prompt.    
The model returns a JSON object containing:    
    - Read only (true/false)    
    - Files required in response (true/false)    
    - Summary (text)    
The result is displayed to the user in a read-only result box.    


______________________________________________________________________________________________________________________________
Getting Started


Clone the repository.    
Run npm install to install frontend dependencies.    
Run pip install -r requirements.txt to install backend dependencies.    
Add your Gemini API key as an environment variable.    
Run npm start to launch the app locally.    

______________________________________________________________________________________________________________________________

License    
ISC


Author    
Ayush Aditya

