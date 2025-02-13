import time
import random

# get random sample of 1000 English words
# word_file = "/usr/share/dict/words"
# WORDS = open(word_file).read().splitlines()
# random_words = random.sample(WORDS, 100)
# print(random_words)
random_words = ['unclerically', 'protophytic', 'gasolineless', 'interregimental', 'dibrom', 'stamping', 'frightment', 'severally', 'polypnoeic', 'unhot', 'barraclade', 'phytosociologic', 'unprejudicedly', 'disgustedness', 'prayer', 'demurely', 'counterscrutiny', 'Coroado', 'touristy', 'bimasty', 'subgod', 'quatrible', 'duffer', 'bale', 'Asperula', 'auxiliator', 'upplough', 'Sabbatian', 'mesophragma', 'aproterodont', 'fatter', 'gramenite', 'alderman', 'octocorallan', 'banister', 'ablush', 'rebeg', 'Marchantiaceae', 'hypernomic', 'constitutor', 'springing', 'meromorphic', 'profane', 'unheart', 'orchichorea', 'afformative', 'Pythios', 'enteropneust', 'monkeyry', 'Duculinae', 'Blepharoceridae', 'fasciotomy', 'citril', 'pukish', 'blepharosymphysis', 'pressmanship', 'begin', 'insouciance', 'proemployee', 'unproducedness', 'tergal', 'satrapal', 'upcarry', 'unreceived', 'biradial', 'ferroboron', 'Taoist', 'tristearate', 'sandspit', 'Dipteraceae', 'panurgy', 'blauwbok', 'calcined', 'Anneslia', 'afterswarm', 'dacryosolenitis', 'plumping', 'antipass', 'isleless', 'anamnionic', 'Daltonist', 'wullcat', 'insensibilization', 'antiquarian', 'threatproof', 'whirlpuff', 'grope', 'lampistry', 'oligoprothetic', 'consubstantially', 'autoplagiarism', 'perilymphatic', 'uncommunicating', 'Paralipomenon', 'snithe', 'countertripping', 'offward', 'quintennial', 'vesicotomy', 'unworldly', 'amphophilic', 'symplocaceous', 'prodramatic', 'paraphyllium', 'sessionary', 'notched', 'coppery', 'unused', 'migration', 'untunefully', 'Pantagrueline', 'neurogram', 'rout', 'overexertedness', 'Quirites', 'sanga', 'Capsian', 'unexclusive', 'overidealism', 'house', 'seralbumin', 'ornithosaurian', 'Narraganset', 'burnable', 'unsparingly', 'nonrequirement', 'Ionicism', 'birdglue', 'Zaberma', 'presolution', 'squireling', 'tomboyism', 'bootlick', 'Cucujidae', 'horsetongue', 'plainward', 'unpatrolled', 'fissuration', 'acopic', 'rubbish', 'taxonomical', 'circinately', 'ultramodernistic', 'obvallate', 'revolutionariness', 'systemproof', 'haemorrhoid', 'lanket', 'borosilicic', 'shareholdership', 'capably', 'macromethod', 'interanimate', 'unricked', 'borak', 'motherlike', 'cordierite', 'renneting', 'bronchophthisis', 'dextrosinistral', 'aristomonarchy', 'dermatomuscular', 'unintoxicatedness', 'undeclamatory', 'gruiform', 'overnew', 'Ethel', 'unexperiential', 'behenic', 'Arapaho', 'pseudoplasma', 'linteling', 'manipulatory', 'proinjunction', 'photograph', 'trilinolenin', 'carboxyl', 'hypogynous', 'convective', 'twistification', 'pylangial', 'theopneusted', 'acanthophorous', 'gallacetophenone', 'thyroiditis', 'bifronted', 'quartine', 'unbeauteously', 'clapper', 'augen', 'ichthyologist', 'mismade', 'Hyalonema', 'joggler', 'pseudocyesis', 'semimachine', 'lenticula', 'reticulose', 'nanny', 'callosum', 'overfling', 'irrenderable', 'cyclobutane', 'decempunctate', 'wise', 'white', 'sulfuration', 'nonlegal', 'flaith', 'tachometry', 'theoastrological', 'bogier', 'breechesflower', 'coreometer', 'culverineer', 'layship', 'traverse', 'coucher', 'Michelangelism', 'Hypochnus', 'roebuck', 'picul', 'juramentally', 'pyrolaceous', 'psychopetal', 'frontless', 'miscellany', 'coenobe', 'circumspangle', 'hematocyanin', 'gonepoiesis', 'begulf', 'murksome', 'dipterologist', 'sexualize', 'neoteristic', 'overjust', 'waldgravine', 'indurite', 'phos', 'mho', 'frontogenesis', 'incognizable', 'Cochlearia', 'neurexairesis', 'uva', 'dissolvableness', 'underniceness', 'roamingly', 'memorabilia', 'schneider', 'Fibrospongiae', 'godsonship', 'rediscount', 'misoxene', 'phlegmonous', 'bothway', 'calced', 'tentless', 'lambent', 'buckeye', 'loglike', 'psychoanalytically', 'Aotes', 'unabjured', 'muchness', 'hypsiloid', 'cacophonize', 'liveryless', 'organomercury', 'firework', 'Almira', 'grabbable', 'monolobular', 'Angerona', 'sexennial', 'mastodynia', 'wirra', 'unexactedly', 'otoblennorrhea', 'Olympianism', 'styward', 'umph', 'zonic', 'sunbeam', 'Ampelidaceae', 'micropin', 'unhomelikeness', 'untraversable', 'clinoclase', 'hysterometry', 'Epibaterium', 'trisomy', 'musicalness', 'stupefiedness', 'indefeatable', 'binucleated', 'lecaniid', 'pack', 'uneligible', 'retrobronchial', 'valiance', 'subchorionic', 'sulphogermanate', 'Gnathobdellida', 'emphysema', 'spindly', 'Helvella', 'tripel', 'clave', 'woft', 'payment', 'underclothed', 'preallotment', 'caffiso', 'enhydrite', 'coaching', 'chordoid', 'maumet', 'Cystophora', 'preterritorial', 'ischiofemoral', 'Sphakiot', 'springhalt', 'glazing', 'unemotional', 'reinstil', 'usurper', 'letoff', 'conjunctur', 'fleechment', 'Luvian', 'schizogregarine', 'paragogize', 'everwhich', 'iodoxy', 'Koheleth', 'chapper', 'thirteenthly', 'Hemigalus', 'myospasmia', 'correctant', 'redetect', 'tertiate', 'opsonify', 'Anabaptistically', 'posttussive', 'shammocking', 'doarium', 'oftentimes', 'tarbogan', 'Agalinis', 'Paussidae', 'cactiform', 'harvestman', 'requiteful', 'lawlike', 'uninherited', 'Cevenole', 'substratal', 'informality', 'dropcloth', 'coverside', 'candidness', 'universityless', 'ammeter', 'luteolous', 'choler', 'preimpairment', 'nasal', 'ringboned', 'underisive', 'Rivina', 'preconflict', 'schizodinic', 'argentamine', 'Azygobranchia', 'chilarium', 'fibrocystoma', 'believing', 'aardvark', 'metastome', 'antistrophon', 'protutory', 'Folkvangr', 'unlimited', 'deterioration', 'aphanitic', 'anele', 'Catalpa', 'Monomya', 'radiocarbon', 'unfantastic', 'diallel', 'quartziferous', 'latrobe', 'woesome', 'reclaimment', 'confederatism', 'Monotheletic', 'mignon', 'coelioscopy', 'figulated', 'pronounal', 'cureless', 'cholesterinemia', 'ecclesiastic', 'vlei', 'intenable', 'turnery', 'circumspective', 'puberal', 'Lucuma', 'unemployable', 'duomachy', 'typhloempyema', 'Dipladenia', 'oculonasal', 'lengthiness', 'otiant', 'unsoothing', 'ancientry', 'uncoquettishly', 'nonrepentance', 'anepigraphic', 'stabile', 'danburite', 'creepy', 'Scythic', 'triumphator', 'crambambuli', 'steenth', 'Massilia', 'dinoceratan', 'decorously', 'Tetrapneumones', 'kernos', 'Clupeodei', 'unrubified', 'Goddam', 'beta', 'lacework', 'Samucan', 'emphyteutic', 'cathedralesque', 'plerophory', 'Tlapallan', 'nonchokebore', 'drivewell', 'nuciform', 'octary', 'interparenthetical', 'cessionary', 'counterslope', 'commingle', 'polystelic', 'Ceratodidae', 'unstippled', 'unodoriferous', 'liguliform', 'glacialize', 'pneumonotherapy', 'patriarchdom', 'deamidation', 'albescent', 'semiquintile', 'rayless', 'esquire', 'glider', 'nigger', 'underbrim', 'namda', 'passivist', 'Macropodidae', 'laggard', 'enaction', 'ophthalmopod', 'pharmacognosy', 'alienage', 'Delbert', 'reliquary', 'syndication', 'epipoditic', 'jacinthe', 'tobaccoroot', 'ocht', 'adaw', 'allomorphite', 'tricotine', 'agent', 'cajole', 'Origanum', 'unkindlily', 'scintillose', 'inculcation', 'mylonitic', 'uncanonized', 'toupeed', 'fenestral', 'quebrachitol', 'lovesome', 'hetaerist', 'surprisable', 'seriatim', 'taoyin', 'concord', 'prinkle', 'cajuput', 'unidentifiedly', 'spermatoblast', 'petitionist', 'sneakingness', 'dreamful', 'yetapa', 'plungingly', 'diprotodont', 'karyological', 'appellor', 'adscript', 'phytopathology', 'bay', 'nonheathen', 'zealotry', 'reindict', 'subresin', 'Somal', 'overbody', 'insister', 'tineal', 'rhymeless', 'thrasher', 'Mayey', 'dichroiscope', 'uncharnel', 'antilogic', 'hoister', 'canonist', 'attrite', 'sticking', 'overdiversification', 'equate', 'vast', 'ceptor', 'phylon', 'previolate', 'refeed', 'panegyry', 'strychninism', 'isocyanurate', 'pinguefy', 'polyspore', 'glaringness', 'guldengroschen', 'storge', 'perscribe', 'tendance', 'karri', 'cirsophthalmia', 'estivate', 'Elijah', 'cicatricle', 'enlargedness', 'benzoin', 'chandam', 'warnt', 'disappointed', 'Sivapithecus', 'unruledly', 'adjudicator', 'Anguillulidae', 'carnauba', 'stakerope', 'goggan', 'gangsterism', 'Merula', 'prerequisite', 'Picae', 'fluoroform', 'recomplicate', 'aerostatic', 'Honduranean', 'milleporous', 'alight', 'rhamnal', 'distributer', 'multicrystalline', 'cohobation', 'magnetotelegraph', 'bearess', 'eugenesic', 'Satanophany', 'isoerucic', 'heteroinoculable', 'faceplate', 'dipleural', 'metazoal', 'Brassavola', 'oxane', 'kitchenman', 'sellie', 'Canariote', 'longfin', 'incognito', 'Exopterygota', 'palmated', 'electroanalytic', 'mycetology', 'decamerous', 'valetudinarianism', 'arbitress', 'Wallon', 'sporidiferous', 'Mephistopheleanly', 'Neopaleozoic', 'sloush', 'pedocalcic', 'asyndeton', 'sphinxlike', 'acatalectic', 'psychosurgeon', 'trilite', 'abolishment', 'Dianil', 'Chytridiales', 'emesis', 'pickpole', 'sloughy', 'ungroupable', 'cognitive', 'parasystole', 'orthodomatic', 'tavernry', 'nictitate', 'immethodicalness', 'spondylus', 'oxbow', 'antievolutionist', 'uxoriousness', 'tribunate', 'masque', 'requalify', 'coynye', 'jixie', 'catheterism', 'morindone', 'irregularist', 'guillotinade', 'reclothing', 'interfactional', 'nonobligatory', 'ungabled', 'Roccella', 'foolproof', 'argillite', 'leucyl', 'flodge', 'quei', 'nuculoid', 'terdiurnal', 'enlightenedly', 'vail', 'osmetic', 'catawampus', 'hooper', 'carnivalesque', 'reelable', 'embezzle', 'unentreated', 'ungarnered', 'tyrannizer', 'sustainer', 'phosphine', 'resupinate', 'hontish', 'antiglyoxalase', 'comediant', 'Chatillon', 'ruspone', 'fruitarian', 'outthrough', 'presentative', 'convulsible', 'Ioskeha', 'Cephalodiscus', 'lazyhood', 'semisociative', 'confrication', 'carfuffle', 'storeroom', 'colopexotomy', 'kobu', 'interastral', 'stachys', 'nimb', 'Fissidens', 'anthogenous', 'Fissipedia', 'machinist', 'furtherer', 'hydroelectric', 'wicket', 'gyp', 'connective', 'Lar', 'diabolatry', 'paraform', 'unagitation', 'weighhouse', 'glottologist', 'exacerbation', 'barful', 'reminiscent', 'troche', 'uprighteousness', 'colophonite', 'entomology', 'Hockday', 'pyrogenesis', 'unperpetrated', 'without', 'prehensive', 'undramatic', 'unsupportedness', 'gauzy', 'hygienic', 'sorbinose', 'unsensualize', 'undimerous', 'prankishness', 'walkrife', 'Climaciaceae', 'amulla', 'policedom', 'putrescence', 'buttonbur', 'domatium', 'optionally', 'debouchment', 'Midlandize', 'unsafeguarded', 'Narciss', 'lithochromatics', 'Serendib', 'nonsymbiotic', 'cress', 'Muilla', 'thermophilous', 'Ibadite', 'burel', 'tolidine', 'Plasticine', 'moonlighty', 'Amblycephalus', 'guidman', 'hazardry', 'casuary', 'hurried', 'chylaceous', 'lighterman', 'exalbuminous', 'tapet', 'resawer', 'aphakial', 'untranspassable', 'disshadow', 'ilot', 'decommission', 'proterothesis', 'oecumenic', 'unwithstanding', 'pega', 'governorate', 'frenziedly', 'hypoantimonate', 'filmgoer', 'dorsimedian', 'baylike', 'roncador', 'redisposition', 'finagle', 'presupport', 'stanchness', 'copyhold', 'ventifact', 'unbuild', 'mediopontine', 'togalike', 'quinquesyllabic', 'premiss', 'melanosarcomatosis', 'vesiculotomy', 'outerness', 'lansquenet', 'unprecedented', 'Isolde', 'corpusculous', 'coniroster', 'Tamanaca', 'panties', 'caducean', 'bespin', 'tagasaste', 'decarboxylization', 'Spiriferidae', 'preceding', 'reorganization', 'impetre', 'ploughmanship', 'adviser', 'gaw', 'clingingly', 'cleanskins', 'medicophysical', 'probargaining', 'mawk', 'swad', 'compromitment', 'semileafless', 'sacristy', 'entomogenous', 'obsequiosity', 'vomitwort', 'nonsupplication', 'opiniater', 'corticose', 'mallardite', 'chromotropy', 'lemmata', 'sterelminthous', 'Toryize', 'endosternum', 'velellidous', 'photozincography', 'leadable', 'reenge', 'bloomage', 'quirl', 'radicalization', 'gleaning', 'raven', 'overstuff', 'Aglipayano', 'lindackerite', 'caraipi', 'Koreish', 'seminaphthalidine', 'chladnite', 'sesquicarbonate', 'diphycercy', 'stickadove', 'Picinae', 'guildhall', 'pawnbroker', 'chargee', 'unshapely', 'lichenivorous', 'cirrigerous', 'sesquioctaval', 'jilt', 'cadaverous', 'gorraf', 'Taluche', 'graminaceous', 'suscept', 'Planorbidae', 'outcharm', 'interpterygoid', 'hesperitin', 'specificly', 'hippomancy', 'patristic', 'champertous', 'nondeliberation', 'alisphenoidal', 'tectibranchian', 'Astacus', 'unmorality', 'amortizable', 'unobsequious', 'xyphoid', 'lamboys', 'Nelumbonaceae', 'triangled', 'tailfirst', 'suppressor', 'desolating', 'uncorruption', 'reimprint', 'rollicker', 'spart', 'nonintellectual', 'protohuman', 'incompactness', 'overrepresent', 'spermatocystic', 'panmeristic', 'neckercher', 'swarthness', 'Neomorpha', 'delicateness', 'parastemon', 'uneatable', 'unsubstantiate', 'phlegmatically', 'ramequin', 'inseer', 'spikenard', 'scurvied', 'Slavonicize', 'Egyptological', 'dialectic', 'unclassible', 'unray', 'heartsome', 'overglorious', 'uncollectedness', 'derout', 'larrikinism', 'whisperer', 'inquisiturient', 'Cadwal', 'psychogenic', 'metromalacoma', 'preacuteness', 'restitutionism', 'ruesomeness', 'hemihypalgesia', 'merger', 'Lyrid', 'vesiculase', 'Yurucari', 'asleep', 'egghead', 'secretary', 'hemiacetal', 'volume', 'yesternight', 'unflurried', 'pyrenomycetous', 'Tetrodon', 'indiscretionary', 'adularescence', 'unadvancing', 'disinterested', 'Alleghenian', 'disarrange', 'belga', 'outban', 'manavelins', 'glibly', 'isoseismic', 'forgot', 'Sistrurus', 'untenably', 'tritencephalon', 'drapable', 'crownlet', 'mastectomy', 'finikin', 'crustalogist', 'codivine', 'buckhorn', 'moralist', 'gallicole', 'diluted', 'fostell', 'interdestructiveness', 'prereadiness', 'infantilism', 'specimenize', 'marteline', 'unimpurpled', 'definably', 'beveto', 'entotympanic', 'disparaging', 'underivedness', 'bootlessly', 'discrimination', 'Piscataqua', 'gummy', 'chidra', 'mindlessness', 'microgroove', 'jovialistic', 'Amarantus', 'malapropism', 'calycifloral', 'nonreactor', 'hillocked', 'endocyemate', 'ere', 'reignite', 'permutate', 'cumaphytism', 'forefault', 'unamused', 'symplectic', 'unjudging', 'chelation']

