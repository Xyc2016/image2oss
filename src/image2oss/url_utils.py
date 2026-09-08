import os

OSS_INTERNAL = os.getenv("OSS_INTERNAL", "0") == "1"


def normalize_oss_url(image_url: str, internal: bool = OSS_INTERNAL) -> str:
    """Optionally switch a public Hangzhou OSS URL to its VPC endpoint."""
    if internal:
        return image_url.replace("oss-cn-hangzhou.aliyuncs", "oss-cn-hangzhou-internal.aliyuncs")
    return image_url
