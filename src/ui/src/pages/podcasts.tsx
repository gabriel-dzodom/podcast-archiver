import { Col, Layout, Row } from "antd";
import { FolderFilled } from '@ant-design/icons';
import { Podcast } from "../models/podcast";
import { PodcastCard } from "../components/podcast-card";
import { Link } from "react-router-dom";
import { IconHeader } from "../components/icon-header";

const { Content } = Layout;

type PodcastsPageProps = {
    podcasts: readonly Podcast[];
}

export const PodcastsPage: React.FC<PodcastsPageProps> = ({podcasts}) => {
    return (
        <>
            <IconHeader iconComponent={FolderFilled} title="Podcast Subscriptions" />
            { podcasts.length === 0 ? 
                <Content style={{ margin: '8px', textAlign: 'center', padding: '24px' }} className='layout-dark'>
                    <h2>No Podcast Subscribed</h2>
                    <p><Link to="/podcast/new" title="Add a new podcast">Add a new podcast</Link> to your subscriptions.</p>
                </Content>
                :
                <Content style={{ margin: '8px', }} className='layout-dark'>
                {
                    <Row gutter={[24, 24]}>
                        {
                            podcasts.map((podcast) => (
                                <Col key={podcast.id} className="gutter-row" span={6} >
                                    <PodcastCard key={podcast.id} podcast={podcast} />
                                </Col>
                            ))
                        }
                    </Row>
                }
            </Content>
            }
        </>
    );
}