import { Col, Layout, Row } from "antd";
import { FolderFilled } from '@ant-design/icons';
import { Podcast } from "../models/podcast";
import { PodcastCard } from "../components/podcast-card";

const { Header, Content } = Layout;

type PodcastsPageProps = {
    podcasts: readonly Podcast[];
}


export const PodcastsPage: React.FC<PodcastsPageProps> = ({podcasts}) => {
    return (
        <>
            <Header style={{ height:'128px'}} className='layout-dark podcasts-header'>
                <FolderFilled style={{ fontSize: '48px', marginRight: '16px' }} />
                PODCAST SUBSCRIPTIONS
            </Header>
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
        </>
    );
}