#!/bin/bash
BCFTOOLS="/data/Seqtools/bcftools-1.10.2/bcftools"
VAF_VCF="vaf_snv.vcf.gz"
HEADER_FILE="header.txt"
VCF=$1
if [ ! -e ${VCF}.tbi ]; then
        tabix -p vcf ${VCF}
fi
#echo -e '##FORMAT=<ID=safNormal,Number=1,Type=Float,Description="Normal Variant Allele Fraction">' > $HEADER_FILE
echo -e '##FORMAT=<ID=VAF,Number=1,Type=Float,Description="Variant Allele Fraction">' > $HEADER_FILE
tabix -p vcf ${VAF_VCF}
${BCFTOOLS} annotate -a $VAF_VCF -h $HEADER_FILE -c CHROM,POS,REF,ALT,FORMAT/VAF -Oz -o ${VCF}.vaf.vcf.gz $VCF
tabix -p vcf ${VCF}.vaf.vcf.gz
# cleanup
# rm $VAF_VCF ${VAF_VCF}.tbi $HEADER_FILE
