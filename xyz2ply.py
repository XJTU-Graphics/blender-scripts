# -*- coding: utf-8 -*-

from pathlib import Path
import logging
import sys

import numpy as np
from plyfile import PlyData, PlyElement


base_path = Path('/home/greyishsong/workspace/scps-output')
xyz_path = base_path / 'xyz'
ply_path = base_path / 'ply'

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

for pc_file in xyz_path.iterdir():
    with pc_file.open('r') as f:
        lines = f.readlines()
    vertices = [tuple(line.split()) for line in lines]
    vertices = np.array(vertices, dtype=[('x', 'f4'), ('y', 'f4'), ('z', 'f4')])
    element_v = PlyElement.describe(vertices, 'vertex')
    ply_filename = f'{pc_file.stem}.ply'
    dst_path = ply_path / ply_filename
    PlyData([element_v], text=True).write(dst_path.as_posix())
    logging.info(f'file {dst_path.as_posix()} has been generated')
