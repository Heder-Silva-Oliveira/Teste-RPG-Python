def intro(txt):
    if txt == 'Mago':
        print("  O salão esta em silencio, todos estão focando suas energias para invocar, uma áurea \n" 
        ",porem desta vez não é uma qualquer, esta é superior, você esta sentado no meio do pentagrama\n" 
        "quando percebe uma perturbação nos seus sentidos, você já não consegue distinguir o que é \n" 
        "olfato ou tato, oque é paladar ou audição, tudo esta confuso, você soa com frio, sente \n" 
        "sede estando saciado você não sente o chão, você são sente o ar, você não ente nada.")
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
        print('  Você tenta abrir os olhos, se esforça, você deixa de pensar nos textos lidos, nos rituais e palavras,\n' 
        'e se concentra em se livrar desta sensação, e por fim consegue seus olhos se abrem grandes e assustados,\n' 
        'todos seus sentidos voltam ao normal como se nada houvera mudado. E o sentimento vem forte em você o\n' 
        'sentimento de perda, você sabe que falhou, que jamais conseguirá novamente conjurar essa áurea superior.')
    if decisao == 2:
        print('  Você não se intimida com a força da áurea, você sabe que isso é apenas uma tentativa dela de não ser\n' 
        'conjurada, seu foco aumenta, você se concentra, pouco a pouco sua visão etérea começa a focar e distinguir\n' 
        'seu objetivo, uma silhueta é revelada, você encontrou nos confins do limbo, você esta de frente para a\n' 
        'portadora da áurea')


def jogodormago2(decisao,decisao2):
    if decisao and decisao2 == 1:
        print('Você esta revoltado com sigo, e começa a andar pelo salão alguns outros magos se aproxima de você para\n'
        'conversar mas você os evita, nada é capaz de tirar sua revolta, não agora, você continua andando e quando se\n'
        'da por si, você chega a um corredor onde se depara com uma porta quase imperceptível, pequena e debaixo de uma\n'
        'escada, algo em você já sabe que aquilo que esta porta parece ter sido revelada à você, você se sente escolhido.')
    elif decisao == 1 and decisao2 == 2:
        print('Dois magos ainda estão tentando conjurar, a inveja um sentimento tão primitivo invade você, é inaceitável\n'
        'você um grande mago não conseguir e esses forasteiros sim, você rapidamente olha para o lado e vê um grande \n'
        'candelabro com muitas velas, uma pequena magia sai de seus dedos na direção, no momento em que ninguém te \n'
        'observa, o candelabro cai e a grande cortina próximo dele se incendeia, causando o espanto de todos, isso foi \n'
        'suficiente para desconcentrar os remanescentes, um deles se levanta furioso com olhos flamejantes, olha para \n'
        'todos e foco os olhos em você.')
    elif decisao == 2 and decisao2 == 1:
        print('Você se levanta glorioso você é um dos poucos no mundo a ter uma áurea superior,  ao seu redor  vários\n'
        'outros magos  estão no salão e alguns se aproximam te perguntando se conseguiu o feito, e você não esconde e\n'
        'revela que sim, você é parabenizado, e alguns mais jovens até mesmo demonstram interesse em aprender mais com\n'
        'você, enquanto isso um dos que ainda tentavam conjurar se levanta com um sorriso malévolo no rosto, e sai do\n'
        'salão sem falar com ninguém.')
    elif decisao == 2 and decisao2 == 2:
        print('Você se levanta vencedor, maior que os demais você é um dos poucos no mundo com esta áurea, os outros \n'
        'dois magos ainda persistem, mas você acredita que eles não saberão usa-la com sabedoria, ele irão usar para o \n'
        'mal  irão atrapalhar a vida de outros em beneficio próprio você se julga o único capaz de impedir isso, e de \n'
        'maneira furtiva você invade a mente de um jovem aprendiz, fazendo-o cair  em cima dos dois magos fazendo-os \n'
        'perder a concentração, eles se levantam e furiosos tentam castigar o aprendiz, mas são impedido por outros magos.')



def jogocacador(decisao):
    if decisao == 1:
        print('  Você sabe que não é a melhor ideia prosseguir com o intento, e rápido você escala um grande salgueiro,\n'
        'revelando muitos servos e vario com galhadas enormes você sabe que elas lhe renderam uma boas moedas de ouro\n'
        'o suficiente para passar o inverno muito bem abastecido, e agora só é preciso esperar o momento certo.')
    if decisao == 2:
        print('  A flecha sai do seu arco com força e precisão, golpe fatal para o servo, porem ele não estava sozinho\n'
        'e em um instante todos se dispersam e você pode notar que muito deles tinham enormes galhadas, e estes você não\n'
        'conseguirá emboscar, e o seu abate te dará pouco menos do que você esperava, afinal era um velho servo, ferido\n'
        'e sem chifres')