# **************************** START GUESSING GAME ***************************
def secret_num_dist_comparison(dist_new, dist_old):
    if dist_new > dist_old:
        print('Colder.')
    else:
        print('WARMER!')

def ask_num_game():
    low = 1
    high = 100
    secret_num = random.randint(low, high) # generate random secret number
    num_guess = 0
    temp_dist_to_secret_num = 100
    max_guess = secret_num
    min_guess = secret_num
    game_over = False
    

    while not game_over:
        guess = int(input(f'Input a number between {low} and {high} \n'))

        # Give warnings if player guess larger than max_guess
        # or guess smaller than min_guess
        if num_guess != 0:
            if guess > max_guess and guess > secret_num:
                print('WARNING: Bigger guess than before.')
            else:
                max_guess = guess
            if guess < min_guess and guess < secret_num:
                print('WARNING: Smaller guess than before.')
            else:
                min_guess = guess

        dist_to_secret_num = abs(secret_num - guess)
        
        if guess == secret_num:
            game_over = True
        elif guess < secret_num:
            # Tell player how close they are (low)
            if dist_to_secret_num >= 30 and dist_to_secret_num < 15:
                print('Wayyy too low')
            elif dist_to_secret_num >= 15 and dist_to_secret_num < 30:
                print('Too low')
            else:
                print('Too low but close')
            
            if num_guess != 0:
                secret_num_dist_comparison(dist_to_secret_num, temp_dist_to_secret_num)
            num_guess += 1
        else:
            # Tell player how close they are (high)
            if dist_to_secret_num >= 30 and dist_to_secret_num < 15:
                print('Wayyy too high')
            elif dist_to_secret_num >= 15 and dist_to_secret_num < 30:
                print('Too high')
            else:
                print('Too high but close')

            if num_guess != 0:
                secret_num_dist_comparison(dist_to_secret_num, temp_dist_to_secret_num)
            num_guess += 1

        temp_dist_to_secret_num = dist_to_secret_num
    print('CONGRATULATIONS!!!')
    print(f'Number of guess to win: {num_guess}')

