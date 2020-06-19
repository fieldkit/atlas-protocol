# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fk-atlas.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fk-atlas.proto',
  package='fk_atlas',
  syntax='proto3',
  serialized_options=b'\n org.conservify.fieldkit.atlas.pb',
  serialized_pb=b'\n\x0e\x66k-atlas.proto\x12\x08\x66k_atlas\"\xbb\x02\n\x17\x41tlasCalibrationCommand\x12\x31\n\toperation\x18\x01 \x01(\x0e\x32\x1e.fk_atlas.CalibrationOperation\x12(\n\x04temp\x18\x02 \x01(\x0e\x32\x1a.fk_atlas.TempCalibrations\x12\x31\n\x0f\x64issolvedOxygen\x18\x03 \x01(\x0e\x32\x18.fk_atlas.DoCalibrations\x12$\n\x02ph\x18\x04 \x01(\x0e\x32\x18.fk_atlas.PhCalibrations\x12$\n\x02\x65\x63\x18\x05 \x01(\x0e\x32\x18.fk_atlas.EcCalibrations\x12&\n\x03orp\x18\x06 \x01(\x0e\x32\x19.fk_atlas.OrpCalibrations\x12\r\n\x05which\x18\x08 \x01(\r\x12\r\n\x05value\x18\x07 \x01(\x02\"9\n\x0cTwoWireQuery\x12\x0c\n\x04read\x18\x01 \x01(\r\x12\r\n\x05write\x18\x02 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"$\n\rCompensations\x12\x13\n\x0btemperature\x18\x01 \x01(\x02\"\xc1\x01\n\x0eWireAtlasQuery\x12!\n\x04type\x18\x01 \x01(\x0e\x32\x13.fk_atlas.QueryType\x12\x36\n\x0b\x63\x61libration\x18\x02 \x01(\x0b\x32!.fk_atlas.AtlasCalibrationCommand\x12.\n\rcompensations\x18\x03 \x01(\x0b\x32\x17.fk_atlas.Compensations\x12$\n\x04wire\x18\x04 \x01(\x0b\x32\x16.fk_atlas.TwoWireQuery\"\xa8\x02\n\x16\x41tlasCalibrationStatus\x12\"\n\x04type\x18\x01 \x01(\x0e\x32\x14.fk_atlas.SensorType\x12\x0c\n\x04time\x18\x02 \x01(\r\x12\x0b\n\x03raw\x18\x08 \x01(\r\x12(\n\x04temp\x18\x03 \x01(\x0e\x32\x1a.fk_atlas.TempCalibrations\x12\x31\n\x0f\x64issolvedOxygen\x18\x04 \x01(\x0e\x32\x18.fk_atlas.DoCalibrations\x12$\n\x02ph\x18\x05 \x01(\x0e\x32\x18.fk_atlas.PhCalibrations\x12$\n\x02\x65\x63\x18\x06 \x01(\x0e\x32\x18.fk_atlas.EcCalibrations\x12&\n\x03orp\x18\x07 \x01(\x0e\x32\x19.fk_atlas.OrpCalibrations\"\x1c\n\x0cTwoWireReply\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\";\n\x05\x45rror\x12!\n\x04type\x18\x01 \x01(\x0e\x32\x13.fk_atlas.ErrorType\x12\x0f\n\x07message\x18\x02 \x01(\t\"\xb1\x01\n\x0eWireAtlasReply\x12!\n\x04type\x18\x01 \x01(\x0e\x32\x13.fk_atlas.ReplyType\x12\x1f\n\x06\x65rrors\x18\x02 \x03(\x0b\x32\x0f.fk_atlas.Error\x12\x35\n\x0b\x63\x61libration\x18\x03 \x01(\x0b\x32 .fk_atlas.AtlasCalibrationStatus\x12$\n\x04wire\x18\x04 \x01(\x0b\x32\x16.fk_atlas.TwoWireReply*k\n\nSensorType\x12\x0f\n\x0bSENSOR_NONE\x10\x00\x12\r\n\tSENSOR_PH\x10\x01\x12\x0f\n\x0bSENSOR_TEMP\x10\x02\x12\x0e\n\nSENSOR_ORP\x10\x03\x12\r\n\tSENSOR_DO\x10\x04\x12\r\n\tSENSOR_EC\x10\x05*\x1b\n\tQueryType\x12\x0e\n\nQUERY_NONE\x10\x00*p\n\x14\x43\x61librationOperation\x12\x14\n\x10\x43\x41LIBRATION_NONE\x10\x00\x12\x16\n\x12\x43\x41LIBRATION_STATUS\x10\x01\x12\x15\n\x11\x43\x41LIBRATION_CLEAR\x10\x02\x12\x13\n\x0f\x43\x41LIBRATION_SET\x10\x03*2\n\x10TempCalibrations\x12\r\n\tTEMP_NONE\x10\x00\x12\x0f\n\x0bTEMP_SINGLE\x10\x01*d\n\x14TempCalibrateCommand\x12\x17\n\x13\x43\x41LIBRATE_TEMP_NONE\x10\x00\x12\x18\n\x14\x43\x41LIBRATE_TEMP_CLEAR\x10\x01\x12\x19\n\x15\x43\x41LIBRATE_TEMP_SINGLE\x10\x02*=\n\x0e\x44oCalibrations\x12\x0b\n\x07\x44O_NONE\x10\x00\x12\x11\n\rDO_ATMOSPHERE\x10\x01\x12\x0b\n\x07\x44O_ZERO\x10\x02*w\n\x12\x44oCalibrateCommand\x12\x15\n\x11\x43\x41LIBRATE_DO_NONE\x10\x00\x12\x16\n\x12\x43\x41LIBRATE_DO_CLEAR\x10\x01\x12\x1b\n\x17\x43\x41LIBRATE_DO_ATMOSPHERE\x10\x02\x12\x15\n\x11\x43\x41LIBRATE_DO_ZERO\x10\x03*E\n\x0ePhCalibrations\x12\x0b\n\x07PH_NONE\x10\x00\x12\n\n\x06PH_LOW\x10\x01\x12\r\n\tPH_MIDDLE\x10\x02\x12\x0b\n\x07PH_HIGH\x10\x04*\x89\x01\n\x12PhCalibrateCommand\x12\x15\n\x11\x43\x41LIBRATE_PH_NONE\x10\x00\x12\x16\n\x12\x43\x41LIBRATE_PH_CLEAR\x10\x01\x12\x14\n\x10\x43\x41LIBRATE_PH_LOW\x10\x02\x12\x17\n\x13\x43\x41LIBRATE_PH_MIDDLE\x10\x03\x12\x15\n\x11\x43\x41LIBRATE_PH_HIGH\x10\x04*[\n\x0e\x45\x63\x43\x61librations\x12\x0b\n\x07\x45\x43_NONE\x10\x00\x12\n\n\x06\x45\x43_DRY\x10\x01\x12\r\n\tEC_SINGLE\x10\x02\x12\x0f\n\x0b\x45\x43_DUAL_LOW\x10\x04\x12\x10\n\x0c\x45\x43_DUAL_HIGH\x10\x08*\xa9\x01\n\x12\x45\x63\x43\x61librateCommand\x12\x15\n\x11\x43\x41LIBRATE_EC_NONE\x10\x00\x12\x16\n\x12\x43\x41LIBRATE_EC_CLEAR\x10\x01\x12\x14\n\x10\x43\x41LIBRATE_EC_DRY\x10\x02\x12\x17\n\x13\x43\x41LIBRATE_EC_SINGLE\x10\x03\x12\x19\n\x15\x43\x41LIBRATE_EC_DUAL_LOW\x10\x04\x12\x1a\n\x16\x43\x41LIBRATE_EC_DUAL_HIGH\x10\x05*/\n\x0fOrpCalibrations\x12\x0c\n\x08ORP_NONE\x10\x00\x12\x0e\n\nORP_SINGLE\x10\x01*G\n\x13OrpCalibrateCommand\x12\x16\n\x12\x43\x41LIBRATE_ORP_NONE\x10\x00\x12\x18\n\x14\x43\x41LIBRATE_ORP_SINGLE\x10\x01*b\n\tReplyType\x12\x0e\n\nREPLY_NONE\x10\x00\x12\x0f\n\x0bREPLY_RETRY\x10\x01\x12\x0f\n\x0bREPLY_ERROR\x10\x02\x12\x10\n\x0cREPLY_STATUS\x10\x03\x12\x11\n\rREPLY_COMMAND\x10\x04*2\n\tErrorType\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07GENERAL\x10\x01\x12\x0e\n\nUNEXPECTED\x10\x02\x42\"\n org.conservify.fieldkit.atlas.pbb\x06proto3'
)

