import { PodcastAction, PodcastDispatch } from "../models/podcast";
import * as ActionTypes from "./action-types";

export function fetchPodcasts() {
    const action: PodcastAction = {
        type: ActionTypes.FETCH_PODCASTS,
        payload: [],
    };
    return (dispatch: PodcastDispatch) => {
        dispatch(action);
    };
}