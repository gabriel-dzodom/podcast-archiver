# (c) 2025, Gabriel Dzodom
# All rights reserved.

from fastapi import APIRouter

from .controllers import (
    delete_podcast,
    get_podcast,
    get_podcasts,
    root,
    set_podcast,
    update_podcast
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