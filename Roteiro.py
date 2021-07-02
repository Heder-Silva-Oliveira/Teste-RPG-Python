def intro(txt):
    if txt == 'Mago':
        print("  O salão esta em silencio, todos estão focando suas energias para invocar, uma áurea \n" 
        ",porem desta vez não é uma qualquer, esta é superior, você esta sentado no meio do pentagrama\n" 
        "quando percebe uma perturbação nos seus sentidos, você já não consegue distinguir o que é \n" 
        "olfato ou tato, oque é paladar ou audição, tudo esta confuso, você soa com frio, sente \n" 
        "sede estando saciado você não sente o chão, você são sente o ar, você não sente nada.")
    if txt == 'Caçador':
        print("  As folhas farfalham ao vendo, pássaros grasnam e esses são os sons mais altos que você\n" 
        "ouve porem seus longos anos em florestam e dão a habilidade de escutar além disso, sons de\n" 
        "cacos pisando em folhas e galhos secos, e barulho típico que para você já é conhecido o chão torna-se\n" 
        "claros aos seus ouvidos, e uma grata sensação de vitoria vem a tona, a final você acertou com precisão\n" 
        "o local da emboscada, mas você já esta familiarizado com isso e não deixa a emoção tomar conta. ")
    if txt == 'Guerreiro':
        print('O calor da batalha já fora muitas vezes testado por você, os gritos de dor as suplicas pela vida\n'
        'tudo isso você já conhece, mas esta batalha te parece mais difícil, talvez pela quantidade de inimigos\n'
        'ou também pelo calor do sol que os castiga, mas o certo é, você esta cansado  mais de uma vez no ultimo\n'
        'você consegue desviar fios de estadas e machados, você vê ao seu lado camaradas morrendo, camaradas matando\n'
        'suas forças só estão se mantendo graças a seu condicionamento físico e sua coragem, porem tudo tem seu limite.')

def jogomago(decisao):
    if decisao == 1:
        #A
        print('  Você tenta abrir os olhos, se esforça, você deixa de pensar nos textos lidos, nos rituais e palavras,\n' 
        'e se concentra em se livrar desta sensação, e por fim consegue seus olhos se abrem grandes e assustados,\n' 
        'todos seus sentidos voltam ao normal como se nada houvera mudado. E o sentimento vem forte em você o\n' 
        'sentimento de perda, você sabe que falhou, que jamais conseguirá novamente conjurar essa áurea superior.')
    if decisao == 2:
        #B
        print('  Você não se intimida com a força da áurea, você sabe que isso é apenas uma tentativa dela de não ser\n' 
        'conjurada, seu foco aumenta, você se concentra, pouco a pouco sua visão etérea começa a focar e distinguir\n' 
        'seu objetivo, uma silhueta é revelada, você encontrou nos confins do limbo, você esta de frente para a\n' 
        'portadora da áurea')


