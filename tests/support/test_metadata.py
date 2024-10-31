"""Unit tests for pyatv.support.metadata."""

import math
from pathlib import Path

import pytest

from pyatv.interface import MediaMetadata
from pyatv.support.metadata import get_metadata, merge_into

from tests.utils import data_path


@pytest.mark.parametrize(
    "audio_file",
    [(data_path("only_metadata.wav")), (Path(data_path("only_metadata.wav")))],
)
@pytest.mark.asyncio
async def test_get_metadata_from_file(audio_file):
    metadata = await get_metadata(audio_file)
    assert metadata.artist == "postlund"
    assert metadata.album == "raop"
    assert metadata.title == "pyatv"
    assert metadata.artwork is None
    assert math.isclose(metadata.duration, 0.0)


METADATA_FIELDS = list(MediaMetadata.__dataclass_fields__.keys())


def test_returns_base_instance():
    base = MediaMetadata()
    new_metadata = MediaMetadata()
    merged = merge_into(base, new_metadata)
    assert merged is base


def test_to_empty_metadata():
    # This basically sets the title field to "title", artist to "artist" and so on
    # for all fields and assert that it is correct
    metadata = merge_into(MediaMetadata(), MediaMetadata(*METADATA_FIELDS))
    for field in METADATA_FIELDS:
        assert getattr(metadata, field) == field


def test_no_override_set_value():
    metadata = merge_into(
        MediaMetadata(title="title"), MediaMetadata(title="new title")
    )
    assert metadata.title == "title"
