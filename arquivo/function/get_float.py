import re


def get_float(pattern_preffix: str, pattern_suffix: str, text: str) -> float:
    match = re.search(pattern_preffix + pattern_suffix, text)
    return __get_parsed_float(pattern_preffix, match.group()) if match else 0


def __get_parsed_float(pattern_preffix: str, line: str) -> float:
    match = re.search(pattern_preffix, line)
    replaced = line.replace(match.group(), '')
    end = replaced.find(' ') - 1
    subtext = replaced[0:end]
    return float(subtext.replace('.', '').replace(',', '.'))
