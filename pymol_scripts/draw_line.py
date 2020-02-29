from pymol import cmd, stored
from pymol.cgo import *

def draw_links(at1, at2):
  """
  usage: draw_links sele1 sele2

  """

  m1 = cmd.get_model(at1)
  m2 = cmd.get_model(at2)
  coord1 = []
  coord2 = []

  for a in m1.atom:
    if a.name == 'CA':
      coord1.append(a.coord)
  for b in m2.atom:
        if b.name == 'CA':
          coord2.append(b.coord)
 
  cyl_obj = []
  for x,y in zip(coord1,coord2):
    cyl_obj.extend([CYLINDER] + x + y + [0.1] + [1,0,0] + [1,0,0])
    object_name = "link" + at1 + "_" + at2
  cmd.load_cgo(cyl_obj,object_name)
cmd.extend("draw_links",draw_links)

l = [['196','212'],['197','66']]
chain = 'F'
pdb = "4jhw"

for e in l:
  f1 = pdb + " and " + "chain " + chain + " and resi " + e[0] +","
  f2 = pdb + " and " + "chain " + chain + " and resi " + e[1]
  draw_links(f1, f2)
