import requests
import time


class Suno:
    """
    A Python class for interacting with the Suno API.

    Methods:
    - custom_generate_audio(payload): Generate music in custom mode, supporting lyrics, style, title, etc.
    - extend_audio(payload): Extend the length of an existing audio clip.
    - generate_audio_by_prompt(payload): Generate music based on a text prompt.
    - get_audio_information(audio_ids): Get information about one or more audio clips by their IDs.
    - get_quota_information(): Get information about API usage quotas.
    - get_clip(clip_id): Get information about a specific audio clip by its ID.
    - generate_whole_song(clip_id): Generate a full song based on an existing audio clip.
    - wait_for_audio(ids, max_attempts=60, delay=5): Wait for one or more audio clips to finish processing.
    - download_audio(audio_id, file_path): Download the resulting mp3 from a completed generation.
    - generate_lyrics(payload): Generate lyrics based on a text prompt.
    - get_all_audio_information(): Get information about all audio clips.
    """

    def __init__(self, base_url):
        self.base_url = base_url

    def custom_generate_audio(self, payload):
        """Generate music in custom mode, supporting lyrics, style, title, etc."""
        url = f"{self.base_url}/api/custom_generate"
        response = requests.post(url, json=payload, headers={
                                 'Content-Type': 'application/json'})
        return response.json()

    def extend_audio(self, payload):
        """Extend the length of an existing audio clip."""
        url = f"{self.base_url}/api/extend_audio"
        response = requests.post(url, json=payload, headers={
                                 'Content-Type': 'application/json'})
        return response.json()

    def generate_audio_by_prompt(self, payload):
        """Generate music based on a text prompt."""
        url = f"{self.base_url}/api/generate"
        response = requests.post(url, json=payload, headers={
                                 'Content-Type': 'application/json'})
        return response.json()

    def get_audio_information(self, audio_ids):
        """Get information about one or more audio clips by their IDs."""
        url = f"{self.base_url}/api/get?ids={audio_ids}"
        response = requests.get(url)
        return response.json()

    def get_quota_information(self):
        """Get information about API usage quotas."""
        url = f"{self.base_url}/api/get_limit"
        response = requests.get(url)
        return response.json()

    def get_clip(self, clip_id):
        """Get information about a specific audio clip by its ID."""
        url = f"{self.base_url}/api/clip?id={clip_id}"
        response = requests.get(url)
        return response.json()

    def generate_whole_song(self, clip_id):
        """Generate a full song based on an existing audio clip."""
        payload = {"clip_id": clip_id}
        url = f"{self.base_url}/api/concat"
        response = requests.post(url, json=payload)
        return response.json()

    def wait_for_audio(self, ids, max_attempts=60, delay=5):
        """
        Wait for one or more audio clips to finish processing.

        Args:
        - ids: A comma-separated string of audio clip IDs to wait for.
        - max_attempts: The maximum number of attempts to check the status of the audio clips.
        - delay: The number of seconds to wait between each attempt.

        Returns:
        - The audio information for the specified IDs once they have all finished processing.

        Raises:
        - TimeoutError: If the maximum number of attempts is reached before all audio clips have finished processing.
        """
        for _ in range(max_attempts):
            data = self.get_audio_information(ids)
            if all(item["status"] == 'streaming' for item in data):
                return data
            time.sleep(delay)
        raise TimeoutError(
            f"Timed out waiting for audio after {max_attempts} attempts")

    def download_audio(self, audio_id, file_path):
        """
        Download the resulting mp3 from a completed generation.

        Args:
        - audio_id: The ID of the audio clip to download.
        - file_path: The local file path where the mp3 should be saved.

        Returns:
        - None
        """
        url = f"{self.base_url}/api/download?id={audio_id}"
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        else:
            response.raise_for_status()

    def generate_lyrics(self, payload):
        """Generate lyrics based on a text prompt."""
        url = f"{self.base_url}/api/generate_lyrics"
        response = requests.post(url, json=payload, headers={
                                 'Content-Type': 'application/json'})
        return response.json()

    def get_all_audio_information(self):
        """Get information about all audio clips."""
        url = f"{self.base_url}/api/get"
        response = requests.get(url)
        return response.json()