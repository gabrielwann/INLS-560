# Mad lib example for functions.

def madlib(noun_1, noun_2, verb_1, adjective, verb_2, verb_3, adverb_1, noun_3):
    '''Mad Lib Function'''
    story =f'''
In the cursed land of {noun_1}, a great battle had been foretold between the mighty General Radahn and the graceful yet deadly Malenia, Blade of Miquella. The {noun_2} trembled as Radahn prepared to {verb_1} across the crimson battlefield, his strength unmatched by any in the realm. Meanwhile, Malenia, with her {adjective} wings, would {verb_2} like a whisper through the air, her every move calculated and swift. As they clashed, the ground beneath seemed to {verb_3} with the force of their strikes, and the trees whispered {adverb_1}, sharing the secrets of their ancient rivalry. Even the towering {noun_3} watched in silence, its stones etched with the history of countless battles. 
'''
    return story

output_story = madlib('noun_1', 'noun_2', 'verb_1', 'adjective', 'verb_2', 'verb_3', 'adverb_1', 'noun_3')
print(output_story)