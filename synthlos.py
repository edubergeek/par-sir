import sir3d
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-b","--batch", type=int, default=1, help="batch size")
parser.add_argument("-p","--path", default='./3D/', help="path to the synth.ini file")
parser.add_argument("-X","--x1", type=int, default=0, help="x origin")
parser.add_argument("-Y","--y1", type=int, default=0, help="y origin")
parser.add_argument("-W","--width", type=int, default=1, help="width")
parser.add_argument("-H","--height", type=int, default=1, help="height")
args = parser.parse_args()

sirPath=args.path
x1=args.x1
x2=x1 + args.width
y1=args.y1
y2=y1 + args.height
batchSize=args.batch

iterator = sir3d.synth.Iterator(use_mpi=True, batch=batchSize)

mod = sir3d.synth.Model('%s'%(sirPath), rank=iterator.get_rank())
iterator.use_model(model=mod)

#if (args.width*args.height > 0):
iterator.run_all_pixels(rangex=[0,1], rangey=[0,1])
#else:
#  iterator.run_all_pixels()

