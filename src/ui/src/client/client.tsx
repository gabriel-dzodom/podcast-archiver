import { Podcast } from "../models/podcast";

class PodcastApiClientClass {
    constructor() {}

    getPodcasts = () => {
        const podcasts: Array<Podcast> = []
        for (let i = 0; i < 10; i++) {
            podcasts.push({
                id: `${i}`,
                title: `The Black Myth Podcast ${i}`,
                description: `Description ${i}`,
                icon: `/pa.svg`,
                primary_feed_url: `https://example.com/podcast${i}.xml`,
                secondary_feed_url: `https://example.com/podcast${i}.xml`,
                episodes: [
                    {
                        id: `${i}.1`,
                        title: `Episode ${i}.1`,
                        description: `Description ${i}`,
                        audio_url: `https://example.com/episode${i}.1.mp3`,
                        podcast_id: `${i}`,
                        archived: true,
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

    findPodcasts = (searchTerm: string): Array<Podcast> => {
        const podcasts = new Array<Podcast>();
        const titles = [
            'Chapo Trap House',
            'Citations Needed',
            'Hood Communists',
            'TrueAnon',
            'Guerrilla History',
            'Rev Left Radio',
            'Blowback',
            'The Black Myth Podcast',
        ];

        for (let i = 0; i < titles.length; i++) {
            podcasts.push({
                id: `${i}`,
                title: titles[i],
                description: `${titles[i]}`,
                icon: `/pa.svg`,
                primary_feed_url: `https://example.com/podcast${i}.xml`,
                secondary_feed_url: `https://example.com/podcast${i}.xml`,
                episodes: []
            });
        }

        if (!searchTerm) {
            return new Array<Podcast>();
        }
        const lowerSearchTerm = searchTerm.toLowerCase();
        return podcasts.filter(p => p.title.toLowerCase().includes(lowerSearchTerm) || p.description.toLowerCase().includes(lowerSearchTerm));
    }
}

const PodcastApiClient = new PodcastApiClientClass();
Object.freeze(PodcastApiClient);
export default PodcastApiClient