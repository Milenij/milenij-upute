import logging

def on_page_markdown(markdown, page, config, files):
    # Look for the 'keywords' field from Decap CMS
    if 'keywords' in page.meta:
        keywords_list = page.meta['keywords']
        
        # Ensure it is a list (Decap List Widget), then join it into text
        if isinstance(keywords_list, list):
            keywords_string = ", ".join(keywords_list)
            
            # Append it to the bottom of the text invisibly
            # The Search Engine reads this, but Humans don't see it
            markdown = markdown + f"\n\n<div style='display:none'>{keywords_string}</div>"
            
    return markdown