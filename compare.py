import sys
import pandas as pd
import pyclan as pc


def compare(original, new):
    orig_cf = pc.ClanFile(original)
    new_cf = pc.ClanFile(new)

    results = []

    orig_cf.flatten()
    orig_cf.annotate()
    orig_annots = orig_cf.annotations()

    new_cf.flatten()
    new_cf.annotate()
    new_annots = new_cf.annotations()

    if len(orig_annots) != len(new_annots):
        raise Exception("\n\n\nannotation lengths do not match:\n\norig: {}\nrecode: {}\n\n".format(
            len(orig_annots), len(new_annots)))

    for x in zip(orig_annots, new_annots):
        results.append((x[0].word, x[0].utt_type, x[0].present, x[0].speaker, x[0].onset, x[0].offset,
                        x[1].word, x[1].utt_type, x[1].present, x[1].speaker, x[1].onset, x[1].offset))

    columns = ["orig_word", "orig_utt_type", "orig_present",
               "orig_speaker", "orig_onset", "orig_offset",
               "new_word", "new_utt_type", "new_present",
               "new_speaker", "new_onset", "new_offset", ]
    result = pd.DataFrame(results, columns=columns)
    return result


if __name__ == '__main__':

    original = sys.argv[1]
    new = sys.argv[2]

    result = compare(original, new)

    result.to_csv("{}_blind_compare.csv".format(original[:5]), index=False)
