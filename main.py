import sys
import encoder, decoder

def main(argv):

    if argv[0] == "--encode":
        print encoder.encode("The quick brown fox jumps over the lazy dog")

    if argv[0] == "--decode":
        print decoder.decode("1442779157967667200000|262059538099831245374033664000000000|491524481646305217710445277411617404468653198242187500|54736736297607421875000000|26575780025450776966354193208522490921501091250000000000|5232777644455317290286534758400000|21499084800000|24555699822948576064581298828125000000000000|17936133750000")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "usage: python main.py [--encode|--decode]"
        sys.exit(1)

    main(sys.argv[1:])