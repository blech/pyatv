"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.extension_dict
import google.protobuf.message
import pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class CryptoPairingMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAIRINGDATA_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    ISRETRYING_FIELD_NUMBER: builtins.int
    ISUSINGSYSTEMPAIRING_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    pairingData: builtins.bytes
    """Example: <00010006 0101>"""
    status: builtins.int
    """Example: 0"""
    isRetrying: builtins.bool
    isUsingSystemPairing: builtins.bool
    state: builtins.int
    def __init__(
        self,
        *,
        pairingData: builtins.bytes | None = ...,
        status: builtins.int | None = ...,
        isRetrying: builtins.bool | None = ...,
        isUsingSystemPairing: builtins.bool | None = ...,
        state: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["isRetrying", b"isRetrying", "isUsingSystemPairing", b"isUsingSystemPairing", "pairingData", b"pairingData", "state", b"state", "status", b"status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["isRetrying", b"isRetrying", "isUsingSystemPairing", b"isUsingSystemPairing", "pairingData", b"pairingData", "state", b"state", "status", b"status"]) -> None: ...

global___CryptoPairingMessage = CryptoPairingMessage

CRYPTOPAIRINGMESSAGE_FIELD_NUMBER: builtins.int
cryptoPairingMessage: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2.ProtocolMessage, global___CryptoPairingMessage]
