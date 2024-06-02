# Suno-py

Suno-py is a Python library that provides a convenient wrapper for interacting with the Suno API. It simplifies the process of generating music, extending audio clips, retrieving audio information, and managing API usage quotas.

## Installation

You can install Suno-py using pip:
```bash
pip install suno-py
```


## Usage

First, import the `Suno` class from the `suno` module:

```python
from suno import Suno
```


Then, initialize the `Suno` class with the base URL of the Suno API:

```python
suno = Suno("https:")
```

## Suno Class Documentation

The `Suno` class provides methods to interact with the Suno API:

- `custom_generate_audio(payload)`: Generate music in custom mode, supporting lyrics, style, title, etc.
- `extend_audio(payload)`: Extend the length of an existing audio clip.
- `generate_audio_by_prompt(payload)`: Generate music based on a text prompt.
- `get_audio_information(audio_ids)`: Get information about one or more audio clips by their IDs.
- `get_quota_information()`: Get information about API usage quotas.
- `get_clip(clip_id)`: Get information about a specific audio clip by its ID.
- `generate_whole_song(clip_id)`: Generate a full song based on an existing audio clip.
- `wait_for_audio(ids, max_attempts=60, delay=5)`: Wait for one or more audio clips to finish processing.

## Usage Examples

Here are some examples of how to use the `Suno` class:


### Generate Music in Custom Mode

To generate music in custom mode, use the `custom_generate_audio` method. This method supports lyrics, style, title, and other parameters:

```python
payload = {
"lyrics": "Hello, world",
"style": "pop",
"title": "My Song"
}
response = suno.custom_generate_audio(payload)
print(response)
```


### Extend an Existing Audio Clip

To extend the length of an existing audio clip, use the `extend_audio` method:


```python
payload = {
    "clip_id": "12345",
    "length": 60
}
response = suno.extend_audio(payload)
print(response)gth": 60
```



### Generate Music Based on a Text Prompt

To generate music based on a text prompt, use the `generate_audio_by_prompt` method:

```python
payload = {
"prompt": "A song about the sunrise"
}
response = suno.generate_audio_by_prompt(payload)
print(response)
```


### Get Information About Audio Clips

To get information about one or more audio clips by their IDs, use the `get_audio_information` method:

```python
audio_ids = "12345,67890"
response = suno.get_audio_information(audio_ids)
print(response)
```


### Get API Usage Quotas

To get information about API usage quotas, use the `get_quota_information` method:

```python
response = suno.get_quota_information()
print(response)
```


### Get Information About a Specific Audio Clip

To get information about a specific audio clip by its ID, use the `get_clip` method:

```python
clip_id = "12345"
response = suno.get_clip(clip_id)
print(response)
```


### Generate a Full Song Based on an Existing Audio Clip

To generate a full song based on an existing audio clip, use the `generate_whole_song` method:

```python
clip_id = "12345"
response = suno.generate_whole_song(clip_id)
print(response)
```


### Wait for Audio Clips to Finish Processing

To wait for one or more audio clips to finish processing, use the `wait_for_audio` method:

```python
ids = "12345,67890"
response = suno.wait_for_audio(ids)
print(response)
```



Remember to replace `"http://localhost:3000"` with the actual base URL of the Suno API, and replace the example IDs and payloads with your actual data.


### Initialize the Suno Class

```python
from suno import Suno

# Initialize the Suno class
suno = Suno("http://localhost:3000")

# Generate music in custom mode
payload = {
    "lyrics": "Hello, world",
    "style": "pop",
    "title": "My Song"
}
response = suno.custom_generate_audio(payload)

# Get the ID of the generated audio
audio_id = response['id']

# Wait for the audio to finish processing
suno.wait_for_audio(audio_id)

# Download the audio and save it in the root directory
suno.download_audio(audio_id, './my_song.mp3')

print("Song has been saved as my_song.mp3 in the root directory.")

```
