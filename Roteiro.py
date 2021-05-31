def intro (txt):
    if txt == 'Mago':
        print("  O salão esta em silencio, todos estão focando suas energias para invocar, uma aurea \n" 
        ",porem desta vez não é uma qualquer, esta é superior, você esta sentado no meio do pendagrama\n" 
        "quando percebe uma pertubação nos seus sentidos, você ja não consegue distinguir o que é \n" 
        "oufato ou tato, oque é paladar ou audição, tudo esta confuso, você soua com frio, sente \n" 
        "sede estando saciado você não sente o chão, você são sente o ar, você não ente nada.")
    if txt == 'Caçador':
        print("  As folhas farfalham ao vendo, passaros grasnam e esses são os sons mais altos que você\n" 
        "ouve porem seus longos anos em florestam e dão a habilidade de escutar alem disso, sons de\n" 
        "cacos pisando em folhas e galhos secos, e barulho tipico que para você ja é conhecido o chão torna-se\n" 
        "claros aos seus ouvidos, e uma grata sensação de vitotia vem a tona, a final você acertou comprecisão\n" 
        "o local da emboscada, mas você ja esta familarizzado com isso e não deixa a emoção tomar conta. ")


def jogomago (decisao):
    if decisao == 1:
        print('  Você tenta abrir os olhos, se esforça, você deixa de pensar nos textos lidos, nos rituais e palavras,\n' 
        'e se consentra em se livrar desta senção, e por fim consegue seus olhos se abrem grandes e assustados,\n' 
        'todos seus sentidos voltam ao normal como se nada houvera mudado. E o sentimento vem forte em você o\n' 
        'sentimento de perda, você sabe que falhou, que jamais conseguirá novamente tentar conjurar essa aurea superior.')
    if decisao == 2:
        print('  Você não se intimida com a força da aurea, você sabe que isso é apenas uma tentativa dela de não ser\n' 
        'conjurada, seu foco aumenta, você se consentra, pouco a pouco sua visão eteria começa a focar e distinguir\n' 
        'seu objetivo, uma silueta é revelada, você encontrou nos confis do limbo, você esta de frente para a\n' 
        'portadora da aurea')


def jogocacador (decisao):
    if decisao == 1:
        print('  Você sabe que não é a melhor ideia proceguir com o intento, e rapido você escala um grande salgueiro,\n'
        'revelando muitos servos e vario com galhadas enormes você sabe que elas lhe renderam uma boas moedas de ouro\n'
        'o suficiente para passar o inverno muito bem abastecido, e agora só é preciso esperar o momento certo.')
    if decisao == 2:
        print('  A flexa sai do seu arco com força e precisão, golpe fatal para o servo, porem ele não estava sozinho\n'
        'e em um instante todos se dispersam e você pode notar que muito deles tinham enormes galhadas, e estes você não\n'
        'conseguirá emboscar, e o seu abate te dará pouco menos do que você esperava, afinal era um velho servo, ferido\n'
        'e sem chifres')
