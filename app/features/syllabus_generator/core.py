from app.services.logger import setup_logger
from app.features.syllabus_generator.tools import generate_syllabus
from app.features.syllabus_generator.document_loaders import generate_summary_from_img, summarize_transcript_youtube_url, get_summary
from app.api.error_utilities import SyllabusGeneratorError

logger = setup_logger()

def executor(grade_level: str, 
            course: str, 
            instructor_name: str, 
            instructor_title: str, 
            unit_time: str, 
            unit_time_value: int, 
            start_date: str, 
            assessment_methods: str, 
            grading_scale: str,
            file_url: str,
            file_type: str,
            verbose: bool = True):
    
    if verbose:
        logger.info(f"File URL loaded: {file_url}")
    
    try:
        if file_type == 'img':
            summary = generate_summary_from_img(file_url)
        elif file_type == 'youtube_url':
            summary = summarize_transcript_youtube_url(file_url, verbose=verbose)
        else:
            summary = get_summary(file_url, file_type, verbose=verbose)

        request_args = SyllabusRequestArgs(
                                grade_level,
                                course,
                                instructor_name,
                                instructor_title,
                                unit_time,
                                unit_time_value,
                                start_date,
                                assessment_methods,
                                grading_scale,
                                summary)

        # Call the generate_syllabus function
        syllabus = generate_syllabus(request_args, verbose=verbose)
        
        return syllabus
    
    except Exception as e:
        logger.error(f"Failed to generate syllabus: {str(e)}")
        raise SyllabusGeneratorError(f"Failed to generate syllabus: {str(e)}") from e
