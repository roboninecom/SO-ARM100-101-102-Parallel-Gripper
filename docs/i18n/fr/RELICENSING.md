<!-- translation-navigation -->
[English](../en/RELICENSING.md) · [Русский](../ru/RELICENSING.md) · [Español](../es/RELICENSING.md) · [Français](RELICENSING.md) · [Deutsch](../de/RELICENSING.md) · [Português (Brasil)](../pt-BR/RELICENSING.md) · [简体中文](../zh-CN/RELICENSING.md) · [日本語](../ja/RELICENSING.md) · [हिन्दी](../hi/RELICENSING.md) · [العربية](../ar/RELICENSING.md)

[Source anglaise](../../../RELICENSING.md)

[Français](README.md)

> Traduction automatique intégrale, pas encore relue par des locuteurs natifs. Images, code, CAO et PDF originaux sont partagés. En cas de doute, consultez la source anglaise.
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="relicensing-record"></a>
# Récords de ré-licence

Ce fichier enregistre comment et pourquoi ce projet a quitté la GPL-3.0, et l'accord
de ses contributeurs. Il existe de sorte que l'historique du permis est vérifiable sans
Je fouille dans le git.

**Statut: en cours de développement.** Ce changement ne doit pas être fusionné jusqu'à ce que chaque acc ci-dessous est
enregistré.

<a id="what-changed"></a>
## Ce qui a changé

| Matériel | Avant | Après |
|---|---|---|
| Le matériel / CAD | Uniquement sous licence GPL-3.0 | CERN-OHL-P-2.0 |
| Logiciel | Uniquement sous licence GPL-3.0 | Apache-2.0 |
| Documentation et images | Uniquement sous licence GPL-3.0 | CC BY 4.0 |

Titulaire du droit d'auteur: **Robonine**. Vous voyez ? `LICENSING.md` pour la carte dossier par dossier,
`REUSE.toml` pour la version lisible par machine, et `NOTICE` pour des tiers
attribution.

<a id="why"></a>
## Pourquoi ?

GPL-3.0 est écrit pour le logiciel. Ses définitions  ⁇  "code source", "objet"
code", "Source correspondante"  ⁇  ne sont pas cartographiés de manière claire sur un objet physique, donc
pour la partie CAD de ce projet, il n'a jamais été clair ce qui a effectivement déclenché
les obligations de la licence. CERN-OHL-P-2.0 est écrit pour le matériel et dit
explicitement ce qu'est un produit, une source couverte et un composant disponible.

Le choix permissif est délibéré. Il échange la protection contre les fermetures
les fourches de la prise en échange d'une friction zéro pour les intégrateurs, et
compatibilité avec le courant alternatif SO-ARM100/101 Le projet et le cadre plus large
LeRobot/ROS écosystèmes qui sont Apache-2.0 tout au long.

<a id="licence-history"></a>
## Historique des licences

| Engagement | Date de réception | Quoi ? |
|---|---|---|
| `00fae7b` | 2025-06-27 | Un référentiel créé. `LICENSE` était **Le MIT** 21 lignes). |
| `64d3f01` | 2025-07-01 | `LICENSE` remplacé par GPL-3.0 (674 lignes). |
| `d37855a` | 2025-07-06 | `README.md` mis à jour du MIT à la GPL-3.0. |
| ce changement | — | C'est la fraction tripartite décrite ci-dessus. |

`CONTRIBUTING.md` et `software/python/gripper_control.py` ont été **jamais**
Il a été mis à jour en 2025 et a continué d'indiquer le MIT. C'était une erreur.
une double autorisation délibérée.

Les conséquences sont importantes: chaque contributeur externe a rejoint *après* le remplacement de la GPL,
dans un référentiel dont `CONTRIBUTING.md` Je leur ai toujours dit *"En contribuant, vous
acceptez que vos contributions soient sous licence MIT. "* Les
la licence qu'ils ont effectivement offerte était plus permissive que GPL-3.0. Ce changement
le référentiel est conforme à ce qui a été dit aux contributeurs, et non pas contraire
Je le sais. Nous demandons néanmoins à chacun d'eux explicitement plutôt que de nous appuyer sur
Ça, c'est ça.

<a id="contributor-agreement"></a>
## Accord de contributeur

| Contributeur | Engagements | Scope | - Je vous en prie. |
|---|---|---|---|
| Robonine (Nikita Bragin  ⁇  aussi) `brnikita`, `branikita`) | 76 | Propriétaire | n/a |
| Alan Workaholic (Alan Subin) | 44 | `models/`, `models/parts/`, `assets/images/`, `docs/` | Travail effectué en vertu d'un contrat avec attribution de PI à Robonine; a été demandé par courtoisie |
| sontochémichael (Michael Viacheslavov) | 3 + fichiers téléchargés en son nom | `community/histology-slide-gripper/` | En attente |
| Vladimir Osipov | 1 | `README.md` réparation du lien mort | En attente |
| Syed Azhar Hussain Quadri | 1 | `software/python/gripper_control.py` | En attente |

