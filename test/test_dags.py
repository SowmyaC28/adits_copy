import pytest
from airflow.models import DagBag

def test_no_import_errors():
  dag_bag = DagBag(dag_folder='dags/', include_examples=False)
  assert len(dag_bag.import_errors) == 0, "No Import Failures"
  for dag_id, exception in dag_bag.import_errors.items():
        print(f"Import error for DAG ID '{dag_id}': {str(exception)}")