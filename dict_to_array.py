import random
import string


def dict_to_list(input):

	if  is isinstance(input, dict):
		return [input]
	keys = input.keys()
	dict_list = []
	for key in keys:
		dict_list.append(key)
		dict_list.extend(dict_to_list(input[key]))
	return dict_list


def generate_nested_dict(nested_level):
	sample_dict = {
		''.join(random.choices(string.ascii_letters, k = 2)) : random.randrange(5)
	}
	while nested_level:
		num_of_items = random.randrange(5)
		nested_level -= 1 
		for num in range(num_of_items):
			sample_dict[''.join(random.choices(string.ascii_letters, k = 2))] = generate_nested_dict(nested_level)
	return sample_dict

sample_dict1 = generate_nested_dict(nested_level = 5)
print(sample_dict1)
print(dict_to_list(sample_dict1))