Émission de rélicence: _ à remplir_

<a id="authorship-notes"></a>
### Notes d'auteur

- Commitments rédigés par: `Codex <codex@openai.com>` ont été réalisées par Nikita Bragin
  au nom de Robonine. Ce ne sont pas des contributions de tiers.
- CAD et images de la variante communautaire
  (`community/histology-slide-gripper/cad/*`, `assets/*`) ont été **commis par
  Robonine au nom de Michael Viacheslavov** ⁇  s'engage `537f347` et `b4698e7`
  sont rédigés comme `Codex`. L'auteur de ces dossiers appartient à Michael.
  Les métadonnées ne le reflètent pas, c'est pourquoi elles sont écrites ici.

<a id="decisions-on-the-record"></a>
## Décisions officielles

**`link5_1.stl` est un filet fusionné.** Il combine le courant en amont SO-ARM101 poignet avec
Robonine's `RB9.01.062.010 Main frame` dans un seul corps. Les pièces ne sont pas
séparable dans le fichier, de sorte que l'ensemble du fichier est distribué sous Apache-2.0:
Robonine ne peut pas accorder CERN-OHL-P-2.0 sur la géométrie il ne possède pas, et est libre
d'accorder une licence à sa propre portion en vertu du Apache-2.0. Le re-export comme deux mailles le feraient
Il faut que chaque partie porte sa licence appropriée, ce qui reste à l'avenir.

**Avis pour les fichiers binaires.** CERN-OHL-P-2.0 s'attend à ce que les avis de licence soient
conservé dans la Source. Les fichiers binaires STL et STEP ne peuvent pas les transporter, et
`.pre-commit-config.yaml` exclut délibérément ces formats des crochets de texte.
`REUSE.toml` est la manière dont ce projet remplit cette obligation: il attribue
le droit d'auteur et la licence de chaque fichier par voie; `reuse lint` impose que
Rien n'est laissé découvert.

Les notifications au niveau du répertoire ont été délibérément maintenues à un minimum  ⁇  seulement lorsque
La carte de racine ne contient pas d'informations. Deux ont survécu:
`simulation/so_arm_101_description/meshes/LICENSE.md`, parce que ce répertoire
mélanges Robonine et la géométrie en amont et quelqu'un copiant une maille dehors a besoin de voir
à cet effet; `simulation/so_arm_101_description/LICENSE.md`, parce que cette ROS
le paquet est distribué indépendamment et doit être auto-décrite.

**Les textes de licence existent à deux endroits.** `LICENSES/` est où le REUSE
Les spécifications les exigent; `HARDWARE-LICENSE.txt`, `SOFTWARE-LICENSE.txt` et
`DOCS-LICENSE.txt` à la racine sont ce que dit la détection de licence de GitHub, donc le
le référentiel affiche les trois licences plutôt qu'aucune.

**`software/FD.exe` Il a été retiré.** C' est vrai . Feetechest propriétaire de "FT" SCServo Débogage "
outil, engagé en `7783073` n'a pas obtenu de licence et a été couverte par le
la déclaration générale GPL-3.0 du projet  ⁇  qui était incorrecte. `docs/assembly-guide.md`
indique maintenant FeetechLe téléchargement est le même que celui d'une alternative open source.

**L'historique du Git n'a pas été réécrit.** `FD.exe` reste dans l'histoire et dans la source
archives des communiqués de presse `v0.1.0` à travers `v0.3.1`. La réécriture annulerait tous les
clone, fork et commit SHA référencés à partir de demandes d'attraction en amont ouvertes, qui est
pas la peine pour un outil Feetech distribue gratuitement.

**`ament_copyright` a été abandonné** à partir `package.xml`. Il a été déclaré mais jamais
- Je ne sais pas. Il vérifie les en-têtes de licence dans les fichiers sources, qui
Il s'agit d'un projet de répartition des licences dans le cadre duquel les `REUSE.toml` —
Nous avons été forcés par le fait que la plupart des fichiers ici sont binaires. `reuse lint` couvertures
tous les fichiers du référentiel, pas seulement la douzaine Python fichiers à l'intérieur du ROS
le colis.

<a id="releases"></a>
## Résultats

Cela ne modifie pas rétroactivement les exemptions `v0.1.0` à travers `v0.3.1`, qui
sont disponibles uniquement sous la GPL-3.0.

---

Préparée par les responsables du projet. C'est un enregistrement de décisions, pas légal.
Un conseil.
<!-- /translated-content -->
