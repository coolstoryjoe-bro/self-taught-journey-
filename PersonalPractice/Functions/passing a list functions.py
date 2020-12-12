# Passing a list using a function:
def greet_users(names):
    """This is to greet users"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['hannah', 'john', 'jane']
greet_users(usernames)


# Modifying a List in a Function:
# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to the completed list after printing.
while unprinted_designs:
    current_designs = unprinted_designs.pop()
    print(f"Printing Model: {current_designs}")
    completed_models.append(current_designs)
# Display all completed models:
print(f"\nThe following models have been completed: ")
for completed_model in completed_models:
    print(completed_model)


def print_models(unprinted_design, completed_designs):
    """Simulate printing each design, until none are left. Move each design to completed_models after printing."""
    while unprinted_design:
        current_design = unprinted_design.pop()
        print(f"Printing Models: {current_design}")
        completed_designs.append(current_design)

def show_completed_models(completed_models):
    """Show all completed models"""
    print(f"The following models have completed printing: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# DIY 1
text_messages = ['hello', 'its me', 'darkness', 'your old friend', 'maybe not exactly', 'friend']

def show_messages():
    for messages in text_messages:
        print(f"{messages}")

show_messages()


# DIY 3

text_messages = ['hello', 'its me', 'darkness', 'your old friend', 'maybe not exactly', 'friend']
sent_messages = []
archived_texts = text_messages[:]

def send_messages(archived_texts, sent_messages):
    while archived_texts:
        current_messages = archived_texts.pop()
        print(f"Sending messages: {current_messages}")
        sent_messages.append(current_messages)

send_messages(archived_texts, sent_messages)
print(sent_messages)
print(text_messages)
