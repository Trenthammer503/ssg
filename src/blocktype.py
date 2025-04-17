from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    
    if not block:
        return BlockType.PARAGRAPH
    if block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    if block.startswith('>'):
        return BlockType.QUOTE
    if block.startswith(('* ', '- ', '+ ')):
        return BlockType.UNORDERED_LIST
    if block[0].isdigit() and block[1:].startswith('. '):
        return BlockType.ORDERED_LIST
    for i in range(1, 7):
        if block.startswith('#' * i + ' '):
            return BlockType.HEADING
    # Default to paragraph if no other type matches
    return BlockType.PARAGRAPH