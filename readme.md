# Virtual Therapist - Your AI powered Therapist for all your one stop needs!

This is just a side hobby project started by two dudes. It uses the following stack: Vite, ReactJS, FastAPI and OpenAI's ChatGPT to deliver the full and unique potential
that this bot has to offer. 

To get started with this project this is what you have to do:

## Setup:

### Setup procedure (General):

1. Git clone repo
2. Check Node, NPM and Python are installed and versions using the following:

```
python --version
npm --version
node --version
```

If any of the above doesn't work, that means you will need to install one of the above programs. 

### Backend Specific Setup:


1. Cd into backend folder, create a virtual venv for Python to manage dependcies and such as follows:

```
python -m venv venv
```

2. Activate the virtual environment using the following:

```
./venv/Scripts/activate
```

3. Run the following to install the dependencies (i.e. packages to make sure our Python script works):

```
pip install -r requirements.txt
```

4. Finally, we need to set up our API key. To do so, we need to create a new file called: .env and type the following:

```
OPENAI_API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXX" 
```

5. To test everything works, from the terminal/shell, type this:

```
python src.py
```

If it works, it should print the following message: Retrieved API Key successfully!

### Frontend Specific Setup:

1. Navigate to the folder frontend/virtual-therapist:

```
cd .virtual-therapist/frontend/virtual-therapist
```

2. Run the following:

```
npm install
npm run dev
```

3. To test the front end works, it should launch a new server on your localhost:8000, so you can navigate to your browser and launch the frontend.