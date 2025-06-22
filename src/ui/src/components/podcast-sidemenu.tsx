import { Menu } from 'antd';
import React from 'react';
import { Podcast, PodcastState } from '../models/podcast';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';


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


export const PodcastSideMenu: React.FC = () => {    
    const podcasts: readonly Podcast[] = useSelector((state: PodcastState) => state.podcasts);
    const items = podcasts.map(
        (podcast) => ({
          key: podcast.id,
          icon: PodcastIcon(podcast),
          label: formatPodcastTitle(podcast.title),
          title: podcast.title.toUpperCase(),
          extra: <Link to={`/podcast`} style={{ textDecoration: 'none' }} />
        }),
      );
    
    return (
        <Menu items={items} style={{borderRight:'none', borderRadius: 'none'}} className='layout-dark' />
    );
}
