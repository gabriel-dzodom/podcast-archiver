import { createRoot } from 'react-dom/client'
import './styles/index.css'
import './styles/App.css'
import App from './App.tsx'
import { Provider } from 'react-redux'
import { PodcastAction, PodcastDispatch, PodcastState } from './models/podcast.tsx'
import { Store } from 'redux'
import podcastReducer from './store/reducer.tsx'
import { configureStore } from '@reduxjs/toolkit'

const store: Store<PodcastState, PodcastAction> & { dispatch: PodcastDispatch
} = configureStore({
  reducer: podcastReducer,
})

createRoot(document.getElementById('root')!).render(
  <Provider store={store}>
    <App />
  </Provider>
)
