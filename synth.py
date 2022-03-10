import sir3d
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-b","--batch", type=int, default=128, help="batchsize")
parser.add_argument("-i","--init", default='synth.ini', help="3DSIR configuration file")
parser.add_argument("-X","--x", type=int, default=0, help="x origin")
parser.add_argument("-Y","--y", type=int, default=0, help="y origin")
parser.add_argument("-W","--width", type=int, default=0, help="width")
parser.add_argument("-H","--height", type=int, default=0, help="height")
parser.add_argument("-m","--mpi", dest='useMPI', default=False, action='store_true', help="parallel execution with MPI")
args = parser.parse_args()

iniFile=args.init
x1=args.x
x2=x1 + args.width
y1=args.y
y2=y1 + args.height
batchSize=args.batch

print(args.useMPI)
if args.useMPI:
  iterator = sir3d.synth.Iterator(use_mpi=args.useMPI, batch=batchSize)
  mod = sir3d.synth.Model(iniFile, rank=iterator.get_rank())
  iterator.use_model(model=mod)
else:
  iterator = sir3d.synth.Iterator(use_mpi=args.useMPI)
  mod = sir3d.synth.Model(iniFile, rank=iterator.get_rank())
  iterator.use_model(model=mod)


if (args.width * args.height == 0):
  iterator.run_all_pixels()
else:
  print('running subcube')
  iterator.run_all_pixels(rangex=[x1,x2], rangey=[y1,y2])

