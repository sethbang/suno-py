import unittest
from unittest.mock import patch, MagicMock
from suno_py.suno import Suno
import sys

print(sys.path)


class TestSuno(unittest.TestCase):
    def setUp(self):
        self.suno = Suno("http://localhost:3000")

    @patch('suno.requests.post')
    def test_custom_generate_audio(self, mock_post):
        payload = {
            "lyrics": "Hello, world",
            "style": "pop",
            "title": "My Song"
        }
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "12345"}
        mock_post.return_value = mock_response

        response = self.suno.custom_generate_audio(payload)
        self.assertEqual(response, {"id": "12345"})
        mock_post.assert_called_once_with(
            "http://localhost:3000/api/custom_generate",
            json=payload,
            headers={'Content-Type': 'application/json'}
        )

    @patch('suno.requests.post')
    def test_extend_audio(self, mock_post):
        payload = {
            "clip_id": "12345",
            "length": 60
        }
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "extended"}
        mock_post.return_value = mock_response

        response = self.suno.extend_audio(payload)
        self.assertEqual(response, {"status": "extended"})
        mock_post.assert_called_once_with(
            "http://localhost:3000/api/extend_audio",
            json=payload,
            headers={'Content-Type': 'application/json'}
        )

    @patch('suno.requests.post')
    def test_generate_audio_by_prompt(self, mock_post):
        payload = {
            "prompt": "A song about the sunrise"
        }
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "67890"}
        mock_post.return_value = mock_response

        response = self.suno.generate_audio_by_prompt(payload)
        self.assertEqual(response, {"id": "67890"})
        mock_post.assert_called_once_with(
            "http://localhost:3000/api/generate",
            json=payload,
            headers={'Content-Type': 'application/json'}
        )

    @patch('suno.requests.get')
    def test_get_audio_information(self, mock_get):
        audio_ids = "12345,67890"
        mock_response = MagicMock()
        mock_response.json.return_value = [{"id": "12345"}, {"id": "67890"}]
        mock_get.return_value = mock_response

        response = self.suno.get_audio_information(audio_ids)
        self.assertEqual(response, [{"id": "12345"}, {"id": "67890"}])
        mock_get.assert_called_once_with(
            "http://localhost:3000/api/get?ids=12345,67890"
        )

    @patch('suno.requests.get')
    def test_get_quota_information(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"quota": "1000"}
        mock_get.return_value = mock_response

        response = self.suno.get_quota_information()
        self.assertEqual(response, {"quota": "1000"})
        mock_get.assert_called_once_with(
            "http://localhost:3000/api/get_limit"
        )

    @patch('suno.requests.get')
    def test_get_clip(self, mock_get):
        clip_id = "12345"
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "id": "12345", "status": "completed"}
        mock_get.return_value = mock_response

        response = self.suno.get_clip(clip_id)
        self.assertEqual(response, {"id": "12345", "status": "completed"})
        mock_get.assert_called_once_with(
            "http://localhost:3000/api/clip?id=12345"
        )

    @patch('suno.requests.post')
    def test_generate_whole_song(self, mock_post):
        clip_id = "12345"
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "67890"}
        mock_post.return_value = mock_response

        response = self.suno.generate_whole_song(clip_id)
        self.assertEqual(response, {"id": "67890"})
        mock_post.assert_called_once_with(
            "http://localhost:3000/api/concat",
            json={"clip_id": clip_id}
        )

    @patch('suno.requests.get')
    def test_wait_for_audio(self, mock_get):
        ids = "12345,67890"
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {"id": "12345", "status": "streaming"},
            {"id": "67890", "status": "streaming"}
        ]
        mock_get.return_value = mock_response

        response = self.suno.wait_for_audio(ids)
        self.assertEqual(response, [
            {"id": "12345", "status": "streaming"},
            {"id": "67890", "status": "streaming"}
        ])
        self.assertEqual(mock_get.call_count, 1)

    @patch('suno.requests.get')
    def test_download_audio(self, mock_get):
        audio_id = "12345"
        file_path = './my_song.mp3'
        mock_response = MagicMock()
        mock_response.iter_content.return_value = [b'test']
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        with patch("builtins.open", unittest.mock.mock_open()) as mock_file:
            self.suno.download_audio(audio_id, file_path)
            mock_file.assert_called_once_with(file_path, 'wb')
            mock_file().write.assert_called_once_with(b'test')
        mock_get.assert_called_once_with(
            "http://localhost:3000/api/download?id=12345",
            stream=True
        )

    @patch('suno.requests.post')
    def test_generate_lyrics(self, mock_post):
        payload = {
            "prompt": "A song about the sunset"
        }
        mock_response = MagicMock()
        mock_response.json.return_value = {"lyrics": "Sunset lyrics"}
        mock_post.return_value = mock_response

        response = self.suno.generate_lyrics(payload)
        self.assertEqual(response, {"lyrics": "Sunset lyrics"})
        mock_post.assert_called_once_with(
            "http://localhost:3000/api/generate_lyrics",
            json=payload,
            headers={'Content-Type': 'application/json'}
        )

    @patch('suno.requests.get')
    def test_get_all_audio_information(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = [{"id": "12345"}, {"id": "67890"}]
        mock_get.return_value = mock_response

        response = self.suno.get_all_audio_information()
        self.assertEqual(response, [{"id": "12345"}, {"id": "67890"}])
        mock_get.assert_called_once_with(
            "http://localhost:3000/api/get"
        )


if __name__ == '__main__':
    unittest.main()
