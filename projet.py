#Auteur : SABIL MOHAMED AMINE
#PROJET AP1


from random import randint
import random
from interface import*

#FONCTION qui return une liste d'entiers compris entre 1 et 3
def generateur_liste():
    """
    :return: (list) liste  de int entre 1 et 3 générée aléatoirement
    :CU:Aucune
    :exemples:
    
    >>> l=generateur_liste()
    >>> len(l)
    12
    >>> l=generateur_liste()
    >>> all(i>=1 and i<=3 for i in l)
    True
    """
    fini=False
    while fini==False:
        m= input('longueur du plateau : ')
        try:
            assert  int(m)%4==0
            fini=True
        except ValueError:
            print('la longueur du plateau en chiffres entiers svp !')
        except AssertionError:
            print('la longueur du plateau doit etre un multiple de 4')
    liste=[]
    for i in range(int(m)):
        liste+=[randint(1,3)]
    return liste

#fonction qui retourne la liste des pseudos des joueurs de la partie
def pseudos():
    """
    :return:(list) la liste contenant les pseudos des joueurs
    :CU:Aucune
    :Exemples:
    >>> pseudos()
    ["a",'b','c','d']
    >>> pseudos()
    ['amine','mehdi']
    """
    fini = False
    while fini == False:
        nombre_joueur = input('Nombre(s) de joueur(s) : ')
        try:
            assert 1<=int(nombre_joueur) <= 4
            fini = True
        except ValueError:
            print('Nombre(s) de joueur(s) en chiffres décimaux !')
        except AssertionError:
            print('Nombre(s) de joueur(s) compris entre 1 et 4 svp')
    res=[] 
    for i in range(int(nombre_joueur)):
        fini=False
        a='Choisissez le pseudo du joueur n°'+ str(i+1) +' : '
        while fini==False:
            b=input(a)
            try:
                assert not b in res
                fini = True
            except AssertionError:
                print('Pseudo déjà selectionné !')
        res.append(b)
    return res
 
#Fonction qui permet à l'utilisateur de choisir le nombre de tours qu'il veut joueur  
def nbre_tours():
    """
    :return: (int)Le nombre de tours pour la partie
    :CU: Aucune
    :exemples:
    >>> nbre_tours()
    4
    >>> nbre_tours()
    5

    """
    fini=False
    while fini==False:
        nombre_tour= input('Nombre de tours : ')
        try:
            assert  1<=int(nombre_tour)
            fini=True
        except ValueError:
            print('Nombre de tours en chiffres entiers svp !')
        except AssertionError:
            print('Nombre de tours plus grand que 0 !')
    return int(nombre_tour)
            
#la fonction dico_joueur nous fournie  une liste de  dictionnaire adapté aux joueurs en fonction de leurs pseudo 
def dico_joueur(l):
    """
    :param l: (list) liste de pseudo de joueurs
    :return: (list) renvoie une liste de dictionnaire adapté aux joueurs en fonction de leurs pseudo
    :CU: l est une liste de str non vide
    :exemples:
    >>> dico_joueur(['aaaaa','coloc'])
    [{'casesparcourues':0,'pseudo':'aaaaa','position': 0, 'pieces': 5, 'etoiles': 0, 'objets': {'Voleur 5': 0, 'Voleur Etoile': 0, 'Dé chance': 0,"malchance":0, 'Dé méchant': 0}}, {'casesparcourues':0,'pseudo:'coloc','position': 0, 'pieces': 5, 'etoiles': 0, 'objets': {'Voleur 5': 0, 'Voleur Etoile': 0, 'Dé chance': 0,'malchance':0 'Dé méchant': 0}}]
    
    """
    joueurs=[]
    for i in range(len(l)):
        joueurs+=[{'casesparcourues':0,'pseudo':l[i],'position':0,'pieces' :5,'etoiles':0,'objets':{'Voleur 5': 0, 'Voleur Etoile': 0, 'Dé chance': 0, 'Dé méchant': 0,"malchance":0}}]
    return joueurs

