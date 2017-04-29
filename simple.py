import sys
import argparse

arguments = sys.argv[0:]
parser = argparse.ArgumentParser()

parser.add_argument('--i', '--initial', type=str, dest='InitialArgument')
args = parser.parse_args()

print(__name__)


print(type(arguments), arguments)
