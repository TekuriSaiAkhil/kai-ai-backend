from features.dynamo.tools import summarize_transcript, summarize_pdf, generate_flashcards
from services.logger import setup_logger
from api.error_utilities import VideoTranscriptError

logger = setup_logger(__name__)

def executor(youtube_url: str, pdf_file_url:str, verbose=False):
    if len(youtube_url)!=0:
        summary = summarize_transcript(youtube_url, verbose=verbose)
    elif len(pdf_file_url)!=0:
        summary = summarize_pdf(pdf_file_url, verbose=verbose)
    else:
        summary = ""
    
    flashcards = generate_flashcards(summary)

    sanitized_flashcards = []
    for flashcard in flashcards:
        if 'concept' in flashcard and 'definition' in flashcard:
            sanitized_flashcards.append({
                "concept": flashcard['concept'],
                "definition": flashcard['definition']
            })
        else:
            logger.warning(f"Malformed flashcard skipped: {flashcard}")

    return sanitized_flashcards 