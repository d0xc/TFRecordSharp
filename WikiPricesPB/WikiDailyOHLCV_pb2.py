# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WikiDailyOHLCV.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WikiDailyOHLCV.proto',
  package='d1100.data',
  syntax='proto3',
  serialized_pb=_b('\n\x14WikiDailyOHLCV.proto\x12\nd1100.data\"\xf3\x01\n\x0eWikiDailyOHLCV\x12\x0e\n\x06ticker\x18\x01 \x01(\t\x12\n\n\x02ts\x18\x02 \x01(\x03\x12\x0c\n\x04open\x18\x03 \x01(\x01\x12\x0c\n\x04high\x18\x04 \x01(\x01\x12\x0b\n\x03low\x18\x05 \x01(\x01\x12\r\n\x05\x63lose\x18\x06 \x01(\x01\x12\x0e\n\x06volume\x18\x07 \x01(\x01\x12\x12\n\nexDividend\x18\x08 \x01(\x01\x12\x12\n\nsplitRatio\x18\t \x01(\x01\x12\x0f\n\x07\x61\x64jOpen\x18\n \x01(\x01\x12\x0f\n\x07\x61\x64jHigh\x18\x0b \x01(\x01\x12\x0e\n\x06\x61\x64jLow\x18\x0c \x01(\x01\x12\x10\n\x08\x61\x64jClose\x18\r \x01(\x01\x12\x11\n\tadjVolume\x18\x0e \x01(\x01\"\x86\x02\n\x11WikiDailyColOHLCV\x12\r\n\x05\x64\x61yts\x18\x01 \x01(\x06\x12\x0f\n\x07tickers\x18\x02 \x03(\t\x12\r\n\x05opens\x18\x03 \x03(\x01\x12\r\n\x05highs\x18\x04 \x03(\x01\x12\x0c\n\x04lows\x18\x05 \x03(\x01\x12\x0e\n\x06\x63loses\x18\x06 \x03(\x01\x12\x0f\n\x07volumes\x18\x07 \x03(\x01\x12\x13\n\x0b\x65xDividends\x18\x08 \x03(\x01\x12\x13\n\x0bsplitRatios\x18\t \x03(\x01\x12\x10\n\x08\x61\x64jOpens\x18\n \x03(\x01\x12\x10\n\x08\x61\x64jHighs\x18\x0b \x03(\x01\x12\x0f\n\x07\x61\x64jLows\x18\x0c \x03(\x01\x12\x11\n\tadjCloses\x18\r \x03(\x01\x12\x12\n\nadjVolumes\x18\x0e \x03(\x01\"\x8b\x02\n\x16WikiDailyColBytesOHLCV\x12\r\n\x05\x64\x61yts\x18\x01 \x01(\x06\x12\x0f\n\x07tickers\x18\x02 \x03(\t\x12\r\n\x05opens\x18\x03 \x01(\x0c\x12\r\n\x05highs\x18\x04 \x01(\x0c\x12\x0c\n\x04lows\x18\x05 \x01(\x0c\x12\x0e\n\x06\x63loses\x18\x06 \x01(\x0c\x12\x0f\n\x07volumes\x18\x07 \x01(\x0c\x12\x13\n\x0b\x65xDividends\x18\x08 \x01(\x0c\x12\x13\n\x0bsplitRatios\x18\t \x01(\x0c\x12\x10\n\x08\x61\x64jOpens\x18\n \x01(\x0c\x12\x10\n\x08\x61\x64jHighs\x18\x0b \x01(\x0c\x12\x0f\n\x07\x61\x64jLows\x18\x0c \x01(\x0c\x12\x11\n\tadjCloses\x18\r \x01(\x0c\x12\x12\n\nadjVolumes\x18\x0e \x01(\x0c\x62\x06proto3')
)




_WIKIDAILYOHLCV = _descriptor.Descriptor(
  name='WikiDailyOHLCV',
  full_name='d1100.data.WikiDailyOHLCV',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ticker', full_name='d1100.data.WikiDailyOHLCV.ticker', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts', full_name='d1100.data.WikiDailyOHLCV.ts', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='open', full_name='d1100.data.WikiDailyOHLCV.open', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high', full_name='d1100.data.WikiDailyOHLCV.high', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='low', full_name='d1100.data.WikiDailyOHLCV.low', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close', full_name='d1100.data.WikiDailyOHLCV.close', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume', full_name='d1100.data.WikiDailyOHLCV.volume', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exDividend', full_name='d1100.data.WikiDailyOHLCV.exDividend', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='splitRatio', full_name='d1100.data.WikiDailyOHLCV.splitRatio', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adjOpen', full_name='d1100.data.WikiDailyOHLCV.adjOpen', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adjHigh', full_name='d1100.data.WikiDailyOHLCV.adjHigh', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adjLow', full_name='d1100.data.WikiDailyOHLCV.adjLow', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adjClose', full_name='d1100.data.WikiDailyOHLCV.adjClose', index=12,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adjVolume', full_name='d1100.data.WikiDailyOHLCV.adjVolume', index=13,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=280,
)


