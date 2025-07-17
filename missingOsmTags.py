#!/usr/bin/env -S uv run python
from osmTags import osmTagsForTheme
from themes import themes


def main():
    for collection in themes:
        for theme in collection.themes:
            if theme.umKey not in osmTagsForTheme:
                print(f'"{theme.umKey}": [["TAG=TODO"]],')


if __name__ == "__main__":
    main()
