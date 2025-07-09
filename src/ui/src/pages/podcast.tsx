import { Layout } from "antd";
import { Podcast } from "../models/podcast";

const { Header, Content } = Layout;

type PodcastPageProps = {
    podcast: Podcast | null;
}


export const PodcastPage: React.FC<PodcastPageProps> = ({podcast}) => {
    // If no podcast is selected, redirect
    if (!podcast) {
        // do something else
        // return <Navigate to="/" replace />;
    }
    return (
        <>
            <Header style={{ height:'128px'}} className='layout-dark'>
                {podcast ? podcast.title : 'Podcast Details Header'}
            </Header>
            <Content style={{ margin: '8px', }} className='layout-dark'>
            <div>
                {podcast ? podcast.description : 'Podcast Details Content'}
            </div>
            </Content>
        </>
    );
}