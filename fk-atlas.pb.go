// Code generated by protoc-gen-go. DO NOT EDIT.
// source: fk-atlas.proto

package fk_atlas

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type SensorType int32

const (
	SensorType_SENSOR_NONE SensorType = 0
	SensorType_SENSOR_PH   SensorType = 1
	SensorType_SENSOR_TEMP SensorType = 2
	SensorType_SENSOR_ORP  SensorType = 3
	SensorType_SENSOR_DO   SensorType = 4
	SensorType_SENSOR_EC   SensorType = 5
)

var SensorType_name = map[int32]string{
	0: "SENSOR_NONE",
	1: "SENSOR_PH",
	2: "SENSOR_TEMP",
	3: "SENSOR_ORP",
	4: "SENSOR_DO",
	5: "SENSOR_EC",
}

var SensorType_value = map[string]int32{
	"SENSOR_NONE": 0,
	"SENSOR_PH":   1,
	"SENSOR_TEMP": 2,
	"SENSOR_ORP":  3,
	"SENSOR_DO":   4,
	"SENSOR_EC":   5,
}

func (x SensorType) String() string {
	return proto.EnumName(SensorType_name, int32(x))
}

func (SensorType) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_822d05f6175684bb, []int{0}
}

type QueryType int32

const (
	QueryType_QUERY_NONE QueryType = 0
)

var QueryType_name = map[int32]string{
	0: "QUERY_NONE",
}

var QueryType_value = map[string]int32{
	"QUERY_NONE": 0,
}

func (x QueryType) String() string {
	return proto.EnumName(QueryType_name, int32(x))
}

func (QueryType) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_822d05f6175684bb, []int{1}
}

type CalibrationOperation int32

const (
	CalibrationOperation_CALIBRATION_NONE   CalibrationOperation = 0
	CalibrationOperation_CALIBRATION_STATUS CalibrationOperation = 1
	CalibrationOperation_CALIBRATION_CLEAR  CalibrationOperation = 2
	CalibrationOperation_CALIBRATION_SET    CalibrationOperation = 3
)

var CalibrationOperation_name = map[int32]string{
	0: "CALIBRATION_NONE",
	1: "CALIBRATION_STATUS",
	2: "CALIBRATION_CLEAR",
	3: "CALIBRATION_SET",
}

var CalibrationOperation_value = map[string]int32{
	"CALIBRATION_NONE":   0,
	"CALIBRATION_STATUS": 1,
	"CALIBRATION_CLEAR":  2,
	"CALIBRATION_SET":    3,
}

func (x CalibrationOperation) String() string {
	return proto.EnumName(CalibrationOperation_name, int32(x))
}

func (CalibrationOperation) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_822d05f6175684bb, []int{2}
}

type TempCalibrations int32

const (
	TempCalibrations_TEMP_NONE   TempCalibrations = 0
	TempCalibrations_TEMP_SINGLE TempCalibrations = 1
)

var TempCalibrations_name = map[int32]string{
	0: "TEMP_NONE",
	1: "TEMP_SINGLE",
}

var TempCalibrations_value = map[string]int32{
	"TEMP_NONE":   0,
	"TEMP_SINGLE": 1,
}

func (x TempCalibrations) String() string {
	return proto.EnumName(TempCalibrations_name, int32(x))
}

func (TempCalibrations) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_822d05f6175684bb, []int{3}
}

type DoCalibrations int32

const (
	DoCalibrations_DO_NONE       DoCalibrations = 0
	DoCalibrations_DO_ATMOSPHERE DoCalibrations = 1
	DoCalibrations_DO_ZERO       DoCalibrations = 2
)

var DoCalibrations_name = map[int32]string{
	0: "DO_NONE",
	1: "DO_ATMOSPHERE",
	2: "DO_ZERO",
}

var DoCalibrations_value = map[string]int32{
	"DO_NONE":       0,
	"DO_ATMOSPHERE": 1,
	"DO_ZERO":       2,
}

func (x DoCalibrations) String() string {
	return proto.EnumName(DoCalibrations_name, int32(x))
}

func (DoCalibrations) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_822d05f6175684bb, []int{4}
}

type PhCalibrations int32

const (
	PhCalibrations_PH_NONE   PhCalibrations = 0
	PhCalibrations_PH_LOW    PhCalibrations = 1
	PhCalibrations_PH_MIDDLE PhCalibrations = 2
	PhCalibrations_PH_HIGH   PhCalibrations = 4
)

var PhCalibrations_name = map[int32]string{
	0: "PH_NONE",
	1: "PH_LOW",
	2: "PH_MIDDLE",
	4: "PH_HIGH",
}

var PhCalibrations_value = map[string]int32{
	"PH_NONE":   0,
	"PH_LOW":    1,
	"PH_MIDDLE": 2,
	"PH_HIGH":   4,
}

