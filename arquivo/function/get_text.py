def get_text(pages):
    texts = []
    [__append(texts, page) for page in pages]
    return ''.join(texts)


def __append(texts, page):
    texts.append(page.extract_text())
