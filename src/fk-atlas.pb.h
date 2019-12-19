/* Automatically generated nanopb header */
/* Generated by nanopb-0.4.0-dev */

#ifndef PB_FK_ATLAS_FK_ATLAS_PB_H_INCLUDED
#define PB_FK_ATLAS_FK_ATLAS_PB_H_INCLUDED
#include <pb.h>

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 40
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Enum definitions */
typedef enum _fk_atlas_SensorType {
    fk_atlas_SensorType_SENSOR_NONE = 0,
    fk_atlas_SensorType_SENSOR_PH = 1,
    fk_atlas_SensorType_SENSOR_TEMP = 2,
    fk_atlas_SensorType_SENSOR_ORP = 3,
    fk_atlas_SensorType_SENSOR_DO = 4,
    fk_atlas_SensorType_SENSOR_EC = 5
} fk_atlas_SensorType;
#define _fk_atlas_SensorType_MIN fk_atlas_SensorType_SENSOR_NONE
#define _fk_atlas_SensorType_MAX fk_atlas_SensorType_SENSOR_EC
#define _fk_atlas_SensorType_ARRAYSIZE ((fk_atlas_SensorType)(fk_atlas_SensorType_SENSOR_EC+1))

typedef enum _fk_atlas_QueryType {
    fk_atlas_QueryType_QUERY_NONE = 0
} fk_atlas_QueryType;
#define _fk_atlas_QueryType_MIN fk_atlas_QueryType_QUERY_NONE
#define _fk_atlas_QueryType_MAX fk_atlas_QueryType_QUERY_NONE
#define _fk_atlas_QueryType_ARRAYSIZE ((fk_atlas_QueryType)(fk_atlas_QueryType_QUERY_NONE+1))

typedef enum _fk_atlas_CalibrationOperation {
    fk_atlas_CalibrationOperation_CALIBRATION_NONE = 0,
    fk_atlas_CalibrationOperation_CALIBRATION_STATUS = 1,
    fk_atlas_CalibrationOperation_CALIBRATION_CLEAR = 2,
    fk_atlas_CalibrationOperation_CALIBRATION_SET = 3
} fk_atlas_CalibrationOperation;
#define _fk_atlas_CalibrationOperation_MIN fk_atlas_CalibrationOperation_CALIBRATION_NONE
#define _fk_atlas_CalibrationOperation_MAX fk_atlas_CalibrationOperation_CALIBRATION_SET
#define _fk_atlas_CalibrationOperation_ARRAYSIZE ((fk_atlas_CalibrationOperation)(fk_atlas_CalibrationOperation_CALIBRATION_SET+1))

typedef enum _fk_atlas_TempCalibrations {
    fk_atlas_TempCalibrations_TEMP_NONE = 0,
    fk_atlas_TempCalibrations_TEMP_SINGLE = 1
} fk_atlas_TempCalibrations;
#define _fk_atlas_TempCalibrations_MIN fk_atlas_TempCalibrations_TEMP_NONE
#define _fk_atlas_TempCalibrations_MAX fk_atlas_TempCalibrations_TEMP_SINGLE
#define _fk_atlas_TempCalibrations_ARRAYSIZE ((fk_atlas_TempCalibrations)(fk_atlas_TempCalibrations_TEMP_SINGLE+1))

typedef enum _fk_atlas_DoCalibrations {
    fk_atlas_DoCalibrations_DO_NONE = 0,
    fk_atlas_DoCalibrations_DO_ATMOSPHERE = 1,
    fk_atlas_DoCalibrations_DO_ZERO = 2
} fk_atlas_DoCalibrations;
#define _fk_atlas_DoCalibrations_MIN fk_atlas_DoCalibrations_DO_NONE
#define _fk_atlas_DoCalibrations_MAX fk_atlas_DoCalibrations_DO_ZERO
#define _fk_atlas_DoCalibrations_ARRAYSIZE ((fk_atlas_DoCalibrations)(fk_atlas_DoCalibrations_DO_ZERO+1))

typedef enum _fk_atlas_PhCalibrations {
    fk_atlas_PhCalibrations_PH_NONE = 0,
    fk_atlas_PhCalibrations_PH_LOW = 1,
    fk_atlas_PhCalibrations_PH_MIDDLE = 2,
    fk_atlas_PhCalibrations_PH_HIGH = 4
} fk_atlas_PhCalibrations;
#define _fk_atlas_PhCalibrations_MIN fk_atlas_PhCalibrations_PH_NONE
#define _fk_atlas_PhCalibrations_MAX fk_atlas_PhCalibrations_PH_HIGH
#define _fk_atlas_PhCalibrations_ARRAYSIZE ((fk_atlas_PhCalibrations)(fk_atlas_PhCalibrations_PH_HIGH+1))

