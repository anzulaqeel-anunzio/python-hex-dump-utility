# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dump.core import HexDumper

def main():
    parser = argparse.ArgumentParser(description="Hex Dump Utility")
    parser.add_argument("file", help="Input file")
    parser.add_argument("--width", "-w", type=int, default=16, help="Bytes per line (default: 16)")
    parser.add_argument("--output", "-o", help="Output text file")

    args = parser.parse_args()

    # Generator to memory efficient
    lines = HexDumper.dump(args.file, args.width)
    
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                for line in lines:
                    f.write(line + "\n")
            print(f"Hex dump saved to {args.output}")
        except Exception as e:
            print(f"Error writing output: {e}")
            sys.exit(1)
    else:
        for line in lines:
            print(line)
            # Simple error handling if generator yields error first
            if line.startswith("Error"):
                sys.exit(1)

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