def jogodorcacador2(decisao,decisao2):
    if decisao and decisao2 == 1:
        print('Você chega ao centro do vilarejo e segue ate o açougueiro e tira da garupa de seu cavalo grande parte\n'
        'da carne do servo e negocia com o comerciante, no fim você teve a impressão de ter se saído melhor na negociação\n'
        'que o açougueiro, saindo de lá você chega ao artesão para vender parte do couro obtido, feito a venda você sai\n'
        'com um grande sorriso, esta vez o negocio foi vantajoso, e por fim passa até o comerciante do vilarejo este que\n'
        'compra e vende as mais variadas coisas, você consegue convence-lo a comprar a grande galhada do servo, mas desta\n'
        'vez o comerciante sai ganhando e com ampla vantagem')
    elif decisao == 1 and decisao2 == 2:
        print('Você chega a sua casa com segurança graças ao seu conhecimento da floresta sabendo os locais a serem \n'
        'evitados, você logo desce do cavalo e começa a preparar a carne  o couro guardando de forma adequada para \n'
        'passar o inverno, terminando, você já a noite acende a lareira e prepara sua janta,  mas um cheiro estranho \n'
        'vindo de cosa da casa de coloca em alerta é cheiro  de predador , algo esta rondando sua casa, você já é capaz\n’'
        'de ouvir os sons dos passos alternando entre duas e quatro patas, um rosnado nunca antes ouvido por você é \n'
        'emitido pelo animal, o medo te visita novamente depois de muito tempo, e o arrependimento e ter trazido toda \n'
        'essa carne para casa vem a sua cabeça.')
    elif decisao == 2 and decisao2 == 1:
        print('Chegando ao vilarejo você vende metade da carne que conseguiu, e uma pequena parte do couro, o açougueiro\n'
        'comprou tudo porque ele oportunamente estava também precisando de couro para um novo avental, você consegue\n'
        'fazer um bom negocio com ele, e sai satisfeito com o negocio e insatisfeito com a caçada, arrependido de\n'
        'não ter esperado o melhor momento, mesmo assim você volta para sua casa.')
    elif decisao == 2 and decisao2 == 2:
        print('Você chega a sua casa sem dinheiro porque considerou pouco demais para vender, é preciso deixar carne \n'
        'para passar o inverno, você é sozinho, não tem família, não precisa de muita carne para se manter, mas salgar\n'
        'a carne e trabalhar o couro te deixará ocupado por um longo período, tudo isso antes do inverno, esta foi sua \n'
        'ultima caçada, a próxima só na primavera. ')



def jogoguerreiro(decisao):
    if decisao == 1:
        print('Você lentamente vai se afastando a linha e frente, até chegar na retaguarda onde não há choque de\n'
        'espadas mas há e muito gritos de dor pois é aqui onde os mutilaos são trazidos para os cuidados dos médicos\n'
        'você se senta e bebe um odre de água, seu corpo agradece, os poucos momentos de descanso é o suficiente para\n'
        'seu vigor voltar')
    if decisao == 2:
        print('Você grita palavras de ordens muito mais alto que os gritos dos outros, você vê seus aliados ao seu redor\n'
        'respondendo e avançando com mais força e por um momento isso foi suficiente para intimidar vários os advesários\n'
        'que estavam ao seu redor, mas esse seu esforço foi além do que seu corpo é capaz, suas vistas escurecem e os sons\n'
        'sobem e o silencio chega até você')


def jogoquerreiro2(decisao, decisao2):
    if decisao and decisao2 == 1:
        print('Você se aproxima dos seus camaradas para beber junto, conforme se aproxima os olhares de todos começa\n'
        'começa a te fitar, com expressões de indignação e raiva, mas ninguém fala nada apenas te olham com julgamento\n'
        'você sabe que isso esta acontecendo porque você saiu do meio da batalha para descansar enquanto muitos dos\n'
        'seus irmãos tombaram em batalha')
    elif decisao == 1 and decisao2 == 2:
        print('A adentrar a grande tenta do hospital você encontra vários amigos algum agonizando ante a morte outros\n'
        'em profundo sono induzido, ao continuar caminhando você escuta um murmúrio diferente alguém esta gemendo de\n'
        'dor mas isso deveria ser comum naquele ambiente, porém com mais atenção você percebe que não é gemido de dor\n'
        'física, é um tormento mental, ao olhar para o paciente o rosto dele esta em volto em um lençol, ele esta\n'
        'separado deitado isolado em um canto da tenda')
    elif decisao == 2 and decisao2 == 1:
        print('Você sai da tenda do hospital se aproxima de seus camaradas e alguns deles se levantam e grita seu nome,\n'
        'e brindam sua bravura, alguns poucos até mesmo chegam a dizer que a vitória foi alcançada graças ao\n'
        'todos se alegram seu encorajamento, essas palavras foram bem aceitas pela maioria, mas alguns não gostaram \n'
        'muito, você se sente bem por estar com eles, apesar das dores e sequelas da batalha.')
    elif decisao == 2 and decisao2 == 2:
        print('Você abre seus olhos lentamente e junto com a visão vem as dores, inúmeras e por toda parte de seu corpo\n'
        'você geme de dor involuntariamente, passando alguns minutos você se da conta de que esta em uma tenda de hospital\n'
        'os anteriores sons de estadas se chocando e gritos de batalha deram lugar a gritos de dores, tão desesperadores\n'
        'que te deixaram feliz por não sentir o mesmo que muitos deles, alguns nunca mas voltaram a ver, outros não andarão\n'
        'e a maioria nunca mais estarão entre os vivos.')

