import dendropy as dp
import pandas as pd
from dendropy.calculate import treecompare
from glob import glob

diffs = []

file_list = glob.glob("output/*.tre")

bardenTree = dp.Tree.get_from_path("data/barden.tre", schema = "nexus", preserve_underscores = True)

for f in file_list:
  estimatedTree = d.Tree.get_from_path(f, schema = "nexus", preserve_underscores = True)

  estimatedTree.migrate_taxon_namespace(bardenTree.taxon_namespace)
  total_diffs = 2*len(bardenTree.nodes() - 2)

  diffs.append((treecompare.symmetric_difference(estimatedTree,bardenTree))/total_diffs)

df =   pd.DataFrame(
      {'rep': file_list,
       'RF': diffs
        })

df.to_csv("output")
