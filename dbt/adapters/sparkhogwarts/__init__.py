from dbt.adapters.sparkhogwarts.connections import SparkConnectionManager  # noqa
from dbt.adapters.sparkhogwarts.connections import SparkCredentials
from dbt.adapters.sparkhogwarts.relation import SparkRelation  # noqa
from dbt.adapters.sparkhogwarts.column import SparkColumn  # noqa
from dbt.adapters.sparkhogwarts.impl import SparkHogwartsAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import spark

Plugin = AdapterPlugin(
    adapter=SparkHogwartsAdapter, credentials=SparkCredentials, include_path=spark.PACKAGE_PATH  # type: ignore
)
