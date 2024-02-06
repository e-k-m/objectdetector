"""
CLI of objectdetector.

Usage
-----
objectdetector I love batman

or

python -m objectdetector.cli my I love batman
"""

import argparse
import sys

import objectdetector


def main():
    parser = argparse.ArgumentParser(description="objectdetector <some message>")
    parser.add_argument("message", nargs="*")
    args = " ".join(parser.parse_args().message)
    if args:
        print(objectdetector.say(args))
    else:
        print(objectdetector.say("no message"))


if __name__ == "__main__":
    sys.exit(main())
