from emoji import emojize

# Prompt the user for a str in English.
user = input('Type Between 2 colons (:input:):- ').strip().lower()

# When there is no corresponding emoji.
if not emojize(user, language='alias'):

    # Printing str as it is.
    print(emojize(user))

# Output the “emojized” version of that str.
else:
    # Converting any codes (or aliases) therein to their corresponding emoji.
    print(emojize(user, language='alias'))
   