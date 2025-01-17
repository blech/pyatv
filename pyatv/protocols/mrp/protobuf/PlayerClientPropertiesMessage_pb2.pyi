"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.extension_dict
import google.protobuf.message
import pyatv.protocols.mrp.protobuf.PlayerPath_pb2
import pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class PlayerClientPropertiesMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PLAYERPATH_FIELD_NUMBER: builtins.int
    LASTPLAYINGTIMESTAMP_FIELD_NUMBER: builtins.int
    lastPlayingTimestamp: builtins.float
    @property
    def playerPath(self) -> pyatv.protocols.mrp.protobuf.PlayerPath_pb2.PlayerPath: ...
    def __init__(
        self,
        *,
        playerPath: pyatv.protocols.mrp.protobuf.PlayerPath_pb2.PlayerPath | None = ...,
        lastPlayingTimestamp: builtins.float | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["lastPlayingTimestamp", b"lastPlayingTimestamp", "playerPath", b"playerPath"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["lastPlayingTimestamp", b"lastPlayingTimestamp", "playerPath", b"playerPath"]) -> None: ...

global___PlayerClientPropertiesMessage = PlayerClientPropertiesMessage

PLAYERCLIENTPROPERTIESMESSAGE_FIELD_NUMBER: builtins.int
playerClientPropertiesMessage: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2.ProtocolMessage, global___PlayerClientPropertiesMessage]
