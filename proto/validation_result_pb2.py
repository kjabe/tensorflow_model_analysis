# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow_model_analysis/proto/validation_result.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow_model_analysis.proto import config_pb2 as tensorflow__model__analysis_dot_proto_dot_config__pb2
from tensorflow_model_analysis.proto import metrics_for_slice_pb2 as tensorflow__model__analysis_dot_proto_dot_metrics__for__slice__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow_model_analysis/proto/validation_result.proto',
  package='tensorflow_model_analysis',
  syntax='proto3',
  serialized_pb=_b('\n7tensorflow_model_analysis/proto/validation_result.proto\x12\x19tensorflow_model_analysis\x1a,tensorflow_model_analysis/proto/config.proto\x1a\x37tensorflow_model_analysis/proto/metrics_for_slice.proto\"\xe2\x01\n\x11ValidationFailure\x12\x38\n\nmetric_key\x18\x01 \x01(\x0b\x32$.tensorflow_model_analysis.MetricKey\x12\x44\n\x10metric_threshold\x18\x02 \x01(\x0b\x32*.tensorflow_model_analysis.MetricThreshold\x12<\n\x0cmetric_value\x18\x03 \x01(\x0b\x32&.tensorflow_model_analysis.MetricValue\x12\x0f\n\x07message\x18\x04 \x01(\t\"\xce\x01\n\x0eSlicingDetails\x12>\n\x0cslicing_spec\x18\x01 \x01(\x0b\x32&.tensorflow_model_analysis.SlicingSpecH\x00\x12I\n\x12\x63ross_slicing_spec\x18\x03 \x01(\x0b\x32+.tensorflow_model_analysis.CrossSlicingSpecH\x00\x12\x1b\n\x13num_matching_slices\x18\x02 \x01(\x05\x42\x14\n\x12slicing_spec_oneof\"W\n\x11ValidationDetails\x12\x42\n\x0fslicing_details\x18\x01 \x03(\x0b\x32).tensorflow_model_analysis.SlicingDetails\"\xed\x01\n\x19MetricsValidationForSlice\x12\x38\n\tslice_key\x18\x02 \x01(\x0b\x32#.tensorflow_model_analysis.SliceKeyH\x00\x12\x43\n\x0f\x63ross_slice_key\x18\x04 \x01(\x0b\x32(.tensorflow_model_analysis.CrossSliceKeyH\x00\x12>\n\x08\x66\x61ilures\x18\x03 \x03(\x0b\x32,.tensorflow_model_analysis.ValidationFailureB\x11\n\x0fslice_key_oneof\"\x8c\x03\n\x10ValidationResult\x12\x15\n\rvalidation_ok\x18\x01 \x01(\x08\x12\x1a\n\x12missing_thresholds\x18\x06 \x01(\x08\x12Z\n\x1cmetric_validations_per_slice\x18\x02 \x03(\x0b\x32\x34.tensorflow_model_analysis.MetricsValidationForSlice\x12>\n\x0emissing_slices\x18\x03 \x03(\x0b\x32&.tensorflow_model_analysis.SlicingSpec\x12I\n\x14missing_cross_slices\x18\x05 \x03(\x0b\x32+.tensorflow_model_analysis.CrossSlicingSpec\x12H\n\x12validation_details\x18\x04 \x01(\x0b\x32,.tensorflow_model_analysis.ValidationDetails\x12\x14\n\x0crubber_stamp\x18\x07 \x01(\x08\x62\x06proto3')
  ,
  dependencies=[tensorflow__model__analysis_dot_proto_dot_config__pb2.DESCRIPTOR,tensorflow__model__analysis_dot_proto_dot_metrics__for__slice__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_VALIDATIONFAILURE = _descriptor.Descriptor(
  name='ValidationFailure',
  full_name='tensorflow_model_analysis.ValidationFailure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metric_key', full_name='tensorflow_model_analysis.ValidationFailure.metric_key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metric_threshold', full_name='tensorflow_model_analysis.ValidationFailure.metric_threshold', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metric_value', full_name='tensorflow_model_analysis.ValidationFailure.metric_value', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='tensorflow_model_analysis.ValidationFailure.message', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=190,
  serialized_end=416,
)


_SLICINGDETAILS = _descriptor.Descriptor(
  name='SlicingDetails',
  full_name='tensorflow_model_analysis.SlicingDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='slicing_spec', full_name='tensorflow_model_analysis.SlicingDetails.slicing_spec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cross_slicing_spec', full_name='tensorflow_model_analysis.SlicingDetails.cross_slicing_spec', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_matching_slices', full_name='tensorflow_model_analysis.SlicingDetails.num_matching_slices', index=2,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
    _descriptor.OneofDescriptor(
      name='slicing_spec_oneof', full_name='tensorflow_model_analysis.SlicingDetails.slicing_spec_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=419,
  serialized_end=625,
)


_VALIDATIONDETAILS = _descriptor.Descriptor(
  name='ValidationDetails',
  full_name='tensorflow_model_analysis.ValidationDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='slicing_details', full_name='tensorflow_model_analysis.ValidationDetails.slicing_details', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=627,
  serialized_end=714,
)


_METRICSVALIDATIONFORSLICE = _descriptor.Descriptor(
  name='MetricsValidationForSlice',
  full_name='tensorflow_model_analysis.MetricsValidationForSlice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='slice_key', full_name='tensorflow_model_analysis.MetricsValidationForSlice.slice_key', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cross_slice_key', full_name='tensorflow_model_analysis.MetricsValidationForSlice.cross_slice_key', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='failures', full_name='tensorflow_model_analysis.MetricsValidationForSlice.failures', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
    _descriptor.OneofDescriptor(
      name='slice_key_oneof', full_name='tensorflow_model_analysis.MetricsValidationForSlice.slice_key_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=717,
  serialized_end=954,
)


_VALIDATIONRESULT = _descriptor.Descriptor(
  name='ValidationResult',
  full_name='tensorflow_model_analysis.ValidationResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='validation_ok', full_name='tensorflow_model_analysis.ValidationResult.validation_ok', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='missing_thresholds', full_name='tensorflow_model_analysis.ValidationResult.missing_thresholds', index=1,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metric_validations_per_slice', full_name='tensorflow_model_analysis.ValidationResult.metric_validations_per_slice', index=2,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='missing_slices', full_name='tensorflow_model_analysis.ValidationResult.missing_slices', index=3,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='missing_cross_slices', full_name='tensorflow_model_analysis.ValidationResult.missing_cross_slices', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='validation_details', full_name='tensorflow_model_analysis.ValidationResult.validation_details', index=5,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rubber_stamp', full_name='tensorflow_model_analysis.ValidationResult.rubber_stamp', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=957,
  serialized_end=1353,
)

_VALIDATIONFAILURE.fields_by_name['metric_key'].message_type = tensorflow__model__analysis_dot_proto_dot_metrics__for__slice__pb2._METRICKEY
_VALIDATIONFAILURE.fields_by_name['metric_threshold'].message_type = tensorflow__model__analysis_dot_proto_dot_config__pb2._METRICTHRESHOLD
_VALIDATIONFAILURE.fields_by_name['metric_value'].message_type = tensorflow__model__analysis_dot_proto_dot_metrics__for__slice__pb2._METRICVALUE
_SLICINGDETAILS.fields_by_name['slicing_spec'].message_type = tensorflow__model__analysis_dot_proto_dot_config__pb2._SLICINGSPEC
_SLICINGDETAILS.fields_by_name['cross_slicing_spec'].message_type = tensorflow__model__analysis_dot_proto_dot_config__pb2._CROSSSLICINGSPEC
_SLICINGDETAILS.oneofs_by_name['slicing_spec_oneof'].fields.append(
  _SLICINGDETAILS.fields_by_name['slicing_spec'])
_SLICINGDETAILS.fields_by_name['slicing_spec'].containing_oneof = _SLICINGDETAILS.oneofs_by_name['slicing_spec_oneof']
_SLICINGDETAILS.oneofs_by_name['slicing_spec_oneof'].fields.append(
  _SLICINGDETAILS.fields_by_name['cross_slicing_spec'])
_SLICINGDETAILS.fields_by_name['cross_slicing_spec'].containing_oneof = _SLICINGDETAILS.oneofs_by_name['slicing_spec_oneof']
_VALIDATIONDETAILS.fields_by_name['slicing_details'].message_type = _SLICINGDETAILS
_METRICSVALIDATIONFORSLICE.fields_by_name['slice_key'].message_type = tensorflow__model__analysis_dot_proto_dot_metrics__for__slice__pb2._SLICEKEY
_METRICSVALIDATIONFORSLICE.fields_by_name['cross_slice_key'].message_type = tensorflow__model__analysis_dot_proto_dot_metrics__for__slice__pb2._CROSSSLICEKEY
_METRICSVALIDATIONFORSLICE.fields_by_name['failures'].message_type = _VALIDATIONFAILURE
_METRICSVALIDATIONFORSLICE.oneofs_by_name['slice_key_oneof'].fields.append(
  _METRICSVALIDATIONFORSLICE.fields_by_name['slice_key'])
_METRICSVALIDATIONFORSLICE.fields_by_name['slice_key'].containing_oneof = _METRICSVALIDATIONFORSLICE.oneofs_by_name['slice_key_oneof']
_METRICSVALIDATIONFORSLICE.oneofs_by_name['slice_key_oneof'].fields.append(
  _METRICSVALIDATIONFORSLICE.fields_by_name['cross_slice_key'])
_METRICSVALIDATIONFORSLICE.fields_by_name['cross_slice_key'].containing_oneof = _METRICSVALIDATIONFORSLICE.oneofs_by_name['slice_key_oneof']
_VALIDATIONRESULT.fields_by_name['metric_validations_per_slice'].message_type = _METRICSVALIDATIONFORSLICE
_VALIDATIONRESULT.fields_by_name['missing_slices'].message_type = tensorflow__model__analysis_dot_proto_dot_config__pb2._SLICINGSPEC
_VALIDATIONRESULT.fields_by_name['missing_cross_slices'].message_type = tensorflow__model__analysis_dot_proto_dot_config__pb2._CROSSSLICINGSPEC
_VALIDATIONRESULT.fields_by_name['validation_details'].message_type = _VALIDATIONDETAILS
DESCRIPTOR.message_types_by_name['ValidationFailure'] = _VALIDATIONFAILURE
DESCRIPTOR.message_types_by_name['SlicingDetails'] = _SLICINGDETAILS
DESCRIPTOR.message_types_by_name['ValidationDetails'] = _VALIDATIONDETAILS
DESCRIPTOR.message_types_by_name['MetricsValidationForSlice'] = _METRICSVALIDATIONFORSLICE
DESCRIPTOR.message_types_by_name['ValidationResult'] = _VALIDATIONRESULT

ValidationFailure = _reflection.GeneratedProtocolMessageType('ValidationFailure', (_message.Message,), dict(
  DESCRIPTOR = _VALIDATIONFAILURE,
  __module__ = 'tensorflow_model_analysis.proto.validation_result_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow_model_analysis.ValidationFailure)
  ))
_sym_db.RegisterMessage(ValidationFailure)

SlicingDetails = _reflection.GeneratedProtocolMessageType('SlicingDetails', (_message.Message,), dict(
  DESCRIPTOR = _SLICINGDETAILS,
  __module__ = 'tensorflow_model_analysis.proto.validation_result_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow_model_analysis.SlicingDetails)
  ))
_sym_db.RegisterMessage(SlicingDetails)

ValidationDetails = _reflection.GeneratedProtocolMessageType('ValidationDetails', (_message.Message,), dict(
  DESCRIPTOR = _VALIDATIONDETAILS,
  __module__ = 'tensorflow_model_analysis.proto.validation_result_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow_model_analysis.ValidationDetails)
  ))
_sym_db.RegisterMessage(ValidationDetails)

MetricsValidationForSlice = _reflection.GeneratedProtocolMessageType('MetricsValidationForSlice', (_message.Message,), dict(
  DESCRIPTOR = _METRICSVALIDATIONFORSLICE,
  __module__ = 'tensorflow_model_analysis.proto.validation_result_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow_model_analysis.MetricsValidationForSlice)
  ))
_sym_db.RegisterMessage(MetricsValidationForSlice)

ValidationResult = _reflection.GeneratedProtocolMessageType('ValidationResult', (_message.Message,), dict(
  DESCRIPTOR = _VALIDATIONRESULT,
  __module__ = 'tensorflow_model_analysis.proto.validation_result_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow_model_analysis.ValidationResult)
  ))
_sym_db.RegisterMessage(ValidationResult)


# @@protoc_insertion_point(module_scope)