func (x PhCalibrations) String() string {
	return proto.EnumName(PhCalibrations_name, int32(x))
}

func (PhCalibrations) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_822d05f6175684bb, []int{5}
}

type EcCalibrations int32

const (
	EcCalibrations_EC_NONE      EcCalibrations = 0
	EcCalibrations_EC_DRY       EcCalibrations = 1
	EcCalibrations_EC_SINGLE    EcCalibrations = 2
	EcCalibrations_EC_DUAL_LOW  EcCalibrations = 4
	EcCalibrations_EC_DUAL_HIGH EcCalibrations = 8
)

var EcCalibrations_name = map[int32]string{
	0: "EC_NONE",
	1: "EC_DRY",
	2: "EC_SINGLE",
	4: "EC_DUAL_LOW",
	8: "EC_DUAL_HIGH",
}

var EcCalibrations_value = map[string]int32{
	"EC_NONE":      0,
	"EC_DRY":       1,
	"EC_SINGLE":    2,
	"EC_DUAL_LOW":  4,
	"EC_DUAL_HIGH": 8,
}

func (x EcCalibrations) String() string {
	return proto.EnumName(EcCalibrations_name, int32(x))
}

func (EcCalibrations) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_822d05f6175684bb, []int{6}
}

type OrpCalibrations int32

const (
	OrpCalibrations_ORP_NONE   OrpCalibrations = 0
	OrpCalibrations_ORP_SINGLE OrpCalibrations = 1
)

var OrpCalibrations_name = map[int32]string{
	0: "ORP_NONE",
	1: "ORP_SINGLE",
}

var OrpCalibrations_value = map[string]int32{
	"ORP_NONE":   0,
	"ORP_SINGLE": 1,
}

func (x OrpCalibrations) String() string {
	return proto.EnumName(OrpCalibrations_name, int32(x))
}

func (OrpCalibrations) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_822d05f6175684bb, []int{7}
}

type ReplyType int32

const (
	ReplyType_REPLY_NONE          ReplyType = 0
	ReplyType_REPLY_RETRY         ReplyType = 1
	ReplyType_REPLY_ERROR         ReplyType = 2
	ReplyType_REPLY_ATLAS_COMMAND ReplyType = 3
)

var ReplyType_name = map[int32]string{
	0: "REPLY_NONE",
	1: "REPLY_RETRY",
	2: "REPLY_ERROR",
	3: "REPLY_ATLAS_COMMAND",
}

var ReplyType_value = map[string]int32{
	"REPLY_NONE":          0,
	"REPLY_RETRY":         1,
	"REPLY_ERROR":         2,
	"REPLY_ATLAS_COMMAND": 3,
}

func (x ReplyType) String() string {
	return proto.EnumName(ReplyType_name, int32(x))
}

func (ReplyType) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_822d05f6175684bb, []int{8}
}

type ErrorType int32

const (
	ErrorType_NONE       ErrorType = 0
	ErrorType_GENERAL    ErrorType = 1
	ErrorType_UNEXPECTED ErrorType = 2
)

var ErrorType_name = map[int32]string{
	0: "NONE",
	1: "GENERAL",
	2: "UNEXPECTED",
}

var ErrorType_value = map[string]int32{
	"NONE":       0,
	"GENERAL":    1,
	"UNEXPECTED": 2,
}

func (x ErrorType) String() string {
	return proto.EnumName(ErrorType_name, int32(x))
}

func (ErrorType) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_822d05f6175684bb, []int{9}
}

type AtlasCalibrationCommand struct {
	Operation            CalibrationOperation `protobuf:"varint,1,opt,name=operation,proto3,enum=fk_atlas.CalibrationOperation" json:"operation,omitempty"`
	Temp                 TempCalibrations     `protobuf:"varint,2,opt,name=temp,proto3,enum=fk_atlas.TempCalibrations" json:"temp,omitempty"`
	DissolvedOxygen      DoCalibrations       `protobuf:"varint,3,opt,name=dissolvedOxygen,proto3,enum=fk_atlas.DoCalibrations" json:"dissolvedOxygen,omitempty"`
	Ph                   PhCalibrations       `protobuf:"varint,4,opt,name=ph,proto3,enum=fk_atlas.PhCalibrations" json:"ph,omitempty"`
	Ec                   EcCalibrations       `protobuf:"varint,5,opt,name=ec,proto3,enum=fk_atlas.EcCalibrations" json:"ec,omitempty"`
	Orp                  OrpCalibrations      `protobuf:"varint,6,opt,name=orp,proto3,enum=fk_atlas.OrpCalibrations" json:"orp,omitempty"`
	Value                float32              `protobuf:"fixed32,7,opt,name=value,proto3" json:"value,omitempty"`
	XXX_NoUnkeyedLiteral struct{}             `json:"-"`
	XXX_unrecognized     []byte               `json:"-"`
	XXX_sizecache        int32                `json:"-"`
}

