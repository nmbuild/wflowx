import argparse
from ci_converter.core.registry import get_parser, get_generator

def main():
    p = argparse.ArgumentParser(
        description="Convert GH step names → GitLab echo scripts"
    )
    p.add_argument('--from',  dest='src', required=True, choices=['github'])
    p.add_argument('--to',    dest='dst', required=True, choices=['gitlab'])
    p.add_argument('-i','--in',  dest='infile',  required=True)
    p.add_argument('-o','--out', dest='outfile', required=True)
    args = p.parse_args()

    pipeline = get_parser(args.src).parse(args.infile)
    output   = get_generator(args.dst).generate(pipeline)

    with open(args.outfile, 'w') as f:
        f.write(output)
    print(f"Wrote {args.outfile}")

if __name__ == '__main__':
    main()
