# File Hash Generator

A simple Python command-line tool to generate cryptographic hashes of files using any algorithm supported by Python's `hashlib` (MD5, SHA1, SHA256, SHA512, BLAKE2b, etc.).

## Features

- Supports all hash algorithms available in `hashlib`
- Reads files in chunks, so large files are handled without high memory usage
- Compute multiple hashes in a single run (comma-separated list)
- Clear error handling for missing files, permission issues, and unsupported algorithms

## Requirements

- Python 3.8+
- No external dependencies (uses only the standard library)

## Installation

1. Save the script as `hash_gen.py`.
2. No installation needed — just run it with Python.

## Usage

Basic usage (defaults to SHA256):

```bash
python hash_gen.py myfile.txt
```

Specify a single algorithm:

```bash
python hash_gen.py myfile.txt -a md5
```

Specify multiple algorithms at once:

```bash
python hash_gen.py myfile.txt -a md5,sha1,sha256
```

List of available algorithms is shown in the help text:

```bash
python hash_gen.py -h
```

## Example Output

```
$ python hash_gen.py myfile.txt -a md5,sha1,sha256
MD5       : 5d41402abc4b2a76b9719d911017c592
SHA1      : aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
SHA256    : 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

## Arguments

| Argument | Description | Default |
|---|---|---|
| `file` | Path to the file to hash (required) | — |
| `-a`, `--algorithm` | Comma-separated list of hash algorithms | `sha256` |

## Notes

- When multiple algorithms are specified, the file is currently re-read once per algorithm. For very large files and many algorithms, this means multiple full reads.
- Errors (missing file, bad permissions, unsupported algorithm) are reported per-algorithm without stopping the rest of the run.

## License

Free to use and modify.