_SENSORTYPE = _descriptor.EnumDescriptor(
  name='SensorType',
  full_name='fk_atlas.SensorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SENSOR_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_PH', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_TEMP', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_ORP', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_DO', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_EC', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1209,
  serialized_end=1316,
)
_sym_db.RegisterEnumDescriptor(_SENSORTYPE)

SensorType = enum_type_wrapper.EnumTypeWrapper(_SENSORTYPE)
_QUERYTYPE = _descriptor.EnumDescriptor(
  name='QueryType',
  full_name='fk_atlas.QueryType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='QUERY_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1318,
  serialized_end=1345,
)
_sym_db.RegisterEnumDescriptor(_QUERYTYPE)

QueryType = enum_type_wrapper.EnumTypeWrapper(_QUERYTYPE)
_CALIBRATIONOPERATION = _descriptor.EnumDescriptor(
  name='CalibrationOperation',
  full_name='fk_atlas.CalibrationOperation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CALIBRATION_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATION_STATUS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATION_CLEAR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATION_SET', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1347,
  serialized_end=1459,
)
_sym_db.RegisterEnumDescriptor(_CALIBRATIONOPERATION)

CalibrationOperation = enum_type_wrapper.EnumTypeWrapper(_CALIBRATIONOPERATION)
_TEMPCALIBRATIONS = _descriptor.EnumDescriptor(
  name='TempCalibrations',
  full_name='fk_atlas.TempCalibrations',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TEMP_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEMP_SINGLE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1461,
  serialized_end=1511,
)
_sym_db.RegisterEnumDescriptor(_TEMPCALIBRATIONS)

