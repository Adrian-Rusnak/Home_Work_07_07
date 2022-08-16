def first_word(text):
    text = text.replace('.', '').replace(',', '')
    text = text.strip().split(' ')[0]
    return text

print( first_word("don't touch it"))