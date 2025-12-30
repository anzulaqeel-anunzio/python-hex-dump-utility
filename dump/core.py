# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import sys

class HexDumper:
    @staticmethod
    def dump(file_path, width=16):
        try:
            with open(file_path, 'rb') as f:
                offset = 0
                while True:
                    chunk = f.read(width)
                    if not chunk:
                        break
                    
                    # Offset
                    hex_offset = f"{offset:08x}"
                    
                    # Hex bytes
                    hex_bytes = " ".join(f"{b:02x}" for b in chunk)
                    
                    # Ascii representation
                    ascii_repr = "".join(chr(b) if 32 <= b <= 126 else "." for b in chunk)
                    
                    # Padding if last chunk
                    padding = "   " * (width - len(chunk))
                    
                    yield f"{hex_offset}  {hex_bytes}{padding}  |{ascii_repr}|"
                    
                    offset += len(chunk)
                    
        except FileNotFoundError:
            yield f"Error: File '{file_path}' not found."
        except Exception as e:
            yield f"Error reading file: {e}"

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
