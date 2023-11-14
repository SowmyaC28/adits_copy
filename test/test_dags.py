import pytest
from airflow.models import DagBag

def test_no_import_errors():
  dag_bag = DagBag(dag_folder='dags/', include_examples=False)
  dag_list = []
  for dag_id in dag_bag.dags:
    
        dag_list.append(dag_id)
  assert len(dag_list) == 1, "only custom dag must be present"      