# GitHub free-for-all test set

| Version | 0.1.0rc4 |
|:--------|:--------------------|
| Date    | 2023-06-22 15:00:31.948080+00:00 |
| CPU     | Intel64 Family 6 Model 142 Stepping 9, GenuineIntel |
| Run by  | [@ZAKIAkram](https://github.com/ZAKIAkram/) |

## Contents

* [Description](#description)
* [Solvers](#solvers)
* [Settings](#settings)
* [Known limitations](#known-limitations)
* [Results by settings](#results-by-settings)
    * [Default](#default)
    * [High accuracy](#high-accuracy)
    * [Low accuracy](#low-accuracy)
* [Results by metric](#results-by-metric)
    * [Success rate](#success-rate)
    * [Computation time](#computation-time)
    * [Optimality conditions](#optimality-conditions)
        * [Primal residual](#primal-residual)
        * [Dual residual](#dual-residual)
        * [Duality gap](#duality-gap)
    * [Cost error](#cost-error)

## Description

hdf5 test set, contains qp problems related to robots movements

## Solvers

| solver   | version   |
|:---------|:----------|
| clarabel | 0.5.1     |
| cvxopt   | 1.3.1     |
| daqp     | 0.5.1     |
| ecos     | 2.0.12    |
| highs    | 1.5.3     |
| osqp     | 0.6.3     |
| proxqp   | 0.3.7     |
| quadprog | 0.1.11    |
| scs      | 3.2.3     |

All solvers were called via
[qpsolvers](https://github.com/stephane-caron/qpsolvers)
v3.4.0.

## Settings

There are 3 settings: *default*, *high_accuracy*
and *low_accuracy*. They validate solutions using the following
tolerances:

| tolerance   |   default |   low_accuracy |   high_accuracy |
|:------------|----------:|---------------:|----------------:|
| ``cost``    |    0.0001 |         0.001  |           1e-05 |
| ``dual``    |    0.001  |         0.001  |           1e-07 |
| ``gap``     |    0.001  |         0.0001 |           0.001 |
| ``primal``  |    0.001  |         0.001  |           1e-07 |
| ``runtime`` |    1      |         1      |           1     |

Solvers for each settings are configured as follows:

| solver   | parameter                        | default   |   high_accuracy |   low_accuracy |
|:---------|:---------------------------------|:----------|----------------:|---------------:|
| clarabel | ``tol_feas``                     | -         |           1e-09 |          0.001 |
| clarabel | ``tol_gap_abs``                  | -         |           1e-09 |          0.001 |
| clarabel | ``tol_gap_rel``                  | -         |           0     |          0     |
| cvxopt   | ``feastol``                      | -         |           1e-09 |          0.001 |
| daqp     | ``dual_tol``                     | -         |           1e-09 |          0.001 |
| daqp     | ``primal_tol``                   | -         |           1e-09 |          0.001 |
| ecos     | ``feastol``                      | -         |           1e-09 |          0.001 |
| highs    | ``dual_feasibility_tolerance``   | -         |           1e-09 |          0.001 |
| highs    | ``primal_feasibility_tolerance`` | -         |           1e-09 |          0.001 |
| highs    | ``time_limit``                   | 1         |           1     |          1     |
| osqp     | ``eps_abs``                      | -         |           1e-09 |          0.001 |
| osqp     | ``eps_rel``                      | -         |           0     |          0     |
| osqp     | ``time_limit``                   | 1         |           1     |          1     |
| proxqp   | ``check_duality_gap``            | -         |           1     |          1     |
| proxqp   | ``eps_abs``                      | -         |           1e-09 |          0.001 |
| proxqp   | ``eps_duality_gap_abs``          | -         |           1e-09 |          0.001 |
| proxqp   | ``eps_duality_gap_rel``          | -         |           0     |          0     |
| proxqp   | ``eps_rel``                      | -         |           0     |          0     |
| scs      | ``eps_abs``                      | -         |           1e-09 |          0.001 |
| scs      | ``eps_rel``                      | -         |           0     |          0     |
| scs      | ``time_limit_secs``              | 1         |           1     |          1     |

## Known limitations

The following [issues](https://github.com/qpsolvers/qpsolvers_benchmark/issues)
have been identified as impacting the fairness of this benchmark. Keep them in
mind when drawing conclusions from the results.

- [#60](https://github.com/qpsolvers/qpsolvers_benchmark/issues/60):
  Conversion to SOCP limits performance of ECOS

## Results by settings

### Default

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                87.3 |                                  2.7 |                                         1.0 |                                    99.0 |                           1749456.0 |                               1.0 |
| cvxopt   |                                87.3 |                                 62.7 |                                         1.0 |                                     1.0 |                          15833559.0 |                               1.0 |
| daqp     |                                87.3 |                                  1.2 |                                         1.0 |                                     1.0 |                                 1.0 |                               1.0 |
| ecos     |                                87.3 |                                  5.9 |                                         1.0 |                             655416894.0 |                           2063259.0 |                               1.0 |
| highs    |                                26.0 |                               1616.5 |                              157620312750.0 |                         1267915943521.0 |                      178817976389.0 |                               1.2 |
| osqp     |                                87.3 |                                  4.1 |                               29823090582.0 |                           15810307520.0 |                         811108465.0 |                               1.0 |
| proxqp   |                                87.3 |                                 19.6 |                                 199248150.0 |                               2148359.0 |                         144964621.0 |                               1.0 |
| quadprog |                                87.3 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |                               1.0 |
| scs      |                                87.3 |                                  4.3 |                               16327694017.0 |                            9389729045.0 |                         275241210.0 |                               1.0 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                68.0 |                                  2.8 |                                         1.0 |                                    19.0 |                             61684.0 |                               1.0 |
| cvxopt   |                                68.0 |                                 62.5 |                                         1.0 |                                     1.0 |                          15833559.0 |                               1.0 |
| daqp     |                                68.0 |                                  1.1 |                                         1.0 |                                     1.0 |                                 1.0 |                               1.0 |
| ecos     |                                 6.0 |                                  6.1 |                                         1.0 |                             655416894.0 |                           2063259.0 |                               1.0 |
| highs    |                                 5.3 |                               1617.5 |                                  15762601.0 |                         1110280310193.0 |                      178817976389.0 |                               1.0 |
| osqp     |                                68.0 |                                  4.3 |                                     30804.0 |                                 21219.0 |                               714.0 |                               1.0 |
| proxqp   |                                68.0 |                                 21.1 |                                     24971.0 |                                117874.0 |                              9029.0 |                               1.0 |
| quadprog |                                68.0 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |                               1.0 |
| scs      |                                67.3 |                                 42.6 |                                    410831.0 |                                389176.0 |                        3752813980.0 |                               1.0 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                93.3 |                                  2.7 |                                         1.0 |                                     1.0 |                        1859344978.0 |                               1.0 |
| cvxopt   |                                93.3 |                                 67.2 |                                         1.0 |                                     1.0 |                          15833559.0 |                               1.0 |
| daqp     |                                92.0 |                                  1.2 |                               61088618598.0 |                                     1.0 |                                 1.0 |                               1.0 |
| ecos     |                                93.3 |                                  6.4 |                                         1.0 |                             655416894.0 |                           2063259.0 |                               1.0 |
| highs    |                                26.0 |                               1730.9 |                              157620312750.0 |                         1267915943521.0 |                       36959671447.0 |                               2.7 |
| osqp     |                                93.3 |                                  4.3 |                               29860224064.0 |                           15282109354.0 |                         763156130.0 |                               1.0 |
| proxqp   |                                93.3 |                                 18.2 |                               43168390911.0 |                              39645049.0 |                        1756648110.0 |                               1.0 |
| quadprog |                                93.3 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |                               1.0 |
| scs      |                                93.3 |                                  4.7 |                               19605389903.0 |                           11381779457.0 |                         765322808.0 |                               1.0 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |        87 |              68 |             93 |
| cvxopt   |        87 |              68 |             93 |
| daqp     |        87 |              68 |             92 |
| ecos     |        87 |               6 |             93 |
| highs    |        26 |               5 |             26 |
| osqp     |        87 |              68 |             93 |
| proxqp   |        87 |              68 |             93 |
| quadprog |        87 |              68 |             93 |
| scs      |        87 |              67 |             93 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider
that a solver successfully solved a problem when (1) it returned with a success
status and (2) its solution satisfies optimality conditions within
[tolerance](#settings). The second table below summarizes the frequency at
which solvers return success (1) and the corresponding solution did indeed pass
tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |        87 |              68 |             93 |
| cvxopt   |        87 |              68 |             93 |
| daqp     |        87 |              68 |             92 |
| ecos     |        87 |               6 |             93 |
| highs    |        54 |              33 |             54 |
| osqp     |        87 |              68 |             93 |
| proxqp   |        87 |              68 |             93 |
| quadprog |        87 |              68 |             93 |
| scs      |        87 |              68 |             93 |

### Computation time

We compare solver computation times over the whole test set using the shifted
geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of
Y is Y times slower than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       2.7 |             2.8 |            2.7 |
| cvxopt   |      62.7 |            62.5 |           67.2 |
| daqp     |       1.2 |             1.1 |            1.2 |
| ecos     |       5.9 |             6.1 |            6.4 |
| highs    |    1616.5 |          1617.5 |         1730.9 |
| osqp     |       4.1 |             4.3 |            4.3 |
| proxqp   |      19.6 |            21.1 |           18.2 |
| quadprog |       1.0 |             1.0 |            1.0 |
| scs      |       4.3 |            42.6 |            4.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in
the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time
limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint
violation in the solution returned by a solver. We use the shifted geometric
mean to compare solver primal residuals over the whole test set. Intuitively, a
solver with a shifted-geometric-mean primal residual of Y is Y times less
precise on constraints than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |        default |   high_accuracy |   low_accuracy |
|:---------|---------------:|----------------:|---------------:|
| clarabel |            1.0 |             1.0 |            1.0 |
| cvxopt   |            1.0 |             1.0 |            1.0 |
| daqp     |            1.0 |             1.0 |  61088618598.0 |
| ecos     |            1.0 |             1.0 |            1.0 |
| highs    | 157620312750.0 |      15762601.0 | 157620312750.0 |
| osqp     |  29823090582.0 |         30804.0 |  29860224064.0 |
| proxqp   |    199248150.0 |         24971.0 |  43168390911.0 |
| quadprog |            1.0 |             1.0 |            1.0 |
| scs      |  16327694017.0 |        410831.0 |  19605389903.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a primal residual equal to the
full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility
condition in the solution returned by a solver. We use the shifted geometric
mean to compare solver dual residuals over the whole test set. Intuitively, a
solver with a shifted-geometric-mean dual residual of Y is Y times less precise
on the dual feasibility condition than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |         default |   high_accuracy |    low_accuracy |
|:---------|----------------:|----------------:|----------------:|
| clarabel |            99.0 |            19.0 |             1.0 |
| cvxopt   |             1.0 |             1.0 |             1.0 |
| daqp     |             1.0 |             1.0 |             1.0 |
| ecos     |     655416894.0 |     655416894.0 |     655416894.0 |
| highs    | 1267915943521.0 | 1110280310193.0 | 1267915943521.0 |
| osqp     |   15810307520.0 |         21219.0 |   15282109354.0 |
| proxqp   |       2148359.0 |        117874.0 |      39645049.0 |
| quadprog |             1.0 |             1.0 |             1.0 |
| scs      |    9389729045.0 |        389176.0 |   11381779457.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a dual residual equal to the full
[dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions
returned by a solver. A duality gap close to zero ensures that the
complementarity slackness optimality condition is satisfied. We use the shifted
geometric mean to compare solver duality gaps over the whole test set.
Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times
less precise on the complementarity slackness condition than the best solver
over the test set. See [Metrics](../README.md#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |        default |   high_accuracy |   low_accuracy |
|:---------|---------------:|----------------:|---------------:|
| clarabel |      1749456.0 |         61684.0 |   1859344978.0 |
| cvxopt   |     15833559.0 |      15833559.0 |     15833559.0 |
| daqp     |            1.0 |             1.0 |            1.0 |
| ecos     |      2063259.0 |       2063259.0 |      2063259.0 |
| highs    | 178817976389.0 |  178817976389.0 |  36959671447.0 |
| osqp     |    811108465.0 |           714.0 |    763156130.0 |
| proxqp   |    144964621.0 |          9029.0 |   1756648110.0 |
| quadprog |            1.0 |             1.0 |            1.0 |
| scs      |    275241210.0 |    3752813980.0 |    765322808.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a duality gap equal to the full
[gap tolerance](#settings).

### Cost error

The cost error measures the difference between the known optimal objective and
the objective at the solution returned by a solver. We use the shifted
geometric mean to compare solver cost errors over the whole test set.
Intuitively, a solver with a shifted-geometric-mean cost error of Y is Y times
less precise on the optimal cost than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric means of solver cost errors (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       1.0 |             1.0 |            1.0 |
| cvxopt   |       1.0 |             1.0 |            1.0 |
| daqp     |       1.0 |             1.0 |            1.0 |
| ecos     |       1.0 |             1.0 |            1.0 |
| highs    |       1.2 |             1.0 |            2.7 |
| osqp     |       1.0 |             1.0 |            1.0 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| quadprog |       1.0 |             1.0 |            1.0 |
| scs      |       1.0 |             1.0 |            1.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