# la fonction nous informe des détails de chaque joueur 
def deroulement(m,a):
    """
    :param m: (str) pseudo
    :param a: (dict) dictionnaire avec les stats de la partie
    :CU:pseudo appartient a a
    :return:(str) une chaine de caracteres qui passe avant chaque passage des joueurs
    :Exemples:
    >>> deroulement('c',{'casesparcourues':0,'pseudo':'c','position':0,'pieces' :5,'etoiles':0,'objets':{'Voleur 5': 0, 'Voleur Etoile': 0, 'Dé chance': 0, 'Dé méchant': 0,"malchance":0}}
    Au tour de c !
    Tu as :
    Piece(s): 5
    Etoile(s): 0
    Objet(s): Voleur 5: 0 - Voleur Etoile: 0
          Dé chance: 0 - Dé méchant: 0
    """
    ligne1='\n'+'Au tour de '+m+' !'
    ligne2='\n'+'Tu as :'
    ligne3='\n'+'Piece(s): '+str(a['pieces'])+'\n'+'Etoile(s): '+str(a['etoiles'])+'\n'+'Objet(s): '+'Voleur 5: '+str(a['objets']['Voleur 5'])+' - '+'Voleur Etoile: '+str(a['objets']['Voleur Etoile'])+'\n'+'          '+'Dé chance: '+str(a['objets']['Dé chance'])+' - '+'Dé méchant: '+str(a['objets']['Dé méchant'])
    return ligne1+ligne2+ligne3

#Fonction qui lance le dé
def de():
    """
    :return:(int) un entier entre 1 et 6.
    :CU:Aucune
    :Exemples:
    >>> de()
    3
    >>> de()
    5
    """
    return randint(1,6)

#Fonction qui nous informe si un joueur a des objets ou non 
def a_des_objets(m):
    """
    :param m: (dict) dictionnaire d'objets
    :return:(bool)True si m possede des objets et False sinon
    :CU:Aucune
    :Exemples:
    >>> a_des_objets({'Voleur 5': 0, 'Voleur Etoile': 0, 'Dé chance': 0, 'Dé méchant': 0,"malchance":0})
    False
    """
    a=0
    for i in m:
        if m[i] > 0:
            a+=1
        a=a-m['malchance']
    return a>0


#Fonction qui retourne les détails des objets du joueur qui a la main  
def objets_possedes(m):
    """
    :param m: (dict) dictionnaire d'objets
    :return :(str)une chaine de caracteres des objets possédés.
    :Exemples:
    >>> objets_possedes({'Voleur 5': 0, 'Voleur Etoile': 0, 'Dé chance': 0, 'Dé méchant': 0,"malchance":0})
    "Voleur 5: 0 - Voleur Etoile: 0 - Dé chance: 0 - Dé méchant: 0"
    """
    return 'Voleur 5: '+str(m['Voleur 5'])+' - '+'Voleur Etoile: '+str(m['Voleur Etoile'])+' - '+'Dé chance: '+str(m['Dé chance'])+' - '+'Dé méchant: '+str(m['Dé méchant'])

#Fonction qui nous informe de la case sur laquelle le joueur est tombé 
def detecteur_de_case(pos,plateau,perso):
    """
    :param pos: (int) position du perso dans le plateau
    :param plateau: (list) liste contenant les cases du plateau
    :param perso: (str) pseudo du perso
    :return :(str) une chaîne de caractères
    :CU:Aucune
    """
    if plateau[pos] == 1:
        return ('Vert',perso+' est tombé sur une case verte,\nIl gagne 3 pièces !')
    elif plateau[pos] == 2:
        return ('Rouge',perso+' est tombé sur une case rouge,\nIl perd 3 pièces !')
    else:
        return ('Bleu',perso+' est tombé sur une case bleue')

#Fonction qui génére un objet au hasard        
def objet_hasard():
    """
    :CU: Aucune
    :return:(str) un objet au hasard
    """
    l=['Dé méchant','Dé chance','Voleur 5','Voleur Etoile']
    a=randint(0,3)
    return l[a]
    
