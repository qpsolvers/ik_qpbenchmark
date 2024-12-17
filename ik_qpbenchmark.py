#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

from pathlib import Path

import qpbenchmark
from qpbenchmark.benchmark import main


class IkQpbenchmark(qpbenchmark.ParquetTestSet):
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
        script_dir = Path(__file__).resolve().parent
        parquet_path = script_dir / "data" / "ik_qpbenchmark.parquet"
        super().__init__(parquet_path)


if __name__ == "__main__":
    test_set_path = Path(__file__).resolve()
    results_path = (
        test_set_path.parent / "results" / "qpbenchmark_results.parquet"
    )
    main(test_set_path=test_set_path, results_path=results_path)
