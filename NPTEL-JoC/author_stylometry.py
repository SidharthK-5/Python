import nltk

papers = {
    "Madison": [
        10,
        14,
        37,
        39,
        40,
        41,
        42,
        43,
        44,
        45,
        46,
        47,
        48,
        64,
        86,
        87,
        88,
        89,
        90,
        91,
        92,
        93,
        94,
        95,
        96,
        97,
        98,
        99,
        100,
    ],
    "Hamilton": [
        1,
        6,
        7,
        8,
        9,
        11,
        12,
        13,
        15,
        16,
        17,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        59,
        60,
        61,
        65,
        66,
        67,
        68,
        69,
        70,
        71,
        72,
        73,
        74,
        75,
        76,
        77,
        78,
        79,
        80,
        81,
        82,
        83,
        84,
        85,
    ],
    "Jay": [2, 3, 4, 5],
    "Shared": [18, 19, 20],
    "Disputed": [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 62, 63],
}


def read_files(file_name):
    strings = []

    for file in file_name:
        with open(
            f"data/author_stylometry_source/federalist_{file}.txt",
            "r",
            encoding="utf-8",
        ) as f:
            strings.append(f.read())
    return "\n".join(strings)


federalist_by_author = {}
for author, files in papers.items():
    federalist_by_author[author] = read_files(files)

authors = ("Madison", "Hamilton", "Jay", "Shared", "Disputed")

author_tokens = {}
length_distribution = {}

for author in authors:
    tokens = nltk.word_tokenize(federalist_by_author[author])
    author_tokens[author] = [token for token in tokens if token.isalpha()]
    token_lengths = [len(token) for token in author_tokens[author]]
    length_distribution[author] = nltk.FreqDist(token_lengths)
    length_distribution[author].plot(15, title=f"Word Length Distribution for {author}")
