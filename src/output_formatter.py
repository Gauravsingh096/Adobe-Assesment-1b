def generate_output(metadata, extracted_sections, sub_section_analysis):
    return {
        "metadata": metadata,
        "extracted_sections": [
            {
                "document": s.get("document"),
                "page_number": s.get("page_number"),
                "section_title": s.get("section_title"),
                "importance_rank": s.get("importance_rank")
            } for s in extracted_sections
        ],
        "sub_section_analysis": sub_section_analysis
    }
# Output formatting utilities

def generate_output(metadata, extracted_sections, sub_section_analysis):
    return {
        "metadata": metadata,
        "extracted_sections": [
            {
                "document": s.get("document"),
                "page_number": s.get("page_number"),
                "section_title": s.get("section_title"),
                "importance_rank": s.get("importance_rank")
            } for s in extracted_sections
        ],
        "sub_section_analysis": sub_section_analysis
    }
