newJob = {'occupation': 'lumberjack', 'hours': 'all day', 'rest': 'all night'}
print("I'm a {0} and I'm okay, I sleep {2} and I work {1}.\n "
      "He's a {0} and he's okay, he sleeps {2} and he works {1}!"
      .format(newJob['occupation'], newJob['hours'], newJob['rest']))

print(f"I'm a {newJob['occupation']} and I'm okay...")

print("I'm a " + newJob['occupation'] + " and I'm okay...")

string = "I'm a", newJob['occupation'], "and I'm okay..."
print(string)
print(type(string))

myJob = "I work as a {}".format(newJob['occupation'])
print(myJob)
newJob['occupation'] = 'parrot enthusiast'
print(newJob['occupation'])
print(myJob)
