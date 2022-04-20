from calendar import c
#from tkinter import scrolledtext
from flask import Blueprint, flash, redirect, render_template, request, send_from_directory, url_for
import random
#from gtts import gTTS
#import pyttsx3

from App.models.user import User
#engine = pyttsx3.init()

api_views = Blueprint('api_views', __name__, template_folder='../templates')

easy = """gel
train
sport
rich
eel
fans
dome
tall
better
hit
peanut
cake
bite
noon
gummy
sting
ray
dusk
mops
thanks
dash
skin
star
began
grew
fine
day
upset
father
jam
mugs
fair
dinner
rats
fed
sir
boom
wave
trunk
sleepy
full
huge
born
jumping
damp
hunch
each
shade
ribs
forever
freeze
scorch
motor
talking
money
couch
nibble
strands
chapter
chess
slimy
squeak
friend
laptop
movie
known
suffer
double
watch
ahoy
dream
whine
beans
child
space
princess
piper
hear
sprint
awe
afar
bowl
sweat
cost
sleek
bottle
smart
stared
plopped
darted
angry
sidekick
stuff
least
little
felt
summer
carefully
would
shambles
taillight
quicken
presence
sizzle
hatchling
razz
followed
purple
entire
December
sudden
slither
combed
patrol
epic
vital
window
pocket
project
goofy
remember
travel
cranky
career
disease
trophy
athlete
jotted
swirled
amount
sighed
sheen
worse
sandwich
duo
gleaming
repress
clothes
either
rely
chose
belle
picture
prepare
percent
afraid
rescue
gradual
ferocious
frequently
permission
towel
sundae
ornament
rooster
scold
organza
fragile
galaxy
complaint
curries
tennis
grumbling
garlic
hula
reactionary
muscular
drizzle
accurate
studio
illusionist
genetic
levity
moisture
toughness
tasteless
astute
turtle
Pinkerton
fortune
sluggard
bedlam
shortfall
cowlick
opinionated
slogan
triumphant
parenthetic
listener
guardian
dwindled
fraught
sturdy
treadmill
originate
eavesdrop
January
scruple
moxie
winnow
incentive
admirer
emotional
chia
raspberry
bogus
recoup
bookworm
veteran
erase
handcuffs
spinal
demolition
gargantuan
salsa
chaotic
shrimp
mandate
turret
pigeon
satellite
parasite
cascade
dandelion
famous
pristine
golden
modesty
amphibian
jealousy
remedial
vouch
trivia
shoulder
zebra
butterscotch
apron
beagle
kidney
wistful
raven
fructose
Amazon
companion
panorama
gimmick
flannel
cucumber
McMansion
janitor
lionize
headdress
ludicrous
pear
system
pedigree
empty
amulet
guess
magician
carrot
meteor
distraught
freight
honeybee
blemish
crumpet
blizzard
squirm
harmonious
lawyer
valiant
purse
raisin
trumpet
bias
lettuce
shamrock
Americana
monopolize
water
marathon
omission
newbie
spreadsheet
badger
fortification
hydra
grouse
manta
astonish
fashionista
stubble
genius
nuance
stencil
penguin
freckle
blooper
misconception
lambkin
chowder
sunflower
lambasted
volumetric
flattery
simmer
whisk
bathtub
fantastically
failure
tolerable
mosquito
target
angora
snippet
ascribe
hodgepodge
verbiage
nephew
imbibe
savvy
reckon
boorish
tarmac
iteration
nurture
volcano
forensics
miraculous
trendy
permafrost
iceberg
cactus
nationalism
leeway
pilferer
rollicking
quart
lactose
domineering
onion
abandon
vault
junior
hamlet
jubilant"""

