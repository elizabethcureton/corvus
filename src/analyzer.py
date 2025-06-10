from schema.schema import IntelEvaluation
from pydantic import ValidationError

def safe_parse_ai_response(text: str) -> IntelEvaluation | None:
    try:
        return IntelEvaluation.parse_raw(text)
    except ValidationError as e:
        print("Validation failed:", e)
        return None