def jogodormago2(decisao,decisao2):
    if decisao and decisao2 == 1:
        #AA
        print('Você esta revoltado com sigo, e começa a andar pelo salão alguns outros magos se aproxima de você para\n'
        'conversar mas você os evita, nada é capaz de tirar sua revolta, não agora, você continua andando e quando se\n'
        'da por si, você chega a um corredor onde se depara com uma porta quase imperceptível, pequena e debaixo de uma\n'
        'escada, você acredita que esta porta parece ter sido revelada somente à você, você se sente escolhido.')
    elif decisao == 1 and decisao2 == 2:
        #AB
        print('Um mago ainda esta tentando conjurar, a inveja um sentimento tão primitivo invade você, é inaceitável\n'
        'você um grande mago não conseguir e esse forasteiro sim, você rapidamente olha para o lado e vê um grande \n'
        'candelabro com muitas velas, uma pequena magia sai de seus dedos na direção, no momento em que ninguém te \n'
        'observa, o candelabro cai e a grande cortina próximo dele se incendeia, causando o espanto de todos, isso foi \n'
        'suficiente para desconcentrar o remanescente,e dele se levanta furioso com olhos flamejantes, olha para \n'
        'todos e foca os olhos em você.')
    elif decisao == 2 and decisao2 == 1:
        #BA
        print('Você se levanta glorioso você é um dos poucos no mundo a ter uma áurea superior,  ao seu redor  vários\n'
        'outros magos  estão no salão e alguns se aproximam te perguntando se conseguiu o feito, e você não esconde e\n'
        'revela que sim, você é parabenizado, e alguns mais jovens até mesmo demonstram interesse em aprender mais com\n'
        'você, enquanto isso o mago que ainda tentava conjurar a áurea se levanta com um sorriso malévolo no rosto, e sai do\n'
        'salão sem falar com ninguém.')
    elif decisao == 2 and decisao2 == 2:
        #BB
        print('Você se levanta vencedor, maior que os demais você é um dos poucos no mundo com esta áurea, os outros \n'
        'um mago ainda persiste, mas você acredita que ele não saberá usa-la com sabedoria, ele irá usar para o \n'
        'mal,  irá atrapalhar a vida de outros em beneficio próprio você se julga o único capaz de impedir isso, e de \n'
        'maneira furtiva você invade a mente de um jovem aprendiz, fazendo-o cair  em cima do mago. perdendo toa a \n'
        'concentração, ele se levanta e furioso tentam castigar o aprendiz, mas é impedido por outros magos.')


def jogodormago3(guia):
    if guia == 'MAAA':
        print("Você abre a porta sem dificuldade, e antes e entrar uma breve olhada  ao redor para não ser notado por \n"
      "outros, entrando o que se revela a você é assustador, mesmo para um mago e conjuração,, tomos antigos com símbolos\n"
      "profanos e alguns com rostos entalhados na capa, estão por toda parte pergaminhos com selos macabros, estão amontoados\n"
      "em prateleiras , ao caminhar mais para o fundo da sala, um som como de um vento passa por você e a porta que \n"
      "outrora aberta, simplesmente deixa de existir você esta selado dentro da câmara, chamas azuis se acendem empiras\n"
      "espalhadas pela sala, e um grande livro centrado em um pedestal se abre te convidando a lê-lo.  ")
    elif guia == "MAAB":
        print('Você não se sente seguro sendo atraído por essa oportunidade, os anos já vividos te deram esse discernimento,\n'
      'você já se sente cansado, foi árduo a tentativa de conjuração, você vai a caminho da porta para sair do salão \n'
      'onde os magos se reúnem, e já a alguns minutos de distancia andando a pé você houve um gritos aterradores, vindo \n'
      'de uma cabana não muito afastada da estrada onde você caminha, correndo em direção aos gritos, já se cessaram, \n'
      'você já sabe o que causou isso, você entra na cabana, e você vê um jovem casal, mortos e uma fumaça negra saindo \n'
      'de seus corpos, você sabe que foi o mago que você deixou terminar o ritual, ele se tornou o que você temia.')
    elif guia == 'MABA':
        print('Sem perguntar nada ele já se prepara para te atacar conjurando magias')
    elif guia == 'MABB':
        print('Sem perguntar nada ele já se prepara para te atacar conjurando magias')
    elif guia == 'MBAA':
        print('De imediato e se desvencilhando dos outros magos, você sai ao encalço da ameaça, já a alguns minutos de\n'
      'corrida você consegue ver ele se aproximando de uma cabana, não tão longe da estrada, seu instinto te faz lançar\n'
      'sobre ele uma magia, porque a intenção dele não é outra se não aniquilar as vidas dos que ali habitam a fim de \n'
      'fortalecer a áurea dele com as almas dos pobres coitados.')
    elif guia == 'MBAB':
        print('Você deixa o mago partir sem se intrometer, e deixa que a fama momentânea tome conta da situação, depois \n'
      'de horas de e conversas aleatórias, um pensamento vem a sua cabeça, o que poderia fazer aquele forasteiro com todo \n'
      'aquele poder que você igualmente agora possui, seria ele também forte o bastante para não se corromper, seria ele \n'
      'agora a mais nova ameaça?, se isso acontecer você seria responsável por ser o único capaz de detê-lo e não o fez.')
    elif guia == 'MBBA':
        print("Você deixa eles se entenderem, decide não participar da confusão e começa a andar despretensiosamente \n"
      "pelo salão, faz isso para se afastar o tumulto,  passando por varias estantes de livros e já bem distante da \n"
      "presença e outros magos, um livro te chama a atenção, nele existem letras desconhecidas, sua curiosidade o faz \n"
      "pega-lo e abri-lo, sua áurea recém possuída agita em você e as letras começam a se tornar compreensíveis,   você \n"
      "o lê, a partir de agora você começa a ver o mundo com mais nitidez, o que era oculto as olhos agora se revelam, \n"
      "nada pode se esconder de você.")
    elif guia == 'MBBB':
        print("Você decide acabar rápido com toda a confusão, você conjura uma magia, ao redor e todos, fazendo-os \n"
      "imóveis, você consegue êxito menos com o mago forasteiro, este se vira para você e conjura uma magia de ataque.")



