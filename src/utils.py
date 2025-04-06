import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = list()

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split = node.text.split(delimiter)

        if len(split) % 2 == 0:
            raise Exception("Invalid markdown")

        for i in range(len(split)):
            if len(split[i]) == 0:
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(text=split[i], text_type=TextType.TEXT))
            else:
                new_nodes.append(TextNode(text=split[i], text_type=text_type))

    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_text_nodes(node, text_type, matches):
    result = list()

    text = node.text

    for match in matches:
        image_split = f"![{match[0]}]({match[1]})"
        link_split = f"[{match[0]}]({match[1]})"
        split = text.split(
            image_split if text_type == TextType.IMAGE else link_split, 1
        )

        if split[0] != "":
            result.append(TextNode(split[0], TextType.TEXT))

        result.append(TextNode(match[0], text_type, match[1]))

        text = split[1]

    if len(text) > 0:
        result.append(TextNode(text, TextType.TEXT))

    return result


def split_nodes_image(old_nodes):
    result = list()

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        matches = extract_markdown_images(node.text)
        if len(matches) == 0:
            result.append(node)
        else:
            result.extend(extract_text_nodes(node, TextType.IMAGE, matches))

    return result


def split_nodes_link(old_nodes):
    result = list()

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        matches = extract_markdown_links(node.text)
        if len(matches) == 0:
            result.append(node)
        else:
            result.extend(extract_text_nodes(node, TextType.LINK, matches))

    return result
