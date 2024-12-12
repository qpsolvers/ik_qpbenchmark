#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

import argparse
import glob
import os
import subprocess
from pathlib import Path
from typing import List

import numpy as np
import qpbenchmark
import qpsolvers
from pink import build_ik
from qpbenchmark.exceptions import ResultsError
from qpbenchmark.spdlog import logging

import pink_bench


def parse_command_line_arguments() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        Namespace resulting from parsing command-line arguments.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--plot-mpc-axis",
        help="plot to debug LIP model predictive control",
        choices=("x", "y", None),
        default=None,
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
        choices=list([name for name in pink_bench.scenarios.keys()]),
    )
    parser.add_argument(
        "--timestep",
        help="Timestep in seconds between differential IK problems",
        type=float,
        default=0.005,
    )
    parser.add_argument(
        "--record",
        help="Record video from MeshCat",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "--visualize",
        help="Display scenes in MeshCat while they play out",
        default=False,
        action="store_true",
    )
    return parser.parse_args()


def generate_problems(
    scene: pink_bench.Scene,
    scenario_name: str,
    dt: float,
    qpsolver: str,
) -> qpbenchmark.ProblemList:
    problems = qpbenchmark.ProblemList()
    for it_num, t in enumerate(np.arange(0.0, scenario.duration, dt)):
        scene.step_targets(dt)
        qp = build_ik(scene.configuration, scene.tasks, dt)
        problems.append(
            qpbenchmark.Problem.from_qpsolvers(
                qp,
                name=f"{scenario_name}_{it_num:05}",
            )
        )
        result = qpsolvers.solve_problem(qp, solver=qpsolver)
        Delta_q = result.x
        if Delta_q is None:
            raise ResultsError("Could not solve differential IK problem")
        velocity = Delta_q / dt
        scene.step_velocity(velocity, dt)
    return problems


def save_video(name: str, frequency: int) -> None:
    video_output = f"videos/{name}.mp4"
    print(f"Saving video to {video_output}...")
    subprocess.run(
        [
            "ffmpeg",
            "-r",
            f"{frequency}",
            "-f",
            "image2",
            "-s",
            "1920x1080",
            "-i",
            f"videos/{name}_%04d.png",
            "-vcodec",
            "libx264",
            "-crf",
            "20",
            "-pix_fmt",
            "yuv420p",
            "-y",
            video_output,
        ]
    )
    print(f"Saved video to {video_output}")

    save_dir = f"videos/src-{name}"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    for img in glob.glob(f"videos/{name}_*.png"):
        subprocess.run(["mv", img, save_dir])
    print(f"Backed up images to {save_dir}")


if __name__ == "__main__":
    args = parse_command_line_arguments()
    scenarios: List[str] = (
        [args.scenario]
        if args.scenario is not None
        else list(pink_bench.scenarios.keys())
    )
    data_dir = Path(__file__).resolve().parent.parent / "data"
    problems = qpbenchmark.ProblemList()
    for scenario_name in scenarios:
        logging.info('Generating problems for scenario "%s"...', scenario_name)
        scenario = pink_bench.scenarios[scenario_name]
        scene = pink_bench.Scene(scenario, visualize=args.visualize)
        if args.plot_mpc_axis is not None:
            plot_axis = 0 if args.plot_mpc_axis == "x" else 1
            scene.plot_mpc_axis(plot_axis)
        problems.extend(
            generate_problems(
                scene,
                scenario_name,
                dt=args.timestep,
                qpsolver=args.qpsolver,
            )
        )
    problems.to_parquet(data_dir / "ik_qpbenchmark.parquet")
