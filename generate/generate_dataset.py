#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

import argparse
from pathlib import Path
from typing import List, Tuple

import h5py
import ik_bench
import numpy as np
import pink
import qpsolvers
from numpy.typing import NDArray
from pink import build_ik
from qpbenchmark.exceptions import ResultsError

data_dir = Path(__file__).resolve().parent.parent / "data"


def parse_command_line_arguments() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        Namespace resulting from parsing command-line arguments.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--damping",
        help="Thikonov damping value for differential IK",
        type=float,
        default=1e-12,
    )
    parser.add_argument(
        "--qpsolver",
        help="solver for the QP-based approach",
        default="proxqp",
        choices=qpsolvers.available_solvers,
    )
    parser.add_argument(
        "--scenario",
        help="generate problems only from a single scenario",
        choices=list([name for name in ik_bench.scenarios.keys()]),
    )
    parser.add_argument(
        "--timestep",
        help="Timestep in seconds between differential IK problems",
        type=float,
        default=0.005,
    )
    return parser.parse_args()


def build_and_solve_qp(
    configuration,
    tasks: List[pink.Task],
    dt: float,
    qpsolver: str,
    damping: float,
) -> Tuple[qpsolvers.Problem, NDArray[float]]:
    configuration.update()
    qp = build_ik(configuration, tasks, dt, damping=damping)
    result = qpsolvers.solve_problem(qp, solver=qpsolver)
    Delta_q = result.x
    if Delta_q is None:
        raise ResultsError("Could not solve differential IK problem")
    velocity = Delta_q / dt
    return qp, velocity


def generate_scenario(
    scenario_name: str,
    dt: float,
    qpsolver: str,
    damping: float,
):
    scenario = ik_bench.scenarios[scenario_name]
    scene = ik_bench.Scene(scenario)
    scene.reset()
    for it_num, t in enumerate(np.arange(0.0, scenario.duration, dt)):
        scene.step_targets(dt)
        scene.update_viewer()
        velocity = solve_qp(
            scene.configuration,
            scene.tasks,
            dt,
            qpsolver,
            damping,
        )
        if verbose:
            print(f"t={t:.2f}\tq={np.round(scene.configuration.q, 2)}\t")
        scene.step(velocity, dt)


if __name__ == "__main__":
    args = parse_command_line_arguments()
    scenarios: List[str] = (
        [args.scenario]
        if args.scenario is not None
        else list(ik_bench.scenarios.keys())
    )
    for scenario_name in scenarios:
        generate_scenario(
            scenario_name, args.timestep, args.qpsolver, args.damping
        )
