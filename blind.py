import os
import sys

import pyclan as pc


def insert_annot(line, annot, orig=False):
    tab_i = line.line.find("\t")
    if orig:
        blank_annot = annot.annot_string() + " "
    else:
        blank_annot = annot.annot_string(
            word=False, utt_type=False, present=False, speaker=False) + " "
    line.line = line.line[:tab_i + 1] + blank_annot + line.line[tab_i + 1:]


def process_cha(clan_file):
    clan_file.annotate()
    annots = clan_file.annotations()
    clan_file.clear_annotations()

    for annot in annots:
        line = clan_file.line_map[annot.line_num]
        insert_annot(line, annot)

    return clan_file


def blind():
    for root, _, files in os.walk(start_dir):
        for file in files:
            if file.endswith(".cha"):
                clan_file = pc.ClanFile(os.path.join(root, file))
                clan_file = process_cha(clan_file)
                clan_file.write_to_cha(os.path.join(
                    out_dir, file.replace(".cha", "")))
                print file


if __name__ == "__main__":
    start_dir = sys.argv[1]
    out_dir = sys.argv[2]

    blind()
