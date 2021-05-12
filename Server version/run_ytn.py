#!/usr/local/anaconda3/bin/python3
import cgitb;
cgitb.enable()
import cgi,re,os
import YutanpaNet as ytn
import sys
import random

dir = '../Documents/biotools/yutanpa/upload'
print ("Content-type: text/html")
print ()
form = cgi.FieldStorage()


# A nested FieldStorage instance holds the file
rn = form['rawnodes']

# Test if the file was uploaded
if rn.filename:

    rn_file_path = os.path.join(dir,os.path.basename(rn.filename))
    open( rn_file_path, 'wb').write(rn.file.read())

re = form['rawedges']

# Test if the file was uploaded
if re.filename:

    re_file_path = os.path.join(dir,os.path.basename(re.filename))
    open( re_file_path, 'wb').write(re.file.read())

pn = form['recnodes']

# Test if the file was uploaded
if pn.filename:

    pn_file_path = os.path.join(dir,os.path.basename(pn.filename))
    open( pn_file_path, 'wb').write(pn.file.read())

pe = form['recedges']

# Test if the file was uploaded
if pe.filename:

    pe_file_path = os.path.join(dir,os.path.basename(pe.filename))
    open( pe_file_path, 'wb').write(pe.file.read())

ft = form['ft']

# Test if the file was uploaded
if ft.filename:

    ft_file_path = os.path.join(dir,os.path.basename(ft.filename))
    open( ft_file_path, 'wb').write(ft.file.read())


G = ytn.load_network(rn_file_path,re_file_path)
P = ytn.load_network(pn_file_path,pe_file_path)
l = form.getvalue('acc')
nodes = [str(item) for item in l.split(',')]
plots = form.getvalue('plots')
if not plots:
    plots = ' '
index = random.randrange(100000,1000000)
outFile = os.path.join(dir,'isolated_system_{}.html'.format(str(index)))
ytn.show_subnetwork(P,G,nodes,ft_file_path,form.getvalue('lou')+plots,form.getvalue('status'),outFile)
redirectURL = "http://biotools.tcdb.org/yutanpa/upload/{}".format('isolated_system_%s.html'%str(index))
print('<html>')
print('  <head>')
print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />')
print('  </head>')
print('</html>')
