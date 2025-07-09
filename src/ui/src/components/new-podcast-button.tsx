import { Button } from "antd";
import { PlusSquareOutlined } from '@ant-design/icons';
import { Link } from "react-router-dom";
import { useDispatch } from "react-redux";
import { Dispatch } from "redux";
import { selectPodcast } from "../store/actions";

export const NewPodcastButton : React.FC = () => {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const dispatch: Dispatch<any> = useDispatch();
    const onNewPodcastClicked = () => {
        dispatch(selectPodcast(""));
    };

    return (
    <Link to="/podcast/new" style={{ textDecoration: 'none' }} onClick={onNewPodcastClicked}>
        <div className='add-podcast-button-container'> 
          <Button title='Import a new podcast' className="add-podcast-button" size='large' icon={<PlusSquareOutlined />}>
            NEW PODCAST
          </Button>
        </div>
      </Link>
    );
}