#Fonction qui nous informe de notre gain ou de perte après chaque lancement de 
def types_cases(l,d):
    """
    :param l:(list) une liste de joueurs
    :param d:(dict) dictionnaire d'un joueur
    :effet de bord: le joueur perd ou gagne des objets .
    """
    pos=d['position']
    if l[pos]==1:
        print('Félicitations,vous avez gagné 3 pièces car vous etes tombé dans une case verte')
        d['pieces']=d['pieces']+3
    elif l[pos]==2:
        print('Malheureusement,vous avez perdu 3 pièces car vous etes tombé dans une case rouge')
        d['pieces']=d['pieces']-3
        if d['pieces']<0:
            d['pieces']=0
    elif l[pos]==3:
        print('Félicitations vous avez gagné un objet aléatoire car vous etes tombé dans une case bleue')
        hasard=objet_hasard()
        print("Félicitations vous avez gagné un",hasard)
        for obj in d["objets"]:
            if obj==hasard:
                d["objets"][obj]= d["objets"][obj]+1
    
    
#Fonction qui permet au joueur qui a la main d'enlever 3 au dé d'un autre joueur  
def De_mechant(l,j,pseudos):
    """
    :param l:(list) liste des dictionnaires des joueurs
    :param j:(str) pseudo du joueur qui a la main
    :param pseudos:(list) liste des pseudos des joueurs
    :CU:None
    :effet de bord: demande à l'utilisatur de choisir un adversaire pour lui prendre un objet et affiche un message
    
    """
    fini=False
    while fini == False:
        cible = input('Sur quel joueur voulez-vous l\'utiliser ? ')
        try:
            assert cible in pseudos
            fini=True
        except AssertionError:
            print('Choisissez un adversaire existant svp !')
        for dic in l:
            if dic['pseudo']==cible:
                dic['objets']['malchance']+=1
            if dic['pseudo']==j:
                x=l.index(dic)
                l[x]['objets']['Dé méchant']-=1
                
        print(j+' a maudit '+cible)

#fonction qui permet au joueur de voler une étoile à un autre joueur
def voleur_etoile(l,j,pseudos):
    """
    :param l:(list) liste des dictionnaires des joueurs
    :param j:(str) pseudo du joueur qui a la main
    :param pseudos:(list) liste des pseudos des joueurs
    :CU:None
    :return:(str) une chaîne de caractères
    """
    vol=0
    fini=False
    while fini == False:
        cible = input('\nSur quel joueur voulez-vous l\'utiliser ? ')
        try:
            assert (cible in pseudos) or cible == 'Personne'
            fini=True
        except AssertionError:
            print('Choisissez un adversaire existant svp !')
    for dic in l:
        if dic['pseudo']==cible:
            z=l.index(dic)
        if dic['pseudo']==j:
            x=l.index(dic)
    if cible == 'Personne':
        print('Vous n\'avez pas utilisé votre Voleur Etoile.')
        return 'Personne'
    elif l[z]['etoiles'] > 0:
        l[z]['etoiles'] -=1
        l[x]['etoiles'] += 1
        print(j+' a volé 1 étoile à '+cible)
        l[x]['objets']['Voleur Etoile']-=1
    else:
        print('Vous n\'avez rien volé, c\'est dommage...')