# **************************** END GUESSING GAME ****************************

# **************************** START HANGMAN ****************************
MAX_STRIKES = 6
SECRET_WORD = random_words[random.randint(1, len(random_words) - 1)].upper() # randomly select secret word from list of words

def make_guess_word():
    guess_word = []
    for letter in SECRET_WORD:
        guess_word.append('_')
    return guess_word

def place_instances_of_letter(cur_word, letter):
    letter_indices = []
    secret_word_as_list = list(SECRET_WORD)

    # get indices of guessed letter
    for i in range(len(secret_word_as_list)):
        if secret_word_as_list[i] == letter:
            letter_indices.append(i)
    # replace instances of guessed letter in cur_word
    for i in letter_indices:
        print(cur_word[i])
        print(i)
        cur_word[i] = letter
    return cur_word

def hangman():
    strikes = 0
    game_over = False
    cur_word = make_guess_word() # represented as a list, not a string
    letters_remaining = set(SECRET_WORD)

    print(cur_word)

    while not game_over:
        guess_letter = input('Guess a letter! \n').upper()
        if guess_letter in letters_remaining:
            letters_remaining.remove(guess_letter)
            cur_word = place_instances_of_letter(cur_word, guess_letter)

            print(f'{guess_letter} is part of the secret word!')
            print(cur_word)
            
            if len(letters_remaining) <= 0:
                game_over = True
                print('YOU WON THE GAME!')
                print(f'The secret word was {SECRET_WORD}')
        else:
            strikes += 1
            if strikes >= MAX_STRIKES:
                game_over = True
                print('Sorry, try again :(')
                print(f'The word was {str(SECRET_WORD)}')
            print(f'Num Strikes: {strikes}')

