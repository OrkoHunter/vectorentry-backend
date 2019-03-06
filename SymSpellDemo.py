import os

from symspellpy.symspellpy import SymSpell, Verbosity


class SpellCorrect:
	def __init__(self, max_dictionary_edit_distance = 2, prefix_length = 7, dictionary_path = None):
		# maximum edit-distance for doing lookups
		self.max_dictionary_edit_distance = max_dictionary_edit_distance

		# Length of word prefixes used for spell checking
		self.prefix_length = prefix_length

		# create object
		self.sym_spell = SymSpell(max_dictionary_edit_distance = self.max_dictionary_edit_distance, prefix_length = self.prefix_length)

		# load dictionary
		if dictionary_path is None:
			dictionary_path = os.path.join(os.path.dirname('__file__'), "frequency_dictionary_en_82_765.txt")

		term_index = 0  # column of the term in the dictionary text file
		count_index = 1  # column of the term frequency in the dictionary text file

		if not self.sym_spell.load_dictionary(dictionary_path, term_index, count_index):
		    print('Dictionary file not found')

	def spelling_correct(self, input_term):
		# lookup suggestions for multi-word input strings (supports compound
		# splitting & merging)

		# max edit distance per lookup (per single word, not per whole input string)
		max_edit_distance_lookup = 2

		suggestions = self.sym_spell.lookup_compound(phrase = input_term, max_edit_distance = max_edit_distance_lookup)

		return "".join([suggestion.term for suggestion in suggestions])