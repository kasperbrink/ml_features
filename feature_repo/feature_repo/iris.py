from datetime import timedelta

from google.protobuf.duration_pb2 import Duration

from feast import Entity, Feature, FeatureView, ValueType, Field
from feast import FileSource
from feast.types import Float32, Float64, Int64, String


iris_observations = FileSource(
    path="/home/kasperbrink/ml_features/feature_repo/feature_repo/data/iris.parquet",
    event_timestamp_column="observation_date",
)

iris_id = Entity(name="iris_id", value_type=ValueType.INT64, description="Iris identifier",)

iris_observations_view = FeatureView(
    name="iris_observations",
    entities=[iris_id],
    ttl=timedelta(days=-1),
    schema=[
        Field(name="sepal_length", dtype=Float32),
        Field(name="sepal_width", dtype=Float32),
        Field(name="petal_length", dtype=Int64),
        Field(name="petal_width", dtype=Int64),
        Field(name="species", dtype=String),
    ],
    online=False,
    source=iris_observations,
    tags={}
)