func (m *AtlasCalibrationCommand) Reset()         { *m = AtlasCalibrationCommand{} }
func (m *AtlasCalibrationCommand) String() string { return proto.CompactTextString(m) }
func (*AtlasCalibrationCommand) ProtoMessage()    {}
func (*AtlasCalibrationCommand) Descriptor() ([]byte, []int) {
	return fileDescriptor_822d05f6175684bb, []int{0}
}

func (m *AtlasCalibrationCommand) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_AtlasCalibrationCommand.Unmarshal(m, b)
}
func (m *AtlasCalibrationCommand) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_AtlasCalibrationCommand.Marshal(b, m, deterministic)
}
func (m *AtlasCalibrationCommand) XXX_Merge(src proto.Message) {
	xxx_messageInfo_AtlasCalibrationCommand.Merge(m, src)
}
func (m *AtlasCalibrationCommand) XXX_Size() int {
	return xxx_messageInfo_AtlasCalibrationCommand.Size(m)
}
func (m *AtlasCalibrationCommand) XXX_DiscardUnknown() {
	xxx_messageInfo_AtlasCalibrationCommand.DiscardUnknown(m)
}

var xxx_messageInfo_AtlasCalibrationCommand proto.InternalMessageInfo

func (m *AtlasCalibrationCommand) GetOperation() CalibrationOperation {
	if m != nil {
		return m.Operation
	}
	return CalibrationOperation_CALIBRATION_NONE
}

func (m *AtlasCalibrationCommand) GetTemp() TempCalibrations {
	if m != nil {
		return m.Temp
	}
	return TempCalibrations_TEMP_NONE
}

func (m *AtlasCalibrationCommand) GetDissolvedOxygen() DoCalibrations {
	if m != nil {
		return m.DissolvedOxygen
	}
	return DoCalibrations_DO_NONE
}

func (m *AtlasCalibrationCommand) GetPh() PhCalibrations {
	if m != nil {
		return m.Ph
	}
	return PhCalibrations_PH_NONE
}

func (m *AtlasCalibrationCommand) GetEc() EcCalibrations {
	if m != nil {
		return m.Ec
	}
	return EcCalibrations_EC_NONE
}

func (m *AtlasCalibrationCommand) GetOrp() OrpCalibrations {
	if m != nil {
		return m.Orp
	}
	return OrpCalibrations_ORP_NONE
}

func (m *AtlasCalibrationCommand) GetValue() float32 {
	if m != nil {
		return m.Value
	}
	return 0
}

