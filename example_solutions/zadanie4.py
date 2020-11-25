import pandas as pd

DATA_FILE = 'CPCT02220079.annotated.processed.tsv'

def load_data(file):
    return pd.read_csv(file, sep='\t', usecols=['CHROM', 'POS', 'REF', 'ALT'])


if __name__ == '__main__':
    df = load_data(DATA_FILE)

    def classify_variant(s):
        ref_len = len(s['REF'])
        alt_len = len(s['ALT'])

        if ref_len < alt_len:
            return 'INS'
        elif ref_len > alt_len:
            return 'DEL'
        elif ref_len == alt_len == 1:
            return 'SNP'
        else:
            print(s)
            return None
            # raise Exception('reflen and altlen error')

    df['VARIANT_CLASS'] = df.apply(classify_variant, axis=1)

    print(df['VARIANT_CLASS'].value_counts())

    print(df.head())
