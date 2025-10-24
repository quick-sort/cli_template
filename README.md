A Simple Cli Tempalte
=====================

```
uv run python app/cli/main.py echo test
```

Add new command file in `app/cli` folder.

For example

```python
async def command(args):
    print(args.content)


def registry_command(subparsers):
    parser = subparsers.add_parser("echo", help="Echo command")
    parser.set_defaults(func=command)
    parser.add_argument("content", help="Echo content")
    return parser
```