type TwoWireQuery struct {
	Read                 uint32   `protobuf:"varint,1,opt,name=read,proto3" json:"read,omitempty"`
	Write                uint32   `protobuf:"varint,2,opt,name=write,proto3" json:"write,omitempty"`
	Data                 []byte   `protobuf:"bytes,3,opt,name=data,proto3" json:"data,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *TwoWireQuery) Reset()         { *m = TwoWireQuery{} }
func (m *TwoWireQuery) String() string { return proto.CompactTextString(m) }
func (*TwoWireQuery) ProtoMessage()    {}
func (*TwoWireQuery) Descriptor() ([]byte, []int) {
	return fileDescriptor_822d05f6175684bb, []int{1}
}

func (m *TwoWireQuery) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_TwoWireQuery.Unmarshal(m, b)
}
func (m *TwoWireQuery) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_TwoWireQuery.Marshal(b, m, deterministic)
}
func (m *TwoWireQuery) XXX_Merge(src proto.Message) {
	xxx_messageInfo_TwoWireQuery.Merge(m, src)
}
func (m *TwoWireQuery) XXX_Size() int {
	return xxx_messageInfo_TwoWireQuery.Size(m)
}
func (m *TwoWireQuery) XXX_DiscardUnknown() {
	xxx_messageInfo_TwoWireQuery.DiscardUnknown(m)
}

var xxx_messageInfo_TwoWireQuery proto.InternalMessageInfo

func (m *TwoWireQuery) GetRead() uint32 {
	if m != nil {
		return m.Read
	}
	return 0
}

func (m *TwoWireQuery) GetWrite() uint32 {
	if m != nil {
		return m.Write
	}
	return 0
}

func (m *TwoWireQuery) GetData() []byte {
	if m != nil {
		return m.Data
	}
	return nil
}

type WireAtlasQuery struct {
	Type                 QueryType                `protobuf:"varint,1,opt,name=type,proto3,enum=fk_atlas.QueryType" json:"type,omitempty"`
	Calibration          *AtlasCalibrationCommand `protobuf:"bytes,2,opt,name=calibration,proto3" json:"calibration,omitempty"`
	Wire                 *TwoWireQuery            `protobuf:"bytes,3,opt,name=wire,proto3" json:"wire,omitempty"`
	XXX_NoUnkeyedLiteral struct{}                 `json:"-"`
	XXX_unrecognized     []byte                   `json:"-"`
	XXX_sizecache        int32                    `json:"-"`
}

func (m *WireAtlasQuery) Reset()         { *m = WireAtlasQuery{} }
func (m *WireAtlasQuery) String() string { return proto.CompactTextString(m) }
func (*WireAtlasQuery) ProtoMessage()    {}
func (*WireAtlasQuery) Descriptor() ([]byte, []int) {
	return fileDescriptor_822d05f6175684bb, []int{2}
}

func (m *WireAtlasQuery) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_WireAtlasQuery.Unmarshal(m, b)
}
func (m *WireAtlasQuery) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_WireAtlasQuery.Marshal(b, m, deterministic)
}
func (m *WireAtlasQuery) XXX_Merge(src proto.Message) {
	xxx_messageInfo_WireAtlasQuery.Merge(m, src)
}
func (m *WireAtlasQuery) XXX_Size() int {
	return xxx_messageInfo_WireAtlasQuery.Size(m)
}
func (m *WireAtlasQuery) XXX_DiscardUnknown() {
	xxx_messageInfo_WireAtlasQuery.DiscardUnknown(m)
}

var xxx_messageInfo_WireAtlasQuery proto.InternalMessageInfo

func (m *WireAtlasQuery) GetType() QueryType {
	if m != nil {
		return m.Type
	}
	return QueryType_QUERY_NONE
}

func (m *WireAtlasQuery) GetCalibration() *AtlasCalibrationCommand {
	if m != nil {
		return m.Calibration
	}
	return nil
}

func (m *WireAtlasQuery) GetWire() *TwoWireQuery {
	if m != nil {
		return m.Wire
	}
	return nil
}

type AtlasCalibrationStatus struct {
	Type                 SensorType       `protobuf:"varint,1,opt,name=type,proto3,enum=fk_atlas.SensorType" json:"type,omitempty"`
	Time                 uint32           `protobuf:"varint,2,opt,name=time,proto3" json:"time,omitempty"`
	Temp                 TempCalibrations `protobuf:"varint,3,opt,name=temp,proto3,enum=fk_atlas.TempCalibrations" json:"temp,omitempty"`
	DissolvedOxygen      DoCalibrations   `protobuf:"varint,4,opt,name=dissolvedOxygen,proto3,enum=fk_atlas.DoCalibrations" json:"dissolvedOxygen,omitempty"`
	Ph                   PhCalibrations   `protobuf:"varint,5,opt,name=ph,proto3,enum=fk_atlas.PhCalibrations" json:"ph,omitempty"`
	Ec                   EcCalibrations   `protobuf:"varint,6,opt,name=ec,proto3,enum=fk_atlas.EcCalibrations" json:"ec,omitempty"`
	Orp                  OrpCalibrations  `protobuf:"varint,7,opt,name=orp,proto3,enum=fk_atlas.OrpCalibrations" json:"orp,omitempty"`
	XXX_NoUnkeyedLiteral struct{}         `json:"-"`
	XXX_unrecognized     []byte           `json:"-"`
	XXX_sizecache        int32            `json:"-"`
}

func (m *AtlasCalibrationStatus) Reset()         { *m = AtlasCalibrationStatus{} }
func (m *AtlasCalibrationStatus) String() string { return proto.CompactTextString(m) }
func (*AtlasCalibrationStatus) ProtoMessage()    {}
func (*AtlasCalibrationStatus) Descriptor() ([]byte, []int) {
	return fileDescriptor_822d05f6175684bb, []int{3}
}

func (m *AtlasCalibrationStatus) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_AtlasCalibrationStatus.Unmarshal(m, b)
}
func (m *AtlasCalibrationStatus) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_AtlasCalibrationStatus.Marshal(b, m, deterministic)
}
func (m *AtlasCalibrationStatus) XXX_Merge(src proto.Message) {
	xxx_messageInfo_AtlasCalibrationStatus.Merge(m, src)
}
func (m *AtlasCalibrationStatus) XXX_Size() int {
	return xxx_messageInfo_AtlasCalibrationStatus.Size(m)
}
func (m *AtlasCalibrationStatus) XXX_DiscardUnknown() {
	xxx_messageInfo_AtlasCalibrationStatus.DiscardUnknown(m)
}

var xxx_messageInfo_AtlasCalibrationStatus proto.InternalMessageInfo

func (m *AtlasCalibrationStatus) GetType() SensorType {
	if m != nil {
		return m.Type
	}
	return SensorType_SENSOR_NONE
}

func (m *AtlasCalibrationStatus) GetTime() uint32 {
	if m != nil {
		return m.Time
	}
	return 0
}

func (m *AtlasCalibrationStatus) GetTemp() TempCalibrations {
	if m != nil {
		return m.Temp
	}
	return TempCalibrations_TEMP_NONE
}

func (m *AtlasCalibrationStatus) GetDissolvedOxygen() DoCalibrations {
	if m != nil {
		return m.DissolvedOxygen
	}
	return DoCalibrations_DO_NONE
}

func (m *AtlasCalibrationStatus) GetPh() PhCalibrations {
	if m != nil {
		return m.Ph
	}
	return PhCalibrations_PH_NONE
}

func (m *AtlasCalibrationStatus) GetEc() EcCalibrations {
	if m != nil {
		return m.Ec
	}
	return EcCalibrations_EC_NONE
}

func (m *AtlasCalibrationStatus) GetOrp() OrpCalibrations {
	if m != nil {
		return m.Orp
	}
	return OrpCalibrations_ORP_NONE
}

type TwoWireReply struct {
	Data                 []byte   `protobuf:"bytes,1,opt,name=data,proto3" json:"data,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *TwoWireReply) Reset()         { *m = TwoWireReply{} }
func (m *TwoWireReply) String() string { return proto.CompactTextString(m) }
func (*TwoWireReply) ProtoMessage()    {}
func (*TwoWireReply) Descriptor() ([]byte, []int) {
	return fileDescriptor_822d05f6175684bb, []int{4}
}

func (m *TwoWireReply) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_TwoWireReply.Unmarshal(m, b)
}
func (m *TwoWireReply) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_TwoWireReply.Marshal(b, m, deterministic)
}
func (m *TwoWireReply) XXX_Merge(src proto.Message) {
	xxx_messageInfo_TwoWireReply.Merge(m, src)
}
func (m *TwoWireReply) XXX_Size() int {
	return xxx_messageInfo_TwoWireReply.Size(m)
}
func (m *TwoWireReply) XXX_DiscardUnknown() {
	xxx_messageInfo_TwoWireReply.DiscardUnknown(m)
}