medium  = """antsy
hover
billow
posh
Canada
toga
bison
strum
dangerous
pluck
squid
Frisbee
teeter
chives
rallies
pastry
coveralls
ponytail
clatter
snout
tumbling
cradle
firefly
serious
banners
mention
spoken
record
bridge
pinpoint
wisdom
slate
drape
countless
hideout
ruins
Mexico
glazed
scanner
oncoming
flimsy
launch
rubble
tourists
laughter
window
meeting
plush
helmet
whimper
bracelet
inwardly
mobility
eddy
fanged
bough
listlessly
cautioned
flurry
glisten
accuse
drowsy
scoff
opposite
instrument
blissfully
coarse
activists
commute
cocoa
nutrients
scarcely
stretcher
lairs
hybrid
mustard
cruel
schedule
goblins
splutter
convince
grateful
gesture
formation
previous
imposing
complicated
unnoticed
agreement
dappled
rustle
chef
crease
whales
mislead
subtitles
fragment
retreat
implore
lento
Scandinavia
haggis
dolce
opus
pedestrian
snorkels
lullaby
FORTRAN
tangents
expression
violin
binary
semicolon
patent
incantations
treble
Baltic
ventured
deities
feta
proverb
indecipherable
podium
terraced
Aztec
laboratory
sinister
runes
ancestors
convulsive
jasper
berth
deference
detergent
sheathed
mantle
streamlet
strait
congratulate
fountain
curtly
garish
gilded
contingent
swerve
president
depths
Oregon
purpose
hexagonal
litmus
seethe
antiquarian
phalanges
bachelorette
frontier
unctuous
fluoride
moorage
Minotaur
intermezzo
edification
vacuousness
epilepsy
importunate
recuperation
citronella
palliative
abhorrence
personnel
vexatious
faux
sophisticated
nebulous
genus
legionnaire
sternutation
subcutaneous
alacrity
choreographer
leguminous
ceramics
mimetic
unabated
petrifying
specimen
interlocutor
machete
dulcet
salubrious
rotisserie
omnibus
biscotti
calibrate
appellation
duodenum
isotopic
carpal
quizzical
heliotrope
squander
prenuptial
succulent
bedraggled
rectitude
uranium
inundate
wunderkind
filial
wearisome
visage
fascinator
testimony
beaucoup
banal
seismologist
spectacles
innovator
bursary
hallowed
apogee
hiatus
freesia
exoneration
duvet
turpitude
platitude
nobiliary
commerce
keratitis
kookaburra
napoleon
superlative
oxygenate
annihilate
sarcophagus
surrogate
terabyte
uncouth
onerous
macrocosm
bulbous
umpirage
heredity
philharmonic
endorphin
pharmacy
fondant
cupola
herbaceous
tentativeness
pachinko
decrepitude
redux
dramaturgy
murmuration
Clydesdale
phonics
calisthenics
obediential
odiferous
combination
torrent
arsenic
invertebrate
manipulable
axiomatic
indefatigable
ulterior
oligarchy
pianola
dignify
allegiance
basaltic
scorpion
planetarium
ecstatic
cinnamon
pharaoh
opponency
referendum
quaver
rabbinic
lapel
mackerel
callow
biscuit
flourish
beatific
repository
dissipate
accomplice
kerchief
whimsical
stamina
criteria
reprieve
consequent
contusion
mulligan
sabermetrics
elocution
dowager
comparison
diaphanous
agoraphobia
buffet
tortoise
surmountable
endure
bonobo
abrogate
effusive
primitive
fabulist
comportment
taciturn
sophomoric
laureate
Goliath
splenetic
legato
slovenly
aerobics
paisley
contrariwise
petroleum
regalia
incinerate
flagon
incoherent
tercentenary
vituperative
churlish
riviera
laconic
excision
emblazoned
bric-a-brac
longitude
maverick
retrograde
partridge
insignia
binomial
"""
hard = """cladding
scallion
stealthily
warden
copious
hurtle
fester
intoxicating
outlandish
porcupine
lurching
ineffective
trough
parchment
leach
wrath
corporate
propane
dissuade
profusion
appalling
divulge
meditation
franchise
pretentious
embellishes
appropriate
rummages
constricting
inevitable
engrossed
strife
hindmost
eviction
protruding
substantial
hooey
blight
fronds
authority
mechanics
bankrupt
insurance
dismayed
offspring
pillage
anguish
increments
Odin
parishioner
astrologers
devout
shrike
Vancouver
conjure
stalagmite
traitorous
condominium
impenetrable
intercede
defector
livery
scuttlebutt
battalion
chalet
Lutheran
roiling
psychiatrist
disconcerting
Jesuit
fodder
sinuously
irreversible
barricade
unprepossessing
bipolar
torpid
featherbrained
immoderate
arrayed
countenance
scourge
irreverent
apparition
dosages
superintendent
exhalation
discord
clamorous
grimaces
inheritance
plumage
propound
chauffeurs
disconsolate
testosterone
minivets
proscenium
politesse
chanteuse
arrondissement
carabinieri
tamarisk
liana
sibilant
au revoir
bitumen
sacristy
Salzkammergut
frisson
Aachen
oriole
Ganges
niagara
carrion
samosas
chalice
necromancer
proffered
colonel
subaltern
Etruscan
cloisters
redound
Benedictine
arcane
soleil
copse
scabbard
courtiers
assuage
adjutant
inexorably
disgorged
Algiers
primavera
souterrain
knickerbockers
litany
unsullied
Carthusian
arret
marquee
imaret
cornichon
devastavit
Mediterranean
longevous
digerati
solecism
hypertrophy
ravigote
inchoate
judoka
vaccary
Adelaide
unwonted
tazza
damson
pelisse
succade
tumulus
dorsiflexor
profiterole
valetudinary
aristoi
vireo
rococo
lachsschinken
wakame
bathos
nihilism
ustion
sumpsimus
morel
abeyance
rongeur
mountebank
allelopathy
capoeira
agnolotti
ballabile
draegerman
prescient
Fribourg
tenon
nubilous
iatrogenic
onychitis
roux
tuatara
chicle
sulcus
thalamus
gyttja
jibboom
vestigial
Orwellian
cabaletta
hesped
umami
persiflage
toreador
vermicelli
frangipane
reseau
moulage
interpellate
genuflect
cinerarium
polemic
paladin
totipotency
agnomen
Bauhaus
sacerdotal
skeuomorph
binturong
mamushi
lipophilic
codicil
coulomb
violaceous
Rorschach
arthralgia
desman
jacaranda
huapango
predilection
entomophagy
paronomasia
facsimile
renminbi
interferon
sedulous
velouté
Aesopian
frigate
enoptromancy
satiety
perorate
danseur
chevalier
taurine
hierurgical
melee
emolument
ikebana
exaugural
gaillardia
caryatid
heliacal
schefflera
contrapposto
temblor
insouciance
catarrh
quattrocento
millegrain
canaille
verisimilitude
Keynesian
akaryote
azulejo
hauberk
bouillon
tarpaulin
cephalopod
pulchritude
pekoe
patois
Rubicon
bourgeois
aerophilatelic
ankh
contumelious
vicissitudes
lilliputian
Sbrinz
kathakali
cozen
oxalis
myeloma
lebensraum
mufti
dirigible
surcease
ascetic
oolite
revanche
megrims
podagra
palaver
luthier
yttriferous
vermeil
Ouagadougou
bibliopegist
plagiarism
holobenthic
boutonniere
anodyne
saccharide
boulevardier
quokka
lidocaine
contretemps
a posteriori
scaberulous
anaglyphy
realpolitik
colloque
onychorrhexis
paraffin
vigneron
tannined
spiedini
anhinga
jai alai
Rastafarian
succussion
avifauna
joropo
toxicosis
agitprop
Achernar
cassock
meringue
mackinaw
sambal
yuloh
hermeneutics
tikkun
macaque
lassitude
oeuvre
altazimuth
Castilian
trichinosis
ecclesiology
teppanyaki
cicatrize
somnolent
intonaco
realia
"""

