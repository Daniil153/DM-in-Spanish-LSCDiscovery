#!/bin/bash
cd WUGs
chmod 755 scripts/*.sh
cd scripts
sed -i 's/max=4/max=2/' parameters_opt.sh
sed -i 's/threshold=2.5/threshold=1.5/' parameters_opt.sh
sed -i 's|source $scriptsdir/parameters_test.sh|source $scriptsdir/parameters_opt.sh|' run_uug.sh
sed -i.bak '8i\
scriptsdir=scripts\
' run_uug.sh
cd ../..
