from pydantic import BaseModel, Field
from typing import List, Literal
from typing_extensions import Annotated

# TODO: Maybe extract a readable template from this schema document to pass back into the LLM call to simplify the repo (versus extra/existing template files)
class Entities(BaseModel):
    person: List[str] = Field(default_factory=list, description="List of identified persons")
    organization: List[str] = Field(default_factory=list, description="List of identified organizations")
    location: List[str] = Field(default_factory=list, description="List of identified locations")
    technology: List[str] = Field(default_factory=list, description="List of identified technologies")
    threat_actor: List[str] = Field(default_factory=list, description="List of identified threat actors")
    vulnerabilities: List[str] = Field(default_factory=list, description="List of identified vulnerabilities")
    events: List[str] = Field(default_factory=list, description="List of identified events")

# TODO: Consider our category breakdown closer to testing and implementation. There's some philosophy to it.
class ThreatAnalysis(BaseModel):
    threat_type: Literal["Physical", "Cybersecurity", "Political", "Other"]
    description: str
    severity: Literal["Low", "Medium", "High", "Critical"]
    likelihood: Literal["Unlikely", "Possible", "Likely", "Certain"]
    recommended_actions: List[str]

class IntelEvaluation(BaseModel):
    entities: Entities
    threat_analysis: ThreatAnalysis
    confidence: Annotated[float, Field(ge=0.0, le=1.0)]
