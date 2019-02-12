import argparse
import unicodedata
import grapheme
import csv


# set up argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("infile", help="the name of the input file",
                    type=str)
args = parser.parse_args()


# count the grapheme occurrences
grapheme_counts = dict()
with open(args.infile, "r") as infile:
    for graph in grapheme.graphemes(infile.read()):
        grapheme_counts.setdefault(graph, 0)
        grapheme_counts[graph] += 1
        
        
# print out the summary
with open(args.infile + '.csv', 'w', newline='') as csvfile:
    columns = ['grapheme', 'count', 'number of codepoints', 'codepoint names']
    statistics_file = csv.DictWriter(csvfile, fieldnames=columns)
    statistics_file.writeheader()

    for (graph, count) in grapheme_counts.items():
        grapheme_codepoint_names = list()
        not_found_codepoints = dict()
        for codepoint in graph:
            try:
                name = unicodedata.name(codepoint)
                grapheme_codepoint_names.append(name)
            except:
                not_found_codepoints.setdefault(codepoint, 0)
                not_found_codepoints[codepoint] += 1
                
        # check if everythin is allright
        if len(not_found_codepoints) != 0 and len(grapheme_codepoint_names) == 0:
            continue
        elif len(not_found_codepoints) == 0 and len(grapheme_codepoint_names) != 0:
            pass
        else:
            print("Something could be wrong!")
            
        # create a record for the csv row
        entry = dict()
        entry['grapheme'] = graph
        entry['count'] = count
        entry['codepoint names'] = "; ".join(grapheme_codepoint_names)
        entry['number of codepoints'] = len(grapheme_codepoint_names)
        
        statistics_file.writerow(entry)
        
