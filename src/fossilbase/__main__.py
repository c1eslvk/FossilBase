from .services import pbdb, rendering


def main() -> None:
    rendering.render_map(pbdb.find_occurrences('Diplodocus,Ankylosaurus', None, None))


if __name__ == "__main__":
    main()