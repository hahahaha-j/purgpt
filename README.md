# PurGPT.py Documentation

The `PurGPT.py` Python package provides easy access to the PurGPT API for various natural language processing and AI tasks. This documentation explains the methods and their usage within the `PurGPT` class.

For full documentation, please visit [https://purgpt.xyz](https://purgpt.xyz)

---

## Getting a token

Think you're worthy to start with PurGPT? We sure do! If you agree with us, simply follow the steps below!

- Head over to the [Discord server](https://discord.gg) <-- Invites are currently paused!

Once there, click into the [``# bots``](https://discord.com/channels/1117511140440821852/1117527621459267694) channel

Run the `/key` command

The PurGPT bot will respond with your key. **Do not, under any circumstance, share it with anyone!** It's yours :)

Now that you have your token, you can move on!

## Initializing the class

### `ai = purgpt.PurGPT(token, dev = True)`

Initialize the `PurGPT` class with a token and an optional development mode flag.

- `token` (str): The API token for authentication! 
- `dev` (bool, optional): If set to `True`, the package will return the full JSON response from the request. If `False` (default), it will return important information or an error.

---

## Methods

### Test method: `test()`

Test the API by recieving a test message. The AI will respond and tell a funny joke if it is online. 

- Returns:
  - (dict or str): If in development mode (`dev=True`), returns the full JSON response or an error message. Otherwise, returns the AI's response or an error message.

### Generate method: `generate(prompt, provider="openai", beta=True)`

Generate individual text based on a prompt.

- `prompt` (str): The text prompt for the AI.
- `provider` (str, optional): The provider for text generation (default is "openai").
- `beta` (bool, optional): Whether to use the beta version (default is `True`).

### Chat method: `chat(messages, provider="openai", beta=True)`

Engage in a chat conversation with AI.

- `messages` (list): List of message objects for the conversation. (Same formatting as with OpenAI's package!)
- `provider` (str, optional): The provider for chat completion (default is "openai").
- `beta` (bool, optional): Whether to use the beta version (default is `True`).

### Document Analysis: `document_analysis(document_url: str, prompt: str, beta=True)`

Analyze documents or images with AI.

- `document_url` (str): The URL of the document or image to analyze.
- `prompt` (str): A prompt for the analysis.
- `beta` (bool, optional): Whether to use the beta version (default is `True`).

### Contend Moderation: `moderations(prompt, beta=True)`

Perform content moderation on text.

- `prompt` (str): The text to be moderated.
- `beta` (bool, optional): Whether to use the beta version (default is `True`).

### Image Generation: `image(prompt, provider="openai", beta=True)`

Generate images based on a text prompt.

- `prompt` (str): The text prompt for image generation.
- `provider` (str, optional): The provider for image generation (default is "openai").
- `beta` (bool, optional): Whether to use the beta version (default is `True`).

### Audio Transcription: `transcribe(file_url, beta=True)`

Transcribe an audio file from its URL.

- `file_url` (str): The URL of the audio file.
- `beta` (bool, optional): Whether to use the beta version (default is `True`).

### Audio Translation: `translate(file_url, beta=True)`

Translate an audio file from its URL.

- `file_url` (str): The URL of the audio file.
- `beta` (bool, optional): Whether to use the beta version (default is `True`).

### Other: `custom(owner, endpoint, body, subdomain)`

Use a custom API endpoint.

- `owner` (str): The owner/provider of the custom endpoint.
- `endpoint` (str): The custom endpoint to call.
- `body` (dict): The request body as a dictionary.
- `subdomain` (str): The subdomain to use for the custom request. (i.e. "rp" (if you know you know 😉))

**Note:** For more details and usage examples, refer to the [PurGPT API documentation.](https://purgpt.xyz)

---

# Quickstart

```py
import purgpt
import os

token = "" #replace with your actuall token 

ai = purgpt.PurGPT(token)

print(ai.generate("Say hello"))
```

## Thats all! 
If you have any questions, feel free to reach out to [`@thecatsmoo`](https://tcm.gay) on Discord!
