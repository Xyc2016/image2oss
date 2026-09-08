#!/usr/bin/env python

"""Tests for `image2oss` URL handling."""

from src.image2oss.url_utils import normalize_oss_url


def test_normalize_public_hangzhou_oss_url_to_internal():
    url = "https://zhiyi-image.oss-cn-hangzhou.aliyuncs.com/devops/comfyui/input/a.png"

    assert normalize_oss_url(url, internal=True) == (
        "https://zhiyi-image.oss-cn-hangzhou-internal.aliyuncs.com/devops/comfyui/input/a.png"
    )


def test_keep_public_oss_url_when_internal_disabled():
    url = "https://zhiyi-image.oss-cn-hangzhou.aliyuncs.com/devops/comfyui/input/a.png"

    assert normalize_oss_url(url, internal=False) == url


def test_keep_non_hangzhou_url_unchanged():
    url = "https://example.com/images/a.png"

    assert normalize_oss_url(url, internal=True) == url
