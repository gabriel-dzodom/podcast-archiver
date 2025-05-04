import React from 'react';
import { UploadOutlined, UserOutlined, VideoCameraOutlined } from '@ant-design/icons';
import { Layout, Menu, } from 'antd';
import { Home } from './components/home';

const { Header, Content, Footer, Sider } = Layout;

const items = [UserOutlined, VideoCameraOutlined, UploadOutlined, UserOutlined].map(
  (icon, index) => ({
    key: String(index + 1),
    icon: React.createElement(icon),
    label: `nav ${index + 1}`,
  }),
);

const App: React.FC = () => {
  return (
    <Layout style={{ minHeight: '100vh', minWidth: '60vw'}} className='layout-dark'>
      <Sider style={{borderRight:'1px solid rgba(240, 240, 240, 0.50)'}} width={224} className='layout-dark'>
        <Home />
        <Menu defaultSelectedKeys={['4']} items={items} style={{borderRight:'none', borderRadius: 'none'}} className='layout-dark' />
      </Sider>
      <Layout style={{ }} className='layout-dark'>
        <Header style={{ height:'128px'}} className='layout-dark' />
        <Content style={{ margin: '8px', }} className='layout-dark'>
          <div>
            content
          </div>
        </Content>
        <Footer style={{ height: '32px', textAlign: 'center',fontSize:'12px', padding:'8px 24px'}} className='layout-dark'>
          Pod Archiver © {new Date().getFullYear()} Created by Gabriel Dzodom
        </Footer>
      </Layout>
    </Layout>
  );
};

export default App;