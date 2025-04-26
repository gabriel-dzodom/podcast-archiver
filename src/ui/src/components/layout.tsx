import { Layout } from "antd";

type LayoutProps = {
    children: React.ReactNode;
    style?: React.CSSProperties;
}

export const PALayout = (props: LayoutProps) => {
    return (
        <Layout className="layout-dark" style={props.style}>
            {props.children}
        </Layout>
    );
}

export const PAHeader = (props: LayoutProps) => {
    return (
        <Layout.Header className="layout-dark" style={props.style}>
            {props.children}
        </Layout.Header>
    );
}

export const PAContent = (props: LayoutProps) => {
    return (
        <Layout.Content className="layout-dark" style={props.style}>
            {props.children}
        </Layout.Content>
    );
}
export const PAFooter = (props: LayoutProps) => {
    return (
        <Layout.Footer className="layout-dark" style={props.style}>
            {props.children}
        </Layout.Footer>
    );
}