from textnode import TextNode, TextType


def main():
    text_node = TextNode("Go to boot.dev", TextType.LINK, "https://boot.dev")
    print(text_node)


main()
