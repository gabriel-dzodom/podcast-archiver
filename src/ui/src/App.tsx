import React from 'react';
import { Layout, } from 'antd';
import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';
import { Home } from './components/home';
import { PodcastSideMenu } from './components/podcast-sidemenu';
import { PodcastsPage } from './pages/podcasts';
import { PodcastPage } from './pages/podcast';
import { useSelector } from 'react-redux';
import { Podcast, PodcastState } from './models/podcast';

const { Footer, Sider } = Layout;

const App: React.FC = () => {

  const podcasts: readonly Podcast[] = useSelector((state: PodcastState) => state.podcasts);
  const selectedPodcast: Podcast | null = useSelector((state: PodcastState) => state.selectedPodcast);

  return (
    <Router>
      <Layout style={{ minHeight: '100vh', minWidth: '60vw'}} className='layout-dark'>
        <Sider style={{borderRight:'1px solid rgba(240, 240, 240, 0.50)'}} width={224} className='layout-dark'>
          <Home />
          <PodcastSideMenu podcasts={podcasts} selectedPodcast={selectedPodcast} />
        </Sider>
        <Layout className='layout-dark'>
          <Routes>
            <Route path="/" element={<PodcastsPage />} />
            <Route path="/podcast" element={<PodcastPage podcast={selectedPodcast} />} />
          </Routes>
          <Footer style={{ height: '32px', textAlign: 'center',fontSize:'12px', padding:'8px 24px'}} className='layout-dark'>
            Pod Archiver © {new Date().getFullYear()} Created by Gabriel Dzodom
          </Footer>
        </Layout>
      </Layout>
    </Router>
  );
};

export default App;