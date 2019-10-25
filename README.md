# README

## Simulation tree and Datasets

Simulate under the tree from [Barden and Grimaldi (2016)](http://www.cell.com/current-biology/abstract/S0960-9822(16)00041-5). This is a 41 taxon tree with 42 binary and MS characters.

1) Simulate 100 sets of binary and trinary characters. Combine these into datasets that have 2 & 3 state characters. Estimate phylogenies under a tristate model, and under one where the number of states is partitioned.

2) Repeat for 4 and 5 state characters. For each, hold the number of sites constant, but increase the division. I.e., for 4 state, each state number partition should be 1/3 of the dataset. Run under both the highest number of states single partition, and each state being its own partition. We are doing this to see how far we can subdivide and still have the analysis converge. Paleo datasets can be quite small.








## Hidden state simulations

1) Replace the third state with a '-'. Run under a binary model.