typedef enum _fk_atlas_EcCalibrations {
    fk_atlas_EcCalibrations_EC_NONE = 0,
    fk_atlas_EcCalibrations_EC_DRY = 1,
    fk_atlas_EcCalibrations_EC_SINGLE = 2,
    fk_atlas_EcCalibrations_EC_DUAL_LOW = 4,
    fk_atlas_EcCalibrations_EC_DUAL_HIGH = 8
} fk_atlas_EcCalibrations;
#define _fk_atlas_EcCalibrations_MIN fk_atlas_EcCalibrations_EC_NONE
#define _fk_atlas_EcCalibrations_MAX fk_atlas_EcCalibrations_EC_DUAL_HIGH
#define _fk_atlas_EcCalibrations_ARRAYSIZE ((fk_atlas_EcCalibrations)(fk_atlas_EcCalibrations_EC_DUAL_HIGH+1))

typedef enum _fk_atlas_OrpCalibrations {
    fk_atlas_OrpCalibrations_ORP_NONE = 0,
    fk_atlas_OrpCalibrations_ORP_SINGLE = 1
} fk_atlas_OrpCalibrations;
#define _fk_atlas_OrpCalibrations_MIN fk_atlas_OrpCalibrations_ORP_NONE
#define _fk_atlas_OrpCalibrations_MAX fk_atlas_OrpCalibrations_ORP_SINGLE
#define _fk_atlas_OrpCalibrations_ARRAYSIZE ((fk_atlas_OrpCalibrations)(fk_atlas_OrpCalibrations_ORP_SINGLE+1))

typedef enum _fk_atlas_ReplyType {
    fk_atlas_ReplyType_REPLY_NONE = 0,
    fk_atlas_ReplyType_REPLY_RETRY = 1,
    fk_atlas_ReplyType_REPLY_ERROR = 2,
    fk_atlas_ReplyType_REPLY_ATLAS_COMMAND = 3
} fk_atlas_ReplyType;
#define _fk_atlas_ReplyType_MIN fk_atlas_ReplyType_REPLY_NONE
#define _fk_atlas_ReplyType_MAX fk_atlas_ReplyType_REPLY_ATLAS_COMMAND
#define _fk_atlas_ReplyType_ARRAYSIZE ((fk_atlas_ReplyType)(fk_atlas_ReplyType_REPLY_ATLAS_COMMAND+1))

typedef enum _fk_atlas_ErrorType {
    fk_atlas_ErrorType_NONE = 0,
    fk_atlas_ErrorType_GENERAL = 1,
    fk_atlas_ErrorType_UNEXPECTED = 2
} fk_atlas_ErrorType;
#define _fk_atlas_ErrorType_MIN fk_atlas_ErrorType_NONE
#define _fk_atlas_ErrorType_MAX fk_atlas_ErrorType_UNEXPECTED
#define _fk_atlas_ErrorType_ARRAYSIZE ((fk_atlas_ErrorType)(fk_atlas_ErrorType_UNEXPECTED+1))

/* Struct definitions */
typedef struct _fk_atlas_AtlasCalibrationCommand {
    fk_atlas_CalibrationOperation operation;
    fk_atlas_TempCalibrations temp;
    fk_atlas_DoCalibrations do;
    fk_atlas_PhCalibrations ph;
    fk_atlas_EcCalibrations ec;
    fk_atlas_OrpCalibrations orp;
    float value;
/* @@protoc_insertion_point(struct:fk_atlas_AtlasCalibrationCommand) */
} fk_atlas_AtlasCalibrationCommand;


typedef struct _fk_atlas_AtlasCalibrationStatus {
    fk_atlas_SensorType type;
    uint32_t time;
    fk_atlas_TempCalibrations temp;
    fk_atlas_DoCalibrations do;
    fk_atlas_PhCalibrations ph;
    fk_atlas_EcCalibrations ec;
    fk_atlas_OrpCalibrations orp;
/* @@protoc_insertion_point(struct:fk_atlas_AtlasCalibrationStatus) */
} fk_atlas_AtlasCalibrationStatus;


typedef struct _fk_atlas_Error {
    fk_atlas_ErrorType type;
    pb_callback_t message;
/* @@protoc_insertion_point(struct:fk_atlas_Error) */
} fk_atlas_Error;


