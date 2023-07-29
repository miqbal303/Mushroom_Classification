import os
import sys
import pandas as pd
import pymongo
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')

class DataIngestion:
    def __init__(self, uri, db_name, collection_name):
        self.uri = uri
        self.db_name = db_name
        self.collection_name = collection_name
        self.ingestion_config = DataIngestionConfig()

    def connect_to_mongodb(self):
        try:
            client = pymongo.MongoClient(self.uri)
            self.db = client[self.db_name]
            self.collection = self.db[self.collection_name]
            print("Connected to MongoDB!")
        except Exception as e:
            raise CustomException(e, sys)        

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion start')
        try:
            # Connect to MongoDB
            self.connect_to_mongodb()

            # Fetch data from MongoDB and convert to DataFrame
            all_documents = list(self.collection.find())
            df = pd.DataFrame(all_documents)

            # Define the new column names
            new_columns = {
                'class': 'class',
                'cap-shape': 'cap_shape',
                'cap-surface': 'cap_surface',
                'cap-color': 'cap_color',
                'bruises': 'bruises',
                'odor': 'odor',
                'gill-attachment': 'gill_attachment',
                'gill-spacing': 'gill_spacing',
                'gill-size': 'gill_size',
                'gill-color': 'gill_color',
                'stalk-shape': 'stalk_shape',
                'stalk-root': 'stalk_root',
                'stalk-surface-above-ring': 'stalk_surface_above_ring',
                'stalk-surface-below-ring': 'stalk_surface_below_ring',
                'stalk-color-above-ring': 'stalk_color_above_ring',
                'stalk-color-below-ring': 'stalk_color_below_ring',
                'veil-type': 'veil_type',
                'veil-color': 'veil_color',
                'ring-number': 'ring_number',
                'ring-type': 'ring_type',
                'spore-print-color': 'spore_print_color',
                'population': 'population',
                'habitat': 'habitat'
            }
            df = df.rename(columns=new_columns)
            logging.info('Dataset read data as pandas dataframe')
            logging.info(f'{df.head()}')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info('raw data save')

            df.drop(columns=['_id','veil_type'], axis=1, inplace=True)
            logging.info("Droping veil type from dataframe")

            # Check for '?' in each column
            columns_with_question_mark = df.columns[df.apply(lambda col: col.str.contains('\?', na=False)).any()]
            print("columns_with_question_mark name: ",columns_with_question_mark)

            # Replace '?' with None
            df['stalk_root'].replace('?', None, inplace=True)
            df['stalk_root'].fillna(df['stalk_root'].mode()[0], inplace=True)
            logging.info("Removing ? and replace with mode value")

            logging.info('train test split')
            train_set, test_set = train_test_split(df, test_size=0.3, random_state=101)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Ingestion of Data is completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info('Exception occurred at data ingestion stage')
            raise CustomException(e, sys)

if __name__ == '__main__':
    # MongoDB Connection Configuration
    mongodb_uri = "mongodb+srv://miqbal:miqbal@cluster1.mr340pr.mongodb.net/?retryWrites=true&w=majority"
    database_name = "Mushroom_Classification"
    collection_name = "Mushroom"

    # Initialize DataIngestion with MongoDB connection parameters
    obj = DataIngestion(mongodb_uri, database_name, collection_name)

    # Run Data Ingestion
    obj.initiate_data_ingestion()
