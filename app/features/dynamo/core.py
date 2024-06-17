from features.dynamo.tools import summarize_transcript, summarize_pdf, generate_flashcards
from services.logger import setup_logger
from api.error_utilities import VideoTranscriptError
from services.tool_registry import ToolFile

logger = setup_logger(__name__)

def executor(youtube_url: str, document_urls: list[str], verbose=False):
    if len(youtube_url)!=0:
        summary = summarize_transcript(youtube_url, verbose=verbose)
    elif len(document_urls)!=0:
        summary = ""
        for url in document_urls:
            if url.split(".")[-1]=="pdf":
                summary = summary +"\n" + summarize_pdf(url, verbose=verbose)
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