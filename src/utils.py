import hashlib
import re
import unicodedata

# Normalize input text for analysis
def normalize_for_hash(text: str) -> bytes:
    # Unicode normalize text with NFKC
    string = unicodedata.normalize("NFKC", text)
    # Remove leading/trailing whitespace
    string = string.strip()
    # Collapse run of whitespaces into one space
    string = re.sub(r"\s+", " ", string)
    # Format as lowercase
    string = string.lower()
    # UTF-8 encode for hashing
    return string.encode("utf-8")

# Function to assign SHA256 ID to normalized input
def compute_report_id(raw_message: str) -> str:
    normalized_bytes = normalize_for_hash(raw_message)
    return hashlib.sha256(normalized_bytes).hexdigest()