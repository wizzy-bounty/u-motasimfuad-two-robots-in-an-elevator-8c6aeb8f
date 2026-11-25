import os

TEXT = "Your floor? My arm firmware calls pressing it flirting."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
