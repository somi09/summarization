import fastapi

from src.api.schemas.summarize import SummarizeTextRequest, SummarizeWebPageRequest, SummarizeResponse
from src.summarizer.parse_webpages import WebpageParser
from src.summarizer.summary_gen import recursive_summarize

router = fastapi.APIRouter(prefix="/summarize", tags=["summarize"])



@router.post("/webpage")
async def summarize_webpages(data: SummarizeWebPageRequest) -> SummarizeResponse:
    parser = WebpageParser()
    text = parser.parse(data.url)
    summary = recursive_summarize(text, data.summary_len)
    return SummarizeResponse(summary=summary, number_of_words=len(summary.split(' ')))


@router.post("/text")
async def summarize_webpages(data: SummarizeTextRequest) -> SummarizeResponse: 
    summary = recursive_summarize(data.text, data.summary_len)
    return SummarizeResponse(summary=summary, number_of_words=len(summary.split(' ')))



    
    
