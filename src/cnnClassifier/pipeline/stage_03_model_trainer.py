from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_trainer import Training



STAGE_NAME = "Prepare base model"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()