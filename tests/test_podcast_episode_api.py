# (c) 2025, Gabriel Dzodom
# All rights reserved.

import os
from typing import List
from fastapi.testclient import TestClient

from src.services.podcasts.models import Podcast, PodcastEpisode
from src.services.podcasts.storage import SQL_FILE_PATH, Storage
from src.main import app


class TestPodcastEpisodeApi:
    def setup_method(self):
        storage = Storage()
        storage.initialize() 
        self.client = TestClient(app)
        
    def teardown_method(self):
        if os.path.exists(SQL_FILE_PATH):
            os.remove(SQL_FILE_PATH)
    
    def _test_get_podcast_episodes(self, podcast_id:str, expected_count: int):
        response = self.client.get(f"/api/v1/podcasts/{podcast_id}/episodes")   
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, List)
        assert len(data) == expected_count
    
    def test_podcast_episode_api(self):
        podcast: Podcast = Podcast(
            title="Sample Podcast",
            description="Sample description",
            icon="http://example.com/icon.png",
            primary_feed_url="http://example.com/feed",
            secondary_feed_url="http://example.com/secondary_feed",
        )
        
        # Create a podcast
        response = self.client.post(
            "/api/v1/podcasts",
            headers={"Content-Type": "application/json"},
            json=podcast.model_dump(mode="json"),
        )
        assert response.status_code == 200
        
        self._test_get_podcast_episodes(podcast.id, 0)  # Ensure no episodes exist initially
        
        episodes: List[PodcastEpisode] = [
            PodcastEpisode(
                title="Episode 1",
                description="Description for episode 1",
                audio_url="http://example.com/audio1.mp3",
                podcast_id=podcast.id,
            ),
            PodcastEpisode(
                title="Episode 2",
                description="Description for episode 2",
                audio_url="http://example.com/audio2.mp3",
                podcast_id=podcast.id,
            )
        ]
        
        for episode in episodes:
            response = self.client.post(
                f"/api/v1/podcasts/{podcast.id}/episodes",
                headers={"Content-Type": "application/json"},
                json=episode.model_dump(mode="json"),
            )
            assert response.status_code == 200
            data = response.json()
            assert data["id"] is not None
            assert data["id"] == episode.id
            assert data["title"] == episode.title
            assert data["description"] == episode.description
            assert data["audio_url"] == episode.audio_url
            assert data["podcast_id"] == episode.podcast_id
            assert data["archived"] == episode.archived
            assert data["published_on"] == episode.published_on
            
        self._test_get_podcast_episodes(podcast.id, 2)
        
        episode_id = episodes[0].id
        response = self.client.get(f"/api/v1/podcasts/{podcast.id}/episodes/{episode_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == episode_id
        assert data["title"] == episodes[0].title
        assert data["description"] == episodes[0].description
        assert data["audio_url"] == episodes[0].audio_url
        assert data["podcast_id"] == episodes[0].podcast_id
        assert data["archived"] == episodes[0].archived
        assert data["published_on"] == episodes[0].published_on
        
        # Test updating an episode
        updated_episode = PodcastEpisode(
            id=episode_id,
            title="Updated Episode 1",
            description="Updated description for episode 1",
            audio_url="http://example.com/updated_audio1.mp3",
            podcast_id=podcast.id,
        )
        response = self.client.put(
            f"/api/v1/podcasts/{podcast.id}/episodes",
            headers={"Content-Type": "application/json"},
            json=updated_episode.model_dump(mode="json"),
        )
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == updated_episode.id
        assert data["title"] == updated_episode.title
        assert data["description"] == updated_episode.description
        assert data["audio_url"] == updated_episode.audio_url
        assert data["podcast_id"] == updated_episode.podcast_id
        assert data["archived"] == updated_episode.archived
        assert data["published_on"] == updated_episode.published_on
        
        # Verify the episode was updated
        response = self.client.get(f"/api/v1/podcasts/{podcast.id}/episodes/{episode_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == updated_episode.id
        assert data["title"] == updated_episode.title
        assert data["description"] == updated_episode.description
        assert data["audio_url"] == updated_episode.audio_url
        assert data["podcast_id"] == updated_episode.podcast_id
        assert data["archived"] == updated_episode.archived
        assert data["published_on"] == updated_episode.published_on
        
        # Test deleting an episode
        response = self.client.delete(f"/api/v1/podcasts/{podcast.id}/episodes/{episode_id}")
        assert response.status_code == 200
        data = response.json()
        assert data == episode_id
        self._test_get_podcast_episodes(podcast.id, 1)
        
        # Verify the episode was deleted
        response = self.client.get(f"/api/v1/podcasts/{podcast.id}/episodes/{episode_id}")
        assert response.status_code == 404
        assert response.json() == {"detail": f"Podcast episode not found with id {episode_id}"}
        
        # Test deleting the remaining episode
        remaining_episode_id = episodes[1].id
        response = self.client.delete(f"/api/v1/podcasts/{podcast.id}/episodes/{remaining_episode_id}")
        assert response.status_code == 200
        data = response.json()
        assert data == remaining_episode_id
        self._test_get_podcast_episodes(podcast.id, 0)
        # Verify the episode was deleted
        response = self.client.get(f"/api/v1/podcasts/{podcast.id}/episodes/{remaining_episode_id}")
        assert response.status_code == 404
        assert response.json() == {"detail": f"Podcast episode not found with id {remaining_episode_id}"}
        
        # delete the podcast
        response = self.client.delete(f"/api/v1/podcasts/{podcast.id}")
        assert response.status_code == 200
        data = response.json()
        assert data == podcast.id
        
        # Verify the podcast was deleted
        response = self.client.get(f"/api/v1/podcasts/{podcast.id}")
        assert response.status_code == 404
        assert response.json() == {"detail": "Podcast not found"}

    def test_delete_all_podcast_episodes(self):
        podcast: Podcast = Podcast(
            title="Sample Podcast",
            description="Sample description",
            icon="http://example.com/icon.png",
            primary_feed_url="http://example.com/feed",
            secondary_feed_url="http://example.com/secondary_feed",
        )
        
        # Create a podcast
        self.client.post(
            "/api/v1/podcasts",
            headers={"Content-Type": "application/json"},
            json=podcast.model_dump(mode="json"),
        )
        
        self._test_get_podcast_episodes(podcast.id, 0)  # Ensure no episodes exist initially
        
        episodes: List[PodcastEpisode] = [
            PodcastEpisode(
                title="Episode 1",
                description="Description for episode 1",
                audio_url="http://example.com/audio1.mp3",
                podcast_id=podcast.id,
            ),
            PodcastEpisode(
                title="Episode 2",
                description="Description for episode 2",
                audio_url="http://example.com/audio2.mp3",
                podcast_id=podcast.id,
            )
        ]
        
        for episode in episodes:
            self.client.post(
                f"/api/v1/podcasts/{podcast.id}/episodes",
                headers={"Content-Type": "application/json"},
                json=episode.model_dump(mode="json"),
            )

        self._test_get_podcast_episodes(podcast.id, 2)
        
        # Test deleting all episodes
        response = self.client.delete(f"/api/v1/podcasts/{podcast.id}/episodes")
        assert response.status_code == 200
        data = response.json()
        assert data == podcast.id
        self._test_get_podcast_episodes(podcast.id, 0)
