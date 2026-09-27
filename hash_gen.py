import hashlib
import argparse
import sys

def hash_file(filepath, algorithm='sha256', chunk_size=8192):
    """Compute the hash of a file using the specified algorithm."""
    try:
        hasher = hashlib.new(algorithm)
    except ValueError:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(chunk_size):
                hasher.update(chunk)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except PermissionError:
        raise PermissionError(f"Permission denied: {filepath}")

    return hasher.hexdigest()


def main():
    parser = argparse.ArgumentParser(description="Generate hash(es) of a file.")
    parser.add_argument("file", help="Path to the file")
    parser.add_argument(
        "-a", "--algorithm",
        default="sha256",
        help="Hash algorithm(s), comma-separated (e.g. md5,sha1,sha256). "
             f"Available: {', '.join(sorted(hashlib.algorithms_available))}"
    )
    args = parser.parse_args()

    algorithms = [a.strip() for a in args.algorithm.split(',')]

    for algo in algorithms:
        try:
            digest = hash_file(args.file, algo)
            print(f"{algo.upper():10s}: {digest}")
        except (ValueError, FileNotFoundError, PermissionError) as e:
            print(f"Error ({algo}): {e}", file=sys.stderr)


if __name__ == "__main__":
    main()