var xxx_messageInfo_TwoWireReply proto.InternalMessageInfo

func (m *TwoWireReply) GetData() []byte {
	if m != nil {
		return m.Data
	}
	return nil
}

type Error struct {
	Type                 ErrorType `protobuf:"varint,1,opt,name=type,proto3,enum=fk_atlas.ErrorType" json:"type,omitempty"`
	Message              string    `protobuf:"bytes,2,opt,name=message,proto3" json:"message,omitempty"`
	XXX_NoUnkeyedLiteral struct{}  `json:"-"`
	XXX_unrecognized     []byte    `json:"-"`
	XXX_sizecache        int32     `json:"-"`
}

func (m *Error) Reset()         { *m = Error{} }
func (m *Error) String() string { return proto.CompactTextString(m) }
func (*Error) ProtoMessage()    {}
func (*Error) Descriptor() ([]byte, []int) {
	return fileDescriptor_822d05f6175684bb, []int{5}
}

func (m *Error) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Error.Unmarshal(m, b)
}
func (m *Error) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Error.Marshal(b, m, deterministic)
}
func (m *Error) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Error.Merge(m, src)
}
func (m *Error) XXX_Size() int {
	return xxx_messageInfo_Error.Size(m)
}
func (m *Error) XXX_DiscardUnknown() {
	xxx_messageInfo_Error.DiscardUnknown(m)
}

var xxx_messageInfo_Error proto.InternalMessageInfo

func (m *Error) GetType() ErrorType {
	if m != nil {
		return m.Type
	}
	return ErrorType_NONE
}

func (m *Error) GetMessage() string {
	if m != nil {
		return m.Message
	}
	return ""
}

type WireAtlasReply struct {
	Type                 ReplyType               `protobuf:"varint,1,opt,name=type,proto3,enum=fk_atlas.ReplyType" json:"type,omitempty"`
	Error                *Error                  `protobuf:"bytes,2,opt,name=error,proto3" json:"error,omitempty"`
	Calibration          *AtlasCalibrationStatus `protobuf:"bytes,3,opt,name=calibration,proto3" json:"calibration,omitempty"`
	Wire                 *TwoWireReply           `protobuf:"bytes,4,opt,name=wire,proto3" json:"wire,omitempty"`
	XXX_NoUnkeyedLiteral struct{}                `json:"-"`
	XXX_unrecognized     []byte                  `json:"-"`
	XXX_sizecache        int32                   `json:"-"`
}

func (m *WireAtlasReply) Reset()         { *m = WireAtlasReply{} }
func (m *WireAtlasReply) String() string { return proto.CompactTextString(m) }
func (*WireAtlasReply) ProtoMessage()    {}
func (*WireAtlasReply) Descriptor() ([]byte, []int) {
	return fileDescriptor_822d05f6175684bb, []int{6}
}

func (m *WireAtlasReply) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_WireAtlasReply.Unmarshal(m, b)
}
func (m *WireAtlasReply) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_WireAtlasReply.Marshal(b, m, deterministic)
}
func (m *WireAtlasReply) XXX_Merge(src proto.Message) {
	xxx_messageInfo_WireAtlasReply.Merge(m, src)
}
func (m *WireAtlasReply) XXX_Size() int {
	return xxx_messageInfo_WireAtlasReply.Size(m)
}
func (m *WireAtlasReply) XXX_DiscardUnknown() {
	xxx_messageInfo_WireAtlasReply.DiscardUnknown(m)
}

