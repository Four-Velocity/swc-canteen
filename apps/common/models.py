from pydantic import BaseModel, Field


class Badge(BaseModel):
    schema_version: int = Field(alias="schemaVersion")
    label: str
    message: str
    color: str
    label_color: str = Field(alias="labelColor")
    named_logo: str = Field(alias="namedLogo")
    style: str
    cache_seconds: int = Field(alias="cacheSeconds")
