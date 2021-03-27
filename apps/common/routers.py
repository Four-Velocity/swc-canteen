from fastapi import APIRouter
from .models import Badge

router = APIRouter()


@router.get("/badges/website/", response_model=Badge)
def website_badge():
    return {
        "schemaVersion": 1,
        "label": "",
        "message": "live",
        "color": "#7673C0",
        "labelColor": "#430098",
        "namedLogo": "heroku",
        "style": "for-the-badge",
        "cacheSeconds": 500
    }