var xxx_messageInfo_WireAtlasReply proto.InternalMessageInfo

func (m *WireAtlasReply) GetType() ReplyType {
	if m != nil {
		return m.Type
	}
	return ReplyType_REPLY_NONE
}

func (m *WireAtlasReply) GetError() *Error {
	if m != nil {
		return m.Error
	}
	return nil
}

func (m *WireAtlasReply) GetCalibration() *AtlasCalibrationStatus {
	if m != nil {
		return m.Calibration
	}
	return nil
}

func (m *WireAtlasReply) GetWire() *TwoWireReply {
	if m != nil {
		return m.Wire
	}
	return nil
}

func init() {
	proto.RegisterEnum("fk_atlas.SensorType", SensorType_name, SensorType_value)
	proto.RegisterEnum("fk_atlas.QueryType", QueryType_name, QueryType_value)
	proto.RegisterEnum("fk_atlas.CalibrationOperation", CalibrationOperation_name, CalibrationOperation_value)
	proto.RegisterEnum("fk_atlas.TempCalibrations", TempCalibrations_name, TempCalibrations_value)
	proto.RegisterEnum("fk_atlas.DoCalibrations", DoCalibrations_name, DoCalibrations_value)
	proto.RegisterEnum("fk_atlas.PhCalibrations", PhCalibrations_name, PhCalibrations_value)
	proto.RegisterEnum("fk_atlas.EcCalibrations", EcCalibrations_name, EcCalibrations_value)
	proto.RegisterEnum("fk_atlas.OrpCalibrations", OrpCalibrations_name, OrpCalibrations_value)
	proto.RegisterEnum("fk_atlas.ReplyType", ReplyType_name, ReplyType_value)
	proto.RegisterEnum("fk_atlas.ErrorType", ErrorType_name, ErrorType_value)
	proto.RegisterType((*AtlasCalibrationCommand)(nil), "fk_atlas.AtlasCalibrationCommand")
	proto.RegisterType((*TwoWireQuery)(nil), "fk_atlas.TwoWireQuery")
	proto.RegisterType((*WireAtlasQuery)(nil), "fk_atlas.WireAtlasQuery")
	proto.RegisterType((*AtlasCalibrationStatus)(nil), "fk_atlas.AtlasCalibrationStatus")
	proto.RegisterType((*TwoWireReply)(nil), "fk_atlas.TwoWireReply")
	proto.RegisterType((*Error)(nil), "fk_atlas.Error")
	proto.RegisterType((*WireAtlasReply)(nil), "fk_atlas.WireAtlasReply")
}

func init() { proto.RegisterFile("fk-atlas.proto", fileDescriptor_822d05f6175684bb) }

