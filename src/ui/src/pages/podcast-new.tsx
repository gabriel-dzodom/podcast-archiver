import { Layout, Space, Input, List, Skeleton, Modal, Card } from "antd";
import { IconHeader } from "../components/icon-header";
import { FolderAddFilled } from '@ant-design/icons';
import type { GetProps } from 'antd';
import PodcastApiClient from "../client/client";
import { Podcast } from "../models/podcast";
import React from "react";

type SearchProps = GetProps<typeof Input.Search>;

const { Content } = Layout;
const { Search } = Input;

const SearchResults: React.FC<{ podcasts: Podcast[] }> = ({ podcasts }) => {
    const [modalOpen, setModalOpen] = React.useState<boolean>(false);
    const [selectedPodcast, setSelectedPodcast] = React.useState<Podcast | null>(null);
    const openModal = () => setModalOpen(true);
    const closeModal = () => setModalOpen(false);

    return (
        <Content style={{ margin: '8px', }} className='layout-dark'>
            { podcasts.length === 0 ? 
                <div style={{ textAlign: 'center', padding: '24px' }}>
                    <h2>No Podcasts Found</h2>
                    <p>Try searching with different keywords.</p>
                </div>
                :
                <>
                    <List
                        itemLayout="horizontal"
                        dataSource={podcasts}
                        renderItem={(podcast) => (
                            <List.Item onClick={() => {
                                setSelectedPodcast(podcast);
                                openModal();
                            }}> 
                                <Skeleton avatar title={false} loading={false} active>
                                    <List.Item.Meta
                                        avatar={<img src={podcast.icon} alt={podcast.title} style={{ width: '48px', height: '48px'}} />}
                                        title={podcast.title.toUpperCase()}
                                        description={podcast.description}
                                    />
                                </Skeleton>
                            </List.Item>
                        )}
                        style={{ overflowY: 'auto' }}
                    />
                    <Modal
                        open={modalOpen}
                        onCancel={closeModal}
                        title="SUBSCRIPTION DETAILS"
                        width={360}
                        footer={[
                            <button key="subscribe" onClick={closeModal} className="modal-button">
                            SUBSCRIBE
                            </button>,
                        ]}
                        style={{ padding: '16px'}}
                    >
                        <Card
                            style={{ width: '100%', background: 'rgb(24,24,24)', border: 'unset' }}
                            cover={<img alt={selectedPodcast?.title} src={selectedPodcast?.icon} />}
                            
                        >
                            <Card.Meta 
                                title={selectedPodcast ? selectedPodcast.title.toUpperCase() : 'Podcast Title'}
                                description={selectedPodcast ? selectedPodcast.description : 'Podcast Description'} 
                            />
                        </Card>
                    </Modal>
                </>
            }
        </Content>
    );
}

export const NewPodcastPage: React.FC = () => {
    const [initLoading, setInitLoading] = React.useState<boolean>(true);
    const [podcasts, setPodcasts] = React.useState<Podcast[]>(new Array<Podcast>());

    const onSearch: SearchProps['onSearch'] = (value) => {
        if (!value || value.trim() === "") {
            setPodcasts([]);
            return;
        }
        const results = PodcastApiClient.findPodcasts(value)
        setInitLoading(false);
        setPodcasts(results)
    }

    React.useEffect(() => {
        // Initial load can be empty or some default podcasts
        setInitLoading(true);
    }, []);

    return (
        <>
            <IconHeader iconComponent={FolderAddFilled} title="Subscribe to a New Podcast" />
            <Content style={{ margin: '8px', }} className='layout-dark'>
                <Space direction="vertical" style={{ width: '100%' }}>
                    <Search
                        onSearch={onSearch}
                        size="large"
                        placeholder="Search for a podcast by name or description"
                        style={{ width: '100%' }}
                    />
                    {initLoading ? null : (
                        <SearchResults podcasts={podcasts} />
                    )}
                </Space>
            </Content>
        </>
    );
}