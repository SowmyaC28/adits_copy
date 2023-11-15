import sys
import os
import unittest
from airflow.models import DagBag
import pandas as pd
import pickle

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

class TestPipeline(unittest.TestCase):

    def sample(self):
        self.assertEqual(1+1,2)

    def setUp(self):
        self.dagbag = DagBag(dag_folder = "dags/", include_examples = False)
        
    def test_task_count(self):
        """Check task count of pipeline dag"""
        dag_id='pipeline'
        dag = self.dagbag.get_dag(dag_id)
        self.assertEqual(len(dag.tasks), 9)  
        
    def test_dependencies_of_drop_task(self):
        """Check the task dependencies of drop_task in pipeline dag"""
        dag_id='pipeline'
        dag = self.dagbag.get_dag(dag_id)
        drop_task = dag.get_task('drop_task')


        upstream_task_ids = list(map(lambda task: task.task_id, drop_task.upstream_list))
        self.assertListEqual(upstream_task_ids, ['load_data_task'])
        downstream_task_ids = list(map(lambda task: task.task_id, drop_task.downstream_list))
        self.assertListEqual(downstream_task_ids, ['Convert_string_date_to_datetime'])
      
        
    '''    

    def test_number_of_columns(self):

        print(project_root)

        dag_id = 'pipeline'
        dag = self.dagbag.get_dag(dag_id)

        print(dag)
        if dag:
            dag.clear()

        dag.run()

        task_instance = dag.get_task('OHE')
       
        df = task_instance.output

        self.assertTrue(len(df) > 0, "DataFrame should not be empty")
        self.assertEqual(df.shape[1], 68, "Number of columns should be 68" )

    def test_ohe(self):

        dag_id = 'pipeline'
        dag = self.dagbag.get_dag(dag_id)

        if dag:
            dag.clear()

        dag.run()

        task_instance = dag.get_task('OHE')
        

        df = task_instance.output

        def is_one_hot_encoded(column):
            unique_values = column.unique()
            if set(unique_values) == {0, 1}:
                if 1 in unique_values:
                    if column.sum() == len(column):
                        return True
                    
        male = is_one_hot_encoded(df['gender_M'])
        female = is_one_hot_encoded(df['gender_F'])

        self.assertEqual(male, True)
        self.assertEqual(female, True)

if __name__ == 'main':
    unittest.main()'''