# **************************** END HANGMAN ****************************


# **************************** START PRIMES ****************************

def prime_nums_slow():
    n = 50000
    start = time.time() # Get current timestamp

    for number_to_test in range(3, n):
        is_a_prime = True

        for current_divide_by in range(3,int(number_to_test)+1,2):
            if number_to_test % current_divide_by == 0:
                is_a_prime = False
    
    end = time.time()
    print("Total Time Non-Optimized for up to 50000:", end - start)
    return end - start

def prime_nums_optimized():
    n = 50000
    start = time.time() # Get current timestamp

    for number_to_test in range(3, n ,2):
        is_a_prime = True

        for current_divide_by in range(3,int(number_to_test**0.5)+1,2):
            if number_to_test % current_divide_by == 0:
                is_a_prime = False
    
    end = time.time()
    print("Total Time Optimized for up to 50000:", end - start)
    return end - start

def get_Nth_prime(n: int) -> int:
    list_primes = [2, 3]

    # special case where user is asking for 1st or 2nd prime
    if n == 1 or n == 2:
        return list_primes[n - 1]

    next_prime = list_primes[len(list_primes) - 1]	# set next_prime to end of list_primes, which = 3
    # loop while we havent added the next prime
    while len(list_primes) != n:
        next_prime += 2
        if is_prime(next_prime, list_primes):
            list_primes.append(next_prime)
    # print(list_primes)
    print(f'{n}th Prime = {next_prime}')
    return next_prime

