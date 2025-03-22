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
