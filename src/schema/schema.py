from pydantic import BaseModel, Field, validator
from typing import List, Literal, Optional
from typing_extensions import Annotated
from datetime import datetime, timezone

class Timeframe(BaseModel):
    reported_at: Optional[datetime] = None
    began_at:     Optional[datetime] = None

    @validator("reported_at", "began_at", pre=True)
    def parse_datetime_allow_naive(cls, v):
        if v is None:
            return None
        dt = datetime.fromisoformat(v)
        # If no tzinfo, assume UTC
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt

class ReporterInfo(BaseModel):
    id:      Optional[str]   = None
    role:    Optional[str]   = None
    contact: List[str]       = Field(default_factory=list)

class Entities(BaseModel):
    person:        List[str] = Field(default_factory=list)
    organization:  List[str] = Field(default_factory=list)
    location:      List[str] = Field(default_factory=list)
    technology:    List[str] = Field(default_factory=list)
    threat_actor:  List[str] = Field(default_factory=list)
    vulnerabilities: List[str] = Field(default_factory=list)

class ThreatAnalysis(BaseModel):
    threat_type:        Literal["Physical", "Cybersecurity", "Political", "Other"]
    description:        str
    severity:           Literal["Low", "Medium", "High", "Critical"]
    likelihood:         Literal["Unlikely", "Possible", "Likely", "Certain"]
    recommended_actions: List[str]

class IntelEvaluation(BaseModel):
    # Optional fields
    report_id:        Optional[str]       = None
    summary:          Optional[str]       = None
    timeframe:        Optional[Timeframe] = None
    reporter_info:    Optional[ReporterInfo] = None

    # Core required fields
    entities:         Entities
    assets_affected:  List[str]        = Field(default_factory=list)
    impact:           List[str]        = Field(default_factory=list)
    threat_analysis:  ThreatAnalysis
    confidence:       Annotated[float, Field(ge=0.0, le=1.0)]

    # Optional raw input
    raw_message:      Optional[str]    = None
