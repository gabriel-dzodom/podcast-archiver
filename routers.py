

from fastapi import APIRouter

from controllers import root


router = APIRouter()
router.prefix = "/api/v1"
router.add_api_route(
    "/",
    root,
    methods=["GET"],
)