var fileDescriptor_822d05f6175684bb = []byte{
	// 835 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x9c, 0x55, 0x5f, 0x6f, 0xe3, 0x44,
	0x10, 0xc7, 0x8e, 0xd3, 0x34, 0x93, 0x36, 0xd9, 0xdb, 0x96, 0x9e, 0x01, 0x09, 0x95, 0x48, 0x88,
	0xca, 0x88, 0x22, 0x95, 0x57, 0x78, 0x70, 0xed, 0x55, 0x13, 0xe4, 0x64, 0x7d, 0x6b, 0x97, 0xa3,
	0xf0, 0x10, 0xf9, 0x9a, 0xbd, 0x6b, 0xd4, 0xa4, 0xb6, 0x1c, 0xf7, 0x4a, 0xbe, 0x12, 0x5f, 0x85,
	0x17, 0x3e, 0x03, 0x9f, 0x04, 0xed, 0xfa, 0xdf, 0x3a, 0xba, 0x48, 0x55, 0xdf, 0x76, 0x66, 0x7e,
	0xbf, 0x99, 0xd9, 0xd9, 0xdf, 0xd8, 0xd0, 0x7f, 0x7f, 0xff, 0x43, 0x94, 0x2d, 0xa3, 0xf5, 0x79,
	0x92, 0xc6, 0x59, 0x8c, 0xf7, 0xdf, 0xdf, 0xcf, 0xa4, 0x3d, 0xfc, 0x4f, 0x87, 0xd7, 0xb6, 0x38,
	0x39, 0xd1, 0x72, 0xf1, 0x2e, 0x8d, 0xb2, 0x45, 0xfc, 0xe0, 0xc4, 0xab, 0x55, 0xf4, 0x30, 0xc7,
	0x3f, 0x43, 0x37, 0x4e, 0x78, 0xee, 0x33, 0xb5, 0x53, 0xed, 0xac, 0x7f, 0xf1, 0xf5, 0x79, 0xc9,
	0x3c, 0x57, 0x08, 0xb4, 0x44, 0xb1, 0x9a, 0x80, 0xcf, 0xc1, 0xc8, 0xf8, 0x2a, 0x31, 0x75, 0x49,
	0xfc, 0xb2, 0x26, 0x86, 0x7c, 0x95, 0x28, 0xe4, 0x35, 0x93, 0x38, 0x7c, 0x09, 0x83, 0xf9, 0x62,
	0xbd, 0x8e, 0x97, 0x1f, 0xf9, 0x9c, 0xfe, 0xb5, 0xf9, 0xc0, 0x1f, 0xcc, 0x96, 0xa4, 0x9a, 0x35,
	0xd5, 0x8d, 0x1b, 0xc4, 0x6d, 0x02, 0x3e, 0x03, 0x3d, 0xb9, 0x33, 0x8d, 0x6d, 0x9a, 0x7f, 0xd7,
	0xa0, 0xe9, 0xc9, 0x9d, 0x40, 0xf2, 0x5b, 0xb3, 0xbd, 0x8d, 0x24, 0xb7, 0x4d, 0x24, 0xbf, 0xc5,
	0xdf, 0x43, 0x2b, 0x4e, 0x13, 0x73, 0x4f, 0x42, 0xbf, 0xa8, 0xa1, 0x34, 0x6d, 0xde, 0x42, 0xa0,
	0xf0, 0x31, 0xb4, 0x3f, 0x46, 0xcb, 0x47, 0x6e, 0x76, 0x4e, 0xb5, 0x33, 0x9d, 0xe5, 0xc6, 0xd0,
	0x83, 0x83, 0xf0, 0x29, 0x7e, 0xbb, 0x48, 0xf9, 0x9b, 0x47, 0x9e, 0x6e, 0x30, 0x06, 0x23, 0xe5,
	0xd1, 0x5c, 0xce, 0xf4, 0x90, 0xc9, 0xb3, 0x60, 0x3e, 0xa5, 0x8b, 0x8c, 0xcb, 0x79, 0x1d, 0xb2,
	0xdc, 0x10, 0xc8, 0x79, 0x94, 0x45, 0x72, 0x12, 0x07, 0x4c, 0x9e, 0x87, 0x7f, 0x6b, 0xd0, 0x17,
	0xb9, 0xe4, 0xb3, 0xe5, 0x09, 0xbf, 0x03, 0x23, 0xdb, 0x24, 0xbc, 0x78, 0xa4, 0xa3, 0xba, 0x49,
	0x19, 0x0e, 0x37, 0x09, 0x67, 0x12, 0x80, 0x1d, 0xe8, 0xdd, 0xd6, 0x4d, 0xcb, 0x5a, 0xbd, 0x8b,
	0x6f, 0x6a, 0xfc, 0x0e, 0x29, 0x30, 0x95, 0x85, 0x2d, 0x30, 0x9e, 0x16, 0x29, 0x97, 0x4d, 0xf5,
	0x2e, 0x4e, 0x94, 0x97, 0x55, 0x2e, 0xc9, 0x24, 0x66, 0xf8, 0x8f, 0x0e, 0x27, 0xdb, 0x49, 0x83,
	0x2c, 0xca, 0x1e, 0xd7, 0xf8, 0xac, 0xd1, 0xf4, 0x71, 0x9d, 0x26, 0xe0, 0x0f, 0xeb, 0x38, 0x55,
	0xba, 0xc6, 0x60, 0x64, 0x8b, 0x55, 0x39, 0x1a, 0x79, 0xae, 0xe4, 0xd5, 0x7a, 0xb9, 0xbc, 0x8c,
	0x97, 0xc9, 0xab, 0xfd, 0x6c, 0x79, 0xed, 0x3d, 0x5f, 0x5e, 0x9d, 0xe7, 0xc8, 0x6b, 0x38, 0xac,
	0x84, 0xc4, 0x78, 0xb2, 0xdc, 0x54, 0xf2, 0xd0, 0x14, 0x79, 0xfc, 0x0a, 0x6d, 0x92, 0xa6, 0x71,
	0xba, 0x5b, 0x14, 0x32, 0xac, 0x8c, 0xd7, 0x84, 0xce, 0x8a, 0xaf, 0xd7, 0xd1, 0x87, 0x7c, 0xc2,
	0x5d, 0x56, 0x9a, 0xc3, 0x7f, 0x55, 0xa9, 0xe5, 0x25, 0x77, 0x66, 0x95, 0x61, 0x25, 0xeb, 0xb7,
	0xd0, 0xe6, 0xa2, 0x50, 0x21, 0xb2, 0xc1, 0x56, 0x7d, 0x96, 0x47, 0xf1, 0x65, 0x53, 0x91, 0xb9,
	0xa6, 0x4e, 0x77, 0x2b, 0x32, 0x17, 0xcf, 0xa7, 0x05, 0x69, 0xec, 0x10, 0xa4, 0x6c, 0x2d, 0x17,
	0xa4, 0x75, 0x0f, 0x50, 0xeb, 0x0b, 0x0f, 0xa0, 0x17, 0x90, 0x69, 0x40, 0xd9, 0x6c, 0x4a, 0xa7,
	0x04, 0x7d, 0x86, 0x0f, 0xa1, 0x5b, 0x38, 0xfc, 0x11, 0xd2, 0x94, 0x78, 0x48, 0x26, 0x3e, 0xd2,
	0x71, 0x1f, 0xa0, 0x70, 0x50, 0xe6, 0xa3, 0x96, 0x82, 0x77, 0x29, 0x32, 0x14, 0x93, 0x38, 0xa8,
	0x6d, 0x7d, 0x05, 0xdd, 0x6a, 0x03, 0x05, 0xf5, 0xcd, 0x35, 0x61, 0x37, 0x45, 0x29, 0x2b, 0x81,
	0xe3, 0x4f, 0x7d, 0x43, 0xf1, 0x31, 0x20, 0xc7, 0xf6, 0xc6, 0x97, 0xcc, 0x0e, 0xc7, 0x74, 0x5a,
	0x36, 0x76, 0x02, 0x58, 0xf5, 0x06, 0xa1, 0x1d, 0x5e, 0x07, 0x48, 0xc3, 0x9f, 0xc3, 0x2b, 0xd5,
	0xef, 0x78, 0xc4, 0x66, 0x48, 0xc7, 0x47, 0x30, 0x68, 0xc0, 0x49, 0x88, 0x5a, 0xd6, 0x05, 0xa0,
	0xed, 0xed, 0x10, 0x1d, 0x8b, 0xab, 0x95, 0x65, 0x06, 0xd0, 0x93, 0x66, 0x30, 0x9e, 0x5e, 0x79,
	0x04, 0x69, 0xd6, 0x2f, 0xd0, 0x6f, 0xae, 0x05, 0xee, 0x41, 0xc7, 0xa5, 0x25, 0xfe, 0x15, 0x1c,
	0xba, 0x74, 0x66, 0x87, 0x13, 0x1a, 0xf8, 0x23, 0xc2, 0x08, 0xd2, 0x8a, 0xf8, 0x1f, 0x84, 0x51,
	0xa4, 0x5b, 0x04, 0xfa, 0xcd, 0xf5, 0x10, 0x61, 0x7f, 0x54, 0xd2, 0x01, 0xf6, 0xfc, 0xd1, 0xcc,
	0xa3, 0x6f, 0x91, 0x26, 0x3a, 0xf1, 0x47, 0xb3, 0xc9, 0xd8, 0x75, 0x3d, 0x82, 0xf4, 0x02, 0x37,
	0x1a, 0x5f, 0x8d, 0x90, 0x61, 0xfd, 0x09, 0xfd, 0xe6, 0xee, 0x88, 0x30, 0x71, 0x94, 0x34, 0xc4,
	0x99, 0xb9, 0xec, 0x26, 0x4f, 0x43, 0x9c, 0xb2, 0x7f, 0x5d, 0x5c, 0x48, 0x84, 0xae, 0x6d, 0x4f,
	0x96, 0x31, 0x30, 0x82, 0x83, 0xd2, 0x21, 0x93, 0xef, 0x5b, 0x3f, 0xc2, 0x60, 0x6b, 0xdb, 0xf0,
	0x01, 0xec, 0x53, 0x56, 0x0d, 0xa5, 0x0f, 0x20, 0xac, 0x6a, 0x26, 0xbf, 0x41, 0xb7, 0x52, 0xbb,
	0x08, 0x32, 0xe2, 0x7b, 0x37, 0xca, 0x04, 0x73, 0x9b, 0x91, 0x50, 0x36, 0x54, 0x39, 0x08, 0x63,
	0x54, 0xbc, 0xcd, 0x6b, 0x38, 0xca, 0x1d, 0x76, 0xe8, 0xd9, 0xc1, 0xcc, 0xa1, 0x93, 0x89, 0x3d,
	0x75, 0xe5, 0xfb, 0x74, 0xab, 0xdd, 0xc4, 0xfb, 0x60, 0x14, 0x19, 0x7b, 0xd0, 0xb9, 0x22, 0x53,
	0xc2, 0x6c, 0x0f, 0x69, 0xa2, 0xdc, 0xf5, 0x94, 0xfc, 0xee, 0x13, 0x27, 0x24, 0x2e, 0xd2, 0xdf,
	0xed, 0xc9, 0x3f, 0xfa, 0x4f, 0xff, 0x07, 0x00, 0x00, 0xff, 0xff, 0xd3, 0xbc, 0xab, 0x8f, 0xe3,
	0x07, 0x00, 0x00,
}
