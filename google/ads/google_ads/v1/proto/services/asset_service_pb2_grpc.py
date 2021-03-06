# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v1.proto.resources import asset_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_asset__pb2
from google.ads.google_ads.v1.proto.services import asset_service_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_asset__service__pb2


class AssetServiceStub(object):
  """Service to manage assets.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetAsset = channel.unary_unary(
        '/google.ads.googleads.v1.services.AssetService/GetAsset',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_asset__service__pb2.GetAssetRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_asset__pb2.Asset.FromString,
        )
    self.MutateAssets = channel.unary_unary(
        '/google.ads.googleads.v1.services.AssetService/MutateAssets',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_asset__service__pb2.MutateAssetsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_asset__service__pb2.MutateAssetsResponse.FromString,
        )


class AssetServiceServicer(object):
  """Service to manage assets.
  """

  def GetAsset(self, request, context):
    """Returns the requested asset in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateAssets(self, request, context):
    """Creates assets. Operation statuses are returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AssetServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetAsset': grpc.unary_unary_rpc_method_handler(
          servicer.GetAsset,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_asset__service__pb2.GetAssetRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_asset__pb2.Asset.SerializeToString,
      ),
      'MutateAssets': grpc.unary_unary_rpc_method_handler(
          servicer.MutateAssets,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_asset__service__pb2.MutateAssetsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_asset__service__pb2.MutateAssetsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.AssetService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
