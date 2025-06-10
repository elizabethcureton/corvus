from ai_client import ask_ai
from analyzer import safe_parse_ai_response
from pdf_generator import create_threat_report

with open("prompt_templates/incident_report.txt") as f:
    incident_report = f.read()

def run_pipeline(text):
    raw_response = ask_ai(text)
    print("Raw Response:", raw_response)

    parsed = safe_parse_ai_response(raw_response)
    if parsed:
        print(parsed)
        # Generate PDF report
        output_path = create_threat_report(parsed)
        print(f"PDF report generated: {output_path}")
    else:
        print("Parsing failed")

if __name__ == "__main__":
    # TODO: Integrate this function with a test input
    run_pipeline(incident_report)