def Convert(string):
    li = string.lower()
    li = list(string.split("\n"))
    return li

easy_words = Convert(easy)
medium_words = Convert(medium)
hard_words = Convert(hard)

counter = 0

bob = User("bobby", "bob@mail.com", "bobpass", 3, 0, 0)
#score = 0

@api_views.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@api_views.route('/profile', methods=['GET'])
def profile():
    return render_template('profile.html', yhighscore = bob.highscore)

@api_views.route('/lost_easy', methods=['GET'])
def lost_easy():
    return render_template('lost_easy.html')

@api_views.route('/win_easy', methods=['GET'])
def win_easy():
    return render_template('win_easy.html')

@api_views.route('/lost_medium', methods=['GET'])
def lost_medium():
    return render_template('lost_medium.html')

@api_views.route('/win_medium', methods=['GET'])
def win_medium():
    return render_template('win_medium.html')

@api_views.route('/lost_hard', methods=['GET'])
def lost_hard():
    return render_template('lost_hard.html')

@api_views.route('/win_hard', methods=['GET'])
def win_hard():
    return render_template('win_hard.html')

#def tts(word):
#    engine.say(word)
#    engine.runAndWait()
#    engine.endLoop()
#    engine.stop()

@api_views.route('/easy', methods = ['GET', 'POST'])
def play_easy():
    global counter
    bee_word = easy_words[counter]
    #tts(bee_word)
    message = ""
    gametype = "Easy"
    #pyttsx3.speak(bee_word)
    while counter == len(easy_words) -1:
        counter = 0
        if bob.lives < 3:
            bob.lives = 3
        if bob.highscore < bob.score:
            bob.highscore = bob.score
        bob.score = 0
        return render_template("win_easy.html")
    if request.method == 'POST':
        form = request.form
        user_spelling = form["spelling"]
        if bee_word == user_spelling:
            message = "Correct"
            bob.score +=10
            counter += 1
        else:
            message = "Wrong, try again!"
            bob.lives -= 1
        if bob.lives == 0:
            bob.lives = 3
            counter = 0
            if bob.highscore < bob.score:
                bob.highscore = bob.score
            bob.score = 0
            return render_template("lost_easy.html")
    return render_template("game.html", message = message, gametype=gametype, score = bob.score, yhighscore = bob.highscore, word = easy_words[counter])

