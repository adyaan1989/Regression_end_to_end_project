from dataclasses import dataclass


# data ingestion path
@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str
    

#data validation path
@dataclass
class DataValidationArtifact:
    validation_status: bool
    message: str
    drift_report_file_path:str
    
