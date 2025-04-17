def split_blocks(markdown):
    blocks = markdown.split('\n\n')
    new_blocks = []
    for block in blocks:
        cleaned_block = block.strip()
        if cleaned_block:
            new_blocks.append(cleaned_block)
    return new_blocks
