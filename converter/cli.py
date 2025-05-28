import argparse
from ci_converter.core.registry import get_parser, get_generator

parser = argparse.ArgumentParser()
parser.add_argument('--from',   dest='src', required=True,
                    choices=['github','jenkins','azure'])
parser.add_argument('--to',     dest='dst', required=True,
                    choices=['gitlab','jenkinsfile','azure'])
parser.add_argument('-i','--in',  dest='infile',  required=True)
parser.add_argument('-o','--out', dest='outfile', required=True)
args = parser.parse_args()

pipeline = get_parser(args.src).parse(args.infile)
text     = get_generator(args.dst).generate(pipeline)

with open(args.outfile,'w') as f:
    f.write(text)
print(f"Wrote {args.outfile}")