def jogocacador(decisao):
    if decisao == 1:
        #A
        print('  Você sabe que não é a melhor ideia prosseguir com o intento, e rápido você escala um grande salgueiro,\n'
        'revelando muitos servos e vario com galhadas enormes você sabe que elas lhe renderam uma boas moedas de ouro\n'
        'o suficiente para passar o inverno muito bem abastecido, e agora só é preciso esperar o momento certo.')
    if decisao == 2:
        #B
        print('  A flecha sai do seu arco com força e precisão, golpe fatal para o servo, porem ele não estava sozinho\n'
        'e em um instante todos se dispersam e você pode notar que muito deles tinham enormes galhadas, e estes você não\n'
        'conseguirá emboscar, e o seu abate te dará pouco menos do que você esperava, afinal era um velho servo, ferido\n'
        'e sem chifres')


def jogodorcacador2(decisao,decisao2):
    if decisao and decisao2 == 1:
        #AA
        print('Você chega ao centro do vilarejo e segue ate o açougueiro e tira da garupa de seu cavalo grande parte\n'
        'da carne do servo e negocia com o comerciante, no fim você teve a impressão de ter se saído melhor na negociação\n'
        'que o açougueiro, saindo de lá você chega ao artesão para vender parte do couro obtido, feito a venda você sai\n'
        'com um grande sorriso, esta vez o negocio foi vantajoso, e por fim passa até o comerciante do vilarejo este que\n'
        'compra e vende as mais variadas coisas, você consegue convence-lo a comprar a grande galhada do servo, mas desta\n'
        'vez o comerciante sai ganhando e com ampla vantagem')
    elif decisao == 1 and decisao2 == 2:
        #AB
        print('Você chega a sua casa com segurança graças ao seu conhecimento da floresta sabendo os locais a serem \n'
        'evitados, você logo desce do cavalo e começa a preparar a carne  o couro guardando de forma adequada para \n'
        'passar o inverno, terminando, você já a noite acende a lareira e prepara sua janta,  mas um cheiro estranho \n'
        'vindo de cosa da casa de coloca em alerta é cheiro  de predador , algo esta rondando sua casa, você já é capaz\n’'
        'de ouvir os sons dos passos alternando entre duas e quatro patas, um rosnado nunca antes ouvido por você é \n'
        'emitido pelo animal, o medo te visita novamente depois de muito tempo, e o arrependimento e ter trazido toda \n'
        'essa carne para casa vem a sua cabeça.')
    elif decisao == 2 and decisao2 == 1:
        #BA
        print('Chegando ao vilarejo você vende metade da carne que conseguiu, e uma pequena parte do couro, o açougueiro\n'
        'comprou tudo porque ele oportunamente estava também precisando de couro para um novo avental, você consegue\n'
        'fazer um bom negocio com ele, e sai satisfeito com o negocio e insatisfeito com a caçada, arrependido de\n'
        'não ter esperado o melhor momento, mesmo assim você volta para sua casa.')
    elif decisao == 2 and decisao2 == 2:
        #BB
        print('Você chega a sua casa sem dinheiro porque considerou pouco demais para vender, é preciso deixar carne \n'
        'para passar o inverno, você é sozinho, não tem família, não precisa de muita carne para se manter, mas salgar\n'
        'a carne e trabalhar o couro te deixará ocupado por um longo período, tudo isso antes do inverno, esta foi sua \n'
        'ultima caçada, a próxima só na primavera. ')



