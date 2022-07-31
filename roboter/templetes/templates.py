#!/usr/bin/env python3

import sys
import string


def load_template(template_file):
    with open(template_file, "r") as template_file:
        t = string.Template(template_file.read())
        contents = t.substitute(name="John", contents="How are you?")
        print(contents)


def main():
    load_template("frontpage/index_templates.html")


if __name__ == "__main__":
    main()
