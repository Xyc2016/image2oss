import os

INTERNAL_DEFAULT = os.getenv("INTERNAL_DEFAULT", "0") == "1"


def normalize_oss_url(image_url: str, internal: bool = INTERNAL_DEFAULT) -> str:
    """Optionally switch a public Hangzhou OSS URL to its VPC endpoint."""
    if internal:
        return image_url.replace("cn-hangzhou.", "cn-hangzhou-internal.")
    return image_url