TempCalibrations = enum_type_wrapper.EnumTypeWrapper(_TEMPCALIBRATIONS)
_TEMPCALIBRATECOMMAND = _descriptor.EnumDescriptor(
  name='TempCalibrateCommand',
  full_name='fk_atlas.TempCalibrateCommand',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CALIBRATE_TEMP_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATE_TEMP_CLEAR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATE_TEMP_SINGLE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1513,
  serialized_end=1613,
)
_sym_db.RegisterEnumDescriptor(_TEMPCALIBRATECOMMAND)

TempCalibrateCommand = enum_type_wrapper.EnumTypeWrapper(_TEMPCALIBRATECOMMAND)
_DOCALIBRATIONS = _descriptor.EnumDescriptor(
  name='DoCalibrations',
  full_name='fk_atlas.DoCalibrations',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DO_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DO_ATMOSPHERE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DO_ZERO', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1615,
  serialized_end=1676,
)
_sym_db.RegisterEnumDescriptor(_DOCALIBRATIONS)

DoCalibrations = enum_type_wrapper.EnumTypeWrapper(_DOCALIBRATIONS)
_DOCALIBRATECOMMAND = _descriptor.EnumDescriptor(
  name='DoCalibrateCommand',
  full_name='fk_atlas.DoCalibrateCommand',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CALIBRATE_DO_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATE_DO_CLEAR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATE_DO_ATMOSPHERE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATE_DO_ZERO', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1678,
  serialized_end=1797,
)
_sym_db.RegisterEnumDescriptor(_DOCALIBRATECOMMAND)

DoCalibrateCommand = enum_type_wrapper.EnumTypeWrapper(_DOCALIBRATECOMMAND)
_PHCALIBRATIONS = _descriptor.EnumDescriptor(
  name='PhCalibrations',
  full_name='fk_atlas.PhCalibrations',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PH_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PH_LOW', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PH_MIDDLE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PH_HIGH', index=3, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1799,
  serialized_end=1868,
)
_sym_db.RegisterEnumDescriptor(_PHCALIBRATIONS)

