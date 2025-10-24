async def command(args):
    print(args.content)


def registry_command(subparsers):
    parser = subparsers.add_parser("echo", help="Echo command")
    parser.set_defaults(func=command)
    parser.add_argument("content", help="Echo content")
    return parser
