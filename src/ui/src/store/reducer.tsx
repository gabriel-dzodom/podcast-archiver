import { PodcastAction, PodcastEpisode, PodcastState } from '../models/podcast';
import * as ActionTypes from './action-types';
import { Podcast } from '../models/podcast';
import PodcastApiClient from '../client/client';

const initialState: PodcastState = {
    podcasts: PodcastApiClient.getPodcasts(),
    selectedPodcast: null,
    selectedEpisode: null,
    loading: false,
    error: null,
};

export default function podcastReducer(state = initialState, action: PodcastAction): PodcastState {
    switch (action.type) {
        case ActionTypes.FETCH_PODCASTS:
            return {
                ...state,
                podcasts: PodcastApiClient.getPodcasts(),
            };
        case ActionTypes.SELECT_PODCAST: {
            const selectedPodcast = state.podcasts.find(p => p.id === (action.payload as string));
            return {
                ...state,
                selectedPodcast: selectedPodcast as Podcast,
            };
        }
        case ActionTypes.SELECT_EPISODE:
            return {
                ...state,
                selectedEpisode: action.payload as PodcastEpisode,
            };
        case ActionTypes.SET_LOADING:
            return {
                ...state,
                loading: action.payload as boolean,
            };
        case ActionTypes.SET_ERROR:
            return {
                ...state,
                error: action.payload as string,
            };
        default:
            return state;
    }
}