import { Layout } from "antd";
import Icon from '@ant-design/icons';
import { CustomIconComponentProps } from "@ant-design/icons/lib/components/Icon";

const { Header } = Layout;

type IconHeaderProps = {
    iconComponent: React.ForwardRefExoticComponent<CustomIconComponentProps>;
    title: string;
}

export const IconHeader: React.FC<IconHeaderProps> = ({ iconComponent, title }) => {
    return (
        <>
            <Header style={{ height:'128px'}} className='layout-dark podcasts-header'>
                <Icon 
                    component={iconComponent} style={{ fontSize: '48px', marginRight: '16px' }}
                />
                {title.toUpperCase()}
            </Header>
        </>
    );
};