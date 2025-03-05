# J.A.R.V.I.S - Your Personal Voice Assistant

J.A.R.V.I.S is a simple AI-powered voice assistant that can perform various tasks, including opening websites, playing YouTube songs, fetching news, and answering your questions using an AI model. You can enhance its capabilities by modifying the existing code.

## Installation

Follow these steps to set up and run J.A.R.V.I.S on your system:

### Step 1: Install Requirements
Ensure you have Python installed, then run the following command to install all required dependencies:
```sh
pip install -r requirements.txt
```

### Step 2: Run the Application
Execute the following command to start J.A.R.V.I.S:
```sh
python main.py
```

### Step 3: Activate J.A.R.V.I.S
Once the program is running, say **"Jarvis"** to wake up the assistant.

## Features

### 1. Open Websites
J.A.R.V.I.S can open frequently used websites such as:
- Google
- Facebook
- Instagram
- YouTube
- LinkedIn

You can extend this functionality by adding more websites in the `processCommand` function.

### 2. Play YouTube Songs
J.A.R.V.I.S can play songs on YouTube. To play a song, use the command:
```sh
play songname
```
The assistant currently has five predefined songs in the `musicLibrary.py` file, but you can add more.

### 3. Fetch Latest News
J.A.R.V.I.S can read the latest news headlines using the News API. To use this feature, integrate your own [NewsAPI](https://newsapi.org/) key.

### 4. AI-Powered Question Answering
J.A.R.V.I.S can answer your questions using an AI model. To enable this, add your own Gemini API key.

## How to Customize?
- **Add More Websites**: Modify `processCommand` in `main.py`.
- **Expand Music Library**: Edit `musicLibrary.py` and add more songs.
- **Enable News Feature**: Add your API key in the news-fetching function.
- **Improve AI Model**: Replace the existing API key with your own Gemini API key.

## Contributing
Feel free to improve J.A.R.V.I.S by adding new features and optimizing the code. Pull requests are welcome!

## License
This project is open-source and available for personal and educational use.

---

Enjoy using J.A.R.V.I.S! 🚀