#fonction qui permet au joueur de voler 5 pièces à un autre joueur
def voleur_5(l,j,pseudos):
    """
    :param l:(list) liste des dictionnaires des joueurs
    :param j:(str) pseudo du joueur qui a la main
    :param pseudos:(list) liste des pseudos des joueurs
    :CU:None
    :return:(str) une chaîne de caractères
    """

    fini=False
    while fini == False:
        cible = input('\nSur quel joueur voulez-vous l\'utiliser ? ')
        try:
            assert (cible in pseudos) or cible == 'Personne'
            fini=True
        except AssertionError:
            print('Choisissez un adversaire existant svp !')
    for dic in l:
        if dic['pseudo']==cible:
            z=l.index(dic)
        if dic['pseudo']==j:
            x=l.index(dic)    
    if cible == 'Personne':
        print('Vous n\'avez pas utilisé votre Voleur 5.')
        return 'Personne'
    elif l[z]['pieces'] < 5 :
        vol=l[z]['pieces']
        l[z]['pieces'] = 0
        l[x]['pieces']+= vol
        l[x]['objets']['Voleur 5']-=1
        print(p+' a volé '+vol+' piece(s) à '+cible)
    else:
        l[z]['pieces']-=5
        l[x]['pieces']+=5
        l[x]['objets']['Voleur 5']-=1
        print(j+' a volé 5 pieces à '+cible)

#Fonction qui permet au joueur d'acheter l'étoile 
def achete_etoile(pse,l,prix,a):
    """
    :param pse: (str) pseudo du joueur en question
    :param l: (list) liste des dictionnaires des joueurs
    :param prix: (int) prix de l'etoile
    :param a: (int) l'indice du dictionnaire du joueur en cours
    :CU:None
    :return:(str) Oui ou Non
    :Exemple:
    >>> achete_etoile('aaaaa', [{'casesparcourues':0,'pseudo':'aaaaa','position': 0, 'pieces': 5, 'etoiles': 0, 'objets': {'Voleur 5': 0, 'Voleur Etoile': 0, 'Dé chance': 0,"malchance":0, 'Dé méchant': 0}}],5,0)
    Oui
    """
    if l[a]['pieces'] >= prix:
        fini = False
        while fini == False:
            w=input('Veux tu acheter l\'étoile au prix de '+str(prix)+'(Oui ou non)')
            try:
                assert w == 'Oui' or w == 'Non'
                fini = True
            except AssertionError:
                print('Veuillez ecrire Oui ou Non !')
        if w == 'Oui':
            l[a]['pieces'] -= prix
            l[a]['etoiles'] += 1
            print('Vous avez acheté l\'étoile au prix de',prix)
            prix+=5
        else:
            pass
        return w
    else:
        print('Nous sommes désolés, vous ,n\'avez pas assez de pièces pour acheter l\'étoile')
        return 'Non'       
            
#Fonction qui classe les joueurs à la fin de la partie dans un fichier            
def classement(l,fichier):
    """
    :param l:(list) liste des dictionnaires des joueurs
    :param fichier:(fichier) le nom du fichier
    :CU:Aucune
    :effet de bord: elle classe les joueurs  dans le fichier 
    """
    res=[]
    res2=[]
    for dic in l:
        res+=[(dic['etoiles'],dic['pieces'],dic['casesparcourues'],dic['pseudo'])]
    res.sort(reverse=True)
    for t in res:
        res2.append(t[3]+' est classé '+str(res.index(t)+1)+' a la fin de la partie avec '+str(t[0])+' etoiles, '+str(t[1])+' pièces et '+str(t[2])+' cases parcourues\n')
    canal=open(fichier,'wt')
    canal.write('Voici le résultat de votre passionnante partie:\n')
    canal.writelines(res2)
    canal.write('Ce jeu vous a été présenté par :\n')
    canal.write('MOHAMED AMINE SABIL\n')
    canal.write('ELMEHDI OUWAB ELIDRISSI\n')
    canal.write('A la prochaine pour une nouvelle partie !!\n')
    canal.close()
    
#fonction qui fait commencer le jeu.
    
