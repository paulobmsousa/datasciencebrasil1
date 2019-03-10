# BIC - Bit Inversion Code

import glob, os, sys, time

def bic(inputfile, outputfile):
   f1 = open(inputfile, 'rb')
   f2 = open(outputfile, 'wb')
   byte = f1.read(1)
   contbytes = 0
   while (byte):
      contbytes += 1
      ch1 = byte.decode('latin-1','ignore')
      int1 = ord(ch1)
      int2 = 255-int1
      ch2 = chr(int2)
      byte2 = ch2.encode('latin-1','ignore')
      f2.write(byte2)
      byte = f1.read(1)
   f1.close()
   f2.close()
   os.remove(inputfile)
   return contbytes

def chname(filename):
   outputfile = ''
   for ch in filename:
      int1 = ord(ch)
      if (int1>=48 and int1<=57):
         int2 = abs(48-int1)+48
      elif (int1>=65 and int1<=90):
         int2 = abs(90-int1)+65
      elif (int1>=97 and int1<=122):
         int2 = abs(122-int1)+97
      else:
         int2 = int1
      ch2 = chr(int2)
      outputfile += ch2
   return outputfile

def bicfile(inputfile, op):
   outputfile = ''
   contbytes = 0
   if not(os.path.isdir(inputfile)):
      if op=='a':
         if inputfile.endswith('.bic'):
            outputfile = inputfile[:-4]
            pathdir, filename = os.path.split(outputfile)
            outputfile = pathdir+os.sep+chname(filename)
            print(inputfile,'>',outputfile)
            contbytes = bic(inputfile, outputfile)
         else:
            pathdir, filename = os.path.split(inputfile)
            outputfile = pathdir+os.sep+chname(filename)+'.bic'
            print(inputfile,'>',outputfile)
            contbytes = bic(inputfile, outputfile)
      elif op=='b':
         if not(inputfile.endswith('.inv')):
            pathdir, filename = os.path.split(inputfile)
            outputfile = pathdir+os.sep+chname(filename)+'.inv'
            print(inputfile,'>',outputfile)
            contbytes = bic(inputfile, outputfile)
      elif op=='c':
         if inputfile.endswith('.inv'):
            outputfile = inputfile[:-4]
            pathdir, filename = os.path.split(outputfile)
            outputfile = pathdir+os.sep+chname(filename)
            print(inputfile,'>',outputfile)
            contbytes = bic(inputfile, outputfile)
      elif op=='d':
         if not(inputfile.endswith('.ren')):
            outputfile = inputfile
            pathdir, filename = os.path.split(outputfile)
            outputfile = pathdir+os.sep+chname(filename)+'.ren'
            os.rename(inputfile, outputfile)
            print(inputfile,'>',outputfile)
      elif op=='e':
         if inputfile.endswith('.ren'):
            outputfile = inputfile[:-4]
            pathdir, filename = os.path.split(outputfile)
            outputfile = pathdir+os.sep+chname(filename)
            os.rename(inputfile, outputfile)
            print(inputfile,'>',outputfile)
   return contbytes

def main(argv):
   inputfile = ''
   outputfile = ''
   if len(sys.argv)==3:
      inputfile = sys.argv[1]
      op = sys.argv[2]
      if os.path.exists(inputfile):
         if op in ['a', 'b', 'c', 'd', 'e']:
            print('*** STARTING CONVERSION  ***')
            contfiles = 0
            contbytes = 0
            conttime1 = time.time()
            if os.path.isdir(inputfile):
               for filename in glob.iglob(inputfile+'/**/*.*', recursive=True):
                  if not(os.path.isdir(filename)):
                     contfiles += 1
                     contbytesat = bicfile(filename, op)
                     contbytes += contbytesat
            else:
               contfiles += 1
               contbytes = bicfile(inputfile, op)
            conttime2 = time.time()
            tottime = conttime2-conttime1
            print(' #Files:',contfiles,'- #Bytes:',contbytes,'#Time:',tottime,'secs.')
            print('***  ENDING CONVERSION   ***')
         else:
            print(' - ERROR: option invalid (must be \'a\', \'b\', \'c\', \'d\' or \'e\')!')
      else:
         print(' - ERROR:',inputfile,'does not exists!')
   else:
       print (sys.argv[0], '<FileOrDir> <Op: a=all, b=bin, c=ret d=ren e=nam>')

if __name__ == '__main__':
   main(sys.argv[1:])

