from fastapi import FastAPI

app = FastAPI()


@app.get("api/badge")
def badge():
    return {
        "schemaVersion": 1,
        "label": "",
        "message": "live",
        "color": "#7673C0",
        "labelColor": "#430098",
        "namedLogo": "heroku",
        "style": "flat-square",
        "cacheSeconds": 500
    }
