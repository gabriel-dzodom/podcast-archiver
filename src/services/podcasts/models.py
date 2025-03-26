# (c) 2025, Gabriel Dzodom
# All rights reserved.

from datetime import datetime
from enum import Enum
from typing import List, Optional
import uuid
from sqlmodel import Field, Relationship, SQLModel

def generate_uuid():
    """Generate a new UUID."""
    return str(uuid.uuid4())

class BaseModel:
    id: str = Field(primary_key=True, max_length=36, default_factory=generate_uuid, description="Unique identifier for the record")

class PodcastEpisode(BaseModel, SQLModel, table=True):
    title: str = Field(
        description="The title of the episode",
    )
    description: Optional[str] = Field(
        default=None,
        description="A description of the episode",
    )
    audio_url: str = Field(
        index=True,
        description="The URL of the audio file",
    )
    podcast_id: str = Field(
        foreign_key="podcast.id",
        description="The ID of the podcast this episode belongs to",
    )
    podcast: "Podcast" = Relationship(back_populates="episodes")
    archived: bool = Field(
        default=False,
        description="Whether the episode is archived",
    )
    published_on: Optional[datetime] = Field( # type: ignore
        default=None,
        description="The date the episode was published",
    )

class Podcast(BaseModel, SQLModel, table=True):
    title: str = Field(
        index=True,
        description="The title of the podcast",
    )
    description: Optional[str] = Field(
        default="",
        description="A description of the podcast",
    )
    icon: Optional[str] = Field(
        default="",
        description="The icon of the podcast",
    )
    primary_feed_url: str = Field(
        index=True,
        description="The primary feed URL of the podcast",
    )
    secondary_feed_url: Optional[str] = Field(
        default="",
        description="The secondary feed URL of the podcast",
    )
    episodes: List[PodcastEpisode] = Relationship(back_populates="podcast", sa_relationship_kwargs={"lazy": "selectin"})
    
class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    
class Task(BaseModel, SQLModel, table=True):
    status: TaskStatus = Field(
        default=TaskStatus.PENDING,
        description="The status of the task",
    )
    progress: Optional[float] = Field(
        default=None,
        description="The progress of the task",
    )
    error_message: Optional[str] = Field(
        default=None,
        description="The error message if the task failed",
    )
    podcast_episode_id: str = Field(
        foreign_key="podcastepisode.id",
        description="The ID of the podcast episode this task is related to",
    )
