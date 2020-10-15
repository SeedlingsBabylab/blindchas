# blindcha

This is a script which will read in all the CLAN files in a directory and output blinded versions of those CLAN files to an output directory. It depends on the [pyclan](https://github.com/SeedlingsBabylab/pyclan) library.

**original**:
```
someword &=d_y_MOT
```
**blinded**
```
XXXX &=X_X_XXX
```

## usage


#### make the blinded version of a cha file
```bash
$ python blind.py [input_dir] [output_dir]
```

#### make comparison csv file for original vs. blinded versions

```
$ python compare.py [original.cha] [new.cha]
```
