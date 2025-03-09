

import datetime
from enum import Enum
from typing import Optional
import uuid
from sqlmodel import Field, SQLModel


class BaseModel(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True, default=uuid.uuid4())

class Podcast(BaseModel):
    title: str = Field(
        index=True,
        description="The title of the podcast",
        example="The Daily",
    )
    description: Optional[str] = Field(
        default=None,
        description="A description of the podcast",
        example="This is a daily news podcast",
    )
    icon = Optional[str] = Field(
        default=None,
        description="The icon of the podcast",
        example="https://example.com/icon.png",
    )
    primary_feed_url: str = Field(
        index=True,
        description="The primary feed URL of the podcast",
        example="https://example.com/feed.xml",
    )
    secondary_feed_url: Optional[str] = Field(
        default=None,
        description="The secondary feed URL of the podcast",
        example="https://example.com/secondary_feed.xml",
    )

class PodcastEpisode(BaseModel):
    title: str = Field(
        description="The title of the episode",
        example="Episode 1: The Beginning",
    )
    description: Optional[str] = Field(
        default=None,
        description="A description of the episode",
        example="This is the first episode of the podcast",
    )
    audio_url: str = Field(
        index=True,
        description="The URL of the audio file",
        example="https://example.com/episode1.mp3",
    )
    podcast_id: uuid.UUID = Field(
        foreign_key="podcast.id",
        description="The ID of the podcast this episode belongs to",
        example=uuid.uuid4(),
    )
    archived: bool = Field(
        default=False,
        description="Whether the episode is archived",
        example=False,
    )
    published_on: Optional[datetime] = Field( # type: ignore
        default=None,
        description="The date the episode was published",
        example="2023-01-01T00:00:00Z",
    )
    
class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    
class Task(BaseModel):
    status: TaskStatus = Field(
        default=TaskStatus.PENDING,
        description="The status of the task",
        example="pending",
    )
    progress: Optional[float] = Field(
        default=None,
        description="The progress of the task",
        example=0.5,
    )
    error_message: Optional[str] = Field(
        default=None,
        description="The error message if the task failed",
        example="An error occurred",
    )
    podcast_episode_id: uuid.UUID = Field(
        foreign_key="podcast_episode.id",
        description="The ID of the podcast episode this task is related to",
        example=uuid.uuid4(),
    )
