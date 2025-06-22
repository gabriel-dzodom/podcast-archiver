import { Menu } from 'antd';
import { Podcast } from '../models/podcast';
import { Link } from 'react-router-dom';
import { Dispatch } from 'redux';
import { useDispatch } from 'react-redux';
import { selectPodcast } from '../store/actions';


export const PodcastIcon = (podcast: Podcast) => {
    return (
        <img src={podcast.icon} style={{width: '20px', height: '20px' }} />
    );
}

const formatPodcastTitle = (_title: string) => {
    const maxLength = 15;
    const title = _title.toUpperCase();
    if (title.length > maxLength) {
        return title.substring(0, maxLength) + '...';
    }
    return title.toUpperCase();
}

type SideMenuProps = {
    podcasts: readonly Podcast[];
    selectedPodcast: Podcast | null;
}

export const PodcastSideMenu: React.FC<SideMenuProps> = ({podcasts, selectedPodcast}) => {    
    // const podcasts: readonly Podcast[] = useSelector((state: PodcastState) => state.podcasts);
    const items = podcasts.map(
        (podcast) => ({
            key: podcast.id,
            icon: PodcastIcon(podcast),
            label: formatPodcastTitle(podcast.title),
            title: podcast.title.toUpperCase(),
            extra: <Link to={`/podcast`} style={{ textDecoration: 'none' }} />
        }),
    );

    const selectedkeys = selectedPodcast ? [selectedPodcast.id] : [];
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const dispatch : Dispatch<any> = useDispatch();
    const onPodcastSelected = (e: { key: string }) => {
        dispatch(selectPodcast(e.key));
    };
    
    return (
        <Menu
            items={items}
            selectedKeys={selectedkeys}
            style={{borderRight:'none', borderRadius: 'none'}}
            className='layout-dark'
            onSelect={onPodcastSelected}
        />
    );
}
