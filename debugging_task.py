# Function to print dictionary values given the keys
def print_values_of(dictionary, keys, x, y):
    #removed for loop
    print(dictionary[keys])
    print(dictionary[x])
    print(dictionary[y])

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!", 
                         "maggie": "(Pacifier Suck)"
                         }

print_values_of(simpson_catch_phrases, 'lisa', 'bart', 'homer')

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''
#fiddled until it worked, dont realy understand user defined functions so didnt have a hypothmapotomis :(
