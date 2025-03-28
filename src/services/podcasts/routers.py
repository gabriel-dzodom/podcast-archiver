# (c) 2025, Gabriel Dzodom
# All rights reserved.

from fastapi import APIRouter

from .controllers import (
    delete_podcast,
    delete_podcast_episode,
    delete_podcast_episodes,
    get_podcast,
    get_podcast_episode,
    get_podcast_episodes,
    get_podcasts,
    root,
    set_podcast,
    set_podcast_episode,
    update_podcast,
    update_podcast_episode
)

router = APIRouter()
router.prefix = "/api/v1"
router.add_api_route(
    "/",
    root,
    methods=["GET"],
)
router.add_api_route(
    "/podcasts",
    get_podcasts,
    methods=["GET"],
)
router.add_api_route(
    "/podcasts/{podcast_id}",
    get_podcast,
    methods=["GET"],
)
router.add_api_route(
    "/podcasts",
    set_podcast,
    methods=["POST"],
)
router.add_api_route(
    "/podcasts",
    update_podcast,
    methods=["PUT"],
)
router.add_api_route(
    "/podcasts/{podcast_id}",
    delete_podcast,
    methods=["DELETE"],
)
router.add_api_route(
    "/podcasts/{podcast_id}/episodes",
    delete_podcast_episodes, 
    methods=["DELETE"],
)
router.add_api_route(
    "/podcasts/{podcast_id}/episodes",
    get_podcast_episodes, 
    methods=["GET"],
)
router.add_api_route(
    "/podcasts/{podcast_id}/episodes/{episode_id}",
    get_podcast_episode, 
    methods=["GET"],
)
router.add_api_route(
    "/podcasts/{podcast_id}/episodes",
    set_podcast_episode, 
    methods=["POST"],
)
router.add_api_route(
    "/podcasts/{podcast_id}/episodes",
    update_podcast_episode, 
    methods=["PUT"],
)
router.add_api_route(
    "/podcasts/{podcast_id}/episodes/{episode_id}",
    delete_podcast_episode, 
    methods=["DELETE"],
)