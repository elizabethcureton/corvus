from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, LongTable
from datetime import datetime, timezone
from schema.schema import IntelEvaluation
import os
import uuid

def generate_report_filename(evaluation: IntelEvaluation) -> str:
    """Generate a standardized filename for the threat intelligence report."""
    # Get current datetime in UTC/Zulu time (YYYYMMDD-HHMMSSZ format)
    datetime_str = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%SZ")
    
    # Get threat type and severity
    threat_type = evaluation.threat_analysis.threat_type.lower()
    severity = evaluation.threat_analysis.severity.lower()
    
    # Generate a short unique identifier (first 8 chars of UUID)
    unique_id = str(uuid.uuid4())[:8]
    
    # Format: YYYYMMDD-HHMMSSZ-INTEL-[THREAT_TYPE]-[SEVERITY]-[ID].pdf
    filename = f"{datetime_str}-INTEL-{threat_type}-{severity}-{unique_id}.pdf"
    
    return filename

def create_threat_report(evaluation: IntelEvaluation, output_dir: str = "outputs") -> str:
    """Generate a PDF report from an IntelEvaluation object.
    
    Args:
        evaluation: The IntelEvaluation object containing the threat analysis
        output_dir: Directory where the report should be saved (default: "outputs")
        
    Returns:
        str: Path to the generated PDF file
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate filename and full path
    filename = generate_report_filename(evaluation)
    output_path = os.path.join(output_dir, filename)
    
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )

    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30
    )
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=12
    )
    body_style = styles['Normal']
    table_style = ParagraphStyle(
        'TableStyle',
        parent=body_style,
        fontSize=10,
        leading=12
    )
    empty_style = ParagraphStyle(
        'EmptyStyle',
        parent=table_style,
        textColor=colors.gray
    )

    # Content
    story = []
    
    # Title
    story.append(Paragraph("Threat Intelligence Report", title_style))
    story.append(Paragraph(f"Generated on: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}", body_style))
    story.append(Spacer(1, 20))

    # Threat Analysis Section
    story.append(Paragraph("Threat Analysis", heading_style))
    threat_data = [
        ["Threat Type", evaluation.threat_analysis.threat_type],
        ["Severity", evaluation.threat_analysis.severity],
        ["Likelihood", evaluation.threat_analysis.likelihood],
        ["Confidence", f"{evaluation.confidence:.2%}"]
    ]
    threat_table = Table(threat_data, colWidths=[2*inch, 4*inch])
    threat_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(threat_table)
    story.append(Spacer(1, 12))
    story.append(Paragraph("Description:", body_style))
    story.append(Paragraph(evaluation.threat_analysis.description, body_style))
    story.append(Spacer(1, 20))

    # Entities Section
    story.append(Paragraph("Identified Entities", heading_style))
    entity_data = []
    for field, value in evaluation.entities.dict().items():
        # Always include the field, even if empty
        field_name = field.replace('_', ' ').title()
        if value:  # If there are values, show them
            entity_data.append([
                Paragraph(field_name, table_style),
                Paragraph(', '.join(value), table_style)
            ])
        else:  # If empty, show "No entities identified"
            entity_data.append([
                Paragraph(field_name, table_style),
                Paragraph("No entities identified", empty_style)
            ])
    
    if entity_data:
        entity_table = LongTable(entity_data, colWidths=[2*inch, 4*inch])
        entity_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'TOP')
        ]))
        story.append(entity_table)
    story.append(Spacer(1, 20))

    # Recommended Actions Section
    story.append(Paragraph("Recommended Actions", heading_style))
    if evaluation.threat_analysis.recommended_actions:
        for action in evaluation.threat_analysis.recommended_actions:
            story.append(Paragraph(f"• {action}", body_style))
    else:
        story.append(Paragraph("No specific actions recommended", empty_style))
    
    # Build the PDF
    doc.build(story)
    
    return output_path 