Dans Thunder Client
TU rentres : http://localhost:8000/api/api-token
Et tu t'y rends dessus 
Tu remplis les infos de : username et password (ce sont des strings, dans ton cas tu mets **abdou** pour les 2)
Ensuite tu recuperes le token tu repars sur une route existante comme : http://localhost:8000/api/v1/product/ (en POST)
Tu mets ce que tu veux soumettre dans la sous rubrique : **Auth**
Au niveau de Bearer Token où il y a **"entrer le token"** tu mets le token que t'as recuperer
Ensuite tu envoies la requete