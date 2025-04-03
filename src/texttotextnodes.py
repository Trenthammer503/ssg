from splitdelimiter import split_nodes_delimiter
from splitlinks import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text):

    #convert text to a list of text node.
    nodes = [TextNode(text, TextType.TEXT)]

    #process special blocks like images and links
    nodes = (split_nodes_image(nodes))
    nodes = (split_nodes_link(nodes))

    #then process inline formatting
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    return nodes