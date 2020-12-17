#!/usr/bin/python

import vcf
import argparse
import sys
import os

VAF_FILE = "vaf_snv.vcf"

def extract_vaf_from_vcf(vcf_file):
    vcf_reader = vcf.Reader(open(vcf_file, 'r'))
    
    with open(VAF_FILE, "w") as f:
        f.write("\t".join(["CHROM", "POS", "REF", "ALT", "safNormal", "safTumour"])+"\n")

        for record in vcf_reader:
            refCount = record.REF + "U"
            altCount = str(record.ALT[0]) + "U"

            if (record.genotype('TUMOR')[altCount][0] + record.genotype('TUMOR')[refCount][0]) != 0:
                safTumour = record.genotype('TUMOR')[altCount][0] / (record.genotype('TUMOR')[altCount][0] + record.genotype('TUMOR')[refCount][0])
            else:
                safTumour = 0

            if (record.genotype('NORMAL')[altCount][0] + record.genotype('NORMAL')[refCount][0]) != 0:    
                safNormal = record.genotype('NORMAL')[altCount][0] / (record.genotype('NORMAL')[altCount][0] + record.genotype('NORMAL')[refCount][0])
            else:
                safNormal = 0

            write_record = "\t".join([record.CHROM, str(record.POS), record.REF, str(record.ALT[0]), str(safNormal), str(safTumour)])+"\n"

            f.write(write_record)

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="vcf processing")
    parser.add_argument('-i', '--input', help='Absolute path to vcf file', default=sys.stdin)
    args = parser.parse_args()

    if isinstance(args.input, str):
        if not os.path.isfile(args.input):
            logger.exception('Input file not found: {}'.format(args.input))
            raise Exception('Input file not found: %s' % args.input)

    vcf_file = args.input        
    extract_vaf_from_vcf(vcf_file)


