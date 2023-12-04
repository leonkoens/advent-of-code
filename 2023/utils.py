from dataclasses import dataclass


@dataclass
class InputReader:

    filename: str
    parser: object

    def read(self):

        with open(self.filename, 'r') as handle:

            while True:
                line = handle.readline().strip()

                if not line:
                    break

                self.parser.parse_line(line)
        