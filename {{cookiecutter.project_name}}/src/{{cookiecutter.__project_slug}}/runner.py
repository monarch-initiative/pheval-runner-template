"""Runner."""

from dataclasses import dataclass
from pathlib import Path

from pheval.runners.runner import PhEvalRunner


@dataclass
class {{cookiecutter.runner_name}}(PhEvalRunner):
    """Runner class implementation."""

    input_dir: Path
    testdata_dir: Path
    tmp_dir: Path
    output_dir: Path
    config_file: Path
    version: str

    def prepare(self):
        """Prepare."""
        print("preparing")

    def run(self):
        """Run."""
        print("running")

    def post_process(self):
        """Post Process."""
        print("post processing")