def commencer_jeu():
    """
    :effet de bord:lance le déroulement de la partie 
    :CU:None
    """
    efface_plateau()
    c=0
    l=generateur_liste()
    taille=len(l)
    pseudo22=pseudos()
    joueurs=dico_joueur(pseudo22)
    tours=nbre_tours()
    plateau=cree_plateau(l)
    cree_perso(joueurs,l)
    icones=['Mario','Yoshi','Toad','Luigi']
    for c in pseudo22:
        a=pseudo22.index(c)
        print(c+' joue en tant que '+icones[a])
    et_indice=randint(0,taille)
    place_etoile(et_indice,l)
    prix=5
    #tours
    for tour in range(int(tours)):
        if tour == int(tours)-1:
            print('\n','---- DERNIER TOUR ----')
        else:    
            print('\n','---- TOUR ',tour+1,' ----')
        #tour d'un personnage
        for joueur in joueurs:
            texte=deroulement(joueur['pseudo'],joueur)
            print(texte)
            print('\n')
            #objets
            #Test objet
            if a_des_objets(joueur['objets'])==False:
                print("\nTu n'as pas d'objet !")
            else:
                fini=False
                while fini==False:
                    use=input('Voulez-vous utiliser un objet ? (OUI ou NON) ')
                    try:
                        assert use=='OUI' or use=='NON'
                        fini=True
                    except AssertionError:
                        print('Répondez par "Oui" ou "Non" avec la majuscule !')
                print('\n')
                #utilisation d'objets
                if use == 'NON':
                    pass
                if use == 'OUI':
                    #utilisation objet
                    bug=False
                    while bug==False:
                        use2=input('Quel objet voulez-vous utiliser entre '+objets_possedes(joueurs[joueurs.index(joueur)]['objets'])+' ? ')
                        try:
                            assert (use2 == 'Voleur 5' or use2 == 'Voleur Etoile' or use2 == 'Dé chance' or use2 == 'Dé méchant') and joueurs[joueurs.index(joueur)]['objets'][use2] > 0
                            bug=True
                        except AssertionError:
                            print('Veuillez choisir un objet valide svp !')
                    if use2=="Voleur Etoile":
                        voleur_etoile(joueurs,joueur['pseudo'],pseudo22)
                    elif use2=="Voleur 5":
                        voleur_5(joueurs,joueur['pseudo'],pseudo22)
                    elif use2=="Dé méchant":
                        De_mechant(joueurs,joueur["pseudo"],pseudo22)
                    else:
                        c=3
            #lancement du dé
            a=input('appuyez sur Entrée pour lancer le dé')
            b=de()
            #utilisation du dé chance
            if c==3:
                joueur['position']=(joueur['position']+b+3)%len(l)
                joueur["objets"]["Dé chance"]-=1
                joueur["casesparcourues"]+=b+3
                print('votre dé affiche',b)
                print('Votre Dé chance a été utilisé , Le petit Ange vous a ajouté 3 a votre Dé')
                print('Vous avez avancé de ',b+3,'cases')
                bouge_perso(joueurs,l)
                types_cases(l,joueur)
            #utilisation de la malchance qui enlève 3 au dé    
            elif joueur['objets']['malchance']>0:
                joueur['position']=(joueur['position']+b-3)%len(l)
                joueur["objets"]["malchance"]-=1
                print('votre dé affiche',b)
                joueur["casesparcourues"]+=b-3
                print('Votre Malchance a été utilisé , Le Méchant Démon vous a enlevé 3 de votre Dé')
                print('Vous avez avancé de ',b-3,'cases')
                bouge_perso(joueurs,l)
                types_cases(l,joueur)
            else:
                print('votre dé affiche',b)
                print("Vous avez avancé de ",b,"cases")
                joueur["casesparcourues"]+=b
                joueur['position']=(joueur['position']+b)%len(l)
                bouge_perso(joueurs,l)
                types_cases(l,joueur)
            c=0
            #achete_etoile
            if joueur['position']==et_indice:
                s=joueurs.index(joueur)
                if achete_etoile(joueur['pseudo'],joueurs,prix,s)=="Oui":
                    et_indice=randint(1,taille)
                    place_etoile(et_indice,l)
            input('\nAppuyez sur Entrée pour finir votre tour ... ')
    #classement des joueurs et résultat de la partie
    classement(joueurs,"resultats.txt")
    efface_plateau()



            
    
