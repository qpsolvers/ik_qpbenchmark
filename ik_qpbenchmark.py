#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

import os
from typing import Iterator

import qpbenchmark
from qpbenchmark import Problem, ProblemList
from qpbenchmark.benchmark import main


class IkQpbenchmark(qpbenchmark.TestSet):
    """IK test set."""

    @property
    def description(self) -> str:
        return (
            "Differential inverse kinematics QP problems "
            "generated from robot motions"
        )

    @property
    def title(self) -> str:
        return "IK test set"

    @property
    def sparse_only(self) -> bool:
        return False

    def __init__(self):
        super().__init__()
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_dir = os.path.join(script_dir, "data")

    def __iter__(self) -> Iterator[Problem]:
        """Iterate over test set problems."""
        for filename in os.listdir(self.data_dir):
            if filename.endswith(".parquet"):
                filepath = os.path.join(self.data_dir, filename)
                yield from ProblemList.yield_from_parquet(filepath)


if __name__ == "__main__":
    test_set_path = os.path.abspath(__file__)
    test_set_dir = os.path.dirname(test_set_path)
    main(
        test_set_path=test_set_path,
        results_path=f"{test_set_dir}/results/qpbenchmark_results.csv",
    )
