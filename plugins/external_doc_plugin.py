"""
MkDocs plugin to add visual indicators for external documents.
This plugin processes markdown files and adds visual notices for external content.
"""

import re
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options

class ExternalDocPlugin(BasePlugin):
    
    config_scheme = (
        ('enabled', config_options.Type(bool, default=True)),
    )
    
    def on_page_markdown(self, markdown, page, config, files):
        """Process markdown to add visual indicators for external documents."""
        
        if not self.config['enabled']:
            return markdown
        
        # Check if this is an external document
        if '<!-- EXTERNAL DOCUMENT' in markdown:
            # Extract the external document metadata
            marker_pattern = r'<!-- EXTERNAL DOCUMENT(.*?)-->'
            match = re.search(marker_pattern, markdown, re.DOTALL)
            
            if match:
                marker_content = match.group(1)
                
                # Extract key information
                edit_url = None
                repository = None
                
                for line in marker_content.split('\n'):
                    if 'Edit URL:' in line:
                        edit_url = line.split('Edit URL:')[1].strip()
                    elif 'Source:' in line:
                        repository = line.split('Source:')[1].strip()
                
                # Remove the HTML comment from display
                markdown = re.sub(marker_pattern, '', markdown, flags=re.DOTALL)
                
                # Add visual notice at the top of the page
                notice_html = f'''
<div class="external-doc-notice">
    <div class="external-doc-notice-text">
        <strong>External Document:</strong> This documentation is automatically synchronized from 
        <a href="{edit_url}" target="_blank" rel="noopener">{repository}</a>.
        To make changes, please edit the source repository.
    </div>
</div>

'''
                
                # Add the notice after any front matter
                if markdown.startswith('---'):
                    # Has front matter, add after it
                    end_frontmatter = markdown.find('---', 3)
                    if end_frontmatter != -1:
                        markdown = (markdown[:end_frontmatter + 3] + '\n\n' + 
                                  notice_html + markdown[end_frontmatter + 3:])
                    else:
                        markdown = notice_html + markdown
                else:
                    # No front matter, add at the beginning
                    markdown = notice_html + markdown
                
                # Add badge to the first H1 heading
                h1_pattern = r'^# (.+)$'
                h1_replacement = r'# \1 <span class="external-badge">External</span>'
                markdown = re.sub(h1_pattern, h1_replacement, markdown, count=1, flags=re.MULTILINE)
        
        return markdown
    
    def on_nav(self, nav, config, files):
        """Add indicators to navigation for external documents."""
        # This would require more complex navigation tree manipulation
        # For now, CSS handles this via checking for external markers
        return nav