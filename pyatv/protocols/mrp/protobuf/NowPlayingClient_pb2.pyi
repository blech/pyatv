"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class NowPlayingClient(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROCESSIDENTIFIER_FIELD_NUMBER: builtins.int
    BUNDLEIDENTIFIER_FIELD_NUMBER: builtins.int
    PARENTAPPLICATIONBUNDLEIDENTIFIER_FIELD_NUMBER: builtins.int
    PROCESSUSERIDENTIFIER_FIELD_NUMBER: builtins.int
    NOWPLAYINGVISIBILITY_FIELD_NUMBER: builtins.int
    DISPLAYNAME_FIELD_NUMBER: builtins.int
    BUNDLEIDENTIFIERHIERARCHYS_FIELD_NUMBER: builtins.int
    processIdentifier: builtins.int
    bundleIdentifier: builtins.str
    parentApplicationBundleIdentifier: builtins.str
    processUserIdentifier: builtins.int
    nowPlayingVisibility: builtins.int
    displayName: builtins.str
    """   optional TintColor tintColor = 6;"""
    @property
    def bundleIdentifierHierarchys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        processIdentifier: builtins.int | None = ...,
        bundleIdentifier: builtins.str | None = ...,
        parentApplicationBundleIdentifier: builtins.str | None = ...,
        processUserIdentifier: builtins.int | None = ...,
        nowPlayingVisibility: builtins.int | None = ...,
        displayName: builtins.str | None = ...,
        bundleIdentifierHierarchys: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bundleIdentifier", b"bundleIdentifier", "displayName", b"displayName", "nowPlayingVisibility", b"nowPlayingVisibility", "parentApplicationBundleIdentifier", b"parentApplicationBundleIdentifier", "processIdentifier", b"processIdentifier", "processUserIdentifier", b"processUserIdentifier"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bundleIdentifier", b"bundleIdentifier", "bundleIdentifierHierarchys", b"bundleIdentifierHierarchys", "displayName", b"displayName", "nowPlayingVisibility", b"nowPlayingVisibility", "parentApplicationBundleIdentifier", b"parentApplicationBundleIdentifier", "processIdentifier", b"processIdentifier", "processUserIdentifier", b"processUserIdentifier"]) -> None: ...

global___NowPlayingClient = NowPlayingClient
