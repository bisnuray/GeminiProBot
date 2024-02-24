<h1 align="center">Gemini Pro Telegram Bot 🌌</h1>

<p align="center">
  <em>Gemini is an advanced Artificial Intelligence (AI) system designed to intelligently respond to diverse prompts, including pictures, text, speech, music, and code. This Python Telegram Bot script leverages the aiogram library to interact with Google's AI.</em>
</p>
<hr>

## 🌟 Features

- 🔄 **Asynchronous Communication**: Leverages the power of async for seamless interactions.
- ⚙️ **Error Handling**: Robust error handling for a smoother user experience.
- 🍪 **Text Prompt Response**: Accepts text prompts and generates text.
- 🖼️ **Image Recognition**: Can read and interpret images.

For more detailed information on the capabilities and availability of Google Gemini AI, please visit [Google's official blog](https://blog.google/technology/ai/google-gemini-ai/#availability).

## Getting Started 🚀

To utilize Gemini Pro, configure your environment with the necessary API key and service account credentials. Follow these steps to get started:

### Prerequisites

- Python 3.9 or higher 🐍
- Libraries: `aiogram==2.25.1`, `PIL`, `io`, `logging`, `google-generativeai` 📚
- Environment Variables: `GOOGLE_API_KEY`, `GOOGLE_APPLICATION_CREDENTIALS` 🗝️

1. Install the required dependencies, ensuring Python 3.9 or higher:

    ```bash
    pip install aiogram==2.25.1 Pillow google-generativeai
    ```

   Note: The `PIL` package is part of the `Pillow` library, which is a more up-to-date fork of PIL.

2. Create a Google Cloud Platform (GCP) service account and download the JSON key file. Follow these steps:

   - Go to [Google Cloud Console](https://console.cloud.google.com/).
   - Navigate to the project where you want to create a service account.
   - In the left sidebar, click on the hamburger menu and select "IAM & Admin" > "Service accounts."
   - Click on "Create Service Account" at the top of the page.
   - Enter a name for the service account, choose a role (e.g., Project > Editor), and click "Continue."
   - Skip the "Grant users access to this service account" section and click "Done."
   - Locate the newly created service account in the list and click on the pencil icon to the right.
   - Navigate to the "Add Key" tab, choose JSON as the key type, and click "Create." Save the downloaded JSON file to a secure location.

3. Obtain a Google API key by following the link [here](https://makersuite.google.com/app/apikey).

4. Set the Google API key and the path to your service account credentials as environment variables:

    ```bash
    export GOOGLE_API_KEY=<your-api-key>
    export GOOGLE_APPLICATION_CREDENTIALS=/path/to/serviceaccount.json
    ```

   Replace `<your-api-key>` and `/path/to/serviceaccount.json` with your actual Google API key and the path to your service account JSON file, respectively.

<h2 align="center">Setting Environment Variables Permanently on a VPS</h2>

To set environment variables permanently on a VPS :

1. **Open the Profile File**

   For a single user, edit `~/.bashrc`:

    ```bash
    nano ~/.bashrc
    ```

2. **Add the Environment Variables**

   At the bottom, add:

    ```bash
    export GOOGLE_API_KEY="your-api-key-here"
    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/serviceaccount.json"
    ```

   Replace `"your-api-key-here"` and `"/path/to/serviceaccount.json"` with your actual details.

3. **Save and Exit**

   Press `Ctrl + O`, then `Enter` and .Press `Ctrl + X`, to exit 

4. **Apply the Changes**

   Reload the profile:

    ```bash
    source ~/.bashrc
    ```
## Deploy to VPS

```sh
git clone https://github.com/bisnuray/GeminiProBot
cd GeminiProBot
nano gemini.py [ replace with your actual bot token ]
python3 gemini.py
```
### Setting Up the Bot

1. Create a new bot with [@BotFather](https://t.me/botfather) on Telegram and get the bot token.
2. Replace the placeholder token in the script with your actual bot token.

### Running the Bot

Execute the script to start the bot:

```bash
python gemini.py
```
## Usage 🛠️
The bot supports the following commands:

- /gem: Generates a response based on a text prompt.
- /imgai: Generates a response based on an image.
Ensure to reply to an image with /imgai command for it to work.

## Author 📝

- Name: Bisnu Ray
- Telegram: [@SmartBisnuBio](https://t.me/SmartBisnuBio)

Feel free to reach out if you have any questions or feedback.
