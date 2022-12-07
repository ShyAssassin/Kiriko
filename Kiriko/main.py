from Core.Kiriko import Kiriko
from dotenv import load_dotenv
load_dotenv()


def main() -> int:
    kirko = Kiriko()
    kirko.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
