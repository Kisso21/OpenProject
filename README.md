
# Créer un environnement virtuel pour exécuter le programme :

Pour exécuter le programme `BookToScrapped.py`, il est recommandé de créer un environnement virtuel Python pour isoler les dépendances du projet.

### Étapes pour créer et activer l'environnement virtuel :

1. **Ouvrir un terminal :** Ouvrez un terminal ou une invite de commande.

2. **Naviguer vers le répertoire du projet :** Utilisez la commande `cd` pour vous déplacer vers le répertoire où se trouve le fichier `requirements.txt` et `BookToScrapped.py`.

3. **Créer un environnement virtuel :** Utilisez la commande suivante pour créer un environnement virtuel nommé "env" :
   python3 -m venv env

### Activer l'environnement virtuel :
1. **Sur macOS et Linux :**
source env/bin/activate

2. **Sur Windows:**
.\env\Scripts\activate

Lorsque l'environnement virtuel est activé, vous verrez le nom de l'environnement virtuel dans l'invite de commande, indiquant que vous êtes maintenant dans l'environnement virtuel.

### Installer les dépendances nécessaires :

1. **Dans l'environnement virtuel, utilisez la commande suivante pour installer les dépendances requises à partir du fichier requirements.txt :** 
pip install -r requirements.txt

### Exécuter le programme BookToScrapped.py :

Une fois que l'environnement virtuel est créé et que les dépendances sont installées, vous pouvez exécuter le programme BookToScrapped.py en utilisant la commande suivante : 
python3 BookToScrapped.py