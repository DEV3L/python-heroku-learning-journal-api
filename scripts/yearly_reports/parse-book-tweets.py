from functools import reduce

from scripts.tools import load_year_data, year, filter_classifiers, reduce_titles

reading_classifiers = [
    'started reading',
    'finished reading'
]


def filter_books(tweet: dict) -> bool:
    return filter_classifiers(tweet, reading_classifiers)


if __name__ == '__main__':
    tweets_from_year = load_year_data()

    books_from_this_year = list(filter(filter_books, tweets_from_year))
    book_titles = list(reduce(reduce_titles, books_from_this_year, set()))

    print(f'## {year} Books:')
    for book_title in book_titles:
        print(f'- {book_title}')
