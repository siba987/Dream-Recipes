#CFG to compile information into a recipe
import json
import tracery
# with open('rules.json', 'r') as f:
#     rules = json.load(f)

rules = {

"origin": ["#[myThing:#concreteNoun#][mySub:#substance#][myRec:#recipeType#]saying# Welcome to Dream Recipes. ...#[recDesc:#recDescription#][mainIngr:#animal#]intro# Happy cooking!"
+ "\n\nYou will need:"+ "\n#squant# #mainIngr# " #this sometimes gives things like "2 raven"
+ "\n#lquant# of #liquid#."
+ "\n#lquant# #crazyIngred# "
+ "\n#lquant# of #liquid# "
+ "\n#solid.capitalize# for garnish "
+ "\nA medium-sized cauldron"

+ "\n\nMethods"+ "\n1. Take the #squant# #mainIngr#, and shred into #solAdj# pieces using a couple of forks. "
+ "\n2. Heat the cauldron over a flame, and add #lquant# of #liquid#. Add #squant# of #solAdj# #solid#, and #lquant# of #crazyIngred# to the mix."
+ "\n3. Once the pot starts to boil, add the #mainIngr# meat. Fry for 5 mins until crisp. "
+ "\n4. Stir the concoction until it reaches a #glowing#, #color#...now add #lquant# of #liquid#. We'll see it #glowing#, #color#...well, more of #color#ish #color#. "
+ "\n5. Cook for 15 mins to soak the #mainIngr# in the broth. You might need to add an extra ladleful of #liquid# to ensure the #myRec# is #totally# potent. "

+ "\n\n Our tried-and-true formula is sure to be a keeper. Simple ingredients, easy directions, and plenty of #concept# and #concept# make the #myRec# more #evaluationAdjBare# than ever. Best of all, it's totally customizable—add your favorite nutritious mix-ins such as fresh #crazyIngred#, sliced #substance#, or a dollop of #substance#." 
+ "\n#concl# It won't be long until the effect takes place. Until then, goodnight, dear reader. And sweet dreams."],

## this is where user input gets passed
"effectVerb":["conjure", "reveal", "repel", "lift", "mend", "transform", "increase"],
"effect":["aging drinker temporarily", "causing a powerful infatuation within the drinker", "increasing one's brain power", "healing bruises in an hour", "causing the drinker to become infatuated with the giver of the potion"],

#Intro and Conclusion
"intro":["If you follow the steps of your chosen  #myRec#, it will achieve the desired effect of #recDesc#. The best time to administer this #myRec# is when #beingWith# the #natureNoun#. "],
"concl":[" This was a simple recipe, one that you can try with your own #relative#, #youKnow#, #someday#. If not, #vagueReaction#."],

#Inspo quotes : foo and saying
"themeAdj":["lost", "desired", "redeemed", "awakened", "forgotten", "promised", "broken", "forgiven", "remembered", "betrayed"],
"themeNoun":["the future", "love", "drinking", "space travel", "the railroad", "your childhood", "summertime", "the ocean", "wanderlust", "war", "divorce", "nature", "pain", "hope", "a home", "a marriage", "family", "death"],
"theme":["#themeNoun# #themeAdj#"],
"foo":["#never# trust a #concreteNoun#. You can trust a #concreteNoun#, #maybe#", "I #verb#, therefore I am", "it's #concreteNoun.s# all the way down", "#concept# is the new #concept#", "the only good #concreteNoun# is a dead #concreteNoun#"],
"saying":["You #sense# the #myRec# and #react# with #emotion#. The #myThing# #sense.s# you but does not #react#.", "The #natureNoun# is made of #mySub# and #vagueReaction#.", "#[emo1:#transitiveEmotion#]never.capitalize# #emo1# #concept#. Only ever #emo1# #concept#."],

#related to the recipe
"recipeType":["remedy", "poison", "potion"],
"solid":["mistletoe berries", "garlic", "shiitake mushrooms"],
"liquid":["salamander blood", "honeywater","oyster sauce", "leech juice", "tomato puree", "soya sauce"],
"lquant":["a dash","1 teaspoon","4 tablespoons", "1/2 cup", "2 cups", "7 drops"],
"squant":["1 whole", "1 can of", "2", "5"],
"solAdj": ["boneless", "skinless", "bite-size", "minced", "shredded","finely choppped", "powdered"],
"bodyPart":["eyes", "tail", "liver", "brains", "spleen", "breast"],
"crazyIngred":["#animal#'s #bodyPart#"],
"recSentence":["reminding you of the time you had #themeAdj# #themeNoun#", "helping you to understand the #concept#", "#effect#"],
"recDescription":["#recSentence# "],

#Other grammar
"react":["shake", "moan", "cry", "scream", "wail", "rejoice", "dance", "cower", "howl"],
"color":["orange", "blue", "white", "black", "grey", "purple", "indigo"],
"animal":["goat", "spider", "raven", "crow", "scorpion", "coyote", "eagle", "owl", "lizard", "deer", "pig", "frog", "unicorn"],
"concept":["#substance#", "#emotion#", "darkness", "love", "childhood", "time", "loss", "victory", "memory", "art", "thought", "belief", "life", "death", "caring"],
"transitiveEmotion":["fear", "regret", "long for", "love", "distrust", "trust", "envy", "care for"],
"sense":["feel", "hear", "see", "know"],
"natureNoun":["ocean", "mountain", "forest", "cloud", "river", "tree", "sky", "earth", "void", "desert"],
"concreteNoun":["#animal#", "#natureNoun#"],
"verb":["#transitiveEmotion#", "#react#"],
"never":["never", "never again", "hardly ever", "barely", "almost always", "always", "probably never", "even"],
"glowing":["glowing", "rising", "hovering", "pulsing", "blinking", "glistening"],
"beingWith":["talking to", "walking with", "listening to"],
"weirdAdj":["weird", "arcane", "dark"],
"truly":["safely", "truly", "legally", "ever", "already"],
"totally":["fully", "completely", "absolutely", "totally"],
"arentReal":["are illegal", "don't exist"],
"ofCourse":["obviously", "well, clearly", "seriously", "as we #truly# know", "as everybody knows"],
"youKnow":["#ofCourse#", "I mean", "well", "I guess", "you know", "#maybe#"],
"anyway":["anyway", "in such a world as this", "if it were truly so", "if anything ever was"],
"butThen":["but then", "if you could imagine", "for certain"],
"ominousStatement":["who could you #truly# #transitiveEmotion#, #anyway#?", "if you understand my meaning.", "everyone knows that.", "you had known that for years.", "you knew that already."],
"recommend":["mandate", "recommend", "advise", "suggest"],
"asMyGrandmotherSaid":["as #authority# always said", "as #authority# tells us", "as #recommend.ed# by #authority#"],
"substance":["blood", "sand", "dust", "nothingness", "darkness", "light", "soil", "earthdust", "mud", "tar", "water", "bones", "flies", "honey"],
"emotion":["fear", "love", "trust", "desire", "pride", "sorrow", "regret", "confusion", "glee", "happiness", "contentment", "terror", "anger", "rage", "jealousy"],
"evaluationAdjBare":["good", "great", "wonderful", "terrifying", "bewildering", "perfect", "beautiful", "terrible"],
"evaluationAdj":["just #evaluationAdjBare#", "pretty #evaluationAdjBare#", "#evaluationAdjBare#", "really #evaluationAdjBare#"],
"maybe":["I think", "maybe", "probably", "almost certainly"],
"someday":["in the end", "if the sun rises again", "when the time comes", "in a while", "eventually", "sooner or later"],
"relative":["mother", "father", "grandmother", "grandfather", "lover", "friend"],
"authority":["the government", "the sheriff's secret police", "the law", "the radiochip implanted in your mind", "the Constitution", "a secret, yet menacing government society", "your own #relative#", "my own #relative#"],
"vagueReaction":["we all #react# and #react# in #emotion#", "it's about time", "it's #evaluationAdj#", "it's #evaluationAdj#", "I couldn't be happier", "isn't that #evaluationAdj#", "there's nothing that can be done", "but it hasn't always been that way", "but it won't always be that way"]


}

grammar = tracery.Grammar(rules)
print(grammar.flatten("#origin#"))