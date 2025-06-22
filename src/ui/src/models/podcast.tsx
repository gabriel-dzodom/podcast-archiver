interface PodcastEpisode {
    id: string;
    title: string;
    description: string;
    audio_url: string;
    podcast_id: string;
    archived: boolean;
    published_on: Date;
};

interface Podcast {
    id: string;
    title: string;
    description: string;
    icon: string;
    primary_feed_url: string;
    secondary_feed_url: string;
    episodes: PodcastEpisode[];
};

type PodcastState = {
    podcasts: Podcast[];
    selectedPodcast: Podcast | null;
    selectedEpisode: PodcastEpisode | null;
    loading: boolean;
    error: string | null;
};

type PodcastAction = {
    type: string;
    payload?: Podcast[] | Podcast | PodcastEpisode | string | boolean | PodcastEpisode[];
}

type PodcastDispatch = (action: PodcastAction) => PodcastAction;

export type { Podcast, PodcastEpisode, PodcastState, PodcastAction, PodcastDispatch };
