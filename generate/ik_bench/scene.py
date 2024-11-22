#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

from typing import List

import meshcat_shapes
import pink
import pinocchio as pin
from numpy.typing import NDArray
from pink.tasks import FrameTask
from pink.utils import custom_configuration_vector
from pink.visualization import start_meshcat_visualizer
from robot_descriptions.loaders.pinocchio import load_robot_description

from .scenario import Scenario


class Scene:
    configuration: pink.Configuration
    robot: pin.RobotWrapper

    def __init__(
        self, scenario: Scenario, visualize: bool = False, record: bool = False
    ):
        """Create a new scene.

        Args:
            scenario: Scene description.
            visualize: If set, visualize scenario in MeshCat.
            record: If set, each frame will be rendered to an image as well.

        Raises:
            ValueError: if the scenario is empty.
            IndexError: if the initial configuration does not match the robot
                model.
        """
        robot = load_robot_description(
            description_name=scenario.robot_description,
            root_joint=scenario.root_joint,
        )

        visualizer = None
        viewer = None
        if visualize:
            visualizer = start_meshcat_visualizer(robot)
            viewer = visualizer.viewer

        if len(scenario.trajectories) < 1:
            robot_frames = [
                frame.name
                for frame in robot.model.frames
                if frame.name != "universe"
            ]
            raise ValueError(
                "Scenario is empty, maybe add a task for one of:\n\n- "
                + ("\n- ".join(robot_frames))
            )

        try:
            q_init = custom_configuration_vector(
                robot, **scenario.initial_configuration
            )
        except IndexError as exn:
            queried_joints = list(scenario.initial_configuration.keys())
            valid_joints = list(robot.model.names)
            raise IndexError(
                f"One joint in {queried_joints} not found, "
                f"names must be in {valid_joints}"
            ) from exn

        if visualize:
            visualizer.display(q_init)
        configuration = pink.Configuration(robot.model, robot.data, q_init)
        for trajectory in scenario.trajectories:
            trajectory.reset(configuration, viewer)
            task = trajectory.task
            if viewer is not None and hasattr(task, "frame"):
                frame = task.frame
                meshcat_shapes.frame(viewer[f"{frame}_current"], opacity=1.0)
                meshcat_shapes.frame(viewer[f"{frame}_target"], opacity=0.5)

        self.configuration = configuration
        self.record = record
        self.recording_index = 0
        self.q_init = q_init
        self.robot = robot
        self.scenario = scenario
        self.trajectories = scenario.trajectories
        self.viewer = viewer
        self.visualizer = visualizer

    def reset(self):
        model = self.robot.model
        data = self.robot.data
        if self.visualizer is not None:
            self.visualizer.display(self.q_init)
        self.configuration = pink.Configuration(model, data, self.q_init)
        for trajectory in self.scenario.trajectories:
            trajectory.reset(self.configuration, self.viewer)

    @property
    def tasks(self) -> List[pink.Task]:
        return [trajectory.task for trajectory in self.trajectories]

    @property
    def frame_tasks(self) -> List[FrameTask]:
        return [
            trajectory.task
            for trajectory in self.trajectories
            if isinstance(trajectory.task, FrameTask)
        ]

    def step_targets(self, dt: float):
        for trajectory in self.trajectories:
            trajectory.step(dt)

    def update_viewer(self) -> None:
        """Update frames in the viewer."""
        if self.viewer is None:
            return
        for task in self.frame_tasks:
            if not hasattr(task, "frame"):
                continue
            frame = task.frame
            target = task.transform_target_to_world
            current = self.configuration.get_transform_frame_to_world(frame)
            self.viewer[f"{frame}_target"].set_transform(target.np)
            self.viewer[f"{frame}_current"].set_transform(current.np)

    def step(self, velocity: NDArray[float], dt: float) -> None:
        self.configuration.integrate_inplace(velocity, dt)
        if self.visualizer is not None:
            self.visualizer.display(self.configuration.q)
            if self.record:
                fname = f"videos/meshcat_{self.recording_index:04d}.png"
                self.recording_index += 1
                with open(fname, "wb") as fp:
                    self.viewer.get_image().save(fp)
