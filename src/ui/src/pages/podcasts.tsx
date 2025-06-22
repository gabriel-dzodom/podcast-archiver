import { Layout } from "antd";

const { Header, Content } = Layout;

export const PodcastsPage: React.FC = () => {
    return (
        <>
            <Header style={{ height:'128px'}} className='layout-dark'>
                Podcasts Home Header
            </Header>
            <Content style={{ margin: '8px', }} className='layout-dark'>
            <div>
                Podcasts Home Content
            </div>
            </Content>
        </>
    );
}