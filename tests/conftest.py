import os
import sys

from matplotlib.projections import projection_registry

project_root = os.path.join(os.path.dirname(__file__),"..")
print("PROJECT ROOT :", project_root)
sys.path.insert(0, project_root)
print(sys.path)
