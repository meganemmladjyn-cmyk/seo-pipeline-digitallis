# SEO Content Pipeline AI · Cas d'usage : Digitallis Guadeloupe

## Cadre du projet

Projet personnel construit à partir de données publiques simulées pour 
démontrer une stack d'automatisation SEO + IA. Digitallis sert ici de 
cas d'usage benchmark ; ce n'était pas une mission client.

## Enjeu en entreprise

"Passer d'une production manuelle d'articles SEO à un pipeline automatisé 
qui identifie les opportunités, génère du contenu ciblé et évalue sa 
qualité — sans intervention humaine à chaque étape."

## Le problème

Produire des articles SEO de qualité pour le blog Digitallis demandait 
un effort considérable : identifier les mots-clés à potentiel, rédiger 
des articles ancrés localement, évaluer la pertinence SEO et valider 
le contenu — un processus lent et difficilement scalable.

## La solution

Pipeline n8n en 5 étapes :

1. **Collecte automatique** — lecture d'un export GSC simulé (format 
   identique Search Console API), filtre gap SEO automatique 
   (impressions > 100, clics < 10), push vers Google Sheets
2. **Génération de contenu** — appel Claude Sonnet via HTTP Request, 
   prompt engineering avancé ancré dans le marché guadeloupéen, 
   sortie JSON structurée (titre, meta, corps, mots-clés)
3. **Scoring qualité** — évaluation par Claude Haiku sur 4 critères 
   (SEO, lisibilité, pertinence, structure), score /100 automatique
4. **Publication** — création Google Doc par article, corps complet 
   injecté, prêt à publier
5. **Traçabilité** — mise à jour Google Sheets avec score, feedback 
   et date de génération

> En production : le CSV simulé est remplacé par un appel direct 
> à la Search Console API — accès en lecture seule fourni par le 
> client en onboarding.

## Stack technique

| Brique | Outil |
|---|---|
| Orchestration | n8n (self-hosted Docker) |
| Génération | Claude Sonnet 4 (Anthropic API) |
| Scoring | Claude Haiku 4.5 (Anthropic API) |
| Collecte | CSV GSC simulé → Google Sheets |
| Publication | Google Docs API |
| Environnement | Debian / WSL |

## Impact mesuré

- **27 mots-clés** traités automatiquement
- **27 articles** générés et publiés dans Google Docs
- **Score qualité moyen : 76/100** (évaluation Claude Haiku)
- **Temps de production** : ~2 min par article vs 2-3h en rédaction manuelle
- **Économie estimée** : 50+ heures de travail rédactionnel

## Architecture du pipeline
