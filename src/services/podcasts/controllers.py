# (c) 2025, Gabriel Dzodom
# All rights reserved.

from typing import List
from uuid import UUID

from fastapi import HTTPException
from sqlmodel import select

from .models import Podcast, PodcastEpisode
from .storage import SessionDependency


async def root():
    return {"message": "Hello World"}

async def get_podcasts(session: SessionDependency) -> List[Podcast]:
    # Logic to get podcasts
    return session.exec(select(Podcast)).all()

async def get_podcast(podcast_id: str, session: SessionDependency) -> Podcast:
    # Logic to get a podcast
    podcast = session.get(Podcast, podcast_id)
    if podcast:
        return podcast
    else:
        raise HTTPException(status_code=404, detail="Podcast not found")
    
async def set_podcast(podcast: Podcast, session: SessionDependency) -> Podcast:
    # Logic to create a podcast
    session.add(podcast)
    session.commit()
    session.refresh(podcast)
    return podcast

async def update_podcast(podcast: Podcast, session: SessionDependency) -> Podcast:
    # Logic to update a podcast
    if podcast.id is None:
        raise HTTPException(status_code=400, detail="Podcast ID is required")
    else:
        persisted_podcast = session.get(Podcast, podcast.id)
        if persisted_podcast is None:
            raise HTTPException(status_code=404, detail=f"Podcast not found with id {podcast.id}")
        else:
            persisted_podcast.sqlmodel_update(podcast)
            session.add(persisted_podcast)
            session.commit()
            session.refresh(persisted_podcast)
            return persisted_podcast

async def delete_podcast(podcast_id: str, session: SessionDependency) -> str:
    # Logic to delete a podcast
    if podcast_id is None:
        raise HTTPException(status_code=400, detail="Podcast ID is required")
    else:
        podcast = session.get(Podcast, podcast_id)
        if podcast is None:
            raise HTTPException(status_code=404, detail=f"Podcast not found with id {podcast_id}")
        elif podcast.episodes:
            raise HTTPException(status_code=400, detail="Cannot delete podcast with existing episodes")
        else:
            session.delete(podcast)
            session.commit()
            return podcast_id
        
async def delete_podcast_episodes(podcast_id: str, session: SessionDependency) -> str:
    # Logic to delete all episodes of a podcast
    podcast = session.get(Podcast, podcast_id)
    if podcast is None:
        raise HTTPException(status_code=404, detail=f"Podcast not found with id {podcast_id}")
    
    for episode in podcast.episodes:
        session.delete(episode)
    
    session.commit()
    return podcast_id

async def get_podcast_episodes(podcast_id: str, session: SessionDependency) -> List:
    podcast: Podcast = session.get(Podcast, podcast_id)
    if podcast is None:
        raise HTTPException(status_code=404, detail=f"Podcast not found with id {podcast_id}")
    return podcast.episodes if podcast.episodes else []

async def get_podcast_episode(podcast_id:str, episode_id: str, session: SessionDependency):
    podcast_episode = session.get(PodcastEpisode, episode_id)
    if podcast_episode is None:
        raise HTTPException(status_code=404, detail=f"Podcast episode not found with id {episode_id}")
    if podcast_episode.podcast_id != podcast_id:
        raise HTTPException(status_code=404, detail=f"Podcast episode {episode_id} does not belong to podcast {podcast_id}")
    return podcast_episode

async def set_podcast_episode(podcast_id: str, episode: PodcastEpisode, session: SessionDependency) -> PodcastEpisode:
    podcast = session.get(Podcast, podcast_id)
    if podcast is None:
        raise HTTPException(status_code=404, detail=f"Podcast not found with id {podcast_id}")
    episode.podcast_id = podcast_id
    session.add(episode)
    session.commit()
    session.refresh(episode)
    return episode

async def update_podcast_episode(podcast_id: str, episode: PodcastEpisode, session: SessionDependency) -> PodcastEpisode:
    podcast = session.get(Podcast, podcast_id)
    if podcast is None:
        raise HTTPException(status_code=404, detail=f"Podcast not found with id {podcast_id}")
    podcast_episode = session.get(PodcastEpisode, episode.id)
    if podcast_episode is None:
        raise HTTPException(status_code=404, detail=f"Podcast episode not found with id {episode.id}")
    if podcast_episode.podcast_id != podcast_id:
        raise HTTPException(status_code=404, detail=f"Podcast episode {episode.id} does not belong to podcast {podcast_id}")
    if podcast_episode.id != episode.id:
        raise HTTPException(status_code=400, detail="Episode ID in URL does not match the episode ID in the request body")
    
    # Update the episode attributes
    podcast_episode.sqlmodel_update(episode)
    session.add(podcast_episode)
    session.commit()
    session.refresh(podcast_episode)
    return podcast_episode

async def delete_podcast_episode(podcast_id: str, episode_id: str, session: SessionDependency) -> str:
    podcast = session.get(Podcast, podcast_id)
    if podcast is None:
        raise HTTPException(status_code=404, detail=f"Podcast not found with id {podcast_id}")
    
    podcast_episode = session.get(PodcastEpisode, episode_id)
    if podcast_episode is None:
        raise HTTPException(status_code=404, detail=f"Podcast episode not found with id {episode_id}")
    
    if podcast_episode.podcast_id != podcast_id:
        raise HTTPException(status_code=404, detail=f"Podcast episode {episode_id} does not belong to podcast {podcast_id}")
    
    session.delete(podcast_episode)
    session.commit()
    return episode_id
