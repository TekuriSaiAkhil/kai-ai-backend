from app.services.logger import setup_logger
from app.services.tool_registry import WorksheetQuestionModel
logger = setup_logger(__name__)

def executor(topic: str, grade_level: str, worksheet_list: list[WorksheetQuestionModel], file_type: str, file_url: str, verbose=True):
   

    return "Worksheet generator" 