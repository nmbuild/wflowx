import argparse
from ci_converter.core.registry import get_parser, get_generator

def main():
    parser = argparse.ArgumentParser(
        description="Multi‐tool CI/CD converter: parse from one platform and emit to another."
    )
    parser.add_argument(
        '--from', dest='src', required=True,
        choices=list(get_parser.keys()),
        help='Source platform key (e.g. github)'
    )
    parser.add_argument(
        '--to', dest='dst', required=True,
        choices=list(get_generator.keys()),
        help='Target platform key (e.g. gitlab)'
    )
    parser.add_argument('-i','--in',  dest='infile',  required=True,
                        help='Input CI/CD config file')
    parser.add_argument('-o','--out', dest='outfile', required=True,
                        help='Output file to write')

    args = parser.parse_args()

    pipeline = get_parser(args.src).parse(args.infile)
    output  = get_generator(args.dst).generate(pipeline)

    with open(args.outfile, 'w') as f:
        f.write(output)
    print(f"Wrote converted CI file to {args.outfile}")

if __name__ == '__main__':
    main()