import { Link } from "react-router-dom";
import { Podcast } from "../models/podcast";
import { selectPodcast } from "../store/actions";
import { Dispatch } from "redux";
import { useDispatch } from "react-redux";
import { Card } from "antd";


type PodcastCardProps = {
    podcast: Podcast;
}

export const PodcastCard: React.FC<PodcastCardProps> = ({podcast}) => {    
    
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const dispatch : Dispatch<any> = useDispatch();
    const onPodcastSelected = () => {
        dispatch(selectPodcast(podcast.id));
    };

    const episodes_text = `Episodes: ${podcast.episodes.length}`;
    const archived_count = podcast.episodes.filter(e => e.archived).length;
    const archived_text = `Archived: ${archived_count}`;
    const description = `${episodes_text} | ${archived_text}`;

    return (
        <Link title={podcast.title} to="/podcast" style={{ textDecoration: 'none' }} onClick={onPodcastSelected}>
            <Card
                className="podcast-card"
                cover={
                    <img
                        alt={podcast.title}
                        src={podcast.icon}
                    />
                }
            >
                <Card.Meta title={podcast.title} description={description} style={{ textAlign: 'center' }} />
            </Card>
        </Link>
    );
}
