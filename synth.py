import sir3d
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-b","--batch", type=int, default=256, help="batchsize")
parser.add_argument("-p","--path", default='./3D/', help="directory containing the SIR/MURaM files")
parser.add_argument("-X","--x1", type=int, default=0, help="x origin")
parser.add_argument("-Y","--y1", type=int, default=0, help="y origin")
parser.add_argument("-W","--width", type=int, default=0, help="width")
parser.add_argument("-H","--height", type=int, default=0, help="height")
args = parser.parse_args()

sirPath=args.path
x1=args.x1
x2=x1 + args.width
y1=args.y1
y2=y1 + args.height
batchSize=args.batch

iterator = sir3d.synth.Iterator(use_mpi=True, batch=batchSize)

mod = sir3d.synth.Model('%s/synth.ini'%(sirPath), rank=iterator.get_rank())
iterator.use_model(model=mod)

if (args.width * args.height == 0):
  iterator.run_all_pixels()
else:
  iterator.run_all_pixels(rangex=[x1,x2], rangey=[y1,y2])

