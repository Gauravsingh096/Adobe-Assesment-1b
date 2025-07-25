# Entry point for persona-driven document intelligence system
import argparse
import os
import json
from datetime import datetime
from pdf_parser import extract_sections
from relevance_model import rank_sections
from output_formatter import generate_output

def main():

    parser = argparse.ArgumentParser(description="Persona-Driven Document Intelligence")
    parser.add_argument('--persona', type=str, required=True, help='Persona description')
    parser.add_argument('--job', type=str, required=True, help='Job to be done')
    parser.add_argument('--pdfs', nargs='+', required=True, help='List of PDF file paths or a directory containing PDFs')
    parser.add_argument('--output', type=str, default="../output/result.json", help='Output JSON file path')
    args = parser.parse_args()

    # Expand directory to all PDFs if a directory is provided
    pdf_files = []
    for path in args.pdfs:
        if os.path.isdir(path):
            pdf_files.extend([
                os.path.join(path, f) for f in os.listdir(path)
                if f.lower().endswith('.pdf')
            ])
        else:
            pdf_files.append(path)

    # Metadata
    metadata = {
        "input_documents": pdf_files,
        "persona": args.persona,
        "job_to_be_done": args.job,
        "processing_timestamp": datetime.now().isoformat()
    }

    all_sections = []
    for pdf_path in pdf_files:
        sections = extract_sections(pdf_path)
        for section in sections:
            section["document"] = os.path.basename(pdf_path)
        all_sections.extend(sections)

    ranked_sections = rank_sections(all_sections, args.persona, args.job, top_k=10)

    # Placeholder for sub-section analysis (to be implemented)
    sub_section_analysis = []

    output_json = generate_output(metadata, ranked_sections, sub_section_analysis)
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(output_json, f, indent=2, ensure_ascii=False)
    print(f"Output written to {args.output}")

if __name__ == "__main__":
    main()
