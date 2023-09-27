import re


def main():
    print(parse(input("HTML: ")))


def parse(s):

    if match := re.search(r".+src=\"(https?://(?:www\.)?youtube\.com/embed/\w+)\".+", s):
        short_url = re.sub(r"https?://(?:www\.)?youtube\.com/embed", "https://youtu.be",(match[1]))
        return short_url
    else:
        return None


if __name__ == "__main__":
    main()