PhCalibrations = enum_type_wrapper.EnumTypeWrapper(_PHCALIBRATIONS)
_PHCALIBRATECOMMAND = _descriptor.EnumDescriptor(
  name='PhCalibrateCommand',
  full_name='fk_atlas.PhCalibrateCommand',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CALIBRATE_PH_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATE_PH_CLEAR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATE_PH_LOW', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATE_PH_MIDDLE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATE_PH_HIGH', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1871,
  serialized_end=2008,
)
_sym_db.RegisterEnumDescriptor(_PHCALIBRATECOMMAND)

PhCalibrateCommand = enum_type_wrapper.EnumTypeWrapper(_PHCALIBRATECOMMAND)
_ECCALIBRATIONS = _descriptor.EnumDescriptor(
  name='EcCalibrations',
  full_name='fk_atlas.EcCalibrations',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EC_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EC_DRY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EC_SINGLE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EC_DUAL_LOW', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EC_DUAL_HIGH', index=4, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2010,
  serialized_end=2101,
)
_sym_db.RegisterEnumDescriptor(_ECCALIBRATIONS)

EcCalibrations = enum_type_wrapper.EnumTypeWrapper(_ECCALIBRATIONS)
_ECCALIBRATECOMMAND = _descriptor.EnumDescriptor(
  name='EcCalibrateCommand',
  full_name='fk_atlas.EcCalibrateCommand',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CALIBRATE_EC_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATE_EC_CLEAR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATE_EC_DRY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATE_EC_SINGLE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATE_EC_DUAL_LOW', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATE_EC_DUAL_HIGH', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2104,
  serialized_end=2273,
)
_sym_db.RegisterEnumDescriptor(_ECCALIBRATECOMMAND)

EcCalibrateCommand = enum_type_wrapper.EnumTypeWrapper(_ECCALIBRATECOMMAND)
_ORPCALIBRATIONS = _descriptor.EnumDescriptor(
  name='OrpCalibrations',
  full_name='fk_atlas.OrpCalibrations',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ORP_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORP_SINGLE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2275,
  serialized_end=2322,
)
_sym_db.RegisterEnumDescriptor(_ORPCALIBRATIONS)

OrpCalibrations = enum_type_wrapper.EnumTypeWrapper(_ORPCALIBRATIONS)
_ORPCALIBRATECOMMAND = _descriptor.EnumDescriptor(
  name='OrpCalibrateCommand',
  full_name='fk_atlas.OrpCalibrateCommand',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CALIBRATE_ORP_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATE_ORP_SINGLE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2324,
  serialized_end=2395,
)
_sym_db.RegisterEnumDescriptor(_ORPCALIBRATECOMMAND)

OrpCalibrateCommand = enum_type_wrapper.EnumTypeWrapper(_ORPCALIBRATECOMMAND)
_REPLYTYPE = _descriptor.EnumDescriptor(
  name='ReplyType',
  full_name='fk_atlas.ReplyType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REPLY_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REPLY_RETRY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REPLY_ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REPLY_STATUS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REPLY_COMMAND', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2397,
  serialized_end=2495,
)
_sym_db.RegisterEnumDescriptor(_REPLYTYPE)

ReplyType = enum_type_wrapper.EnumTypeWrapper(_REPLYTYPE)
_ERRORTYPE = _descriptor.EnumDescriptor(
  name='ErrorType',
  full_name='fk_atlas.ErrorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GENERAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNEXPECTED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2497,
  serialized_end=2547,
)
_sym_db.RegisterEnumDescriptor(_ERRORTYPE)

