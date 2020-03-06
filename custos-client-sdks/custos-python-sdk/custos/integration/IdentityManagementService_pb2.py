# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IdentityManagementService.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
import custos.core.IdentityService_pb2 as IdentityService__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
import custos.core.CredentialStoreService_pb2 as CredentialStoreService__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='IdentityManagementService.proto',
  package='org.apache.custos.identity.management.service',
  syntax='proto3',
  serialized_options=b'P\001',
  serialized_pb=b'\n\x1fIdentityManagementService.proto\x12-org.apache.custos.identity.management.service\x1a\x1cgoogle/api/annotations.proto\x1a\x15IdentityService.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x19google/protobuf/any.proto\x1a\x1c\x43redentialStoreService.proto\"\x9e\x01\n\x14\x41uthorizationRequest\x12\x11\n\ttenant_id\x18\x01 \x01(\x03\x12\x11\n\tclient_id\x18\x02 \x01(\t\x12\x15\n\rclient_secret\x18\x03 \x01(\t\x12\x14\n\x0credirect_uri\x18\x04 \x01(\t\x12\x15\n\rresponse_type\x18\x05 \x01(\t\x12\r\n\x05scope\x18\x06 \x01(\t\x12\r\n\x05state\x18\x07 \x01(\t\")\n\x15\x41uthorizationResponse\x12\x10\n\x08loginURI\x18\x01 \x01(\t\"x\n\x15GetCredentialsRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12L\n\x0b\x63redentials\x18\x02 \x01(\x0b\x32\x37.org.apache.custos.credential.store.service.Credentials2\xa5\x0b\n\x19IdentityManagementService\x12\xaa\x01\n\x0c\x61uthenticate\x12\x39.org.apache.custos.identity.service.AuthenticationRequest\x1a-.org.apache.custos.identity.service.AuthToken\"0\x82\xd3\xe4\x93\x02*\"(/identity-management/v1.0.0/authenticate\x12\xb5\x01\n\x0fisAuthenticated\x12-.org.apache.custos.identity.service.AuthToken\x1a:.org.apache.custos.identity.service.IsAuthenticateResponse\"7\x82\xd3\xe4\x93\x02\x31\x12//identity-management/v1.0.0/authenticate/status\x12\x8c\x01\n\x07getUser\x12-.org.apache.custos.identity.service.AuthToken\x1a(.org.apache.custos.identity.service.User\"(\x82\xd3\xe4\x93\x02\"\x12 /identity-management/v1.0.0/user\x12\xd3\x01\n*getUserManagementServiceAccountAccessToken\x12\x43.org.apache.custos.identity.service.GetUserManagementSATokenRequest\x1a-.org.apache.custos.identity.service.AuthToken\"1\x82\xd3\xe4\x93\x02+\x12)/identity-management/v1.0.0/account/token\x12\xc5\x01\n\tauthorize\x12\x43.org.apache.custos.identity.management.service.AuthorizationRequest\x1a\x44.org.apache.custos.identity.management.service.AuthorizationResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/identity-management/v1.0.0/authorize\x12\x80\x01\n\x05token\x12\x33.org.apache.custos.identity.service.GetTokenRequest\x1a\x17.google.protobuf.Struct\")\x82\xd3\xe4\x93\x02#\"!/identity-management/v1.0.0/token\x12\xc0\x01\n\x0egetCredentials\x12\x44.org.apache.custos.identity.management.service.GetCredentialsRequest\x1a\x37.org.apache.custos.credential.store.service.Credentials\"/\x82\xd3\xe4\x93\x02)\x12\'/identity-management/v1.0.0/credentials\x12\xaf\x01\n\x14getOIDCConfiguration\x12\x38.org.apache.custos.identity.service.GetOIDCConfiguration\x1a\x17.google.protobuf.Struct\"D\x82\xd3\xe4\x93\x02>\x12</identity-management/v1.0.0/.well-known/openid-configurationB\x02P\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,IdentityService__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,CredentialStoreService__pb2.DESCRIPTOR,])




_AUTHORIZATIONREQUEST = _descriptor.Descriptor(
  name='AuthorizationRequest',
  full_name='org.apache.custos.identity.management.service.AuthorizationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tenant_id', full_name='org.apache.custos.identity.management.service.AuthorizationRequest.tenant_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='org.apache.custos.identity.management.service.AuthorizationRequest.client_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_secret', full_name='org.apache.custos.identity.management.service.AuthorizationRequest.client_secret', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='redirect_uri', full_name='org.apache.custos.identity.management.service.AuthorizationRequest.redirect_uri', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response_type', full_name='org.apache.custos.identity.management.service.AuthorizationRequest.response_type', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scope', full_name='org.apache.custos.identity.management.service.AuthorizationRequest.scope', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='org.apache.custos.identity.management.service.AuthorizationRequest.state', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=223,
  serialized_end=381,
)


_AUTHORIZATIONRESPONSE = _descriptor.Descriptor(
  name='AuthorizationResponse',
  full_name='org.apache.custos.identity.management.service.AuthorizationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='loginURI', full_name='org.apache.custos.identity.management.service.AuthorizationResponse.loginURI', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=383,
  serialized_end=424,
)


_GETCREDENTIALSREQUEST = _descriptor.Descriptor(
  name='GetCredentialsRequest',
  full_name='org.apache.custos.identity.management.service.GetCredentialsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='org.apache.custos.identity.management.service.GetCredentialsRequest.client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='credentials', full_name='org.apache.custos.identity.management.service.GetCredentialsRequest.credentials', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=426,
  serialized_end=546,
)

