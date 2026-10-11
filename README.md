# IK test set for QP solvers

This repository contains quadratic programs (QPs) arising from differential inverse kinematics in robotics, in a format suitable for [qpbenchmark](https://github.com/qpsolvers/qpbenchmark). Here is the report produced by this benchmarking tool:

- 📈 <a href="results/ik_qpbenchmark.md"><strong>IK test set results</strong></a> (⚠️ work in progress: still crunching the 2,592,000 solver calls of the test set)

## Installation

The recommended process is to install the benchmark and all solvers using [pixi](https://pixi.prefix.dev/):

```console
pixi install
```

It is also possible to install the benchmark [from PyPI](https://github.com/qpsolvers/qpbenchmark#installation).

## Usage

Run the test set as follows:

```
pixi run ik-qpbenchmark.py
```

The outcome is a standardized report comparing all available solvers against the different [benchmark metrics](https://github.com/qpsolvers/qpbenchmark#metrics). You can check out and post your own results in the [Results forum](https://github.com/qpsolvers/ik_qpbenchmark/discussions/categories/results).

## Citation

This test set is run using `qpbenchmark`. If you use it in your works, you can refer to it using [this citation](https://github.com/qpsolvers/qpbenchmark#citation).

## See also

Quadratic programs in this test set were generated with the [pink motions](https://github.com/pink-kinematics/pink_motions) library.

There are other test sets in qpbenchmark that may be relevant to your use cases:

- [Free-for-all](https://github.com/qpsolvers/free_for_all_qpbenchmark): community-built test set, new problems welcome!
- [Maros-Meszaros test set](https://github.com/qpsolvers/maros_meszaros_qpbenchmark/): a standard test set with problems designed to be difficult.
- [Model predictive control](https://github.com/qpsolvers/mpc_qpbenchmark): model predictive control problems arising e.g. in robotics.
