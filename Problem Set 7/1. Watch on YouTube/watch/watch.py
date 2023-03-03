def main():
    # Getting user input => sending it to parse & printing it's return value.
    print(parse(input("HTML: ").strip()))


def parse(s):
    """
    Returns string url from the given html string.
    """
    try:
        # Checking if string starts with '<iframe'.
        if s[0:7] == '<iframe':

            # Splitting link in 2 parts.
            embed_split = s.split('/embed/')

            # Splitting 2nd indexed value from embed_split list.
            link_id = embed_split[1].split('"')

            # Returning the final link as string.
            return f'https://youtu.be/{link_id[0]}'

        # Checking if string doesn't start with '<iframe'.
        else:
            return None

    # If incorrect link submitted.
    except IndexError:
        return None


if __name__ == '__main__':
    main()
    