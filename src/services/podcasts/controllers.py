# (c) 2025, Gabriel Dzodom
# All rights reserved.

from typing import List
from uuid import UUID

from fastapi import HTTPException
from sqlmodel import select

from .models import Podcast
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
    

async def get_podcast_episodes(podcast_id):
    # Logic to get podcast episodes
    pass

async def set_podcast(podcast: Podcast, session: SessionDependency) -> Podcast:
    # Logic to create a podcast
    session.add(podcast)
    session.commit()
    session.refresh(podcast)
    return podcast

async def create_podcast_episode(podcast_id, episode_data):
    # Logic to create a podcast episode
    pass

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

async def update_podcast_episode(podcast_id, episode_id, episode_data):
    # Logic to update a podcast episode
    pass

async def delete_podcast(podcast_id: str, session: SessionDependency) -> UUID:
    # Logic to delete a podcast
    if podcast_id is None:
        raise HTTPException(status_code=400, detail="Podcast ID is required")
    else:
        podcast = session.get(Podcast, podcast_id)
        if podcast is None:
            raise HTTPException(status_code=404, detail=f"Podcast not found with id {podcast_id}")
        else:
            session.delete(podcast)
            session.commit()
            return podcast_id

async def delete_podcast_episode(podcast_id, episode_id):
    # Logic to delete a podcast episode
    pass
