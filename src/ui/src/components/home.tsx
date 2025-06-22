import { Link } from "react-router-dom";

const style = {
    display: 'flex',
    color: 'white',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '8px',
}
      
export const Home = () => {
    return (
        <Link to="/" style={{ textDecoration: 'none' }}>
            <div style={style}>
                <img src='/pa.svg' width={32} height={32} alt='logo' />
                <h2>POD ARCHIVER</h2>
            </div>
        </Link>
    );
}