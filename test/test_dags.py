import pytest
from airflow.models import DagBag

def check_dag_list():
  dag_list = []
  dag_bag = DagBag(dag_folder='dags/', include_examples=False)
  
  for dag_id in dag_bag.dags:
        dag_list.append(dag_id)
        
  assert len(dag_list) == 1, "only custom dag must be present"  
  
def check_task_list():
  dag_list = []
  dag_bag = DagBag(dag_folder='dags/', include_examples=False)
  task_list = []
  for dag_id in dag_bag.dags:
    dag = dag_bag.get_dag(dag_id)
    for tasks in dag.tasks:
         task_list.append(tasks)
        
  assert len(task_list) == 2, "2 dummy tasks must be present"       