def jogoguerreiro(decisao):
    if decisao == 1:
        #A
        print('Você lentamente vai se afastando a linha e frente, até chegar na retaguarda onde não há choque de\n'
        'espadas mas há e muito gritos de dor pois é aqui onde os mutilaos são trazidos para os cuidados dos médicos\n'
        'você se senta e bebe um odre de água, seu corpo agradece, os poucos momentos de descanso é o suficiente para\n'
        'seu vigor voltar')
    if decisao == 2:
        #B
        print('Você grita palavras de ordens muito mais alto que os gritos dos outros, você vê seus aliados ao seu redor\n'
        'respondendo e avançando com mais força e por um momento isso foi suficiente para intimidar vários os advesários\n'
        'que estavam ao seu redor, mas esse seu esforço foi além do que seu corpo é capaz, suas vistas escurecem e os sons\n'
        'sobem e o silencio chega até você')


def jogoquerreiro2(decisao, decisao2):
    if decisao and decisao2 == 1:
        #AA
        print('Você se aproxima dos seus camaradas para beber junto, conforme se aproxima os olhares de todos começa\n'
        'começa a te fitar, com expressões de indignação e raiva, mas ninguém fala nada apenas te olham com julgamento\n'
        'você sabe que isso esta acontecendo porque você saiu do meio da batalha para descansar enquanto muitos dos\n'
        'seus irmãos tombaram em batalha')
    elif decisao == 1 and decisao2 == 2:
        #AB
        print('A adentrar a grande tenta do hospital você encontra vários amigos algum agonizando ante a morte outros\n'
        'em profundo sono induzido, ao continuar caminhando você escuta um murmúrio diferente alguém esta gemendo de\n'
        'dor mas isso deveria ser comum naquele ambiente, porém com mais atenção você percebe que não é gemido de dor\n'
        'física, é um tormento mental, ao olhar para o paciente o rosto dele esta em volto em um lençol, ele esta\n'
        'separado deitado isolado em um canto da tenda')
    elif decisao == 2 and decisao2 == 1:
        #BA
        print('Você sai da tenda do hospital se aproxima de seus camaradas e alguns deles se levantam e grita seu nome,\n'
        'e brindam sua bravura, alguns poucos até mesmo chegam a dizer que a vitória foi alcançada graças ao\n'
        'todos se alegram seu encorajamento, essas palavras foram bem aceitas pela maioria, mas alguns não gostaram \n'
        'muito, você se sente bem por estar com eles, apesar das dores e sequelas da batalha.')
    elif decisao == 2 and decisao2 == 2:
        #BB
        print('Você abre seus olhos lentamente e junto com a visão vem as dores, inúmeras e por toda parte de seu corpo\n'
        'você geme de dor involuntariamente, passando alguns minutos você se da conta de que esta em uma tenda de hospital\n'
        'os anteriores sons de estadas se chocando e gritos de batalha deram lugar a gritos de dores, tão desesperadores\n'
        'que te deixaram feliz por não sentir o mesmo que muitos deles, alguns nunca mas voltaram a ver, outros não andarão\n'
        'e a maioria nunca mais estarão entre os vivos.')

