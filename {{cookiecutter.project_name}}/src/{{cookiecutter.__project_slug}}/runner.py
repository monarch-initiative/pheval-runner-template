from dataclasses import dataclass
from pathlib import Path

from pheval.runners.runner import PhEvalRunner


@dataclass
class {{cookiecutter.runner_name}}(PhEvalRunner):

    input_dir: Path
    testdata_dir: Path
    tmp_dir: Path
    output_dir: Path
    config_file: Path
    version: str

    def prepare(self):
        """prepare"""
        print("preparing")

    def run(self):
        """run"""
        print("running")

    def post_process(self):
        """post_process"""
        print("post processing")
