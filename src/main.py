from textnode import TextNode

def main():
    # 1. Create a new TextNode object with dummy values
    node = TextNode("This is a text node", "link", "https://www.boot.dev")

    # 2. Print the node to see the __repr__ output
    print(node)

# Call the main function
if __name__ == "__main__":
    main()