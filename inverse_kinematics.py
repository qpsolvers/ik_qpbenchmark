#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

import os
from typing import Iterator

import h5py
import numpy as np
import qpsolvers
from qpbenchmark.benchmark import main
from qpbenchmark.problem import Problem
from qpbenchmark.test_set import TestSet


class InverseKinematics(TestSet):
    """IK test set."""

    @property
    def description(self) -> str:
        """Description of the test set."""
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
        """Initialize test set."""
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_dir = os.path.join(current_dir, "data")

    def yield_sequence_from_file(self, file: h5py.File) -> qpsolvers.Problem:
        """Yield sequence of problems from a file.

        Args:
            file: The file object from which to yield the problems.

        Yields:
            Problem object read from file.
        """
        group = file["ik_Problem"]
        for problem in list(group.keys()):
            qp_data = {}
            for data_name in group[problem].keys():
                if f"{data_name}/data" in group[problem]:
                    data = group[f"{problem}/{data_name}/data"][:]
                    data[data > 9e19] = +np.inf
                    data[data < -9e19] = -np.inf
                    qp_data[data_name] = data
                else:
                    qp_data[data_name] = None
                qp_data["name"] = (
                    os.path.split(file.filename)[1].replace(".hdf5", "")
                    + "_"
                    + problem
                )
            qp_problem = Problem(**qp_data)
            yield qp_problem

    def __iter__(self) -> Iterator[Problem]:
        """Iterate over test set problems."""
        for filename in os.listdir(self.data_dir):
            if not filename.endswith(".hdf5"):
                continue
            filepath = os.path.join(self.data_dir, filename)
            with h5py.File(filepath, "r") as file:
                yield from self.yield_sequence_from_file(file)


if __name__ == "__main__":
    test_set_path = os.path.abspath(__file__)
    test_set_dir = os.path.dirname(test_set_path)
    main(
        test_set_path=test_set_path,
        results_path=f"{test_set_dir}/results/qpbenchmark_results.csv",
    )
