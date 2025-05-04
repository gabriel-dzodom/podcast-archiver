class Podcast {
    title!: string;
    description!: string;
    icon!: string;
    primary_feed_url!: string;
    secondary_feed_url!: string;
    episodes!: PodcastEpisode[];
}

class PodcastEpisode {
    title!: string;
    description!: string;
    audio_url!: string;
    podcast_id!: string;
    podcast!: Podcast;
    archived!: boolean;
    published_on!: Date;
}
