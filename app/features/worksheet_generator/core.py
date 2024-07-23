from app.services.logger import setup_logger
from app.services.tool_registry import WorksheetQuestionModel
from app.features.worksheet_generator.tools import get_course_type, generate_worksheet
from app.features.worksheet_generator.document_loaders import get_docs
logger = setup_logger(__name__)

def executor(topic: str, grade_level: str, worksheet_list: list[WorksheetQuestionModel], file_type: str, file_url: str, verbose=True):
   

    course_type = get_course_type(topic)
    docs = get_docs(file_url, file_type)
    worksheet = generate_worksheet(course_type, grade_level, worksheet_list, docs)

    return worksheet
    