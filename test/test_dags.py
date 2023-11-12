import pytest
from airflow.models import DagBag

 
  
def test_no_import_errors():
  dag_list = []
  dag_bag = DagBag(dag_folder='dags/', include_examples=False)
  task_list = []
  for dag_id in dag_bag.dags:
    dag = dag_bag.get_dag(dag_id)
    for tasks in dag.tasks:
         task_list.append(tasks)
        
  assert len(task_list) == 2, "2 dummy tasks must be present"       