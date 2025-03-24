from textnode import *

def main():
    test_node = TextNode('This is some anchor text', TextType.LINK_TEXT, 'https://www.boot.dev')
    print(test_node)

main()