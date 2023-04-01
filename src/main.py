import getopt
import random as rand
import sys

import pulp as lp


def main(argv):
    inputfile: str = "in.txt"
    outputfile: str = "out.txt"
    instance: list[list[int]] = []

    help_msg: str = """\
test.py -i <inputfile> -o <outputfile> -r <random_instance>
--rows <number_of_rows> --cols <number_of_cols>
--dens <mine_density>\
"""

    try:
        opts, _ = getopt.getopt(
            argv,
            "hi:o:r",
            [
                "help",
                "input_file=",
                "output_file=",
                "rand_instance",
                "rows=",
                "cols=",
                "dens=",
            ],
        )

    except getopt.GetoptError:
        print(help_msg)
        sys.exit(2)

    opts_dict = dict(opts)

    if "-h" in opts_dict or "--help" in opts_dict:
        print(help_msg)
        sys.exit()
    if "-i" in opts_dict or "--input_file" in opts_dict:
        if "-i" in opts_dict:
            inputfile = opts_dict["-i"]
        else:
            inputfile = opts_dict["--input_file"]
        instance = load_instance(inputfile)
    if "-o" in opts_dict or "--output_file" in opts_dict:
        if "-o" in opts_dict:
            outputfile = opts_dict["-o"]
        else:
            outputfile = opts_dict["--output_file"]

    if "-r" in opts_dict or "--rand_instance" in opts_dict:
        if (
            "--rows" not in opts_dict
            or "--cols" not in opts_dict
            or "--dens" not in opts_dict
        ):
            raise ValueError(
                "Must specify rows, columns, and mine density for random instance."
            )
        else:
            rows = int(opts_dict["--rows"])
            cols = int(opts_dict["--cols"])
            dens = float(opts_dict["--dens"])
        instance = generate_instance(rows, cols, dens)

    result = run_game(instance)

    with open(outputfile, "w") as file:
        for key, value in result.items():
            file.write(f"{key}:\n{value}\n")


def load_instance(filepath: str) -> list[list[int]]:
    instance: list[list[int]] = []
    with open(filepath) as file:
        for line in file:
            instance += [list(map(int, line.split(",")))]
    return instance


def generate_instance(rows: int, cols: int, dens: float) -> list[list[int]]:
    instance: list[list[int]] = [
        [1 if rand.random() <= dens else 0 for _ in range(cols)] for _ in range(rows)
    ]
    return instance


def run_game(instance: list[list[int]]) -> dict[str, str]:
    while True:
        raise NotImplementedError


if __name__ == "__main__":
    main(sys.argv[1:])
