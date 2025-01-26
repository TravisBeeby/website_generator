from markdown.inlinepatterns import SimpleTagInlineProcessor
from markdown.extensions import Extension
from markdown.blockprocessors import BlockQuoteProcessor
import xml.etree.ElementTree as etree

ITALIC_RE = r'(\*)([^*]+)\1'  # Regular expression for italics
BOLD_RE = r'(\*\*)([^*]+)\1'  # Regular expression for bold

class CustomBlockQuoteProcessor(BlockQuoteProcessor):
    def run(self, parent, blocks):
        block = blocks.pop(0).lstrip('> ').strip()
        if block:
            quote = etree.SubElement(parent, 'blockquote')
            quote.text = block

class CustomExtension(Extension):
    def extendMarkdown(self, md):
        md.parser.blockprocessors.register(CustomBlockQuoteProcessor(md.parser), 'blockquote', 75)
        md.inlinePatterns.register(SimpleTagInlineProcessor(BOLD_RE, 'b'), 'strong', 175)
        md.inlinePatterns.register(SimpleTagInlineProcessor(ITALIC_RE, 'i'), 'emphasis', 170)

def makeExtension(**kwargs):
    return CustomExtension(**kwargs)
