import { Podcast } from "../models/podcast";

class PodcastApiClientClass {
    constructor() {}

    getPodcasts = () => {
        const podcasts: Array<Podcast> = []
        for (let i = 0; i < 10; i++) {
            podcasts.push({
                id: `${i}`,
                title: `Podcast ${i}`,
                description: `Description ${i}`,
                icon: `./pa.svg`,
                primary_feed_url: `https://example.com/podcast${i}.xml`,
                secondary_feed_url: `https://example.com/podcast${i}.xml`,
                episodes: [
                    {
                        id: `${i}.1`,
                        title: `Episode ${i}.1`,
                        description: `Description ${i}`,
                        audio_url: `https://example.com/episode${i}.1.mp3`,
                        podcast_id: `${i}`,
                        archived: false,
                        published_on: new Date()
                    },
                    {
                        id: `${i}.2`,
                        title: `Episode ${i}.2`,
                        description: `Description ${i}`,
                        audio_url: `https://example.com/episode${i}.2.mp3`,
                        podcast_id: `${i}`,
                        archived: false,
                        published_on: new Date()
                    },
                ]
            });
        }
        return podcasts;        
    }
}

const PodcastApiClient = new PodcastApiClientClass();
Object.freeze(PodcastApiClient);
export default PodcastApiClient