typedef struct _fk_atlas_WireAtlasQuery {
    fk_atlas_QueryType type;
    fk_atlas_AtlasCalibrationCommand calibration;
/* @@protoc_insertion_point(struct:fk_atlas_WireAtlasQuery) */
} fk_atlas_WireAtlasQuery;


typedef struct _fk_atlas_WireAtlasReply {
    fk_atlas_ReplyType type;
    fk_atlas_Error error;
    fk_atlas_AtlasCalibrationStatus calibration;
/* @@protoc_insertion_point(struct:fk_atlas_WireAtlasReply) */
} fk_atlas_WireAtlasReply;


/* Initializer values for message structs */
#define fk_atlas_AtlasCalibrationCommand_init_default {_fk_atlas_CalibrationOperation_MIN, _fk_atlas_TempCalibrations_MIN, _fk_atlas_DoCalibrations_MIN, _fk_atlas_PhCalibrations_MIN, _fk_atlas_EcCalibrations_MIN, _fk_atlas_OrpCalibrations_MIN, 0}
#define fk_atlas_WireAtlasQuery_init_default     {_fk_atlas_QueryType_MIN, fk_atlas_AtlasCalibrationCommand_init_default}
#define fk_atlas_AtlasCalibrationStatus_init_default {_fk_atlas_SensorType_MIN, 0, _fk_atlas_TempCalibrations_MIN, _fk_atlas_DoCalibrations_MIN, _fk_atlas_PhCalibrations_MIN, _fk_atlas_EcCalibrations_MIN, _fk_atlas_OrpCalibrations_MIN}
#define fk_atlas_Error_init_default              {_fk_atlas_ErrorType_MIN, {{NULL}, NULL}}
#define fk_atlas_WireAtlasReply_init_default     {_fk_atlas_ReplyType_MIN, fk_atlas_Error_init_default, fk_atlas_AtlasCalibrationStatus_init_default}
#define fk_atlas_AtlasCalibrationCommand_init_zero {_fk_atlas_CalibrationOperation_MIN, _fk_atlas_TempCalibrations_MIN, _fk_atlas_DoCalibrations_MIN, _fk_atlas_PhCalibrations_MIN, _fk_atlas_EcCalibrations_MIN, _fk_atlas_OrpCalibrations_MIN, 0}
#define fk_atlas_WireAtlasQuery_init_zero        {_fk_atlas_QueryType_MIN, fk_atlas_AtlasCalibrationCommand_init_zero}
#define fk_atlas_AtlasCalibrationStatus_init_zero {_fk_atlas_SensorType_MIN, 0, _fk_atlas_TempCalibrations_MIN, _fk_atlas_DoCalibrations_MIN, _fk_atlas_PhCalibrations_MIN, _fk_atlas_EcCalibrations_MIN, _fk_atlas_OrpCalibrations_MIN}
#define fk_atlas_Error_init_zero                 {_fk_atlas_ErrorType_MIN, {{NULL}, NULL}}
#define fk_atlas_WireAtlasReply_init_zero        {_fk_atlas_ReplyType_MIN, fk_atlas_Error_init_zero, fk_atlas_AtlasCalibrationStatus_init_zero}

/* Field tags (for use in manual encoding/decoding) */
#define fk_atlas_AtlasCalibrationCommand_operation_tag 1
#define fk_atlas_AtlasCalibrationCommand_temp_tag 2
#define fk_atlas_AtlasCalibrationCommand_do_tag  3
#define fk_atlas_AtlasCalibrationCommand_ph_tag  4
#define fk_atlas_AtlasCalibrationCommand_ec_tag  5
#define fk_atlas_AtlasCalibrationCommand_orp_tag 6
#define fk_atlas_AtlasCalibrationCommand_value_tag 7
#define fk_atlas_AtlasCalibrationStatus_type_tag 1
#define fk_atlas_AtlasCalibrationStatus_time_tag 2
#define fk_atlas_AtlasCalibrationStatus_temp_tag 3
#define fk_atlas_AtlasCalibrationStatus_do_tag   4
#define fk_atlas_AtlasCalibrationStatus_ph_tag   5
#define fk_atlas_AtlasCalibrationStatus_ec_tag   6
#define fk_atlas_AtlasCalibrationStatus_orp_tag  7
#define fk_atlas_Error_type_tag                  1
#define fk_atlas_Error_message_tag               2
#define fk_atlas_WireAtlasQuery_type_tag         1
#define fk_atlas_WireAtlasQuery_calibration_tag  2
#define fk_atlas_WireAtlasReply_type_tag         1
#define fk_atlas_WireAtlasReply_error_tag        2
#define fk_atlas_WireAtlasReply_calibration_tag  3

