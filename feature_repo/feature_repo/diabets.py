from datetime import timedelta

from google.protobuf.duration_pb2 import Duration

from feast import Entity, Feature, FeatureView, ValueType, Field
from feast import FileSource
from feast.types import Float32, Float64, Int64, String, Bool


diabetes_observations = FileSource(
    path="/home/kasperbrink/ml_features/feature_repo/feature_repo/data/diabetes.parquet",
    event_timestamp_column="observation_date",
)

diabetes_id = Entity(name="diabetes_id", value_type=ValueType.INT64, description="Diabetes identifier",)

iris_observations_view = FeatureView(
    name="diabetes_observations",
    entities=[diabetes_id],
    ttl=timedelta(days=-1),
    schema=[
        Field(name="preg", dtype=Float64),
        Field(name="plas", dtype=Float64),
        Field(name="pres", dtype=Float64),
        Field(name="skin", dtype=Float64),
        Field(name="insu", dtype=Float64),
        Field(name="mass", dtype=Float64),
        Field(name="pedi", dtype=Float64),
        Field(name="age", dtype=Float64),
        Field(name="class", dtype=Bool),
    ],
    online=False,
    source=diabetes_observations,
    tags={}
)