ErrorType = enum_type_wrapper.EnumTypeWrapper(_ERRORTYPE)
SENSOR_NONE = 0
SENSOR_PH = 1
SENSOR_TEMP = 2
SENSOR_ORP = 3
SENSOR_DO = 4
SENSOR_EC = 5
QUERY_NONE = 0
CALIBRATION_NONE = 0
CALIBRATION_STATUS = 1
CALIBRATION_CLEAR = 2
CALIBRATION_SET = 3
TEMP_NONE = 0
TEMP_SINGLE = 1
CALIBRATE_TEMP_NONE = 0
CALIBRATE_TEMP_CLEAR = 1
CALIBRATE_TEMP_SINGLE = 2
DO_NONE = 0
DO_ATMOSPHERE = 1
DO_ZERO = 2
CALIBRATE_DO_NONE = 0
CALIBRATE_DO_CLEAR = 1
CALIBRATE_DO_ATMOSPHERE = 2
CALIBRATE_DO_ZERO = 3
PH_NONE = 0
PH_LOW = 1
PH_MIDDLE = 2
PH_HIGH = 4
CALIBRATE_PH_NONE = 0
CALIBRATE_PH_CLEAR = 1
CALIBRATE_PH_LOW = 2
CALIBRATE_PH_MIDDLE = 3
CALIBRATE_PH_HIGH = 4
EC_NONE = 0
EC_DRY = 1
EC_SINGLE = 2
EC_DUAL_LOW = 4
EC_DUAL_HIGH = 8
CALIBRATE_EC_NONE = 0
CALIBRATE_EC_CLEAR = 1
CALIBRATE_EC_DRY = 2
CALIBRATE_EC_SINGLE = 3
CALIBRATE_EC_DUAL_LOW = 4
CALIBRATE_EC_DUAL_HIGH = 5
ORP_NONE = 0
ORP_SINGLE = 1
CALIBRATE_ORP_NONE = 0
CALIBRATE_ORP_SINGLE = 1
REPLY_NONE = 0
REPLY_RETRY = 1
REPLY_ERROR = 2
REPLY_STATUS = 3
REPLY_COMMAND = 4
NONE = 0
GENERAL = 1
UNEXPECTED = 2



_ATLASCALIBRATIONCOMMAND = _descriptor.Descriptor(
  name='AtlasCalibrationCommand',
  full_name='fk_atlas.AtlasCalibrationCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='fk_atlas.AtlasCalibrationCommand.operation', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temp', full_name='fk_atlas.AtlasCalibrationCommand.temp', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dissolvedOxygen', full_name='fk_atlas.AtlasCalibrationCommand.dissolvedOxygen', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ph', full_name='fk_atlas.AtlasCalibrationCommand.ph', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ec', full_name='fk_atlas.AtlasCalibrationCommand.ec', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orp', full_name='fk_atlas.AtlasCalibrationCommand.orp', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='which', full_name='fk_atlas.AtlasCalibrationCommand.which', index=6,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='fk_atlas.AtlasCalibrationCommand.value', index=7,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=344,
)


_TWOWIREQUERY = _descriptor.Descriptor(
  name='TwoWireQuery',
  full_name='fk_atlas.TwoWireQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='read', full_name='fk_atlas.TwoWireQuery.read', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='write', full_name='fk_atlas.TwoWireQuery.write', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='fk_atlas.TwoWireQuery.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=346,
  serialized_end=403,
)


_COMPENSATIONS = _descriptor.Descriptor(
  name='Compensations',
  full_name='fk_atlas.Compensations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='temperature', full_name='fk_atlas.Compensations.temperature', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=405,
  serialized_end=441,
)


_WIREATLASQUERY = _descriptor.Descriptor(
  name='WireAtlasQuery',
  full_name='fk_atlas.WireAtlasQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='fk_atlas.WireAtlasQuery.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='calibration', full_name='fk_atlas.WireAtlasQuery.calibration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compensations', full_name='fk_atlas.WireAtlasQuery.compensations', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wire', full_name='fk_atlas.WireAtlasQuery.wire', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=444,
  serialized_end=637,
)


_ATLASCALIBRATIONSTATUS = _descriptor.Descriptor(
  name='AtlasCalibrationStatus',
  full_name='fk_atlas.AtlasCalibrationStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='fk_atlas.AtlasCalibrationStatus.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='fk_atlas.AtlasCalibrationStatus.time', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raw', full_name='fk_atlas.AtlasCalibrationStatus.raw', index=2,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temp', full_name='fk_atlas.AtlasCalibrationStatus.temp', index=3,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dissolvedOxygen', full_name='fk_atlas.AtlasCalibrationStatus.dissolvedOxygen', index=4,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ph', full_name='fk_atlas.AtlasCalibrationStatus.ph', index=5,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ec', full_name='fk_atlas.AtlasCalibrationStatus.ec', index=6,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orp', full_name='fk_atlas.AtlasCalibrationStatus.orp', index=7,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=640,
  serialized_end=936,
)