/* Struct field encoding specification for nanopb */
#define fk_atlas_AtlasCalibrationCommand_FIELDLIST(X, a) \
X(a, STATIC, SINGULAR, UENUM, operation, 1) \
X(a, STATIC, SINGULAR, UENUM, temp, 2) \
X(a, STATIC, SINGULAR, UENUM, do, 3) \
X(a, STATIC, SINGULAR, UENUM, ph, 4) \
X(a, STATIC, SINGULAR, UENUM, ec, 5) \
X(a, STATIC, SINGULAR, UENUM, orp, 6) \
X(a, STATIC, SINGULAR, FLOAT, value, 7)
#define fk_atlas_AtlasCalibrationCommand_CALLBACK NULL
#define fk_atlas_AtlasCalibrationCommand_DEFAULT NULL

#define fk_atlas_WireAtlasQuery_FIELDLIST(X, a) \
X(a, STATIC, SINGULAR, UENUM, type, 1) \
X(a, STATIC, SINGULAR, MESSAGE, calibration, 2)
#define fk_atlas_WireAtlasQuery_CALLBACK NULL
#define fk_atlas_WireAtlasQuery_DEFAULT NULL
#define fk_atlas_WireAtlasQuery_calibration_MSGTYPE fk_atlas_AtlasCalibrationCommand

#define fk_atlas_AtlasCalibrationStatus_FIELDLIST(X, a) \
X(a, STATIC, SINGULAR, UENUM, type, 1) \
X(a, STATIC, SINGULAR, UINT32, time, 2) \
X(a, STATIC, SINGULAR, UENUM, temp, 3) \
X(a, STATIC, SINGULAR, UENUM, do, 4) \
X(a, STATIC, SINGULAR, UENUM, ph, 5) \
X(a, STATIC, SINGULAR, UENUM, ec, 6) \
X(a, STATIC, SINGULAR, UENUM, orp, 7)
#define fk_atlas_AtlasCalibrationStatus_CALLBACK NULL
#define fk_atlas_AtlasCalibrationStatus_DEFAULT NULL

#define fk_atlas_Error_FIELDLIST(X, a) \
X(a, STATIC, SINGULAR, UENUM, type, 1) \
X(a, CALLBACK, SINGULAR, STRING, message, 2)
#define fk_atlas_Error_CALLBACK pb_default_field_callback
#define fk_atlas_Error_DEFAULT NULL

#define fk_atlas_WireAtlasReply_FIELDLIST(X, a) \
X(a, STATIC, SINGULAR, UENUM, type, 1) \
X(a, STATIC, SINGULAR, MESSAGE, error, 2) \
X(a, STATIC, SINGULAR, MESSAGE, calibration, 3)
#define fk_atlas_WireAtlasReply_CALLBACK NULL
#define fk_atlas_WireAtlasReply_DEFAULT NULL
#define fk_atlas_WireAtlasReply_error_MSGTYPE fk_atlas_Error
#define fk_atlas_WireAtlasReply_calibration_MSGTYPE fk_atlas_AtlasCalibrationStatus

extern const pb_msgdesc_t fk_atlas_AtlasCalibrationCommand_msg;
extern const pb_msgdesc_t fk_atlas_WireAtlasQuery_msg;
extern const pb_msgdesc_t fk_atlas_AtlasCalibrationStatus_msg;
extern const pb_msgdesc_t fk_atlas_Error_msg;
extern const pb_msgdesc_t fk_atlas_WireAtlasReply_msg;

/* Defines for backwards compatibility with code written before nanopb-0.4.0 */
#define fk_atlas_AtlasCalibrationCommand_fields &fk_atlas_AtlasCalibrationCommand_msg
#define fk_atlas_WireAtlasQuery_fields &fk_atlas_WireAtlasQuery_msg
#define fk_atlas_AtlasCalibrationStatus_fields &fk_atlas_AtlasCalibrationStatus_msg
#define fk_atlas_Error_fields &fk_atlas_Error_msg
#define fk_atlas_WireAtlasReply_fields &fk_atlas_WireAtlasReply_msg

/* Maximum encoded size of messages (where known) */
#define fk_atlas_AtlasCalibrationCommand_size    17
#define fk_atlas_WireAtlasQuery_size             21
#define fk_atlas_AtlasCalibrationStatus_size     18
/* fk_atlas_Error_size depends on runtime parameters */
/* fk_atlas_WireAtlasReply_size depends on runtime parameters */

#ifdef __cplusplus
} /* extern "C" */
#endif
/* @@protoc_insertion_point(eof) */

#endif
