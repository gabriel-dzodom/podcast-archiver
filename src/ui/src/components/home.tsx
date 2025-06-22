import { useDispatch } from "react-redux";
import { Link } from "react-router-dom";
import { Dispatch } from "redux";
import { selectPodcast } from "../store/actions";

const style = {
    display: 'flex',
    color: 'white',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '8px',
}
      
export const Home = () => {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const dispatch : Dispatch<any> = useDispatch();
    const onHomeNavigated = () => {
        dispatch(selectPodcast(""));
    };

    return (
        <Link to="/" style={{ textDecoration: 'none' }} onClick={onHomeNavigated}>
            <div style={style}>
                <img src='/pa.svg' width={32} height={32} alt='logo' />
                <h2>POD ARCHIVER</h2>
            </div>
        </Link>
    );
}