# checks if n is evenly divisible by previous primes
def is_prime(n: int, list_primes: list) -> bool:
    n_sqrt = int(n**0.5)
    for prime in list_primes:
        if prime > n_sqrt: 	# an int multiple will be <= half of an int n - so if a prime is > half of n, then n is also prime
            return True
        if n % prime == 0:	# if n evenly divisible by a prime, it is not prime (is composite)
            return False
    return True
# **************************** END PRIMES ****************************

def prompt_menu():
    game = int(input('Press a number: \n 1. Guess Number Game. \n 2. Hangman. \n 3. Print Primes. \n 4. Exit. \n'))
    result = False
    match game:
        # GUESS NUMBER
        case 1:
            # result = ask_num_game()
            result = 1
            ask_num_game()
        # HANGMAN
        case 2:
            result = 2
            hangman()
        # PRIMES
        case 3:
            # n = int(input('Enter prime number upper bound: \n'))
            # result = get_primes_less_than_N_optimized(n)
            print('Computing...')

            prime_time_fast = prime_nums_optimized()
            prime_time_slow = prime_nums_slow()
            print(f'Time saved through optimization with n = 50000: {prime_time_slow - prime_time_fast}')
            # Total Time Non-Optimized for up to 50000: 24.352458000183105
            # Total Time Optimized for up to 50000: 0.05708479881286621
            # Time saved through optimization with n = 50000: 24.29537320137024

            N = 2000000
            start = time.time()
            get_Nth_prime(N)
            end = time.time()
            print(f'Time to get {N}th prime: {end - start}')
            # 2000000th Prime = 32,452,843
            # Time to get 2000000th prime: 60.06425404548645
        # QUIT
        case 4:
            result = False
            print('Thank you for playing! Goodbye.')
    return result

if __name__ == "__main__":
    # Menu Prompting
    game_over = False
    while not game_over:
        result = prompt_menu()
        if result is False:
             game_over = True
    
