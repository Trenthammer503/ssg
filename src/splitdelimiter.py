from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        text = old_node.text

        if text.count(delimiter) < 2:
            new_nodes.append(old_node)
            continue
        
        opening_index = text.find(delimiter)
        closing_index = text.find(delimiter, opening_index + len(delimiter))

        if opening_index == -1 or closing_index == -1:
            new_nodes.append(old_node)
            continue
        
        before_text = text[:opening_index]
        delimited_text = text[opening_index + len(delimiter):closing_index]
        after_text = text[closing_index + len(delimiter):]

        if before_text:
            new_nodes.append(TextNode(before_text, TextType.TEXT))
        
        if delimited_text:
            new_nodes.append(TextNode(delimited_text, text_type))
        
        if after_text:
            new_nodes.append(TextNode(after_text, TextType.TEXT))

    return new_nodes