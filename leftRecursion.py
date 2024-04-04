from prettytable import PrettyTable

def removeLeftRecursion(rulesDiction):
	store = {}
	for lhs in rulesDiction:
		alphaRules = []
		betaRules = []
		allrhs = rulesDiction[lhs]
		for subrhs in allrhs:
			if subrhs[0] == lhs:
				alphaRules.append(subrhs[1:])
			else:
				betaRules.append(subrhs)
		if len(alphaRules) != 0:
			lhs_ = lhs + "'"
			while (lhs_ in rulesDiction.keys()) \
					or (lhs_ in store.keys()):
				lhs_ += "'"
			for b in range(0, len(betaRules)):
				betaRules[b].append(lhs_)
			rulesDiction[lhs] = betaRules
			for a in range(0, len(alphaRules)):
				alphaRules[a].append(lhs_)
			alphaRules.append(['ε'])
			store[lhs_] = alphaRules
	for left in store:
		rulesDiction[left] = store[left]
	return rulesDiction

def string_to_dict(rules):
	diction = {}
	for rule in rules:
		k = rule.split("->")
		k[0] = k[0].strip()
		k[1] = k[1].strip()
		rhs = k[1]
		multirhs = rhs.split('|')
		for i in range(len(multirhs)):
			multirhs[i] = multirhs[i].strip()
			multirhs[i] = multirhs[i].split()
		diction[k[0]] = multirhs
		return diction

def dict_to_string(rules_dict):
    formatted_rules = []
    for non_terminal, productions in rules_dict.items():
        productions_string = ' | '.join([' '.join(production) for production in productions])
        formatted_rules.append(f"{non_terminal} -> {productions_string}")
    return formatted_rules

def printAfterRemoval(rules):
    for rule in rules:
        print(rule)
    print(f"\nAfter elimination of left recursion:\n")
    diction = string_to_dict(rules)
    diction = removeLeftRecursion(diction)
    formatted_rules = dict_to_string(diction)
    for rule in formatted_rules:
        print(rule)



rules=["A -> A a | B a | c | a",
	   "B -> B b | A b | d"]
nonterm_userdef=['A', 'B']
term_userdef=['a', 'b', 'c', 'd']

printAfterRemoval(rules)
