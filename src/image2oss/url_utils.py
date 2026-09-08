import os

OSS_INTERNAL = os.getenv("OSS_INTERNAL", "0") == "1"


def normalize_oss_url(image_url: str) -> str:
    """Optionally switch a public Hangzhou OSS URL to its VPC endpoint."""
    if OSS_INTERNAL:
        normalized_url = image_url.replace("oss-cn-hangzhou.aliyuncs", "oss-cn-hangzhou-internal.aliyuncs")
        if normalized_url != image_url:
            print(f"[image2oss] OSS_INTERNAL enabled, using internal URL: {normalized_url}")
        return normalized_url
    return image_url