@api_views.route('/medium', methods = ['GET', 'POST'])
def play_medium():
    global counter
    bee_word = medium_words[counter]
    #tts(bee_word)
    message = ""
    gametype = "Medium"
    #pyttsx3.speak(bee_word)
    while counter == len(medium_words) -1:
        counter = 0
        if bob.lives < 3:
            bob.lives = 3
        if bob.highscore < bob.score:
            bob.highscore = bob.score
        bob.score = 0
        return render_template("win_medium.html")
    if request.method == 'POST':
        form = request.form
        user_spelling = form["spelling"]
        if bee_word == user_spelling:
            message = "Correct"
            bob.score +=50
            counter += 1
        else:
            message = "Wrong, try again!"
            bob.lives -= 1
        if bob.lives == 0:
            bob.lives = 3
            counter = 0
            if bob.highscore < bob.score:
                bob.highscore = bob.score
            bob.score = 0
            return render_template("lost_medium.html")
    return render_template("game.html", message = message, gametype=gametype, score = bob.score, yhighscore = bob.highscore, word = medium_words[counter])

@api_views.route('/hard', methods = ['GET', 'POST'])
def play_hard():
    global counter
    bee_word = hard_words[counter]
    #tts(bee_word)
    message = ""
    gametype = "Hard"
    #pyttsx3.speak(bee_word)
    while counter == len(hard_words) -1:
        counter = 0
        if bob.lives < 3:
            bob.lives = 3
        if bob.highscore < bob.score:
            bob.highscore = bob.score
        bob.score = 0
        return render_template("win_hard.html")
    if request.method == 'POST':
        form = request.form
        user_spelling = form["spelling"]
        if bee_word == user_spelling:
            message = "Correct"
            bob.score +=100
            counter += 1
        else:
            message = "Wrong, try again!"
            bob.lives -= 1
        if bob.lives == 0:
            bob.lives = 3
            counter = 0
            if bob.highscore < bob.score:
                bob.highscore = bob.score
            bob.score = 0
            return render_template("lost_hard.html")
    return render_template("game.html", message = message, gametype=gametype, score = bob.score, yhighscore = bob.highscore, word = hard_words[counter])



@api_views.route('/game_test', methods = ['GET', 'POST'])
def game_test():
    return render_template('game2.html')