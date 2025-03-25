# (c) 2025, Gabriel Dzodom
# All rights reserved.

import os
from typing import List
from fastapi.testclient import TestClient
from src.services.podcasts.storage import SQL_FILE_PATH, Storage
from src.main import app
from src.services.podcasts.models import Podcast


class TestPodcastAPI:
    def setup_method(self):
        storage = Storage()
        storage.initialize() 
        self.client = TestClient(app)
        
    def teardown_method(self):
        # Cleanup logic if needed
        if os.path.exists(SQL_FILE_PATH):
            os.remove(SQL_FILE_PATH)
    
    def test_root(self):
        response = self.client.get("/api/v1/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}    
    
    def _test_get_podcasts(self, expected_count: int):
        podcasts = self.client.get("/api/v1/podcasts")
        assert podcasts.status_code == 200
        data = podcasts.json()
        assert isinstance(data, List)
        assert len(data) == expected_count
    
    def test_podcast_api(self):
        self._test_get_podcasts(0)  # Ensure no podcasts exist initially
        
        new_podcasts: List[Podcast] = [
            Podcast(
                title="Podcast 1",
                description="Description for podcast 1",
                icon="http://example.com/icon1.png",
                primary_feed_url="http://example.com/feed1",
                secondary_feed_url="http://example.com/secondary_feed1",
            ),
            Podcast(
                title="Podcast 2",
                description="Description for podcast 2",
                icon="http://example.com/icon2.png",
                primary_feed_url="http://example.com/feed2",
                secondary_feed_url="http://example.com/secondary_feed2",
            )
        ]
        
        for podcast in new_podcasts:
            response = self.client.post(
                "/api/v1/podcasts",
                headers={"Content-Type": "application/json"},
                json=podcast.model_dump(mode="json"),
            )
            assert response.status_code == 200
            data = response.json()
            assert data["id"] is not None
            assert data["id"] == podcast.id  # Ensure the ID is returned
            assert data["title"] == podcast.title
            assert data["description"] == podcast.description
            assert data["primary_feed_url"] == podcast.primary_feed_url
            assert data["secondary_feed_url"] == podcast.secondary_feed_url
            assert data["icon"] == podcast.icon
        
        self._test_get_podcasts(2)  # Ensure two podcasts exist now
                
        # Test getting a specific podcast
        podcast_id = new_podcasts[0].id
        response = self.client.get(f"/api/v1/podcasts/{podcast_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == podcast_id
        assert data["title"] == new_podcasts[0].title
        assert data["description"] == new_podcasts[0].description
        assert data["primary_feed_url"] == new_podcasts[0].primary_feed_url
        assert data["secondary_feed_url"] == new_podcasts[0].secondary_feed_url
        assert data["icon"] == new_podcasts[0].icon
        
        # Test updating a podcast
        updated_podcast = Podcast(
            id=podcast_id,
            title="Updated Podcast 1",
            description="Updated description for podcast 1",
            icon="http://example.com/updated_icon1.png",
            primary_feed_url="http://example.com/updated_feed1",
            secondary_feed_url="http://example.com/updated_secondary_feed1",
        )
        response = self.client.put(
            "/api/v1/podcasts",
            headers={"Content-Type": "application/json"},
            json=updated_podcast.model_dump(mode="json"),
        )
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == podcast_id
        assert data["title"] == updated_podcast.title
        assert data["description"] == updated_podcast.description
        assert data["primary_feed_url"] == updated_podcast.primary_feed_url
        assert data["secondary_feed_url"] == updated_podcast.secondary_feed_url
        assert data["icon"] == updated_podcast.icon
        
        # Verify the podcast was updated
        response = self.client.get(f"/api/v1/podcasts/{podcast_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == updated_podcast.id
        assert data["title"] == updated_podcast.title
        assert data["description"] == updated_podcast.description
        assert data["primary_feed_url"] == updated_podcast.primary_feed_url
        assert data["secondary_feed_url"] == updated_podcast.secondary_feed_url
        assert data["icon"] == updated_podcast.icon
        
        # Test deleting a podcast
        response = self.client.delete(f"/api/v1/podcasts/{podcast_id}")
        assert response.status_code == 200
        data = response.json()
        assert data == podcast_id
        self._test_get_podcasts(1)
        
        # Ensure the podcast was deleted
        response = self.client.get(f"/api/v1/podcasts/{podcast_id}")
        assert response.status_code == 404
        assert response.json() == {"detail": "Podcast not found"}
        
        # Test deleting a non-existent podcast
        response = self.client.delete(f"/api/v1/podcasts/{podcast_id}")
        assert response.status_code == 404
        assert response.json() == {"detail": f"Podcast not found with id {podcast_id}"}
        self._test_get_podcasts(1)
        
        # Test deleting all podcasts
        for podcast in new_podcasts[1:]:
            response = self.client.delete(f"/api/v1/podcasts/{podcast.id}")
            assert response.status_code == 200
            data = response.json()
            assert data == podcast.id
            
        self._test_get_podcasts(0)
        