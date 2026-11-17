# Password Generator

A lightweight Python CLI script (`generate-password.py`) that generates hyphen-separated passwords containing lowercase letters, one uppercase letter, and one digit.

## Password Format

Each generated password consists of three 6-character segments separated by hyphens (`xxxxxx-xxxxxx-xxxxxx`, 20 characters total):

- Base characters: random lowercase ASCII letters (`a-z`)
- Guaranteed characters: 1 random uppercase ASCII letter (`A-Z`) and 1 random digit (`0-9`), placed at two distinct non-hyphen positions

Example output:

```text
e9qwpf-mlldwf-jJrlff
3dfolg-ajeOtz-learth
faiufs-pc6aVl-oihmlf
o8Uudu-itvlrs-nkzxxn
qaiofq-0wvqgc-Ksytfr
```

## Requirements

- Python 3 (uses only the standard library: `argparse`, `secrets`, `string`, and `sys`)

## Usage

Run the script interactively with Python 3:

```bash
python3 generate-password.py
```

Or pass the count directly via `-n` / `--count`:

```bash
python3 generate-password.py -n 3
```

You can also run it directly as an executable (uses `#!/usr/bin/env python3`):

```bash
chmod +x generate-password.py
./generate-password.py --count 5
```

When run without `-n` / `--count`, the script prompts until a positive integer is entered:

```text
How many passwords would you like to generate? 3
```

### Options

- `-n`, `--count`: Number of passwords to generate (must be a positive integer). Prompts interactively if omitted.
- `-h`, `--help`: Show usage help and exit.