_TWOWIREREPLY = _descriptor.Descriptor(
  name='TwoWireReply',
  full_name='fk_atlas.TwoWireReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='fk_atlas.TwoWireReply.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=938,
  serialized_end=966,
)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='fk_atlas.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='fk_atlas.Error.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='fk_atlas.Error.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=968,
  serialized_end=1027,
)


_WIREATLASREPLY = _descriptor.Descriptor(
  name='WireAtlasReply',
  full_name='fk_atlas.WireAtlasReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='fk_atlas.WireAtlasReply.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errors', full_name='fk_atlas.WireAtlasReply.errors', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='calibration', full_name='fk_atlas.WireAtlasReply.calibration', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wire', full_name='fk_atlas.WireAtlasReply.wire', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1030,
  serialized_end=1207,
)

_ATLASCALIBRATIONCOMMAND.fields_by_name['operation'].enum_type = _CALIBRATIONOPERATION
_ATLASCALIBRATIONCOMMAND.fields_by_name['temp'].enum_type = _TEMPCALIBRATIONS
_ATLASCALIBRATIONCOMMAND.fields_by_name['dissolvedOxygen'].enum_type = _DOCALIBRATIONS
_ATLASCALIBRATIONCOMMAND.fields_by_name['ph'].enum_type = _PHCALIBRATIONS
_ATLASCALIBRATIONCOMMAND.fields_by_name['ec'].enum_type = _ECCALIBRATIONS
_ATLASCALIBRATIONCOMMAND.fields_by_name['orp'].enum_type = _ORPCALIBRATIONS
_WIREATLASQUERY.fields_by_name['type'].enum_type = _QUERYTYPE
_WIREATLASQUERY.fields_by_name['calibration'].message_type = _ATLASCALIBRATIONCOMMAND
_WIREATLASQUERY.fields_by_name['compensations'].message_type = _COMPENSATIONS
_WIREATLASQUERY.fields_by_name['wire'].message_type = _TWOWIREQUERY
_ATLASCALIBRATIONSTATUS.fields_by_name['type'].enum_type = _SENSORTYPE
_ATLASCALIBRATIONSTATUS.fields_by_name['temp'].enum_type = _TEMPCALIBRATIONS
_ATLASCALIBRATIONSTATUS.fields_by_name['dissolvedOxygen'].enum_type = _DOCALIBRATIONS
_ATLASCALIBRATIONSTATUS.fields_by_name['ph'].enum_type = _PHCALIBRATIONS
_ATLASCALIBRATIONSTATUS.fields_by_name['ec'].enum_type = _ECCALIBRATIONS
_ATLASCALIBRATIONSTATUS.fields_by_name['orp'].enum_type = _ORPCALIBRATIONS
_ERROR.fields_by_name['type'].enum_type = _ERRORTYPE
_WIREATLASREPLY.fields_by_name['type'].enum_type = _REPLYTYPE
_WIREATLASREPLY.fields_by_name['errors'].message_type = _ERROR
_WIREATLASREPLY.fields_by_name['calibration'].message_type = _ATLASCALIBRATIONSTATUS
_WIREATLASREPLY.fields_by_name['wire'].message_type = _TWOWIREREPLY
DESCRIPTOR.message_types_by_name['AtlasCalibrationCommand'] = _ATLASCALIBRATIONCOMMAND
DESCRIPTOR.message_types_by_name['TwoWireQuery'] = _TWOWIREQUERY
DESCRIPTOR.message_types_by_name['Compensations'] = _COMPENSATIONS
DESCRIPTOR.message_types_by_name['WireAtlasQuery'] = _WIREATLASQUERY
DESCRIPTOR.message_types_by_name['AtlasCalibrationStatus'] = _ATLASCALIBRATIONSTATUS
DESCRIPTOR.message_types_by_name['TwoWireReply'] = _TWOWIREREPLY
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.message_types_by_name['WireAtlasReply'] = _WIREATLASREPLY
DESCRIPTOR.enum_types_by_name['SensorType'] = _SENSORTYPE
DESCRIPTOR.enum_types_by_name['QueryType'] = _QUERYTYPE
DESCRIPTOR.enum_types_by_name['CalibrationOperation'] = _CALIBRATIONOPERATION
DESCRIPTOR.enum_types_by_name['TempCalibrations'] = _TEMPCALIBRATIONS
DESCRIPTOR.enum_types_by_name['TempCalibrateCommand'] = _TEMPCALIBRATECOMMAND
DESCRIPTOR.enum_types_by_name['DoCalibrations'] = _DOCALIBRATIONS
DESCRIPTOR.enum_types_by_name['DoCalibrateCommand'] = _DOCALIBRATECOMMAND
DESCRIPTOR.enum_types_by_name['PhCalibrations'] = _PHCALIBRATIONS
DESCRIPTOR.enum_types_by_name['PhCalibrateCommand'] = _PHCALIBRATECOMMAND
DESCRIPTOR.enum_types_by_name['EcCalibrations'] = _ECCALIBRATIONS
DESCRIPTOR.enum_types_by_name['EcCalibrateCommand'] = _ECCALIBRATECOMMAND
DESCRIPTOR.enum_types_by_name['OrpCalibrations'] = _ORPCALIBRATIONS
DESCRIPTOR.enum_types_by_name['OrpCalibrateCommand'] = _ORPCALIBRATECOMMAND
DESCRIPTOR.enum_types_by_name['ReplyType'] = _REPLYTYPE
DESCRIPTOR.enum_types_by_name['ErrorType'] = _ERRORTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AtlasCalibrationCommand = _reflection.GeneratedProtocolMessageType('AtlasCalibrationCommand', (_message.Message,), {
  'DESCRIPTOR' : _ATLASCALIBRATIONCOMMAND,
  '__module__' : 'fk_atlas_pb2'
  # @@protoc_insertion_point(class_scope:fk_atlas.AtlasCalibrationCommand)
  })
