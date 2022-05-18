#!/bin/bash
for arg in "$@"
do
  if [ "$arg" == WIC+RSS+DWUG+XLWSD ]; then
      wget https://zenodo.org/record/6562280/files/WIC%2BRSS%2BDWUG%2BXLWSD.zip
      unzip WIC+RSS+DWUG+XLWSD.zip
      rm WIC+RSS+DWUG+XLWSD.zip
  fi
  if [ "$arg" == WIC_DWUG+XLWSD ]; then
      wget https://zenodo.org/record/6562288/files/WIC_DWUG%2BXLWSD.zip
      unzip WIC_DWUG+XLWSD.zip
      rm WIC_DWUG+XLWSD.zip
  fi
  if [ "$arg" == WIC_RSS ]; then
      wget https://zenodo.org/record/4992613/files/mean_dist_l1ndotn_CE.zip
      unzip mean_dist_l1ndotn_CE.zip
      mv mean_dist_l1ndotn_CE WIC_RSS
      rm mean_dist_l1ndotn_CE.zip
  fi
done
