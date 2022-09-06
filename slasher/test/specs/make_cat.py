from catscii import catscii

##load cat
cat = catscii.load_cat('cesam_vuds_spectra_dr1_ecdfs_catalog_1662472876.txt', True)
ident = cat.get_column('vuds_ident')
z = cat.get_column('z_spec')

###file cat
files = catscii.load_cat('list_files.txt', False)
spec = files.get_column('Col1')
noise = files.get_column('Col2')

F = open('cutter_cat', 'w')

for i,z in zip(ident, z):
    for j in range(len(spec)):
        n = spec[j].split('_')[1]
        if n == i:
            line = '%s\t%s\t%s\n'%(spec[j], noise[j], z)
            F.write(line)

F.close()

