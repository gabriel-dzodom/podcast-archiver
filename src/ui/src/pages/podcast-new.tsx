import { Layout, Space, Input } from "antd";
import { IconHeader } from "../components/icon-header";
import { FolderAddFilled } from '@ant-design/icons';

const { Content } = Layout;
const { Search } = Input;


export const NewPodcastPage: React.FC = () => {
    return (
        <>
            <IconHeader iconComponent={FolderAddFilled} title="Subscribe to a New Podcast" />
            <Content style={{ margin: '8px', }} className='layout-dark'>
                <Space direction="vertical">
                    <Search
                        placeholder="Search for a podcast by name or URL"
                        style={{ width: '100%' }}
                    />
                </Space>
            </Content>
        </>
    );
}