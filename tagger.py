from flask import Flask, render_template, request, json, jsonify
import pyap
import spacy
from spacy_patterns import *
from spacy.matcher import Matcher
from spacy.pipeline import EntityRecognizer
#from spacy import displacy #only available with Spacy v2.0 

def setup_patterns_v20(): #pattern matching with Spacy v2.0
	for pattern in IP_PATTERN_LIST:
		matcher.add('IP', None, pattern)

	for pattern in PHONE_PATTERN_LIST:
		matcher.add('PHONE', None, pattern)

	for pattern in ADDRESS_PATTERN_LIST:
		matcher.add('ADDRESS', None, pattern)

	matcher.add('EMAIL', None, [{'LIKE_EMAIL':True}])
	matcher.add('URL', None, [{'LIKE_URL':True}])
	matcher.add('ACCT',  None, [{'ORTH':'sfdweeipas3412asdf'}]) # placeholder that currently shouldn't match on anything

def setup_patterns_v19(): #pattern matching with Spacy 1.9
#	matcher.add_entity('IP', on_match=None)
        for pattern in IP_PATTERN_LIST:
		matcher.add_pattern('IP', pattern)

#        matcher.add_entity('PHONE', on_match=None)
        for pattern in PHONE_PATTERN_LIST:
                matcher.add_pattern('PHONE', pattern)

#        matcher.add_entity('ADDRESS', on_match=None)
        for pattern in ADDRESS_PATTERN_LIST:
                matcher.add_pattern('ADDRESS', pattern)

#        matcher.add_entity('EMAIL', on_match=None)
        matcher.add_pattern('EMAIL', [{'LIKE_EMAIL':True}])

#        matcher.add_entity('URL', on_match=None)
        matcher.add_pattern('URL', [{'LIKE_URL':True}])

#        matcher.add_entity('ACCT', on_match=None)
        matcher.add_pattern('ACCT', [{'ORTH':'sfdweeipas3412asdf'}]) # placeholder that currently shouldn't match on anything

def ent_list_to_json(ent_list):
       	return [
       		{
       		'start': ent.start_char,
       		'end': ent.end_char,
       		'type': ent.label_,
       		'text': str(ent),
       		} for ent in ent_list
		]

def merge_and_add_ents(doc, matches): # This function deals with the fact some patterns are sub-patterns of other patterns,
	overlap = False               # so it is possible to get multiple matches on portions of an overall entity.
	merged_list = []              # This code looks for overlapping spans of tokens and merges them into one long span

	new_matches = []                                        # This code translates the Spacy v1.9 "matches" format into v2.0 format
	for match in matches:                                   #
		if match[0] == URL_ID and '@' in doc[match[2]:match[3]].text: # works around the '@' bug in the LIKE_URL matcher
			continue				#
		new_matches += [(match[0], match[2], match[3])] # In Spacy v2.0, the "label" column (second from left) is is gone
                                                                #
	matches = new_matches                                   # Remove this line and the 6 above for Spacy v2.0

	for i in range(0, len(matches)):
		if overlap:
			start_idx = min(matches[i][1], start_idx)
			end_idx = max(matches[i][2], end_idx)
		else:
                        start_idx = matches[i][1]
                        end_idx = matches[i][2]

	        if (i <= len(matches) - 2):
			if (matches[i+1][1] < end_idx):
				overlap = True
			else:
				doc.ents += ((matches[i][0], start_idx, end_idx),)
				overlap = False
		else:
			doc.ents += ((matches[i][0], start_idx, end_idx),)

def find_span(doc, addr): # This function finds the first match of addr in the doc, but ignores whitespace tokens, like newlines
    for doc_token in doc:
        if doc_token.is_space:
            continue
        i = doc_token.i
        start_idx = 0
        end_idx = 0
        match = False

        for idx, addr_token in enumerate(addr):
            if addr_token.is_space: #skip to next token in address
                continue
            elif doc[i].is_space: #skip to next token in doc
                while doc[i].is_space:
                    i += 1

            if addr_token.text == doc[i].text: #token match found
                if start_idx == 0: # if start_idx hasn't been set, then set it
                    start_idx = i
                if idx == len(addr) - 1: #if we're here, and we're at the last addr token, all the tokens have matched.
                    end_idx = i # set end_idx
                    match = True # exit outer loop. This function only finds the first match in doc
                i += 1
            else: # the next token in the address the next doc token. Start over at next token in doc
                break

            if i == len(doc): #Prevents index error. Should only happen on partial matches at the end of a doc
                break

        if match: # If we found a match, then we're done. Only finds the first match
            break

    return (start_idx, end_idx)

def process_text(q):
        doc = nlp(q)
        matches = matcher(doc)

        merge_and_add_ents(doc, matches)

        for address in pyap.parse(q, country='US'):
                spn = find_span(doc, nlp(str(address).decode('utf-8')))
                doc.ents += ((ADDRESS_ID, spn[0], spn[1]),)

        filtered_ents = [ent for ent in list(doc.ents) if ent.label_ in ENT_LIST]

	return doc, filtered_ents

#################################################

nlp = spacy.load('en')
matcher = Matcher(nlp.vocab)
ner = EntityRecognizer(nlp.vocab)

ents_to_add = ['IP', 'PHONE', 'ADDRESS', 'EMAIL', 'URL', 'ACCT']

for label in ents_to_add:
    ner.add_label(label)

setup_patterns_v19() #use with Spacy v1.9
#setup_patterns_v20() #use with Spacy v2.0+

IP_ID = nlp.vocab.strings['IP']
PHONE_ID = nlp.vocab.strings['PHONE']
ADDRESS_ID = nlp.vocab.strings['ADDRESS']
EMAIL_ID = nlp.vocab.strings['EMAIL']
URL_ID = nlp.vocab.strings['URL']
ACCT_ID = nlp.vocab.strings['ACCT']

ENT_LIST = ['PERSON', 'NORP', 'ORG', 'GPE', 'PRODUCT', 'FAC', 'MONEY', 'LANGUAGE', 'DATE', 'TIME', 'EMAIL', 'URL', 'IP', 'ACCT', 'PHONE', 'ADDRESS']

app = Flask(__name__)

#################################################

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/api/tag', methods=['GET', 'POST'])
def json_response():
	q = request.values.get('text')

	doc, filtered_ents = process_text(q)

	return jsonify(ent_list_to_json(filtered_ents))

@app.route('/demo', methods=['GET', 'POST'])
def demo():
	q = request.values.get('text')

	doc, filtered_ents = process_text(q)

	if request.values.get('type') == 'html':
		colors = {'PHONE': 'linear-gradient(90deg, #aa9cfc, #fc9ce7)', 'EMAIL': '#b4943e'}
		options = {'ents': ENT_LIST, 'colors': colors}

	        return render_template('displacy.html')
		#return displacy.render(doc, style='ent', page=True, options=options) #displacy only works in Spacy v2.0
	else:
		filtered_ents = [ent for ent in list(doc.ents) if ent.label_ in ENT_LIST]
		return app.response_class(
				response=json.dumps(ent_list_to_json(filtered_ents), indent=4),
				status=200,
				mimetype='text/string'
				)

@app.route('/api/train', methods=['GET', 'POST'])
def train():
	t = request.values.get('json')


if __name__ == '__main__':
     app.run(host='0.0.0.0')
