# Hex Dump Utility

A command-line tool to inspect binary files in hexadecimal format. Useful for debugging, reverse engineering, or analyzing file structures.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Standard Format**: Displays offset, hex bytes, and ASCII representation side-by-side.
*   **Customizable Width**: Adjust the number of bytes shown per line.
*   **Memory Efficient**: Streams file content, suitable for large files.

## Usage

```bash
python run_hexdump.py [file] [options]
```

### Options

*   `--width`, `-w`: Number of bytes per line (default: 16).
*   `--output`, `-o`: Save output to a text file.

### Example

```bash
python run_hexdump.py image.png -w 32
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