_GETCREDENTIALSREQUEST.fields_by_name['credentials'].message_type = CredentialStoreService__pb2._CREDENTIALS
DESCRIPTOR.message_types_by_name['AuthorizationRequest'] = _AUTHORIZATIONREQUEST
DESCRIPTOR.message_types_by_name['AuthorizationResponse'] = _AUTHORIZATIONRESPONSE
DESCRIPTOR.message_types_by_name['GetCredentialsRequest'] = _GETCREDENTIALSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuthorizationRequest = _reflection.GeneratedProtocolMessageType('AuthorizationRequest', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORIZATIONREQUEST,
  '__module__' : 'IdentityManagementService_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.custos.identity.management.service.AuthorizationRequest)
  })
_sym_db.RegisterMessage(AuthorizationRequest)

AuthorizationResponse = _reflection.GeneratedProtocolMessageType('AuthorizationResponse', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORIZATIONRESPONSE,
  '__module__' : 'IdentityManagementService_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.custos.identity.management.service.AuthorizationResponse)
  })
_sym_db.RegisterMessage(AuthorizationResponse)

GetCredentialsRequest = _reflection.GeneratedProtocolMessageType('GetCredentialsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCREDENTIALSREQUEST,
  '__module__' : 'IdentityManagementService_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.custos.identity.management.service.GetCredentialsRequest)
  })
_sym_db.RegisterMessage(GetCredentialsRequest)


DESCRIPTOR._options = None

_IDENTITYMANAGEMENTSERVICE = _descriptor.ServiceDescriptor(
  name='IdentityManagementService',
  full_name='org.apache.custos.identity.management.service.IdentityManagementService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=549,
  serialized_end=1994,
  methods=[
  _descriptor.MethodDescriptor(
    name='authenticate',
    full_name='org.apache.custos.identity.management.service.IdentityManagementService.authenticate',
    index=0,
    containing_service=None,
    input_type=IdentityService__pb2._AUTHENTICATIONREQUEST,
    output_type=IdentityService__pb2._AUTHTOKEN,
    serialized_options=b'\202\323\344\223\002*\"(/identity-management/v1.0.0/authenticate',
  ),
  _descriptor.MethodDescriptor(
    name='isAuthenticated',
    full_name='org.apache.custos.identity.management.service.IdentityManagementService.isAuthenticated',
    index=1,
    containing_service=None,
    input_type=IdentityService__pb2._AUTHTOKEN,
    output_type=IdentityService__pb2._ISAUTHENTICATERESPONSE,
    serialized_options=b'\202\323\344\223\0021\022//identity-management/v1.0.0/authenticate/status',
  ),
  _descriptor.MethodDescriptor(
    name='getUser',
    full_name='org.apache.custos.identity.management.service.IdentityManagementService.getUser',
    index=2,
    containing_service=None,
    input_type=IdentityService__pb2._AUTHTOKEN,
    output_type=IdentityService__pb2._USER,
    serialized_options=b'\202\323\344\223\002\"\022 /identity-management/v1.0.0/user',
  ),
  _descriptor.MethodDescriptor(
    name='getUserManagementServiceAccountAccessToken',
    full_name='org.apache.custos.identity.management.service.IdentityManagementService.getUserManagementServiceAccountAccessToken',
    index=3,
    containing_service=None,
    input_type=IdentityService__pb2._GETUSERMANAGEMENTSATOKENREQUEST,
    output_type=IdentityService__pb2._AUTHTOKEN,
    serialized_options=b'\202\323\344\223\002+\022)/identity-management/v1.0.0/account/token',
  ),
  _descriptor.MethodDescriptor(
    name='authorize',
    full_name='org.apache.custos.identity.management.service.IdentityManagementService.authorize',
    index=4,
    containing_service=None,
    input_type=_AUTHORIZATIONREQUEST,
    output_type=_AUTHORIZATIONRESPONSE,
    serialized_options=b'\202\323\344\223\002\'\022%/identity-management/v1.0.0/authorize',
  ),
  _descriptor.MethodDescriptor(
    name='token',
    full_name='org.apache.custos.identity.management.service.IdentityManagementService.token',
    index=5,
    containing_service=None,
    input_type=IdentityService__pb2._GETTOKENREQUEST,
    output_type=google_dot_protobuf_dot_struct__pb2._STRUCT,
    serialized_options=b'\202\323\344\223\002#\"!/identity-management/v1.0.0/token',
  ),
  _descriptor.MethodDescriptor(
    name='getCredentials',
    full_name='org.apache.custos.identity.management.service.IdentityManagementService.getCredentials',
    index=6,
    containing_service=None,
    input_type=_GETCREDENTIALSREQUEST,
    output_type=CredentialStoreService__pb2._CREDENTIALS,
    serialized_options=b'\202\323\344\223\002)\022\'/identity-management/v1.0.0/credentials',
  ),
  _descriptor.MethodDescriptor(
    name='getOIDCConfiguration',
    full_name='org.apache.custos.identity.management.service.IdentityManagementService.getOIDCConfiguration',
    index=7,
    containing_service=None,
    input_type=IdentityService__pb2._GETOIDCCONFIGURATION,
    output_type=google_dot_protobuf_dot_struct__pb2._STRUCT,
    serialized_options=b'\202\323\344\223\002>\022</identity-management/v1.0.0/.well-known/openid-configuration',
  ),
])
_sym_db.RegisterServiceDescriptor(_IDENTITYMANAGEMENTSERVICE)

DESCRIPTOR.services_by_name['IdentityManagementService'] = _IDENTITYMANAGEMENTSERVICE

# @@protoc_insertion_point(module_scope)
