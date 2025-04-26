import React from 'react';
import { UploadOutlined, UserOutlined, VideoCameraOutlined } from '@ant-design/icons';
import { Layout, Menu, } from 'antd';

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
    <Layout style={{ minHeight: '100vh', minWidth: '60vw', borderRight: '1px solid #f0f0f0', borderLeft: '1px solid #f0f0f0'}} className='layout-dark'>
      <Sider style={{borderRight:'1px solid #f0f0f0'}} className='layout-dark'>
        <h2 className='demo-logo-vertical'>Pod</h2>
        <h4 className='demo-logo-vertical'>Archiver</h4>
        <Menu defaultSelectedKeys={['4']} items={items} style={{borderRight:'none'}} className='layout-dark' />
      </Sider>
      <Layout style={{ }} className='layout-dark'>
        <Header style={{ height:'128px'}} className='layout-dark' />
        <Content style={{ margin: '8px', }} className='layout-dark'>
          <div>
            content
          </div>
        </Content>
        <Footer style={{ height: '32px', textAlign: 'center', borderTop:'1px solid #f0f0f0', fontSize:'12px', padding:'8px 24px'}} className='layout-dark'>
          Pod Archiver © {new Date().getFullYear()} Created by Gabriel Dzodom
        </Footer>
      </Layout>
    </Layout>
  );
};

export default App;