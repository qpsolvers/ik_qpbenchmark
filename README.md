# IK test set for QP solvers

This repository contains quadratic programs (QPs) arising from differential inverse kinematics in robotics, in a format suitable for [qpbenchmark](https://github.com/qpsolvers/qpbenchmark). Here is the report produced by this benchmarking tool:

- 📈 <a href="results/ik_qpbenchmark.md"><strong>IK test set results</strong></a> (⚠️ work in progress: still crunching the 2,592,000 solver calls of the test set)

## Installation

The recommended process is to install the benchmark and all solvers in an isolated environment using `conda`:

```console
conda env create -f environment.yaml
conda activate ik_qpbenchmark
```

It is also possible to install the benchmark [from PyPI](https://github.com/qpsolvers/qpbenchmark#installation).

## Usage

Run the test set as follows:

```
python ./ik_qpbenchmark.py run
```

The outcome is a standardized report comparing all available solvers against the different [benchmark metrics](https://github.com/qpsolvers/qpbenchmark#metrics). You can check out and post your own results in the [Results forum](https://github.com/qpsolvers/ik_qpbenchmark/discussions/categories/results).

## Citation

If you use `qpbenchmark` in your works, please cite all its contributors as follows:

```bibtex
@software{qpbenchmark2024,
  title = {{qpbenchmark: Benchmark for quadratic programming solvers available in Python}},
  author = {Caron, Stéphane and Zaki, Akram and Otta, Pavel and Arnström, Daniel and Carpentier, Justin and Yang, Fengyu and Leziart, Pierre-Alexandre},
  url = {https://github.com/qpsolvers/qpbenchmark},
  license = {Apache-2.0},
  version = {2.4.0},
  year = {2024}
}
```

If you contribute to this repository, don't forget to add yourself to the BibTeX above and to [`CITATION.cff`](https://github.com/qpsolvers/qpbenchmark/blob/main/CITATION.cff).

## See also

Quadratic programs in this test set were generated with [pink bench](https://github.com/stephane-caron/pink_bench).

There are other test sets in qpbenchmark that may be relevant to your use cases:

- [Free-for-all](https://github.com/qpsolvers/free_for_all_qpbenchmark): community-built test set, new problems welcome!
- [Maros-Meszaros test set](https://github.com/qpsolvers/maros_meszaros_qpbenchmark/): a standard test set with problems designed to be difficult.
- [Model predictive control](https://github.com/qpsolvers/mpc_qpbenchmark): model predictive control problems arising e.g. in robotics.
