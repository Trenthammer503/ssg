from extractlinks import *
from textnode import TextNode, TextType


def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        text = old_node.text
        images = extract_markdown_images(text)

        if not images:
            new_nodes.append(old_node)
            continue

        img_alt, img_url = images[0]
        img_markdown = f"![{img_alt}]({img_url})"

        parts = text.split(img_markdown, 1)

        if parts[0]:
            new_nodes.append(TextNode(
                parts[0],
                TextType.TEXT,
            ))

        new_nodes.append(TextNode(
            img_alt,
            TextType.IMAGE,
            img_url
        ))

        if len(parts) > 1 and parts[1]:
            remaining_nodes = split_nodes_image([TextNode(
                parts[1],
                TextType.TEXT
            )])

            new_nodes.extend(remaining_nodes)

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        text = old_node.text
        links = extract_markdown_links(text)

        if not links:
            new_nodes.append(old_node)
            continue

        lnk_alt, lnk_url = links[0]
        lnk_markdown = f"[{lnk_alt}]({lnk_url})"

        parts = text.split(lnk_markdown, 1)

        if parts[0]:
            new_nodes.append(TextNode(
                parts[0],
                TextType.TEXT,
            ))

        new_nodes.append(TextNode(
            lnk_alt,
            TextType.LINK,
            lnk_url
        ))

        if len(parts) > 1 and parts[1]:
            remaining_nodes = split_nodes_link([TextNode(
                parts[1],
                TextType.TEXT
            )])

            new_nodes.extend(remaining_nodes)
            
    return new_nodes