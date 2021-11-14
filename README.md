odoo


# Process

## Nécessaire

- Docker
- Docker-compose

## Spécification

- Postgresql Version 13
  - Identifiant : odoo
  - Mot de passe : myodoo
- Odoo Version 15
  - Identifiant : admin@weebo.fr
  - Mot de passe : odootest0911

## Installation

```shell
docker-compose up -d
```

Permet de démarre une instance d'odoo et de PostgreSql.

Si le dossier data n'existe pas il seras créer.

```shell
docker-compose up -d mydb
```

Permet de démarre uniquement la base de donnée et de lui injecter via un outils comme HeidiSQL un data set de test (dump.sql).


Si vous partez d'une installation fraîche (sans base de donnée ni dataset), veuillez a installer om_cine qui permet l'installation de tout les module nécessaire.