_WIKIDAILYCOLOHLCV = _descriptor.Descriptor(
  name='WikiDailyColOHLCV',
  full_name='d1100.data.WikiDailyColOHLCV',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dayts', full_name='d1100.data.WikiDailyColOHLCV.dayts', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tickers', full_name='d1100.data.WikiDailyColOHLCV.tickers', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opens', full_name='d1100.data.WikiDailyColOHLCV.opens', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='highs', full_name='d1100.data.WikiDailyColOHLCV.highs', index=3,
      number=4, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lows', full_name='d1100.data.WikiDailyColOHLCV.lows', index=4,
      number=5, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='closes', full_name='d1100.data.WikiDailyColOHLCV.closes', index=5,
      number=6, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volumes', full_name='d1100.data.WikiDailyColOHLCV.volumes', index=6,
      number=7, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exDividends', full_name='d1100.data.WikiDailyColOHLCV.exDividends', index=7,
      number=8, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='splitRatios', full_name='d1100.data.WikiDailyColOHLCV.splitRatios', index=8,
      number=9, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adjOpens', full_name='d1100.data.WikiDailyColOHLCV.adjOpens', index=9,
      number=10, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adjHighs', full_name='d1100.data.WikiDailyColOHLCV.adjHighs', index=10,
      number=11, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adjLows', full_name='d1100.data.WikiDailyColOHLCV.adjLows', index=11,
      number=12, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adjCloses', full_name='d1100.data.WikiDailyColOHLCV.adjCloses', index=12,
      number=13, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adjVolumes', full_name='d1100.data.WikiDailyColOHLCV.adjVolumes', index=13,
      number=14, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=283,
  serialized_end=545,
)


_WIKIDAILYCOLBYTESOHLCV = _descriptor.Descriptor(
  name='WikiDailyColBytesOHLCV',
  full_name='d1100.data.WikiDailyColBytesOHLCV',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dayts', full_name='d1100.data.WikiDailyColBytesOHLCV.dayts', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tickers', full_name='d1100.data.WikiDailyColBytesOHLCV.tickers', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opens', full_name='d1100.data.WikiDailyColBytesOHLCV.opens', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='highs', full_name='d1100.data.WikiDailyColBytesOHLCV.highs', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lows', full_name='d1100.data.WikiDailyColBytesOHLCV.lows', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='closes', full_name='d1100.data.WikiDailyColBytesOHLCV.closes', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volumes', full_name='d1100.data.WikiDailyColBytesOHLCV.volumes', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exDividends', full_name='d1100.data.WikiDailyColBytesOHLCV.exDividends', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='splitRatios', full_name='d1100.data.WikiDailyColBytesOHLCV.splitRatios', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adjOpens', full_name='d1100.data.WikiDailyColBytesOHLCV.adjOpens', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adjHighs', full_name='d1100.data.WikiDailyColBytesOHLCV.adjHighs', index=10,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adjLows', full_name='d1100.data.WikiDailyColBytesOHLCV.adjLows', index=11,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adjCloses', full_name='d1100.data.WikiDailyColBytesOHLCV.adjCloses', index=12,
      number=13, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adjVolumes', full_name='d1100.data.WikiDailyColBytesOHLCV.adjVolumes', index=13,
      number=14, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=548,
  serialized_end=815,
)

DESCRIPTOR.message_types_by_name['WikiDailyOHLCV'] = _WIKIDAILYOHLCV
DESCRIPTOR.message_types_by_name['WikiDailyColOHLCV'] = _WIKIDAILYCOLOHLCV
DESCRIPTOR.message_types_by_name['WikiDailyColBytesOHLCV'] = _WIKIDAILYCOLBYTESOHLCV
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WikiDailyOHLCV = _reflection.GeneratedProtocolMessageType('WikiDailyOHLCV', (_message.Message,), dict(
  DESCRIPTOR = _WIKIDAILYOHLCV,
  __module__ = 'WikiDailyOHLCV_pb2'
  # @@protoc_insertion_point(class_scope:d1100.data.WikiDailyOHLCV)
  ))
_sym_db.RegisterMessage(WikiDailyOHLCV)

WikiDailyColOHLCV = _reflection.GeneratedProtocolMessageType('WikiDailyColOHLCV', (_message.Message,), dict(
  DESCRIPTOR = _WIKIDAILYCOLOHLCV,
  __module__ = 'WikiDailyOHLCV_pb2'
  # @@protoc_insertion_point(class_scope:d1100.data.WikiDailyColOHLCV)
  ))
_sym_db.RegisterMessage(WikiDailyColOHLCV)

WikiDailyColBytesOHLCV = _reflection.GeneratedProtocolMessageType('WikiDailyColBytesOHLCV', (_message.Message,), dict(
  DESCRIPTOR = _WIKIDAILYCOLBYTESOHLCV,
  __module__ = 'WikiDailyOHLCV_pb2'
  # @@protoc_insertion_point(class_scope:d1100.data.WikiDailyColBytesOHLCV)
  ))
_sym_db.RegisterMessage(WikiDailyColBytesOHLCV)


# @@protoc_insertion_point(module_scope)
