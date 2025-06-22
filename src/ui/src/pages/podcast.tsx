import { Layout } from "antd";

const { Header, Content } = Layout;

export const PodcastPage: React.FC = () => {
    return (
        <>
            <Header style={{ height:'128px'}} className='layout-dark'>
                Podcast Page Header
            </Header>
            <Content style={{ margin: '8px', }} className='layout-dark'>
            <div>
                Podcast Page Content
            </div>
            </Content>
        </>
    );
}