from textnode import TextNode, TextType  # Assuming this exists
from htmlnode import HTMLNode   # Assuming this exists
from splitblocks import split_blocks
from blocktype import block_to_block_type, BlockType
from texttotextnodes import text_to_textnodes
import re

def markdown_to_html_node(markdown):
    """
    Convert a markdown document into a single parent HTMLNode containing nested elements.
    """
    
    def text_to_children(text):
        """Helper function to convert text to HTMLNode children with inline markdown parsing"""
        text_nodes = text_to_textnodes(text)
        html_nodes = []
        for text_node in text_nodes:
            html_nodes.append(text_node_to_html_node(text_node))
        return html_nodes

    def text_node_to_html_node(text_node):
        """Convert a TextNode to an HTMLNode"""
        if text_node.text_type == TextType.TEXT:
            return HTMLNode(None, text_node.text)
        elif text_node.text_type == TextType.BOLD:
            return HTMLNode("b", text_node.text)
        elif text_node.text_type == TextType.ITALIC:
            return HTMLNode("i", text_node.text)
        elif text_node.text_type == TextType.CODE:
            return HTMLNode("code", text_node.text)
        elif text_node.text_type == TextType.LINK:
            # Check if url attribute exists
            url = getattr(text_node, "url", "")
            return HTMLNode("a", text_node.text, {"href": url})
        elif text_node.text_type == TextType.IMAGE:
            url = getattr(text_node, "url", "")
            return HTMLNode("img", "", {"src": url, "alt": text_node.text})
        else:
            raise ValueError(f"Invalid text type: {text_node.text_type}")

    def handle_code_block(text):
        """Special handler for code blocks that doesn't parse inline markdown"""
        code_node = HTMLNode("code", text)
        pre_node = HTMLNode("pre", None)
        pre_node.children = [code_node]
        return pre_node
    
    # Handle multi-line list itmes
    def parse_list_items(block, is_ordered=False):
        lines = block.split("\n")
        items = []
        current_item = ""

        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Check if this line starts a new list item
            if (is_ordered and re.match(r"^\d+\.\s", line)) or \
               (not is_ordered and re.match(r"^[-*+]\s", line)):
                # if we have a current item in progress, add it to items
                if current_item:
                    items.append(current_item.strip())
                # start a new item, removing he marker
                if is_ordered:
                    current_item = re.sub(r"^\d+\.\s", "", line)
                else:
                    current_item = re.sub(r"^[-*+]\s", "", line)
            else:
                # This is a continuation of the current item
                current_item += " " + line

        # Add the last item if it exists
        if current_item:
            items.append(current_item.strip())

        return items

    # Split markdown into blocks using your existing function
    blocks = split_blocks(markdown)
    
    # Create parent div node
    parent = HTMLNode("div", None)
    parent.children = [] # Initialize the children list
    
    # Process each block
    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.PARAGRAPH:
            block_content = re.sub(r'\n\s*', ' ', block)
            node = HTMLNode("p", None)
            node.children = text_to_children(block_content)
            parent.children.append(node)
        
        elif block_type == BlockType.HEADING:
            # get the first line to determine heading level
            first_line = block.split("\n")[0].strip()
            match = re.match(r"^(#{1,6})\s+(.+)$", first_line)
            if match:
                level = len(match.group(1)) # Number of # characters
                content = match.group(2) # The heading text
                node = HTMLNode(f"h{level}", None)
                node.children = text_to_children(content)
                parent.children.append(node)
        
        elif block_type == BlockType.CODE:
            # Remove code block markers and create code node
            content = "\n".join(block.split("\n")[1:-1])  # Remove first/last lines with ```
            node = handle_code_block(content)
            parent.children.append(node)
        
        elif block_type == BlockType.QUOTE:
            # Remove the > from each line and join them
            lines = block.split("\n")
            content = ""
            for line in lines:
                if line.strip(): # Skip empty lines
                    # Remove > and extra spaces
                    cleaned_line = line.strip()
                    if cleaned_line.startswith(">"):
                        cleaned_line = cleaned_line[1:].strip()
                    content += cleaned_line + " "
            node = HTMLNode("blockquote", None)
            node.children = text_to_children(content.strip())
            parent.children.append(node)
        
        elif block_type == BlockType.UNORDERED_LIST:
            node = HTMLNode("ul", None)
            node.children = []
            items = parse_list_items(block, is_ordered=False)
            for item in items:
                li = HTMLNode("li", None)
                li.children = text_to_children(item)
                node.children.append(li)
            parent.children.append(node)
        
        elif block_type == BlockType.ORDERED_LIST:
            node = HTMLNode("ol", None)
            node.children = []
            items = parse_list_items(block, is_ordered=True)
            for item in items:
                if item.strip():
                    li = HTMLNode("li", None)
                    li.children = text_to_children(item)
                    node.children.append(li)
            parent.children.append(node)

    return parent