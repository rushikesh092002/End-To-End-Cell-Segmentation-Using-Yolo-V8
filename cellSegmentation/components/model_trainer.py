import os
import sys
import shutil
from cellSegmentation.utils.main_utils import read_yaml_file
from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
from cellSegmentation.entity.config_entity import ModelTrainerConfig
from cellSegmentation.entity.artifacts_entity import ModelTrainerArtifact


class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config

    def clean_up_files(self):
        
        try:
            logging.info("Starting cleanup process")

            files_to_remove = [
                "yolov8s-seg.pt", "train", "valid", "test", "data.yaml", "runs"
            ]

            for file in files_to_remove:
                if os.path.exists(file):
                    if os.path.isdir(file):
                        shutil.rmtree(file)
                        logging.info(f"Directory {file} removed.")
                    else:
                        os.remove(file)
                        logging.info(f"File {file} removed.")
            logging.info("Cleanup process completed successfully.")

        except Exception as e:
            logging.error(f"Error during cleanup: {e}")

    def initiate_model_trainer(self,) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            logging.info("Using already unzipped data from data_ingestion/feature_store")

            
            data_path = "artifacts/data_ingestion/feature_store"  
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)

            
            logging.info(f"Training model with weight file: {self.model_trainer_config.weight_name}")
            os.system(f"yolo task=segment mode=train model={self.model_trainer_config.weight_name} data={data_path}/data.yaml epochs={self.model_trainer_config.no_epochs} imgsz=640 save=true")

            
            best_model_path = f"runs/segment/train/weights/best.pt"
            if os.path.exists(best_model_path):
                shutil.copy(best_model_path, f"{self.model_trainer_config.model_trainer_dir}/")
                logging.info(f"Best model weights copied to {self.model_trainer_config.model_trainer_dir}/")

            
            self.clean_up_files()

            
            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path=f"{self.model_trainer_config.model_trainer_dir}/best.pt",
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact

        except Exception as e:
            logging.error(f"Error during model training: {e}")
            raise AppException(e, sys)