_sym_db.RegisterMessage(AtlasCalibrationCommand)

TwoWireQuery = _reflection.GeneratedProtocolMessageType('TwoWireQuery', (_message.Message,), {
  'DESCRIPTOR' : _TWOWIREQUERY,
  '__module__' : 'fk_atlas_pb2'
  # @@protoc_insertion_point(class_scope:fk_atlas.TwoWireQuery)
  })
_sym_db.RegisterMessage(TwoWireQuery)

Compensations = _reflection.GeneratedProtocolMessageType('Compensations', (_message.Message,), {
  'DESCRIPTOR' : _COMPENSATIONS,
  '__module__' : 'fk_atlas_pb2'
  # @@protoc_insertion_point(class_scope:fk_atlas.Compensations)
  })
_sym_db.RegisterMessage(Compensations)

WireAtlasQuery = _reflection.GeneratedProtocolMessageType('WireAtlasQuery', (_message.Message,), {
  'DESCRIPTOR' : _WIREATLASQUERY,
  '__module__' : 'fk_atlas_pb2'
  # @@protoc_insertion_point(class_scope:fk_atlas.WireAtlasQuery)
  })
_sym_db.RegisterMessage(WireAtlasQuery)

AtlasCalibrationStatus = _reflection.GeneratedProtocolMessageType('AtlasCalibrationStatus', (_message.Message,), {
  'DESCRIPTOR' : _ATLASCALIBRATIONSTATUS,
  '__module__' : 'fk_atlas_pb2'
  # @@protoc_insertion_point(class_scope:fk_atlas.AtlasCalibrationStatus)
  })
_sym_db.RegisterMessage(AtlasCalibrationStatus)

TwoWireReply = _reflection.GeneratedProtocolMessageType('TwoWireReply', (_message.Message,), {
  'DESCRIPTOR' : _TWOWIREREPLY,
  '__module__' : 'fk_atlas_pb2'
  # @@protoc_insertion_point(class_scope:fk_atlas.TwoWireReply)
  })
_sym_db.RegisterMessage(TwoWireReply)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {
  'DESCRIPTOR' : _ERROR,
  '__module__' : 'fk_atlas_pb2'
  # @@protoc_insertion_point(class_scope:fk_atlas.Error)
  })
_sym_db.RegisterMessage(Error)

WireAtlasReply = _reflection.GeneratedProtocolMessageType('WireAtlasReply', (_message.Message,), {
  'DESCRIPTOR' : _WIREATLASREPLY,
  '__module__' : 'fk_atlas_pb2'
  # @@protoc_insertion_point(class_scope:fk_atlas.WireAtlasReply)
  })
_sym_db.RegisterMessage(WireAtlasReply)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
